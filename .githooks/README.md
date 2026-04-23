# Local Git hooks (this repository)

`commit-msg` removes an accidental `Made-with: Cursor` trailer line from the commit message before the commit is finalized, so it cannot re-enter public history.

## One-time setup (each clone)

From the repository root:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

## Emergency: disable all hooks (rare)

```bash
git -c core.hooksPath=/dev/null commit ...
```
