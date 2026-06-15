#!/usr/bin/env python3
"""Daily paper push platform.

This wraps papers_cool_bot.py with persistence, scheduling, a local dashboard,
and push channels inspired by ChatDailyPapers' daily automation workflow.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import email.message
import html
import json
import os
import shutil
import smtplib
import sqlite3
import sys
import threading
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

from papers_cool_bot import (
    fetch_papers,
    load_config,
    markdown_report,
    score_paper,
    scored_to_json,
    date_window,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLATFORM_CONFIG = Path(__file__).with_name("platform_config.json")
RUN_LOCK = threading.Lock()
RUN_STATE: dict[str, Any] = {"running": False, "last_error": None, "last_run_at": None}


@dataclasses.dataclass
class RunResult:
    run_id: int
    report_date: dt.date
    report_path: Path
    json_path: Path
    selected_count: int
    candidate_count: int
    delivery_results: list[dict[str, Any]]
    site_path: Path | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Daily paper push platform.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_PLATFORM_CONFIG,
        help="Platform config path.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Run one daily paper job.")
    run.add_argument("--date", default=None, help="Report date, YYYY-MM-DD. Defaults to local date.")
    run.add_argument("--no-push", action="store_true", help="Skip remote push channels.")
    run.add_argument("--min-score", type=int, default=None, help="Override paper min score.")
    run.add_argument("--lookback-days", type=int, default=None, help="Override paper lookback window.")
    run.add_argument("--max-results", type=int, default=None, help="Override paper max results.")

    serve = sub.add_parser("serve", help="Run dashboard and in-process scheduler.")
    serve.add_argument("--host", default=None, help="Override configured host.")
    serve.add_argument("--port", type=int, default=None, help="Override configured port.")
    serve.add_argument("--no-scheduler", action="store_true", help="Disable background daily scheduler.")

    sub.add_parser("init-db", help="Create or migrate the SQLite database.")
    sub.add_parser("latest", help="Print latest run summary.")
    return parser.parse_args()


def load_platform_config(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Platform config not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid platform config: {path}: {exc}") from exc


def resolve_path(path: str | Path, base: Path = ROOT) -> Path:
    path = Path(path)
    if path.is_absolute():
        return path
    return base / path


def local_timezone(config: dict[str, Any]) -> dt.tzinfo:
    tz_name = config.get("timezone", "Asia/Shanghai")
    if ZoneInfo is None:
        return dt.timezone(dt.timedelta(hours=8), name=tz_name)
    return ZoneInfo(tz_name)


def local_today(config: dict[str, Any]) -> dt.date:
    return dt.datetime.now(local_timezone(config)).date()


def parse_report_date(raw: str | None, config: dict[str, Any]) -> dt.date:
    if raw:
        try:
            return dt.date.fromisoformat(raw)
        except ValueError as exc:
            raise SystemExit("--date must use YYYY-MM-DD") from exc
    return local_today(config)


def db_path(config: dict[str, Any]) -> Path:
    data_dir = resolve_path(config.get("data_dir", "paper_bot/data"))
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "paper_push.sqlite3"


def connect_db(config: dict[str, Any]) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path(config))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(config: dict[str, Any]) -> None:
    with connect_db(config) as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                report_date TEXT NOT NULL,
                started_at TEXT NOT NULL,
                finished_at TEXT,
                status TEXT NOT NULL,
                error TEXT,
                candidate_count INTEGER DEFAULT 0,
                selected_count INTEGER DEFAULT 0,
                report_path TEXT,
                json_path TEXT,
                warnings_json TEXT DEFAULT '[]'
            );

            CREATE TABLE IF NOT EXISTS papers (
                arxiv_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                authors_json TEXT NOT NULL,
                summary TEXT NOT NULL,
                updated TEXT NOT NULL,
                categories_json TEXT NOT NULL,
                arxiv_url TEXT NOT NULL,
                pdf_url TEXT NOT NULL,
                papers_cool_url TEXT NOT NULL,
                first_seen TEXT NOT NULL,
                last_seen TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS run_papers (
                run_id INTEGER NOT NULL,
                arxiv_id TEXT NOT NULL,
                rank INTEGER NOT NULL,
                score INTEGER NOT NULL,
                selected INTEGER NOT NULL,
                reason TEXT NOT NULL,
                matched_json TEXT NOT NULL,
                negative_json TEXT NOT NULL,
                PRIMARY KEY (run_id, arxiv_id),
                FOREIGN KEY (run_id) REFERENCES runs(id),
                FOREIGN KEY (arxiv_id) REFERENCES papers(arxiv_id)
            );

            CREATE TABLE IF NOT EXISTS deliveries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id INTEGER NOT NULL,
                channel TEXT NOT NULL,
                status TEXT NOT NULL,
                response TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (run_id) REFERENCES runs(id)
            );

            CREATE INDEX IF NOT EXISTS idx_runs_report_date ON runs(report_date DESC);
            CREATE INDEX IF NOT EXISTS idx_run_papers_run_rank ON run_papers(run_id, selected DESC, rank ASC);
            """
        )


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def run_job(
    config: dict[str, Any],
    report_date: dt.date,
    push: bool = True,
    overrides: dict[str, Any] | None = None,
) -> RunResult:
    init_db(config)
    overrides = overrides or {}
    started_at = now_utc()
    with connect_db(config) as conn:
        cursor = conn.execute(
            "INSERT INTO runs(report_date, started_at, status) VALUES (?, ?, ?)",
            (report_date.isoformat(), started_at, "running"),
        )
        run_id = int(cursor.lastrowid)

    try:
        result = _run_job_inner(config, run_id, report_date, push, overrides)
        with connect_db(config) as conn:
            conn.execute(
                """
                UPDATE runs
                SET finished_at=?, status=?, candidate_count=?, selected_count=?,
                    report_path=?, json_path=?
                WHERE id=?
                """,
                (
                    now_utc(),
                    "success",
                    result.candidate_count,
                    result.selected_count,
                    str(result.report_path),
                    str(result.json_path),
                    run_id,
                ),
            )
        return result
    except Exception as exc:
        error = "".join(traceback.format_exception_only(type(exc), exc)).strip()
        with connect_db(config) as conn:
            conn.execute(
                "UPDATE runs SET finished_at=?, status=?, error=? WHERE id=?",
                (now_utc(), "failed", error, run_id),
            )
        raise


