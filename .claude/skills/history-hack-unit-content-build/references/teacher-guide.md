# Teacher How-to-Use & MTSS Guide

A standalone teacher companion (the "keep-separate" answer keys), generated with `python-docx` to
the canonical brand (0.8"/0.9" margins, Calibri, navy `#1B2A4A` H1/H2, red `#B22234` H3, gold
`#C89B3C` header, page-numbered footer). Reference generator: `scripts/build_teacher_guide.py`
(~18 pp on Unit 6).

## Contents
1. **Cover** — "Teacher How-to-Use & MTSS Guide", marked keep-separate-from-students.
2. **How to Use This Workbook** — the 7-activity cycle; **pacing across the three schedule
   variants** (46-min regular, 43-min activities, 41-min late-start) with the **Exit Ticket
   protected** in every variant; front/back printing model.
3. **UDL · MTSS Implementation** — CORE PATH + the three back-page supports (when to assign each),
   Response Choice, and the IEP/504 non-replacement guardrail.
4. **CER Scoring Rubric** — Claim / Evidence / Reasoning / Conventions, 1–4 (/16), scoring bands.
5. **Per-Standard Answer Keys & Reteach** — for each standard: Practice-Quiz key with per-item
   rationale (from the bank's `explanation`), Exit-Ticket key with rationale, and a reteach move.
   Worked CER/HIPPO models live on the student workbook's support pages (reference them, don't
   duplicate).

## Data it needs (gather before running)
- `quiz_with_exp.json` — the final 4 items/standard (from `references/quiz-sourcing.md`) with the
  bank `explanation` attached. Clean each rationale to 1–2 substantive sentences (drop generic
  "X is incorrect…" filler and never truncate mid-sentence).
- `exit_tickets.json` — per standard the exit-ticket stem, options, and the verified correct letter.
- Per-standard `TITLES`, `EXIT_RAT` (one-line rationale), and `RETEACH` (one targeted move) maps.

## Adapting the script per unit
`scripts/build_teacher_guide.py` embeds Unit 6's content dicts (`quiz`, `TITLES`, `EXIT_RAT`,
`RETEACH`) and reads `quiz_with_exp.json`/`exit_tickets.json` from a scratchpad path. For a new
unit: regenerate those JSONs from that unit's bank picks + exit tickets, replace the per-standard
dicts, and update the standard codes/titles and the scratchpad path. Everything else (styling,
layout, helpers) is unit-agnostic. Render + apply the QC gate (zero blank pages) before shipping.
