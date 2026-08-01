# TEAM-Aligned Lesson Plan Generator

Deterministic, print-first generator that turns a unit's content JSON (the same
file that drives the Course Standard student workbook) into a **TEAM-aligned
teacher lesson plan** — one per standard, plus a combined unit binder.

**Pilot:** Unit 1 (US.01–US.07). Deliverables in
`../deliverables_unit1/lesson_plans/`.

## Why it exists

Tennessee teachers are evaluated on the **TEAM rubric**. A lesson plan is
directly scored on the three PLANNING indicators (Instructional Plans, Student
Work, Assessment) and should walk the teacher in ready on the Instruction
indicators. This generator produces a plan that earns the PLANNING indicators
*structurally* and documents the Instruction indicators, from content the
district already owns — so a teacher does not start from a blank page.

## Design principles

- **Deterministic.** Same input JSON → same output structure every run. No
  per-run AI variance; nothing is invented at generate time.
- **Grounded.** Every subject-specific fact (standard text, I-CAN, criteria,
  vocabulary, primary source, check-for-understanding, Tennessee connection) is
  pulled from the unit content JSON. Pedagogy scaffolding (differentiation,
  environment reminders, reflection) is constant TEAM structure.
- **Print-first.** Letter size, header/footer, page numbers, copyright. Renders
  cleanly to PDF via LibreOffice; editable DOCX ships alongside.
- **Schedule-aware.** Pacing segments scale to the block length and sum-verify
  to the total (default 47-min FHS regular block; `--minutes=43`/`41` for
  Activities/Late-Start).

## Usage

```bash
# docx is not vendored in the repo; point NODE_PATH at an install that has it
export NODE_PATH=/path/to/node_modules
node build_lessonplans.js <unit_content.json> <out_dir> [--minutes=47] [--unit="Unit 1"]

# Unit 1 pilot:
node build_lessonplans.js ../build_unit1/unit1_content.json ./out --minutes=47 --unit="Unit 1"
```

Outputs per run: `US0N_TEAM_Lesson_Plan.docx` for each standard in the unit's
`order`, a `Unit N_TEAM_Lesson_Plans_Binder.docx`, and `manifest.json`.
Render to PDF with:

```bash
libreoffice --headless --convert-to pdf --outdir <out_dir> <out_dir>/*.docx
```

## What each plan contains

Title block (standard + full TN text) · §1 Standards & Objectives (I-CAN +
sub-objectives from the standard's criteria + prior-learning link + Tennessee
connection) · §2 Assessment & Evidence (multiple measures) · §3 Structure &
Pacing (scaled, sum-verified) · §4 Activities & Materials (+ Word Bank; adds a
Geographer's Lens task when the standard carries geography data) · §5
Questioning (DOK 1–4 ladder anchored to the item bank) · §6 Thinking · §7
Grouping & Feedback · §8 Differentiation (UDL/WIDA + IEP/504) · §9 Environment
reminders · §10 Materials & Where to Print · §11 Reflection & Next Steps
(extension + MTSS Tier-2 reteach) · Appendix: TEAM rubric mapping.

## Extending to other units

Point the generator at any unit's `*_content.json` (Units 1–10 already exist
under `../build_unit*/`). Note: the pilot input `build_unit1/unit1_content.json`
has a mislabeled `unit` metadata block ("Unit 4") — the generator takes the unit
label from the `--unit` flag, so this does not affect output, but the source
metadata should be corrected when convenient.

---
© 2026 TroopToTeacher Technologies, LLC · U.S. History Hack™
