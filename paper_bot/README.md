# Papers.cool Daily Paper Push Platform

一个每日论文推送平台：从 `papers.cool` 的 arXiv Atom feeds 拉取最新论文，按 RL、post-training、agentic RL、agent memory、reasoning 等关键词打分，入 SQLite 库，生成 Markdown/JSON 日报，提供本地 Web 面板，并可推送到飞书、GitHub Issue、通用 webhook 或邮件。

设计参考了 `justchenhao/ChatDailyPapers` 的核心流程：关键词订阅、每日自动化、LLM/摘要扩展点、GitHub Actions 定时运行。这里做成更本地优先的平台：先保证你每天有可读日报和可调规则，再按需接推送渠道。

## 快速使用

```bash
python3 paper_bot/papers_cool_bot.py
```

默认输出：

```text
paper_bot/reports/YYYY-MM-DD_agentic_rl.md
```

也可以用包装脚本：

```bash
paper_bot/run_daily.sh
```

## 平台模式

运行一次完整任务：

```bash
python3 paper_bot/platform.py run
```

启动本地面板：

```bash
paper_bot/server.sh start
```

默认地址：

```text
http://127.0.0.1:8770
```

查看最近一次结果：

```bash
python3 paper_bot/platform.py latest
```

服务管理：

```bash
paper_bot/server.sh status
paper_bot/server.sh restart
paper_bot/server.sh stop
paper_bot/server.sh logs
```

平台会生成：

- `paper_bot/data/paper_push.sqlite3`: 运行记录、论文、推送日志。
- `paper_bot/reports/YYYY-MM-DD_agentic_rl.md`: 可直接阅读的日报。
- `paper_bot/reports/YYYY-MM-DD_agentic_rl.json`: 下游集成用结构化数据。

常用参数：

```bash
# 看最近 3 天，阈值更高一点
python3 paper_bot/papers_cool_bot.py --lookback-days 3 --min-score 10

# 只看指定分类
python3 paper_bot/papers_cool_bot.py --category cs.AI --category cs.CL --category cs.LG

# 同时输出 JSON，方便后续接飞书/邮件/数据库
python3 paper_bot/papers_cool_bot.py --json-output paper_bot/reports/latest.json
```

## 配置

编辑 `paper_bot/config.json`：

- `categories`: 关注的 arXiv 分类，默认包含 `cs.AI`, `cs.CL`, `cs.LG`, `cs.RO`, `cs.MA`。
- `keywords`: 关键词组和权重。越能代表你的阅读兴趣，权重越高。
- `negative_keywords`: 用来降权的应用领域或噪声词。
- `min_score`: 进入阅读队列的最低分。
- `max_results`: 单次最多输出多少篇。

编辑 `paper_bot/platform_config.json`：

- `schedule`: 本地平台内置定时器，默认工作日北京时间 10:20。
- `push.channels`: 推送渠道。默认只启用本地文件；飞书、GitHub Issue、通用 webhook、邮件都预留好了。
- 微信推送可走 Server酱 或 WxPusher；个人微信没有官方 webhook。
- `server`: 本地面板 host/port。

## 推送渠道

飞书 webhook：

```bash
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/..."
```

然后把 `paper_bot/platform_config.json` 里 `feishu.enabled` 改成 `true`。

GitHub Issue：

- GitHub Actions 里默认使用 `GITHUB_TOKEN` 和 `GITHUB_REPOSITORY`。
- 把 `github_issue.enabled` 改成 `true` 后，每天会创建一条 issue。

邮件：

```bash
export SMTP_HOST="smtp.example.com"
export SMTP_PORT="587"
export SMTP_USER="..."
export SMTP_PASSWORD="..."
export PAPER_PUSH_EMAIL_FROM="papers@example.com"
export PAPER_PUSH_EMAIL_TO="you@example.com"
```

再启用 `email.enabled`。

## GitHub Actions

仓库已包含 `.github/workflows/daily-paper-push.yml`，默认工作日北京时间 10:20 运行：

```yaml
schedule:
  - cron: "20 2 * * 1-5"
```

Actions 会运行平台任务并提交生成的 `paper_bot/reports` 和 `paper_bot/data`。

更推荐的长期入口是 GitHub Pages，不是本地 `127.0.0.1` 服务。发布步骤见 `paper_bot/github_publish.md`。

## 适合的下一步

- 接 LLM 摘要：对筛出来的 5-10 篇生成中文三段式摘要、阅读价值判断和相关论文链接。
- 接个人阅读状态：在 Web 面板里加 Done / Later / Ignore。
- 接更细主题：例如 `LLM Agent RL`、`RLVR Reasoning`、`Memory Agent`、`Robotics RL` 分栏推送。

macOS 上如果想用 cron，每天 10:20 跑一次可以加：

```cron
20 10 * * 1-5 cd "/Users/dwy/Documents/paper reading" && paper_bot/run_daily.sh
```
