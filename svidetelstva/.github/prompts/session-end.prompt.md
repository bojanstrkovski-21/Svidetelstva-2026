---
description: "End the current work session. Use when done working and want to wrap up, summarize what was accomplished, and update project context."
agent: "agent"
---

# Session End

Wrap up the current work session.

## Steps

1. **Summarize** what was accomplished this session in 3–5 bullet points

2. **Propose updates to `PROJECT.md`:**
   - Add an entry to the **Recent Work** section: `YYYY-MM-DD — [what was done]`
   - Update **Current State** if it changed
   - Update **Next Steps** to reflect what remains or what comes next

3. **If `TODO.md` exists** in the workspace root, propose updates to it as well — tick completed items, add newly discovered tasks

4. **Propose 1–2 tips** learned or reinforced this session and write them to `/memories/best_practices.md`
   - Each tip: one short title + one or two sentences explaining when and why it matters
   - Check what is already there first — do not repeat existing tips

5. **Update `/memories/projects.md`** — append one line:
   `YYYY-MM-DD — [project name] — [one sentence: what was done this session]`
   Create the file with a `# Project History` heading if it does not exist yet

6. Show all proposed changes and ask for confirmation before writing anything

---

## Rules

- Do NOT run any git commands
- Do NOT suggest committing, pushing, branching, or tagging
- Do NOT perform any git operation
- Only update files the user confirms
