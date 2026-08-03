# Unit 6 — Manual QC Package (read me first)

This ZIP is the current Unit 6 Course-Standard set for your manual quality control.
The two files I changed this session are the **Student Workbook** and the **Teacher
Guide** — QC those first. Everything else (decks, assessment book, organizer toolkit,
covers) is included unchanged, for context.

## What changed this session (QC these)

### 1. Student Workbook — `Unit6_Student_Workbook_CourseStandard.docx`
- **Self-scoring rubric on every constructed response.** After the student writes and
  self-checks, they score their OWN work on the same rubric the teacher and the web app
  use, then take it online to compare:
  - **Activity 7 (CER):** "SCORE YOURSELF" grid — Claim / Evidence / Reasoning × levels
    4–1, student marks each and totals /12.
  - **Activity 5 (HIPPO):** compact source-analysis self-scoring rubric.
  - **Final Unit Reflection:** CER self-scoring rubric.
  - Each is followed by a **"Now check yourself on the History Hack web app"** call-out
    (type it in → instant rubric feedback → compare to your own score → revise).
- **Supports-page white space now carries a self-monitoring tracker** (from the prior
  session, included here): a light MY CHECK-IN strip on Activities 1–6 (goal / confidence
  / a Future-Ready line) and a full STANDARD WRAP tracker on Activity 7 (goal met +
  missing-work audit + self-quiz score + Future-Ready).
- **All writing on ruled notebook lines**, including the back-matter "Reflect" prompt
  (previously had no lines).

### 2. Teacher Guide — `Unit6_Teacher_HowToUse_and_MTSS_Guide.docx`
- **§15 rewritten** so teacher, student, and app read ONE rubric:
  - **15a** prints the IDENTICAL student self-scoring grid.
  - **THE WEB-APP CHECK** call-out: use the student's self-score-vs-app-score gap as a
    formative signal.
  - **15b** keeps your 6-point holistic scale and adds a **/12 → 6-point crosswalk**.
  - (This removed a stale line that said students score on a "Full / Developing /
    Beginning" scale — they don't anymore.)

## Automated QC already run (passing)
- Text integrity (no clipped/placeholder text): **0 blocker / 0 major / 0 minor** on both.
- Accessibility font floor: **0 text runs under 9pt** on both (incl. page numbers).
- Every image carries alt text; every rubric/writing table has a header row.
- 29 self-scoring rubrics + 29 web-app CTAs present in the workbook.

## What YOU still need to render-confirm (I could not, in this environment)
LibreOffice PDF conversion is blocked in the remote sandbox, so I built and verified the
`.docx` masters but could **not** produce fresh PDFs. On your build box:

1. Run `bash HistoryHack_Platinum/build_unit6/finish_unit6.sh` (or convert the two DOCX
   with `HOME=/root/lohome soffice --headless --convert-to pdf FILE`).
2. **No-bleed check (important):** the CER (Activity 7) and HIPPO (Activity 5) pages are
   now denser. Confirm the Exit Ticket and analysis don't spill onto a near-empty leaf.
   If they do, tell me and I'll compact those pages.
3. Confirm notebook lines render on every ruled page and there are zero blank pages.

## Stale artifact note
- `Unit6_Teacher_HowToUse_and_MTSS_Guide.pdf` in this ZIP is the **pre-change** render —
  regenerate it from the refreshed `.docx`.
- There is no workbook PDF yet — generate it from the refreshed `.docx`.
