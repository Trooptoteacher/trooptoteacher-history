---
name: history-hack-narrative-textbook-builder
description: "Builds and edits the History Hack **narrative illustrated textbook** — the story-driven, primary-source-illustrated student *reader* (reference edition: **\"To Form a More Perfect Union\"**, U.S. History, released in 5 parts across Units 1–10) — via the WeasyPrint print path (content JSON → HTML → the locked B&W-safe print contract → PDF). This is a DISTINCT product from the 7-activity Course Standard unit workbook (that is `history-hack-unit-content-build`) and from the DBQ SKU (`history-hack-dbq-workbook`); it is the illustrated narrative course a student reads. **Course-parameterized** via `courses/<id>/course.json` (U.S. History is the reference/default; also builds World History, Government, Grade 6/7/8, Tennessee editions with identical structure and gates). Owns: the full-bleed cover, the founder's foreword, the one-page Flight-Crew spread, per-standard **\"stops\"** (hook → primary-source image + a two-tier right column of a Source-It-First WHO/WHEN/WHY sourcing band and an **HVT \"High-Value Target\" must-know box** → EN/ES Word Wall → Tennessee Connection → Flight-Log cue), **CER writing pages** (claim + evidence + self-grade rubric + \"Writing Lab\" workbook⇄app handoff), the **Arc-of-the-Union coordinate-plot section** (students score each milestone −3…+3, plot the points, connect the arc, then read it cross-curricular with math (slope/mean/extrapolate) and science (pattern/turning point)), the **B&W-safe print contract**, per-page copyright footer + page numbers, the LOCKED **white-space ≥90% value rule** enforced by a build-time page-fill QC gate, and the matching **Flight Log companion** (write-in student log with a brand cover and a bidirectional Textbook-Stop-N ⇄ Flight-Log-Entry-N cross-reference generated from the same stop data so it can't drift). Use when asked to build, edit, reformat, fill white space in, re-cover, add a foreword to, add the Arc plot to, or reprint the narrative textbook / the 'To Form a More Perfect Union' PDFs for any unit or course; and to edit the existing Part 1–5 PDFs in code instead of by hand."
license: Proprietary
metadata:
  author: "Sean Reynolds / TroopToTeacher Technologies LLC"
  version: "1.0"
  reference_implementation: "To Form a More Perfect Union — U.S. History, Part 1 (Units 1–3); proof rendered on Unit 1 / US.01 (front matter → Stop 1 → Arc-of-the-Union coordinate plot)"
  product: "Narrative illustrated textbook (student reader) — NOT the unit workbook, DBQ packet, decks, or organizer toolkit"
  render_path: "content → HTML → WeasyPrint → PDF, governed entirely by references/print-contract.css"
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, edit, or QC ANY
> artifact — including this narrative textbook — from memory, a cached copy, or a prior session. **Re-read the
> CURRENT version of THIS skill from `main` first** — skills are the single source of truth and change only via
> skills-only PRs. Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix (US/GC/W/TN/…), and **never** read from or write to the protected
> `us-history` flagship on a non-US build. If you cannot confirm you are on the current skill, STOP and pull it.

# History Hack — Narrative Illustrated Textbook Builder

Load `history-hack-platinum-standard` first (mission, decision rule, tier convention). This skill owns **one
job**: the illustrated narrative *reader* a student reads cover-to-cover — the "To Form a More Perfect Union"
product line. It does not build the unit workbook, the decks, the DBQ packet, the organizer toolkit, or the
assessment bank; those have their own owners (see `SKILLS.md`).

## What this product is (and is not)

- **IS:** a story-driven, primary-source-illustrated textbook, written in the voice of the house author
  ("Sam Calloway"), with a recurring **Flight Crew** (Archive/J. Troop, Spark, Co-Pilot, Navigator, Notetaker,
  Sam Calloway, MSgt "Muck") who *guide*, and composite **era-friends** who lived the year. One **stop per
  standard**. Released per course in **parts** (US History = 5 parts, Units 1–10).
