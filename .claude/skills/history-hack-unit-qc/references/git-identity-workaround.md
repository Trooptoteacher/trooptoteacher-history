# Git Identity and Push Workarounds

Sandbox-specific gotchas for the history-hack-web-app repo.

## `git config --global` does NOT persist

The sandbox resets global git config between sessions. Use the `-c` flag on every commit instead:

```bash
git -c user.name="Sean Reynolds" -c user.email="trooptoteacher31@gmail.com" commit -m "..."
```

**Do not** try:
```bash
git config --global user.name "..."   # ❌ won't persist
git config --global user.email "..."  # ❌ won't persist
```

## Push authentication

The repo is pushed through an authenticated proxy. On every bash call that does `git push`, include:

```python
api_credentials=["github"]
```

The proxy is `git-agent-proxy.perplexity.ai`. The `origin` remote URL should be:

```
https://git-agent-proxy.perplexity.ai/Trooptoteacher/history-hack-web-app.git
```

If someone tries to push without `api_credentials`, it will fail with an auth error.

## Standard commit-and-push pattern

```bash
cd /home/user/workspace/hh-eval/history-hack-web-app && \
  git add <files> && \
  git -c user.name="Sean Reynolds" -c user.email="trooptoteacher31@gmail.com" \
    commit -m "Unit N QC {band}: ..." && \
  git push origin main
```

Run with `api_credentials=["github"]`.

## Identity on record

- Name: Sean Reynolds
- Email: trooptoteacher31@gmail.com
- GitHub org/user: Trooptoteacher

## Branch

Always work on `main`. This repo does not use feature branches. Commit messages should be descriptive enough to serve as the audit trail.

## Pre-commit Validation

Before committing, always validate:
1. JSON files parse correctly (`python3 -c "import json; json.load(open('file.json'))"`)
2. TypeScript files type-check (if touching `lib/` or `data/`)
3. PDF builds cleanly if textbook/unit-N.json was modified
