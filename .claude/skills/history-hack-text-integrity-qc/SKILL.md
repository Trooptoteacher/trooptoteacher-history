---
name: history-hack-text-integrity-qc
description: "End-of-unit quality-control check that catches INCOMPLETE, CLIPPED, or PLACEHOLDER text before a unit ships — decks (.pptx) and workbooks (.docx). Born from a real Unit 6 defect: vocabulary definitions and answer-key rationales authored with a trailing '…' that ran off the card ('…annex the Sudetenland from…'). Run it in the final QC pass on every unit's Student Workbook, Teacher Deck, and Student Deck (alongside the lesson-flow QC and Schedule F self-score). Flags: text cut off mid-clause (ends on a dangling word + ellipsis), long text ending in an ellipsis (verify vs. an intended source elision), text that likely overflows its box (a render-confirm lead), and leftover placeholders (lorem/xxx/TODO/[insert). Deliberately does NOT flag short sentence stems ('My goal is…', 'I can…') or fill-in prompts — those ellipses are intentional. Produces a severity-ranked list (BLOCKER/MAJOR/MINOR) and exits non-zero if any BLOCKER/MAJOR, so it can gate a build. It reports; fixes go to the content owner (history-hack-unit-content-build) or the deck build."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.0"
  reference_implementation: "Unit 6 — WWII (US.45–US.58)"
  origin: "Codified after a truncated-definition defect slipped through once."
---

# History Hack — Text-Integrity QC (no incomplete or clipped text ships)

## Why this exists

We shipped a truncated vocabulary definition once — a card that read "…annex the Sudetenland from…"
and just stopped. The mistake will happen again (generators cut text to fit; edits leave a sentence
dangling). This check makes that error class **impossible to ship silently**: it reads every text
unit in the decks and workbook and flags anything that looks cut off, unfinished, or placeholder.
It is part of the standing end-of-unit QC, run beside `history-hack-lesson-flow-qc` (alignment) and
the Schedule F self-score. Accuracy is foundational (Policy 2.600); an unfinished sentence is a
content error, full stop.

## What it catches (and what it deliberately ignores)

| Signal | Severity | Example |
|---|---|---|
| Long text cut off mid-clause (dangling word **+** ellipsis) | **BLOCKER** | "…one-party dictatorship under leaders like…" |
| Long text ending in an ellipsis (confirm it isn't an intended quote elision) | **MAJOR** | "…the deaths of 6 million Jews and…" |
| Long text ending on a dangling word (no ellipsis) | **MAJOR** | "Directed U.S. grand strategy across two theaters and" |
| Text likely overflowing its box (font-size-aware estimate) | **MAJOR** (render to confirm) | a 210-char definition in a 0.46-in box |
| Leftover placeholder / TODO | **BLOCKER** | "lorem ipsum", "xxx", "TODO", "[insert date]" |
| **Intentional** — short sentence stems / fill-in prompts | *ignored* | "My goal for this unit is…", "LEARNING TARGETS — I can…" |
| **Intentional** — genuine source elision inside a quote | *MAJOR, for a human to dismiss* | "…has made this catastrophe inevitable." |

The stem/elision handling is the whole trick: an ellipsis on **short** text (≤ 70 chars) is a
prompt, not a defect; an ellipsis on **long** text is a cut-off. Never "fix" a sentence stem.

## How to run

```bash
python scripts/scan_text_integrity.py <TEACHER.pptx> <STUDENT.pptx> <WORKBOOK.docx>
# add --all to also run the low-signal "no terminal punctuation" heuristic (noisy)
```

- Text is authoritative for **truncation/placeholder** — those verdicts are reliable from the scan.
- The **overflow** finding is a *lead*: render the flagged slide (`soffice --headless --convert-to
  pdf` + `pypdfium2`/`pdftoppm`) and read it. Pixels decide whether it actually clips.
- Exit code is 1 if any BLOCKER/MAJOR remains, 0 when clean — wire it into the build gate.

## Method (two passes, like the other QC agents)

1. **Mechanical pass (authoritative for text).** Run the scanner over all three files. Every BLOCKER
   is a real cut-off or placeholder. Fix each at the source, then re-run until BLOCKER = 0.
2. **Visual pass (for overflow + borderline elisions).** Render the MAJOR-flagged slides and read
   them. Confirm overflow clips; confirm long-ellipsis endings are true elisions (keep) vs. cut-offs
   (fix). Dismiss confirmed intentional cases.

## Output

A severity-ranked list — `severity · category · file · slide/page/cell · why · snippet`. Report the
honest count. **A clean unit = 0 BLOCKER and every MAJOR either fixed or explicitly confirmed
intentional (elision) / render-verified (overflow).** When invoked inside a review harness, emit via
`ReportFindings`; otherwise print the list (the script already does) or write it to the build folder.

## Fix owner

This agent **reports**; it does not edit. Truncated/placeholder content goes back to
`history-hack-unit-content-build` (workbook) or the deck build. Completing a cut-off sentence is a
content edit — keep it historically accurate (Policy 2.600); when the correct completion is unknown,
shorten to a complete sentence rather than inventing facts.

## Reference finding (Unit 6, 2026-08)

First run flagged the systemic tail of the original defect: truncated vocabulary entries (Communism,
Appeasement) in the workbook vocab tables and both decks, **and** ~12 answer-key rationales trailing
off ("…Hitler…", "…creation of the United Nations, and…"). The short stems ("I can…", "My goal is…")
were correctly left alone. Fixes were made at the source and the scan re-run to BLOCKER = 0.
