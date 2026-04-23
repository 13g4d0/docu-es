# Private repository and push workflow

## Goals

- Keep **GitHub private** for `docu`.
- **Push only at milestone boundaries** (agreed slices of documentation), not on every micro-edit.
- Never store **API keys**, tokens, `.env` values, or customer-specific connection details in tracked files.

## What the automation (or a build agent) needs to `git push`

After you switch the repo to **private**, pushes still use normal Git auth. Typical options:

1. **Deploy key (read/write)**  
   Generate an SSH key pair dedicated to this repo, add the **public** key in GitHub → *Settings → Deploy keys* (allow write if you want pushes from CI/agent). Store the **private** key only on the host that runs pushes, with file permissions `0600`. Do not paste private keys into tickets or chat.

2. **Personal access token (HTTPS)**  
   Prefer fine-scoped classic PAT or GitHub App token with **contents: write** on this repo only. Configure `git credential` or `GIT_ASKPASS` on the push host. Never commit the token; never paste it into the documentation repo.

3. **Human push from your laptop**  
   Clone the private repo with your normal GitHub auth (`gh auth login`, SSH agent, etc.), pull milestone work, then push. No extra secrets on the server.

The assistant does **not** need you to share tokens or private keys in chat. If push from the server is required, configure auth on that server using one of the patterns above, then say “push is configured” and request a milestone push when ready.

## Milestone cadence

1. Accumulate doc changes locally until a **milestone** from `ROADMAP-MILESTONES.md` is complete.
2. Review diff for accidental secrets (grep for `Bearer`, `sk-`, `key=`, private IPs if your policy forbids them, etc.).
3. Single commit (or a small, logical set) with a clear message referencing the milestone id (e.g. `docs(M1.2): system context diagram`).
4. `git push origin main` (or your release branch policy).

## If the repo was public and is now private

- Update remotes if the URL changes (usually unchanged).
- Re-audit `git log` and file history for anything that should not exist even in a private repo (defence in depth).
