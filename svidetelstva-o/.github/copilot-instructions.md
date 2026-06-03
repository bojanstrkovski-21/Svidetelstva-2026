# Copilot Instructions

## Core Rules

- Read `PROJECT.md` before starting any task if it exists in the workspace root
- State exactly what you intend to change and why, then wait for explicit **yes** before touching any file — never assume confirmation
- A yes is only valid for what was explicitly proposed — do not extend scope beyond what was agreed
- If the user re-asks after you proposed something and asked for confirmation, just implement — they confirmed implicitly
- After plan approval, execute all steps without mid-plan check-ins
- Prefer editing existing files over creating new ones
- Ask before creating any new file
- Do not over-engineer: only make changes that are directly requested or clearly necessary
- Do not add comments, docstrings, or error handling beyond what was asked
- Never edit any file listed under **Frozen Files** in `PROJECT.md` without explicit instruction naming that file

## Git

- Never run git commands unless the user explicitly asks
- Never suggest committing, pushing, branching, or tagging
- Never perform any git operation automatically
- You may use `git add .` if `.gitignore` is present and up to date, but review the file list before committing.
- Never create git tags
- Never amend published commits
- Never force push

## Session Workflow

- When the user says **"start session"**, follow `.github/prompts/session-start.prompt.md`
- When the user says **"end session"** or **"wrap up"**, follow `.github/prompts/session-end.prompt.md`
- When the user says **"init git"** or **"do git"**, follow `.github/prompts/git-init.prompt.md`
- When the user says **"push it"** or **"commit push"**, follow `.github/prompts/git-commit.prompt.md`
