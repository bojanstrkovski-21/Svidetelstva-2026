# Svidetelstva

## Overview
Web application for a secondary school in North Macedonia to fill in and print student certificates (сведителства) on official Ministry of Education paper forms (Образец број 20). The paper is pre-printed by the state — the app prints only text at exact coordinates on top of it. Used by ~43-46 class teachers and 1-3 administrators.

> **Diplomas are out of scope for now** — there are several types and scans are not yet available. Once the certificate part is fully working and tested, diplomas are the immediate next phase.

## Stack
- **Language**: Python (backend), HTML, CSS, JavaScript (frontend)
- **Framework / Tools**: Flask, Tailwind CSS
- **Database**: SQLite — single file, no separate DB server needed
- **Hosting**: one school computer on the local network; all users connect via browser using local IP (e.g. `http://192.168.1.x:5000`)

## Certificate Fields (Образец број 20 — new form)

### Сведителство — Side 1
- Назив на средното училиште *(fixed, set once in settings)*
- Општина/Град Скопје *(fixed, set once in settings)*
- Главна книга бр. + /20__ година
- За завршена __ година (со римски број и со букви)
- Ime и презиме на ученикот/ученичката
- Син/ќерка на __ (ime на родителот/старателот)
- Роден/а на __ година
- Во __ општина __
- Држава __ државјанство __
- Во учебната 20__/20__ година по __ (со букви) пат учеше во __ (со римски број и со букви) година
- Наставни предмети/модули + Успех (со букви) + оценка (број) — rows continue onto side 2

### Сведителство — Side 2
- Наставни предмети/модули + Успех — 4 continuation rows *(top of page)*
- Поведение *(dropdown)*
- Изостаноци: оправдани __ неоправдани __ *(below поведение, same section)*
- Според постигнатиот успех ученикот/ученичката заврши __ година (со римски број и со букви)
- (гимназиско/стручно/уметничко) + (подрачје/струка/сектор/насока)
- (образовен профил/квалификација) со општ успех __
- Во __ (место) __ (датум) 20__ година. Дел. бр. __
- Раководител на паралелката *(потпис)*
- Директор *(потпис)*
- Училиштето е верифицирано со акт број __ од __ (датум) година, издаден од __

## Input Types
| Field | Type |
|---|---|
| Назив на училиштето | Fixed (set once in settings) |
| Општина на училиштето | Fixed (set once in settings) |
| Паралелка | Dropdown |
| Предмети/модули | Dropdown (from Google Sheets / Excel import) |
| Поведение | Dropdown |
| Држава на раѓање | Dropdown (list of countries) |
| Град на раѓање — Македонија | Dropdown (macedonian cities) |
| Град на раѓање — странство | Manual text field |
| Сите останати полиња | Manual text input |

## Access Levels
- **Admin accounts (1-3)**: full access — manage users, students, subjects, classes, print all certificates
- **Teacher accounts (8-16)**: each assigned to specific паралелки — can only see and fill certificates for their assigned classes

## Database Tables (SQLite)
- **users** — accounts with role (admin/teacher) and assigned classes
- **students** — ~850 records (name, parent, birth info, паралелка, etc.)
- **subjects** — subjects grouped by струка/профил
- **classes** — list of паралелки
- **behavior_types** — поведение options
- **countries** — country dropdown list
- **certificates** — saved certificates with all filled fields, status (draft/ready)

## Workflow
1. Teacher logs in → sees only their assigned classes
2. Selects class → selects student → fills in certificate fields → saves to DB (status: ready)
3. At the print station: admin opens saved certificates, previews with background scan to verify coordinate alignment
4. If coordinates need adjustment — adjust before printing
5. Print — only text is sent to printer, background scan is hidden

## Conventions
- All field coordinates stored in mm — independent of scan resolution and printer
- Scan of the official form used as background for visual alignment only — hidden at print time
- Coordinates adjustable before printing in case form batches from Ministry have slight differences
- Dark/light mode toggle, preference saved in localStorage
- Macedonian (Cyrillic) and Latin input both supported — depends on OS keyboard layout

## Constraints
- No JavaScript framework (no React, Vue, etc.) — plain HTML/CSS/JS frontend only
- All data stays on the school local network — no cloud, no Google, no Microsoft
- Never print the background scan — only text at exact coordinates
- Login required — app is not accessible without valid credentials

## How to Run
```bash
pip install flask
python app.py
# Open browser on any school PC: http://<server-ip>:5000
```

## Current State
- Planning phase complete
- PROJECT.md fully updated
- Awaiting: scan of certificate form (for coordinate mapping), Excel with subjects/струки/profiles

## Next Steps
1. Set up Flask project structure and SQLite schema
2. Build login system (admin + teacher accounts)
3. Build data entry form with all dropdowns (students, subjects, classes, countries, поведение)
4. Build certificate preview with background scan + text overlay
5. Implement save to DB (status: ready)
6. Implement print function (text only, no background)
7. Build admin panel — manage users, students, subjects, classes
8. Test with real form scan and adjust coordinates

## Recent Work
- 2026-05-23 — Project initialized, PROJECT.md filled from planning conversation
