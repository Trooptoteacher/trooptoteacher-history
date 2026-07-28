# Workbook per-standard activity structure (what the deck aligns to)

The History Hack student workbook runs the same activity sequence for every standard.
The teacher deck's "LESSON → WORKBOOK MAP" slide references these by number, so keep the
names exact. Source: `build_workbook_u<N>.js` headings.

| # | Workbook section (per standard) | Deck slide that drives it |
|---|---------------------------------|---------------------------|
| — | Standard `code` — `title` (opener, "I can") | STANDARD divider |
| — | Before You Begin — Set Your Goal | QUICK REVIEW · CONFIDENCE · HOOK |
| 1 | Activity 1 — Vocabulary (Part A: Reference / Word Bank), EN + ES | KEY VOCABULARY · Word Wall |
| 2 | Activity 2 — Vocabulary Studio (Frayer-inspired) | KEY VOCABULARY · Word Wall |
| **3** | **Activity 3 — Direct Teaching Cornell Notes** (+ Guided / Light Support backs) | **DIRECT INSTRUCTION ×3–4** |
| 4 | Activity 4 — Close Read | PRIMARY SOURCE ANALYSIS |
| — | Geographer's Lens (only when SSP.06 / geo is active) | (DI slide with geographic reasoning) |
| 5 | Activity 5 — Primary Source / Data Analysis | PRIMARY SOURCE ANALYSIS |
| 6 | Activity 6 — Core Application: Practice Quiz | CHECK FOR UNDERSTANDING + ANSWER REVEAL |
| 7 | Activity 7 — Constructed Response (CER) | STUDENT ACTIVITY |
| — | Your Tennessee Connection / Local History Investigation | (TN connection called on the map slide) |
| — | Progress Tracker & Cumulative Review (unit-level) | WRAP-UP |

## The hard requirement — Activity 3 ↔ Direct Instruction
`standards[code].criteria` (the Cornell cues) must equal the deck's DIRECT INSTRUCTION slide
labels, verbatim. This is what lets students take Cornell notes live during the teacher's
direct instruction with the same words on the screen and on the page. `extract_align.py`
checks this and prints EXACT / review per standard.

When the deck has one more DI slide than the workbook has cues (US.03/04/07 in Unit 1), the
extra slide is deeper detail that folds into the existing cues — students capture it in the
Cornell "Key terms →" row. The map slide states this explicitly rather than inventing a 4th cue.

## Cornell cue phrasing in the workbook
The workbook renders each cue as a question: *"What does the passage say about `<criterion>`?"*
plus a final *"Key terms →"* row. The deck map slide shows the criterion itself (not the
question form) so the DECK↔WORKBOOK pairing reads cleanly side by side.
