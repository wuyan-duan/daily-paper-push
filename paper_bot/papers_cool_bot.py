#!/usr/bin/env python3
"""Find RL/post-training/agentic-RL papers from papers.cool.

The script intentionally uses only the Python standard library so it can run as
a tiny local bot without environment setup.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import html
import json
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(?:v\d+)?")
WORD_RE = re.compile(r"[a-z0-9][a-z0-9+\-.]*", re.IGNORECASE)


@dataclasses.dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: list[str]
    summary: str
    updated: dt.datetime
    categories: set[str]
    papers_cool_url: str

    @property
    def arxiv_url(self) -> str:
        return f"https://arxiv.org/abs/{self.arxiv_id}"

    @property
    def pdf_url(self) -> str:
        return f"https://arxiv.org/pdf/{self.arxiv_id}"


@dataclasses.dataclass
class ScoredPaper:
    paper: Paper
    score: int
    matched: dict[str, list[str]]
    negative_matches: list[str]
    reason: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a reading queue from papers.cool for RL/post-training/agentic-RL papers."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).with_name("config.json"),
        help="Path to config JSON.",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Report date as YYYY-MM-DD. Defaults to today's local date.",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=None,
        help="Override config lookback_days.",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=None,
        help="Override config min_score.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=None,
        help="Override config max_results.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Markdown output path. Defaults to reports/YYYY-MM-DD_agentic_rl.md.",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=None,
        help="Optional JSON output path for downstream integrations.",
    )
    parser.add_argument(
        "--category",
        action="append",
        dest="categories",
        help="Override categories. Can be repeated, e.g. --category cs.AI --category cs.CL.",
    )
    parser.add_argument(
        "--include-low-score",
        action="store_true",
        help="Include all fetched papers in JSON, even below min_score.",
    )
    return parser.parse_args()


def load_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Config not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid config JSON: {path}: {exc}") from exc


def parse_report_date(raw: str | None) -> dt.date:
    if raw is None:
        return dt.date.today()
    try:
        return dt.date.fromisoformat(raw)
    except ValueError as exc:
        raise SystemExit("--date must use YYYY-MM-DD") from exc


def fetch_text(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "paper-reading-bot/0.1 (+local research workflow)",
            "Accept": "application/atom+xml,text/html;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to fetch {url}: {exc}") from exc


def parse_atom_datetime(value: str) -> dt.datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    parsed = dt.datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def extract_arxiv_id(*values: str) -> str:
    for value in values:
        match = ARXIV_ID_RE.search(value or "")
        if match:
            return match.group(1)
    return ""


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def parse_feed(xml_text: str, category: str) -> list[Paper]:
    root = ET.fromstring(xml_text)
    papers: list[Paper] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        entry_id = normalize_space(entry.findtext("atom:id", default="", namespaces=ATOM_NS))
        title = normalize_space(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        summary = normalize_space(entry.findtext("atom:summary", default="", namespaces=ATOM_NS))
        updated_raw = normalize_space(entry.findtext("atom:updated", default="", namespaces=ATOM_NS))
        hrefs = [
            link.attrib.get("href", "")
            for link in entry.findall("atom:link", ATOM_NS)
            if link.attrib.get("href")
        ]
        arxiv_id = extract_arxiv_id(entry_id, *hrefs)
        if not arxiv_id:
            continue
        authors = [
            normalize_space(author.findtext("atom:name", default="", namespaces=ATOM_NS))
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        papers.append(
            Paper(
                arxiv_id=arxiv_id,
                title=title,
                authors=[author for author in authors if author],
                summary=summary,
                updated=parse_atom_datetime(updated_raw),
                categories={category},
                papers_cool_url=f"https://papers.cool/arxiv/{arxiv_id}",
            )
        )
    return papers


def fetch_papers(base_url: str, categories: list[str]) -> tuple[dict[str, Paper], list[str]]:
    papers: dict[str, Paper] = {}
    warnings: list[str] = []
    for category in categories:
        url = f"{base_url.rstrip('/')}/arxiv/{urllib.parse.quote(category)}/feed"
        try:
            category_papers = parse_feed(fetch_text(url), category)
        except Exception as exc:  # Keep other categories alive if one feed is down.
            warnings.append(f"{category}: {exc}")
            continue
        for paper in category_papers:
            existing = papers.get(paper.arxiv_id)
            if existing is None:
                papers[paper.arxiv_id] = paper
            else:
                existing.categories.update(paper.categories)
    return papers, warnings


def date_window(report_date: dt.date, lookback_days: int) -> tuple[dt.datetime, dt.datetime]:
    end = dt.datetime.combine(report_date + dt.timedelta(days=1), dt.time.min, tzinfo=dt.timezone.utc)
    start = end - dt.timedelta(days=max(1, lookback_days))
    return start, end


def term_regex(term: str) -> re.Pattern[str]:
    tokens = [re.escape(token) for token in re.split(r"[\s\-/]+", term.strip()) if token]
    pattern = r"(?<![a-z0-9])" + r"[\s\-/]+".join(tokens) + r"(?![a-z0-9])"
    return re.compile(pattern, re.IGNORECASE)


def score_paper(paper: Paper, config: dict) -> ScoredPaper:
    text = f"{paper.title}\n{paper.summary}".lower()
    title = paper.title.lower()
    matched: dict[str, list[str]] = {}
    score = 0
    for group, spec in config["keywords"].items():
        weight = int(spec.get("weight", 1))
        group_terms = []
        for term in spec.get("terms", []):
            if term_regex(term).search(text):
                group_terms.append(term)
                score += weight * (2 if term.lower() in title else 1)
        if group_terms:
            matched[group] = group_terms

    negative_matches = [
        term
        for term in config.get("negative_keywords", [])
        if term_regex(term).search(text)
    ]
    score -= 4 * len(negative_matches)

    # Reward intersectional papers: RL + agent/post-training signal is the main target.
    groups = set(matched)
    if "agentic_rl" in groups and "rl_post_training" in groups:
        score += 8
    if "rl_post_training" in groups and "reasoning" in groups:
        score += 5
    if "agentic_rl" in groups and "memory_and_benchmarks" in groups:
        score += 4

    reason = build_reason(matched, negative_matches)
    return ScoredPaper(
        paper=paper,
        score=max(score, 0),
        matched=matched,
        negative_matches=negative_matches,
        reason=reason,
    )


def build_reason(matched: dict[str, list[str]], negative_matches: list[str]) -> str:
    if not matched:
        return "No configured keywords matched."
    parts = []
    for group, terms in matched.items():
        shown = ", ".join(terms[:4])
        if len(terms) > 4:
            shown += f", +{len(terms) - 4} more"
        parts.append(f"{group}: {shown}")
    if negative_matches:
        parts.append("downranked: " + ", ".join(negative_matches))
    return "; ".join(parts)


def short_summary(summary: str, width: int = 320) -> str:
    summary = normalize_space(summary)
    if len(summary) <= width:
        return summary
    return textwrap.shorten(summary, width=width, placeholder="...")


def author_line(authors: list[str], limit: int = 6) -> str:
    if not authors:
        return "Unknown authors"
    if len(authors) <= limit:
        return ", ".join(authors)
    return ", ".join(authors[:limit]) + f", et al. ({len(authors)} authors)"


def markdown_report(
    scored: list[ScoredPaper],
    all_recent_count: int,
    categories: list[str],
    report_date: dt.date,
    lookback_days: int,
    min_score: int,
    warnings: list[str],
) -> str:
    lines = [
        f"# RL / Post-Training / Agentic RL Reading Queue - {report_date.isoformat()}",
        "",
        f"Source: papers.cool Atom feeds for {', '.join(categories)}.",
        f"Window: last {lookback_days} day(s). Candidates fetched in window: {all_recent_count}. Minimum score: {min_score}.",
        "",
    ]
    if warnings:
        lines.extend(["## Fetch Warnings", ""])
        lines.extend(f"- {warning}" for warning in warnings)
        lines.append("")

    if not scored:
        lines.extend(
            [
                "No papers passed the current threshold.",
                "",
                "Try lowering `min_score`, increasing `lookback_days`, or adding terms in `paper_bot/config.json`.",
            ]
        )
        return "\n".join(lines).rstrip() + "\n"

    lines.extend(["## Top Picks", ""])
    for item in scored:
        paper = item.paper
        lines.extend(
            [
                f"### {item.score} - {paper.title}",
                "",
                f"- arXiv: [{paper.arxiv_id}]({paper.arxiv_url}) | [PDF]({paper.pdf_url}) | [papers.cool]({paper.papers_cool_url})",
                f"- Authors: {author_line(paper.authors)}",
                f"- Published: {paper.updated.strftime('%Y-%m-%d %H:%M UTC')} | Categories: {', '.join(sorted(paper.categories))}",
                f"- Why it matched: {item.reason}",
                f"- Abstract skim: {short_summary(paper.summary)}",
                "",
            ]
        )

    lines.extend(
        [
            "## Tuning Notes",
            "",
            "- Edit `paper_bot/config.json` to add or remove tracked arXiv categories and keyword groups.",
            "- Good next filters to add: preferred labs/authors, exclude applied domains, or separate lists for theory RL vs LLM post-training.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def scored_to_json(scored: list[ScoredPaper], include_low_score: list[ScoredPaper] | None = None) -> dict:
    def convert(item: ScoredPaper) -> dict:
        paper = item.paper
        return {
            "score": item.score,
            "arxiv_id": paper.arxiv_id,
            "title": paper.title,
            "authors": paper.authors,
            "summary": paper.summary,
            "updated": paper.updated.isoformat(),
            "categories": sorted(paper.categories),
            "arxiv_url": paper.arxiv_url,
            "pdf_url": paper.pdf_url,
            "papers_cool_url": paper.papers_cool_url,
            "matched": item.matched,
            "negative_matches": item.negative_matches,
            "reason": item.reason,
        }

    data = {"selected": [convert(item) for item in scored]}
    if include_low_score is not None:
        data["all_scored"] = [convert(item) for item in include_low_score]
    return data


def main() -> int:
    args = parse_args()
    config = load_config(args.config)
    report_date = parse_report_date(args.date)
    lookback_days = args.lookback_days or int(config.get("lookback_days", 7))
    min_score = args.min_score if args.min_score is not None else int(config.get("min_score", 6))
    max_results = args.max_results if args.max_results is not None else int(config.get("max_results", 25))
    categories = args.categories or list(config.get("categories", []))
    if not categories:
        raise SystemExit("No categories configured.")

    papers, warnings = fetch_papers(config.get("base_url", "https://papers.cool"), categories)
    start, end = date_window(report_date, lookback_days)
    recent = [
        paper
        for paper in papers.values()
        if start <= paper.updated.astimezone(dt.timezone.utc) < end
    ]
    all_scored = sorted(
        (score_paper(paper, config) for paper in recent),
        key=lambda item: (item.score, item.paper.updated),
        reverse=True,
    )
    selected = [item for item in all_scored if item.score >= min_score][:max_results]

    output = args.output
    if output is None:
        output = Path(__file__).with_name("reports") / f"{report_date.isoformat()}_agentic_rl.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
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

    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(
                scored_to_json(selected, all_scored if args.include_low_score else None),
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    print(f"Wrote {output} with {len(selected)} selected papers from {len(recent)} recent candidates.")
    if warnings:
        print("Warnings:", file=sys.stderr)
        for warning in warnings:
            print(f"- {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
