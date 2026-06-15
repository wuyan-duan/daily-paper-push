# GitHub 发布方式

这个项目现在按 GitHub-first 设计：

- GitHub Actions 每个工作日北京时间 10:20 自动运行。
- 每次运行生成 `paper_bot/site/index.html` 静态日报。
- GitHub Pages 发布一个长期可访问的网址。
- GitHub Issue 自动创建一条每日推送通知。

## 第一次发布

创建一个 GitHub 仓库后，在本地执行：

```bash
paper_bot/publish_to_github.sh https://github.com/<your-user>/<your-repo>.git
```

然后到 GitHub 仓库：

1. 打开 `Settings -> Pages`。
2. Source 选择 `GitHub Actions`。
3. 打开 `Actions` 页，手动运行 `daily-paper-push` 一次。

运行成功后，入口一般是：

```text
https://<your-user>.github.io/<your-repo>/
```

## 自动推送

默认会创建 GitHub Issue，因为 workflow 中设置了：

```yaml
PAPER_BOT_GITHUB_ISSUE: "1"
```

如果还要推飞书，在仓库 `Settings -> Secrets and variables -> Actions` 里添加：

```text
FEISHU_WEBHOOK_URL
```

并在 `paper_bot/platform_config.json` 里把 `feishu.enabled` 改成 `true`。

## 推送到微信

个人微信没有官方 webhook，需要通过第三方服务：

### Server酱

1. 打开 https://sct.ftqq.com/ ，微信扫码登录并获取 `SendKey`。
2. 在 GitHub 仓库 `Settings -> Secrets and variables -> Actions` 添加：

```text
SERVERCHAN_SENDKEY
```

3. 把 `paper_bot/platform_config.json` 里的 `serverchan.enabled` 改成 `true`。

### WxPusher

1. 打开 https://wxpusher.zjiecode.com/docs/ ，创建应用，获取 `appToken` 和你的 `uid`。
2. 在 GitHub Secrets 添加：

```text
WXPUSHER_APP_TOKEN
WXPUSHER_UID
```

3. 把 `paper_bot/platform_config.json` 里的 `wxpusher.enabled` 改成 `true`。

## 注意

`127.0.0.1` 只适合本地调试。长期入口应使用 GitHub Pages 或 GitHub Issue。
