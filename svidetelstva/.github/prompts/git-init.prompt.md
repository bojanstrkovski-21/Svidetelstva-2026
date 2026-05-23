---
description: "Initialize a git repository, create .gitignore, connect to GitHub remote, and make the first commit. Use when: init git, do git, setup git, create repo, git setup."
agent: "agent"
---

# Git Init

Set up version control for this project from scratch.

## Steps

1. Run `git status` — if a git repo already exists, say so and stop

2. Read `PROJECT.md` to get the project name and stack

3. Run `git init`

4. Propose a `.gitignore` based on the stack from `PROJECT.md`
   - Show the full proposed content
   - Wait for confirmation before writing
   - Ask if anything should be added or removed

5. Ask: **"What is your GitHub username?"**

6. Tell the user:
   > Create a new **empty** GitHub repo named **[project-name]** at https://github.com/new
   > Important: do NOT check "Add README", "Add .gitignore", or "Choose a license" — the repo must be completely empty.
   > Come back here when it is created.

7. Wait for the user to confirm the repo is created

8. Run:
   ```
   git remote add origin https://github.com/[username]/[project-name].git
   git branch -M main
   ```

9. Show `git status` and ask: **"Which of these files should go in the first commit?"**
   - List the files available
   - Never assume — wait for the user to confirm

10. Ask: **"What should the commit message be?"** (suggest: `initial commit`)

11. Run `git add .` if `.gitignore` is present and up to date, otherwise add only confirmed files.

12. Run `git commit -m "[message]"` then `git push -u origin main`

13. Confirm success and show the repo URL: `https://github.com/[username]/[project-name]`

---

## Rules

- You may use `git add .` if `.gitignore` is present and up to date, but always review the file list before committing.
- Never create branches or tags unless explicitly asked
- Never push without user confirming the file list and commit message first
