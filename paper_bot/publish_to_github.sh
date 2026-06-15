#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 https://github.com/<user>/<repo>.git [branch]" >&2
  exit 2
fi

REMOTE_URL="$1"
BRANCH="${2:-master}"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

git add .github .gitignore paper_bot

if git diff --cached --quiet; then
  echo "No staged changes to commit."
else
  git commit -m "feat: add daily paper push platform"
fi

git push -u origin "$BRANCH"

cat <<MSG

Pushed to GitHub.

Next steps:
1. Open the GitHub repository.
2. Go to Settings -> Pages.
3. Set Source to GitHub Actions.
4. Go to Actions -> daily-paper-push -> Run workflow.

After the first successful run, the stable page should be:
https://<user>.github.io/<repo>/
MSG
