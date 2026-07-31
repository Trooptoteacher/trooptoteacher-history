# Unit 6 — Student Workbook (Course Standard Edition) — Build Status

**Working file:** `Unit6_Student_Workbook_CourseStandard.docx` (editable, authoritative)
**Render:** `Unit6_Student_Workbook_CourseStandard.pdf` (QC proof)
**Reference model:** Standard US.45, locked in `00_START_HERE/PLATINUM_REFERENCE_BUILD/`
**Standard:** `00_START_HERE/STUDENT_WORKBOOK_PLATINUM_STANDARD.md`

## Current state
- **164 pages, zero blank / near-empty pages** (verified page-by-page against the §7.5 QC gate).
- All **14 standards (US.45–US.58)** present, each running the 7-activity cycle.
- Front matter complete: cover, copyright/licensing, Unit at a Glance, SSP crosswalk,
  UDL/accessibility matrix, how-to-use, before-you-begin.

## Blank-page defect — RESOLVED
The earlier propagation (US.46–US.58) left 19 blank/near-empty pages. Root causes and fixes:
1. **Front-matter stray page** — empty page-break paragraphs after full pages → converted to
   `pageBreakBefore` on the next heading and removed the empty carrier paragraphs.
2. **Vocabulary orphans** — extra on-page writing lines after "MAKE IT YOURS" (a notebook /
   whiteboard redirect box) spilled to the next page → removed to match US.45.
3. **Intro-page orphans** — HOOK ("think before you dig in") and ACTIVATE ("jot notes in your
   notebook") carried redundant on-page writing lines (both redirect to the notebook) → removed
   uniformly. Four intros with an extra ★ Tennessee Connection box were tightened to fit one page.
4. **Vocabulary "MAKE IT YOURS" spill** — tightened the knowledge-rating grid rows (rating cells
   need only a small mark, not a full writing line) and word-bank line spacing across all 14
   standards so the vocab front page holds its full content.

## Remaining work (not yet done)
- **Phase 2 — back-page supports for US.46–US.58** to match US.45: VOCABULARY SUPPORTS,
  HIPPO SUPPORTS (source analysis), and WRITING SUPPORTS (CER). US.45 already has these.
- **Phase 3 — per-standard content polish**: strong standard-specific HOOKs (some currently
  restate the standard verbatim), worked-example models, and quiz self-check answer keys
  (derive per item; flag for teacher-key cross-check).
- **Teacher edition** of the workbook.
- **Slide decks** (student + teacher) to Course Standard palette/format.
- **Deck ↔ workbook slide-keying** (deferred until decks exist — see standard §7.8).