def _run_job_inner(
    config: dict[str, Any],
    run_id: int,
    report_date: dt.date,
    push: bool,
    overrides: dict[str, Any],
) -> RunResult:
    paper_config_path = resolve_path(config.get("paper_config", "paper_bot/config.json"))
    paper_config = load_config(paper_config_path)
    lookback_days = int(overrides.get("lookback_days") or paper_config.get("lookback_days", 7))
    min_score = int(overrides.get("min_score") or paper_config.get("min_score", 8))
    max_results = int(overrides.get("max_results") or paper_config.get("max_results", 25))
    categories = list(paper_config.get("categories", []))

    papers, warnings = fetch_papers(paper_config.get("base_url", "https://papers.cool"), categories)
    start, end = date_window(report_date, lookback_days)
    recent = [
        paper
        for paper in papers.values()
        if start <= paper.updated.astimezone(dt.timezone.utc) < end
    ]
    all_scored = sorted(
        (score_paper(paper, paper_config) for paper in recent),
        key=lambda item: (item.score, item.paper.updated),
        reverse=True,
    )
    selected = [item for item in all_scored if item.score >= min_score][:max_results]

    reports_dir = resolve_path(config.get("reports_dir", "paper_bot/reports"))
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / f"{report_date.isoformat()}_agentic_rl.md"
    json_path = reports_dir / f"{report_date.isoformat()}_agentic_rl.json"
    report_path.write_text(
        markdown_report(
            selected,
            all_recent_count=len(recent),
            categories=categories,
            report_date=report_date,
            lookback_days=lookback_days,
            min_score=min_score,
            warnings=warnings,
        ),
        encoding="utf-8",
    )
    json_payload = scored_to_json(selected, all_scored)
    json_path.write_text(json.dumps(json_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    persist_run_papers(config, run_id, all_scored, selected, warnings)
    site_path = build_static_site(config, report_date, selected, len(recent), report_path, json_path)
    delivery_results: list[dict[str, Any]] = []
    if push and config.get("push", {}).get("enabled", True):
        delivery_results = push_digest(config, run_id, report_date, report_path, selected, len(recent))
    else:
        delivery_results = [{"channel": "push", "status": "skipped", "response": "Push disabled for this run."}]
    return RunResult(
        run_id=run_id,
        report_date=report_date,
        report_path=report_path,
        json_path=json_path,
        selected_count=len(selected),
        candidate_count=len(recent),
        delivery_results=delivery_results,
        site_path=site_path,
    )


def persist_run_papers(config: dict[str, Any], run_id: int, all_scored: list[Any], selected: list[Any], warnings: list[str]) -> None:
    selected_ids = {item.paper.arxiv_id for item in selected}
    seen_at = now_utc()
    with connect_db(config) as conn:
        conn.execute("UPDATE runs SET warnings_json=? WHERE id=?", (json.dumps(warnings), run_id))
        for rank, item in enumerate(all_scored, start=1):
            paper = item.paper
            conn.execute(
                """
                INSERT INTO papers(
                    arxiv_id, title, authors_json, summary, updated, categories_json,
                    arxiv_url, pdf_url, papers_cool_url, first_seen, last_seen
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(arxiv_id) DO UPDATE SET
                    title=excluded.title,
                    authors_json=excluded.authors_json,
                    summary=excluded.summary,
                    updated=excluded.updated,
                    categories_json=excluded.categories_json,
                    arxiv_url=excluded.arxiv_url,
                    pdf_url=excluded.pdf_url,
                    papers_cool_url=excluded.papers_cool_url,
                    last_seen=excluded.last_seen
                """,
                (
                    paper.arxiv_id,
                    paper.title,
                    json.dumps(paper.authors, ensure_ascii=False),
                    paper.summary,
                    paper.updated.isoformat(),
                    json.dumps(sorted(paper.categories), ensure_ascii=False),
                    paper.arxiv_url,
                    paper.pdf_url,
                    paper.papers_cool_url,
                    seen_at,
                    seen_at,
                ),
            )
            conn.execute(
                """
                INSERT OR REPLACE INTO run_papers(
                    run_id, arxiv_id, rank, score, selected, reason, matched_json, negative_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    run_id,
                    paper.arxiv_id,
                    rank,
                    item.score,
                    1 if paper.arxiv_id in selected_ids else 0,
                    item.reason,
                    json.dumps(item.matched, ensure_ascii=False),
                    json.dumps(item.negative_matches, ensure_ascii=False),
                ),
            )


def compact_digest(
    report_date: dt.date,
    selected: list[Any],
    candidate_count: int,
    max_items: int,
    report_path: Path,
    public_url: str | None = None,
) -> str:
    lines = [
        f"# Daily Papers - {report_date.isoformat()}",
        "",
        f"筛选结果：{len(selected)} 篇入选，候选池 {candidate_count} 篇。",
        f"网页入口：{public_url}" if public_url else f"本地报告：{report_path}",
        "",
    ]
    for index, item in enumerate(selected[:max_items], start=1):
        paper = item.paper
        lines.extend(
            [
                f"## {index}. {paper.title}",
                f"- Score: {item.score}",
                f"- Link: {paper.arxiv_url}",
                f"- PDF: {paper.pdf_url}",
                f"- Why: {item.reason}",
                "",
            ]
        )
    if len(selected) > max_items:
        lines.append(f"... and {len(selected) - max_items} more in the full report.")
    return "\n".join(lines).strip() + "\n"


def wechat_digest(
    report_date: dt.date,
    selected: list[Any],
    candidate_count: int,
    report_path: Path,
    public_url: str | None = None,
    max_items: int = 5,
) -> str:
    shown = selected[:max_items]
    lines = [
        f"# 今日论文速递 · {report_date.isoformat()}",
        "",
        f"入选 **{len(selected)}** 篇，候选池 **{candidate_count}** 篇。微信里先看 Top {len(shown)}，完整列表点下面。",
        "",
    ]
    if public_url:
        lines.extend([f"[打开完整网页]({public_url})", ""])
    else:
        lines.extend([f"本地报告：`{report_path}`", ""])

    for index, item in enumerate(shown, start=1):
        paper = item.paper
        lines.extend(
            [
                f"## {index}. {paper.title}",
                "",
                f"**分数**：{item.score}  ",
                f"**标签**：{format_digest_tags(item)}",
                "",
                f"**看点**：{wechat_takeaway(item)}",
                "",
                f"[arXiv]({paper.arxiv_url}) · [PDF]({paper.pdf_url}) · [papers.cool]({paper.papers_cool_url})",
                "",
                "---",
                "",
            ]
        )

    if len(selected) > len(shown):
        more = len(selected) - len(shown)
        if public_url:
            lines.append(f"还有 **{more}** 篇在[完整网页]({public_url})里。")
        else:
            lines.append(f"还有 **{more}** 篇在完整报告里。")
    return "\n".join(lines).strip() + "\n"


def format_digest_tags(item: Any) -> str:
    tag_names = {
        "agentic_rl": "Agentic RL",
        "rl_post_training": "RL/Post-train",
        "reasoning": "Reasoning",
        "planning_and_action": "Planning/Action",
        "memory_and_benchmarks": "Memory/Eval",
    }
    tags = [tag_names.get(group, group) for group in item.matched.keys()]
    if not tags:
        tags = ["Paper"]
    return " / ".join(tags[:4])


def one_line_takeaway(summary: str, width: int = 180) -> str:
    cleaned = " ".join((summary or "").split())
    if not cleaned:
        return "摘要缺失，建议打开论文页查看。"
    sentence_end = len(cleaned)
    for marker in [". ", "? ", "! "]:
        pos = cleaned.find(marker)
        if 40 <= pos < sentence_end:
            sentence_end = pos + 1
    first = cleaned[:sentence_end].strip()
    if len(first) <= width:
        return first
    return first[: width - 3].rstrip() + "..."


def wechat_takeaway(item: Any) -> str:
    groups = set(item.matched.keys())
    terms = []
    for values in item.matched.values():
        terms.extend(values)
    title = item.paper.title
    if "agentic_rl" in groups and "rl_post_training" in groups:
        return "强相关：同时命中 Agent/工具/多智能体 与 RL/post-training 信号，适合优先判断是否进入精读队列。"
    if "rl_post_training" in groups and "reasoning" in groups:
        return "关注 RLVR/GRPO/奖励模型如何改善推理过程，适合跟进 post-training 方法线。"
    if "agentic_rl" in groups and "memory_and_benchmarks" in groups:
        return "偏 Agent 系统能力与评测，适合看任务设计、工具/记忆/协作 scaffold。"
    if "planning_and_action" in groups:
        return "偏规划、轨迹或环境反馈，适合补 Agent 执行闭环和长程任务视角。"
    if terms:
        return "关键词命中：" + "、".join(terms[:5]) + "。建议先看 abstract 和实验设置。"
    return one_line_takeaway(item.paper.summary)


def push_digest(
    config: dict[str, Any],
    run_id: int,
    report_date: dt.date,
    report_path: Path,
    selected: list[Any],
    candidate_count: int,
) -> list[dict[str, Any]]:
    push_config = config.get("push", {})
    max_items = int(push_config.get("max_items", 10))
    page_url = public_url(config)
    markdown = compact_digest(
        report_date,
        selected,
        candidate_count,
        max_items,
        report_path,
        public_url=page_url,
    )
    wechat_markdown = wechat_digest(
        report_date,
        selected,
        candidate_count,
        report_path,
        public_url=page_url,
        max_items=min(5, max_items),
    )
    title = f"Daily Papers - {report_date.isoformat()}"
    wechat_title = f"论文速递 {report_date.isoformat()} · Top {min(5, len(selected))}"
    results = []
    for channel in push_config.get("channels", []):
        if not channel_enabled(channel):
            continue
        name = channel.get("name") or channel.get("type", "channel")
        try:
            if channel.get("type") == "file":
                status, response = "success", f"Report written to {report_path}"
            elif channel.get("type") == "generic_webhook":
                status, response = push_generic_webhook(channel, title, markdown, selected)
            elif channel.get("type") == "feishu_webhook":
                status, response = push_feishu(channel, title, markdown)
            elif channel.get("type") == "github_issue":
                status, response = push_github_issue(channel, title, markdown)
            elif channel.get("type") == "serverchan":
                status, response = push_serverchan(channel, wechat_title, wechat_markdown)
            elif channel.get("type") == "wxpusher":
                status, response = push_wxpusher(channel, wechat_title, wechat_markdown, config)
            elif channel.get("type") == "email":
                status, response = push_email(channel, title, markdown)
            else:
                status, response = "skipped", f"Unknown channel type: {channel.get('type')}"
        except Exception as exc:
            status, response = "failed", str(exc)
        record_delivery(config, run_id, name, status, response)
        results.append({"channel": name, "status": status, "response": response})
    if not results:
        record_delivery(config, run_id, "push", "skipped", "No enabled channels.")
        results.append({"channel": "push", "status": "skipped", "response": "No enabled channels."})
    return results


def channel_enabled(channel: dict[str, Any]) -> bool:
    if channel.get("enabled", False):
        return True
    if channel.get("type") == "serverchan" and os.environ.get(channel.get("sendkey_env", "SERVERCHAN_SENDKEY"), ""):
        return True
    if channel.get("type") == "wxpusher" and os.environ.get(channel.get("app_token_env", "WXPUSHER_APP_TOKEN"), ""):
        return True
    env_name = channel.get("enabled_env")
    return bool(env_name and os.environ.get(env_name, "").lower() in {"1", "true", "yes", "on"})


def public_url(config: dict[str, Any]) -> str | None:
    env_name = config.get("public_base_url_env", "PAPER_BOT_PUBLIC_BASE_URL")
    url = os.environ.get(env_name, "").strip()
    if not url:
        return None
    return url.rstrip("/") + "/"


def build_static_site(
    config: dict[str, Any],
    report_date: dt.date,
    selected: list[Any],
    candidate_count: int,
    report_path: Path,
    json_path: Path,
) -> Path:
    site_dir = resolve_path(config.get("site_dir", "paper_bot/site"))
    reports_dir = site_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_html_name = f"{report_date.isoformat()}_agentic_rl.html"
    report_md_name = f"{report_date.isoformat()}_agentic_rl.md"
    report_json_name = f"{report_date.isoformat()}_agentic_rl.json"
    shutil.copyfile(report_path, reports_dir / report_md_name)
    shutil.copyfile(json_path, reports_dir / report_json_name)
    (reports_dir / report_html_name).write_text(
        render_markdown_text(report_html_name, report_path.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    (site_dir / "latest.json").write_text(json_path.read_text(encoding="utf-8"), encoding="utf-8")
    (site_dir / "index.html").write_text(
        render_static_index(report_date, selected, candidate_count, report_html_name, report_md_name, report_json_name),
        encoding="utf-8",
    )
    return site_dir / "index.html"


def render_static_index(
    report_date: dt.date,
    selected: list[Any],
    candidate_count: int,
    report_html_name: str,
    report_md_name: str,
    report_json_name: str,
) -> str:
    cards = "\n".join(render_static_card(item, index) for index, item in enumerate(selected, start=1))
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Daily Papers - {report_date.isoformat()}</title>
  <style>{DASHBOARD_CSS}</style>
</head>
<body>
  <main>
    <section class="topbar">
      <div>
        <h1>Daily Papers</h1>
        <p>RL / post-training / agentic RL queue from papers.cool</p>
      </div>
      <div class="actions">
        <a class="button secondary" href="reports/{html.escape(report_html_name)}">Full Report</a>
        <a class="button secondary" href="reports/{html.escape(report_md_name)}">Markdown</a>
        <a class="button secondary" href="reports/{html.escape(report_json_name)}">JSON</a>
      </div>
    </section>
    <section class="stats">
      <div><span>Report Date</span><strong>{report_date.isoformat()}</strong></div>
      <div><span>Selected</span><strong>{len(selected)}</strong></div>
      <div><span>Candidates</span><strong>{candidate_count}</strong></div>
      <div><span>Source</span><strong>papers.cool</strong></div>
    </section>
    <section>
      <h2>Top Papers</h2>
      <div class="papers">{cards or "<p>No selected papers.</p>"}</div>
    </section>
  </main>
</body>
</html>"""


def render_static_card(item: Any, index: int) -> str:
    paper = item.paper
    authors = ", ".join(paper.authors[:5]) + (f", et al. ({len(paper.authors)} authors)" if len(paper.authors) > 5 else "")
    return f"""<article class="paper">
  <div class="score">{item.score}</div>
  <div>
    <h3>{index}. <a href="{html.escape(paper.arxiv_url)}" target="_blank">{html.escape(paper.title)}</a></h3>
    <p class="meta">{html.escape(authors)} · {paper.updated.strftime('%Y-%m-%d')} · {html.escape(', '.join(sorted(paper.categories)))}</p>
    <p>{html.escape(item.reason)}</p>
    <a href="{html.escape(paper.pdf_url)}" target="_blank">PDF</a>
    <a href="{html.escape(paper.papers_cool_url)}" target="_blank">papers.cool</a>
  </div>
</article>"""


def record_delivery(config: dict[str, Any], run_id: int, channel: str, status: str, response: str) -> None:
    with connect_db(config) as conn:
        conn.execute(
            "INSERT INTO deliveries(run_id, channel, status, response, created_at) VALUES (?, ?, ?, ?, ?)",
            (run_id, channel, status, response[:4000], now_utc()),
        )


def env_value(name: str | None, required: bool = True) -> str:
    if not name:
        if required:
            raise RuntimeError("Missing env field name in channel config.")
        return ""
    value = os.environ.get(name, "")
    if required and not value:
        raise RuntimeError(f"Environment variable {name} is not set.")
    return value


def post_json(url: str, payload: dict[str, Any], headers: dict[str, str] | None = None) -> tuple[str, str]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "paper-push-platform/0.1",
            **(headers or {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8", errors="replace")
            return "success", f"HTTP {response.status}: {text[:1000]}"
    except urllib.error.HTTPError as exc:
        text = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {text[:1000]}") from exc


def push_generic_webhook(channel: dict[str, Any], title: str, markdown: str, selected: list[Any]) -> tuple[str, str]:
    url = env_value(channel.get("url_env"))
    payload = {
        "title": title,
        "markdown": markdown,
        "papers": [
            {
                "score": item.score,
                "arxiv_id": item.paper.arxiv_id,
                "title": item.paper.title,
                "url": item.paper.arxiv_url,
                "pdf_url": item.paper.pdf_url,
                "reason": item.reason,
            }
            for item in selected
        ],
    }
    return post_json(url, payload)


def push_feishu(channel: dict[str, Any], title: str, markdown: str) -> tuple[str, str]:
    url = env_value(channel.get("url_env"))
    text = f"{title}\n\n{markdown}"
    payload = {"msg_type": "text", "content": {"text": text[:18000]}}
    return post_json(url, payload)


def push_github_issue(channel: dict[str, Any], title: str, markdown: str) -> tuple[str, str]:
    repo = os.environ.get(channel.get("repo_env", "GITHUB_REPOSITORY"), "")
    token = env_value(channel.get("token_env", "GITHUB_TOKEN"))
    if not repo:
        raise RuntimeError("GitHub repository env is not set.")
    labels = channel.get("labels", [])
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    return post_json(url, {"title": title, "body": markdown, "labels": labels}, headers=headers)


def push_serverchan(channel: dict[str, Any], title: str, markdown: str) -> tuple[str, str]:
    sendkey = env_value(channel.get("sendkey_env", "SERVERCHAN_SENDKEY"))
    url = f"https://sctapi.ftqq.com/{urllib.parse.quote(sendkey)}.send"
    form = urllib.parse.urlencode({"title": title, "desp": markdown[:32000]}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=form,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "User-Agent": "paper-push-platform/0.1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8", errors="replace")
            return "success", f"HTTP {response.status}: {text[:1000]}"
    except urllib.error.HTTPError as exc:
        text = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {text[:1000]}") from exc


def push_wxpusher(channel: dict[str, Any], title: str, markdown: str, config: dict[str, Any]) -> tuple[str, str]:
    app_token = env_value(channel.get("app_token_env", "WXPUSHER_APP_TOKEN"))
    uid = os.environ.get(channel.get("uid_env", "WXPUSHER_UID"), "").strip()
    topic_id = os.environ.get(channel.get("topic_id_env", "WXPUSHER_TOPIC_ID"), "").strip()
    if not uid and not topic_id:
        raise RuntimeError("Set WXPUSHER_UID or WXPUSHER_TOPIC_ID.")
    payload: dict[str, Any] = {
        "appToken": app_token,
        "content": markdown[:32000],
        "summary": title[:99],
        "contentType": 3,
    }
    url = public_url(config)
    if url:
        payload["url"] = url
    if uid:
        payload["uids"] = [uid]
    if topic_id:
        payload["topicIds"] = [int(topic_id)]
    return post_json("https://wxpusher.zjiecode.com/api/send/message", payload)


def push_email(channel: dict[str, Any], title: str, markdown: str) -> tuple[str, str]:
    host = env_value(channel.get("host_env"))
    port = int(os.environ.get(channel.get("port_env", "SMTP_PORT"), "587"))
    user = env_value(channel.get("user_env"), required=False)
    password = env_value(channel.get("password_env"), required=False)
    from_addr = env_value(channel.get("from_env"))
    to_raw = env_value(channel.get("to_env"))
    to_addrs = [addr.strip() for addr in to_raw.split(",") if addr.strip()]
    if not to_addrs:
        raise RuntimeError("No email recipients configured.")
    message = email.message.EmailMessage()
    message["Subject"] = title
    message["From"] = from_addr
    message["To"] = ", ".join(to_addrs)
    message.set_content(markdown)

    use_tls = os.environ.get(channel.get("use_tls_env", "SMTP_USE_TLS"), "1") != "0"
    with smtplib.SMTP(host, port, timeout=30) as smtp:
        if use_tls:
            smtp.starttls()
        if user:
            smtp.login(user, password)
        smtp.send_message(message)
    return "success", f"Sent email to {', '.join(to_addrs)}"


def latest_run(config: dict[str, Any]) -> sqlite3.Row | None:
    init_db(config)
    with connect_db(config) as conn:
        return conn.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 1").fetchone()


def latest_selected(config: dict[str, Any], run_id: int, limit: int = 30) -> list[sqlite3.Row]:
    with connect_db(config) as conn:
        return conn.execute(
            """
            SELECT rp.rank, rp.score, rp.reason, p.*
            FROM run_papers rp
            JOIN papers p ON p.arxiv_id = rp.arxiv_id
            WHERE rp.run_id = ? AND rp.selected = 1
            ORDER BY rp.rank ASC
            LIMIT ?
            """,
            (run_id, limit),
        ).fetchall()


def latest_deliveries(config: dict[str, Any], run_id: int) -> list[sqlite3.Row]:
    with connect_db(config) as conn:
        return conn.execute(
            "SELECT * FROM deliveries WHERE run_id = ? ORDER BY id ASC",
            (run_id,),
        ).fetchall()


def run_history(config: dict[str, Any], limit: int = 20) -> list[sqlite3.Row]:
    init_db(config)
    with connect_db(config) as conn:
        return conn.execute("SELECT * FROM runs ORDER BY id DESC LIMIT ?", (limit,)).fetchall()


class DashboardHandler(BaseHTTPRequestHandler):
    platform_config: dict[str, Any] = {}

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_HEAD(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/" or parsed.path == "/api/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/":
            self.send_html(render_dashboard(self.platform_config))
        elif parsed.path == "/api/status":
            self.send_json(api_status(self.platform_config))
        elif parsed.path.startswith("/reports/"):
            self.serve_report(parsed.path.removeprefix("/reports/"))
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/run":
            if RUN_LOCK.locked():
                self.send_json({"ok": False, "message": "A run is already in progress."}, status=409)
                return
            thread = threading.Thread(target=background_run, args=(self.platform_config,), daemon=True)
            thread.start()
            self.send_json({"ok": True, "message": "Run started."})
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_html(self, body: str, status: int = 200) -> None:
        encoded = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def serve_report(self, filename: str) -> None:
        reports_dir = resolve_path(self.platform_config.get("reports_dir", "paper_bot/reports")).resolve()
        target = (reports_dir / filename).resolve()
        if reports_dir not in target.parents and target != reports_dir:
            self.send_error(HTTPStatus.FORBIDDEN, "Forbidden")
            return
        if not target.exists() or not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "Report not found")
            return
        text = target.read_text(encoding="utf-8")
        self.send_html(render_markdown_text(target.name, text))


def api_status(config: dict[str, Any]) -> dict[str, Any]:
    run = latest_run(config)
    history = run_history(config)
    selected = latest_selected(config, run["id"]) if run else []
    deliveries = latest_deliveries(config, run["id"]) if run else []
    return {
        "run_state": RUN_STATE,
        "latest_run": dict(run) if run else None,
        "selected": [row_to_json(row) for row in selected],
        "deliveries": [dict(row) for row in deliveries],
        "history": [dict(row) for row in history],
    }


def row_to_json(row: sqlite3.Row) -> dict[str, Any]:
    data = dict(row)
    for key in ("authors_json", "categories_json"):
        if key in data:
            data[key.replace("_json", "")] = json.loads(data.pop(key))
    return data


def render_dashboard(config: dict[str, Any]) -> str:
    run = latest_run(config)
    history = run_history(config)
    selected = latest_selected(config, run["id"]) if run else []
    deliveries = latest_deliveries(config, run["id"]) if run else []
    report_link = ""
    if run and run["report_path"]:
        report_name = Path(run["report_path"]).name
        report_link = f'<a class="button secondary" href="/reports/{html.escape(report_name)}">Open Report</a>'
    selected_html = "\n".join(render_paper_card(row) for row in selected) or "<p>No selected papers yet.</p>"
    delivery_html = "\n".join(
        f"<li><strong>{html.escape(row['channel'])}</strong>: {html.escape(row['status'])} <span>{html.escape(row['response'] or '')}</span></li>"
        for row in deliveries
    ) or "<li>No delivery logs yet.</li>"
    history_html = "\n".join(
        f"<tr><td>{row['id']}</td><td>{html.escape(row['report_date'])}</td><td>{html.escape(row['status'])}</td><td>{row['selected_count']}/{row['candidate_count']}</td></tr>"
        for row in history
    )
    schedule = config.get("schedule", {})
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Daily Paper Push</title>
  <style>{DASHBOARD_CSS}</style>
</head>
<body>
  <main>
    <section class="topbar">
      <div>
        <h1>Daily Paper Push</h1>
        <p>RL / post-training / agentic RL paper queue from papers.cool</p>
      </div>
      <div class="actions">
        <button id="runNow">Run Now</button>
        {report_link}
      </div>
    </section>

    <section class="stats">
      <div><span>Latest Run</span><strong>{html.escape(run['report_date']) if run else '-'}</strong></div>
      <div><span>Status</span><strong>{html.escape(run['status']) if run else '-'}</strong></div>
      <div><span>Selected</span><strong>{run['selected_count'] if run else 0}</strong></div>
      <div><span>Candidates</span><strong>{run['candidate_count'] if run else 0}</strong></div>
    </section>

    <section class="layout">
      <div>
        <h2>Top Papers</h2>
        <div class="papers">{selected_html}</div>
      </div>
      <aside>
        <h2>Push Channels</h2>
        <ul class="deliveries">{delivery_html}</ul>
        <h2>Schedule</h2>
        <p class="muted">Enabled: {schedule.get('enabled', True)}<br>Time: {html.escape(str(schedule.get('time', '10:20')))} {html.escape(config.get('timezone', 'Asia/Shanghai'))}<br>Weekdays: {schedule.get('weekdays', [])}</p>
        <h2>Run History</h2>
        <table><thead><tr><th>ID</th><th>Date</th><th>Status</th><th>Hit</th></tr></thead><tbody>{history_html}</tbody></table>
      </aside>
    </section>
  </main>
  <script>
    document.getElementById('runNow').addEventListener('click', async () => {{
      const btn = document.getElementById('runNow');
      btn.disabled = true;
      btn.textContent = 'Running...';
      const res = await fetch('/api/run', {{ method: 'POST' }});
      const data = await res.json();
      alert(data.message || JSON.stringify(data));
      setTimeout(() => location.reload(), 2000);
    }});
  </script>
</body>
</html>"""


def render_paper_card(row: sqlite3.Row) -> str:
    authors = json.loads(row["authors_json"])
    authors_text = ", ".join(authors[:5]) + (f", et al. ({len(authors)} authors)" if len(authors) > 5 else "")
    return f"""<article class="paper">
  <div class="score">{row['score']}</div>
  <div>
    <h3><a href="{html.escape(row['arxiv_url'])}" target="_blank">{html.escape(row['title'])}</a></h3>
    <p class="meta">{html.escape(authors_text)} · {html.escape(row['updated'][:10])} · arXiv:{html.escape(row['arxiv_id'])}</p>
    <p>{html.escape(row['reason'])}</p>
    <a href="{html.escape(row['pdf_url'])}" target="_blank">PDF</a>
    <a href="{html.escape(row['papers_cool_url'])}" target="_blank">papers.cool</a>
  </div>
</article>"""


def render_markdown_text(title: str, text: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{DASHBOARD_CSS}</style></head>
<body><main><p><a href="/">Back</a></p><pre class="report">{html.escape(text)}</pre></main></body></html>"""


DASHBOARD_CSS = """
:root { color-scheme: light; --ink:#202124; --muted:#5f6368; --line:#dadce0; --bg:#f8fafc; --card:#fff; --accent:#0b57d0; --good:#137333; --bad:#a50e0e; }
* { box-sizing: border-box; }
body { margin:0; font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; color:var(--ink); background:var(--bg); }
main { max-width:1180px; margin:0 auto; padding:24px; }
h1,h2,h3,p { margin-top:0; }
a { color:var(--accent); text-decoration:none; }
.topbar { display:flex; justify-content:space-between; gap:24px; align-items:flex-start; margin-bottom:20px; }
.topbar h1 { font-size:28px; margin-bottom:4px; letter-spacing:0; }
.topbar p,.muted,.meta { color:var(--muted); }
.actions { display:flex; gap:10px; }
button,.button { border:1px solid var(--accent); background:var(--accent); color:white; border-radius:6px; padding:8px 12px; cursor:pointer; font:inherit; }
.button.secondary { color:var(--accent); background:white; }
button:disabled { opacity:.6; cursor:wait; }
.stats { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:20px; }
.stats div,.paper,aside { background:var(--card); border:1px solid var(--line); border-radius:8px; }
.stats div { padding:14px; }
.stats span { display:block; color:var(--muted); font-size:12px; }
.stats strong { font-size:24px; }
.layout { display:grid; grid-template-columns:minmax(0,1fr) 330px; gap:20px; align-items:start; }
.papers { display:grid; gap:10px; }
.paper { display:grid; grid-template-columns:48px minmax(0,1fr); gap:14px; padding:14px; }
.paper h3 { font-size:16px; margin-bottom:4px; letter-spacing:0; }
.paper .score { width:40px; height:40px; border-radius:6px; background:#e8f0fe; color:var(--accent); display:grid; place-items:center; font-weight:700; }
.paper p { margin-bottom:8px; }
.paper a + a { margin-left:10px; }
aside { padding:16px; }
aside h2 { font-size:15px; margin:18px 0 8px; }
aside h2:first-child { margin-top:0; }
ul { padding-left:18px; }
li span { color:var(--muted); display:block; overflow-wrap:anywhere; }
table { width:100%; border-collapse:collapse; font-size:12px; }
th,td { border-bottom:1px solid var(--line); text-align:left; padding:6px 4px; }
.report { white-space:pre-wrap; background:white; border:1px solid var(--line); border-radius:8px; padding:18px; overflow:auto; }
@media (max-width: 820px) {
  main { padding:16px; }
  .topbar { display:block; }
  .actions { margin-top:12px; }
  .stats { grid-template-columns:repeat(2,1fr); }
  .layout { grid-template-columns:1fr; }
}
"""


def background_run(config: dict[str, Any]) -> None:
    with RUN_LOCK:
        RUN_STATE.update({"running": True, "last_error": None, "last_run_at": now_utc()})
        try:
            run_job(config, local_today(config), push=True)
        except Exception as exc:
            RUN_STATE["last_error"] = str(exc)
        finally:
            RUN_STATE["running"] = False


def scheduler_loop(config: dict[str, Any]) -> None:
    while True:
        try:
            seconds = seconds_until_next_schedule(config)
            time.sleep(seconds)
            background_run(config)
        except Exception as exc:
            RUN_STATE["last_error"] = f"scheduler: {exc}"
            time.sleep(60)


def seconds_until_next_schedule(config: dict[str, Any]) -> float:
    schedule = config.get("schedule", {})
    tz = local_timezone(config)
    run_time = dt.time.fromisoformat(schedule.get("time", "10:20"))
    weekdays = set(schedule.get("weekdays", [0, 1, 2, 3, 4]))
    now = dt.datetime.now(tz)
    for offset in range(8):
        candidate_date = now.date() + dt.timedelta(days=offset)
        candidate = dt.datetime.combine(candidate_date, run_time, tzinfo=tz)
        if candidate <= now:
            continue
        if candidate.weekday() in weekdays:
            return max(1.0, (candidate - now).total_seconds())
    return 3600.0


def serve(config: dict[str, Any], host: str, port: int, scheduler: bool = True) -> None:
    init_db(config)
    DashboardHandler.platform_config = config
    if scheduler and config.get("schedule", {}).get("enabled", True):
        threading.Thread(target=scheduler_loop, args=(config,), daemon=True).start()
    server = ThreadingHTTPServer((host, port), DashboardHandler)
    print(f"Dashboard: http://{host}:{port}")
    print("Press Ctrl+C to stop.")
    server.serve_forever()


def print_latest(config: dict[str, Any]) -> None:
    run = latest_run(config)
    if not run:
        print("No runs yet.")
        return
    print(f"Run #{run['id']} {run['report_date']} {run['status']} {run['selected_count']}/{run['candidate_count']}")
    if run["report_path"]:
        print(run["report_path"])
    for row in latest_selected(config, run["id"], limit=10):
        print(f"- {row['score']:>3} {row['arxiv_id']} {row['title']}")


def main() -> int:
    args = parse_args()
    config = load_platform_config(args.config)
    if args.command == "init-db":
        init_db(config)
        print(f"Initialized {db_path(config)}")
        return 0
    if args.command == "run":
        report_date = parse_report_date(args.date, config)
        result = run_job(
            config,
            report_date,
            push=not args.no_push,
            overrides={
                "min_score": args.min_score,
                "lookback_days": args.lookback_days,
                "max_results": args.max_results,
            },
        )
        print(
            f"Run #{result.run_id}: wrote {result.report_path} "
            f"with {result.selected_count}/{result.candidate_count} papers."
        )
        for delivery in result.delivery_results:
            print(f"- {delivery['channel']}: {delivery['status']} - {delivery['response']}")
        return 0
    if args.command == "serve":
        server_config = config.get("server", {})
        host = args.host or server_config.get("host", "127.0.0.1")
        port = args.port or int(server_config.get("port", 8765))
        serve(config, host, port, scheduler=not args.no_scheduler)
        return 0
    if args.command == "latest":
        print_latest(config)
        return 0
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
