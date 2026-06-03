---
description: "Commit and push changes to the git repository. Use when: push it, commit push, save to git, git push, git commit, push changes."
agent: "agent"
---

# Git Commit & Push

Save and push the current work to GitHub.

## Steps

1. Run `git status` — show the user exactly what has changed (modified, new, deleted)

2. Ask: **"Which of these files should be included in this commit?"**
   - List each changed file clearly
   - Wait for the user to confirm — never assume all files should be included

3. Ask: **"What is the commit message?"**

4. Run `git add .` if `.gitignore` is present and up to date, otherwise add only confirmed files.

5. Run `git commit -m "[message]"`

6. Run `git push`

7. Confirm success

---

## Rules

- You may use `git add .` if `.gitignore` is present and up to date, but always review the file list before committing.
- Never create branches, tags, or modify anything beyond what was asked
- Never amend published commits
- Never force push
- If `git push` fails because the remote has new commits, tell the user and ask how to proceed — do not auto-pull or rebase