- **IS NOT:** the 7-activity Cornell unit workbook (`history-hack-unit-content-build`), the DBQ SKU
  (`history-hack-dbq-workbook`), the decks (`history-hack-tcap-deck-builder` / `-lean-deck-builder`), or the
  organizer toolkit (`history-hack-graphic-organizer-workbook`).

## Reference implementation

`references/render_textbook.py` + `references/print-contract.css` render the reference proof (Unit 1 / US.01).
`references/build-and-edit-conventions.md` is the LOCKED spec: page order, the stop template, the value-block
menu, the Arc-of-the-Union plot spec, the crew/cover/foreword conventions, the edit-in-code workflow, and the
page-fill QC gate. Build to that spec; do not re-derive it from a rendered PDF.

## Course parameterization

Resolve the course from `courses/<id>/course.json` (`id`, `displayName`, `standardsPrefix`, `standardsFile`).
Derive every label, standard code, footer, and "Tennessee/State Connection" from it — never hardcode
U.S. History / US.01 / TCAP. Defaults to the U.S. History flagship. Narrative + illustrated text is sourced
from the canonical banks in `history-hack-web-app` (primary-sources/images/questions) and the per-course
`content-build/<course>/narrative/unit-NN.json` — **never invent a citation or a source** (Policy 2.600).

## LOCKED gates (run before any part ships)

1. **Page-fill ≥ 90% (build gate).** The renderer measures every page's fill below the running footer and
   FAILS the build if any non-exempt page is < 90%. Exempt: the full-bleed **cover** and the **foreword**
   (fills once personalized). When a page is short, add **value, not filler** — see the value-block menu.
2. **B&W-safe.** Interior prints in black-and-white: dark ink on white/light tints, never white-on-navy or
   gold-on-navy for reading-critical content; color-encoding maps flagged `colorKey` with a "see the deck"
   note. (Guardrail #6.)
3. **Per-page © footer + page number**, running head/foot owned by the print contract.
4. **No internal pages in a distributed file** — strip the "Permissions & Publishing Checklist" and
   print-production/spine notes from any teacher/student-facing download.
5. **Invoke** — do not re-implement — the shared release gates: `history-hack-print-qc-auditor` (print
   defects), `history-hack-text-integrity-qc` (no clipped/placeholder text), `accessibility-qc-agent`
   (WCAG/UA), `historian-factcheck-agent` (Policy 2.600), `tn-textbook-adoption-agent` (Schedule F),
   `ell-bilingual-review-specialist` (EN/ES + ELL), `copyright-integrity-accreditation` (IP/FERPA/COPPA).

## The white-space value rule (LOCKED)

Meaningful white space is a missed teaching moment. Any short page earns a **value block** — a check-in,
self-assessment, prediction/anticipation guide, reflection, plot/data activity, or Future-Ready/ACT-Ready
tie — chosen for high-impact pedagogy (Hattie ≥ 0.40), never filler. The `.value` component and the block
menu live in `references/build-and-edit-conventions.md`.

## Editing the existing PDFs

The already-shipped Part 1–5 PDFs were authored ad hoc and have **no code source**; do not hand-edit the
flattened PDF. Bring the target part into this pipeline (extract images to `references/assets`, capture text
into the course narrative JSON), apply edits in the content + contract, re-render, pass the QC gate, then
replace the served PDF in `history-hack-web-app/public/textbook-pdf/`. See the edit workflow in the
conventions reference.

## Serving

Rendered PDFs are served from `history-hack-web-app/public/textbook-pdf/` (full-book parts + per-unit splits)
and surfaced on the `/textbook` reader. Per-unit split = cover + How-This-Book-Works + that unit + image
credits; the full part is the complete volume. Register new parts in `app/textbook/page.tsx`.
