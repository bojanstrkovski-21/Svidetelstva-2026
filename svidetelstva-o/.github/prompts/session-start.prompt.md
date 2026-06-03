---
description: "Start a new or continue an existing work session. Use when beginning work — new project or returning to one."
agent: "agent"
---

# Session Start

Read `PROJECT.md` in the workspace root.

---

## New Project (PROJECT.md is empty or has unfilled placeholders)

Ask the user the following questions **before doing anything else**:

1. What does this project do? (one sentence)
2. What language / stack / framework?
3. Any hard constraints or preferences? (e.g. no external libraries, target OS, style rules, things to never do)
4. What is the goal for this first session?

Then fill in `PROJECT.md` using the answers. Show the full proposed content and wait for confirmation before writing.

---

## Continuing Project (PROJECT.md exists and is filled in)

1. Read `PROJECT.md` fully
2. Show a compact summary:
   - Project name and what it does
   - Stack
   - Current state
   - Next steps
3. Ask: **"What is the goal for this session?"**
4. Confirm you are ready and what context you have loaded

---

## Rules that apply for the entire session

- Do NOT run any git commands
- Do NOT suggest committing, pushing, branching, or tagging
- Confirm before making any file changes — state what you intend to change and why, then wait
- If the user re-asks after you proposed something and asked for confirmation, just implement — they confirmed implicitly
- After plan approval, execute all steps without mid-plan check-ins
- Prefer editing existing files over creating new ones
- Ask before creating any new file
- Do not touch any file listed under **Frozen Files** in PROJECT.md without explicit instruction

---

## Reminder to show the user at the end of session-start

> **Before closing VS Code, always say "end session" first.**
> Closing without ending the session means PROJECT.md won't reflect where you stopped — next session-start will have stale context.
