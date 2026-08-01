# Unit 6 (WWII · US.45–US.58) — Alignment & QC Report for Official Sign-Off

**Prepared for:** Sean · TroopToTeacher Technologies LLC
**Date:** 2026-08-01 · **Edition:** Course Standard / Platinum
**Prepared by:** autonomous alignment + QC run (you were at the store — this is my best shot, told straight)

---

## Bottom line

- **Workbook (Targets 1a + 1b): DONE and QC-clean.** Guided Cornell cues for all 14 standards
  (Target 1a, already committed) **+** the four-rung NOTES SUPPORTS ladder for all 14 standards
  (Target 1b, this run). 205 pages, **0 blank pages**, notebook lines render, every cloze blank has a
  matching word-bank item. **Schedule F self-score: 32/36 = 89% (PASS).**
- **Decks (Targets 2 + 3): SPECIFIED, HELD FOR YOUR SIGN-OFF.** The student review deck needs a
  content re-key (re-segment DI + move vocab first) and the visual assets need dropping in. I did **not**
  rebuild your strong 112-slide student deck unsupervised — I wrote a deterministic plan so it's a
  low-risk mechanical execution once you approve. See `UNIT6_DECKS_BUILD/DECK_REKEY_PLAN.md`.
- **QC agents run:** lesson-flow QC (student-journey) + Schedule F self-score. Honest counts below.

---

## What I did this run

| # | Item | Status | Evidence |
|---|---|---|---|
| 0 | **Guardrail §7.9a** — Activity 3 pagination & white-space rule (notes recto / supports verso; page-matched; value-question rule) | ✅ committed | `STUDENT_WORKBOOK_PLATINUM_STANDARD.md` §7.9a |
| 1a | **Guided Cornell cues**, all 14 standards, keyed to teacher-deck "DI N of M" | ✅ committed (prior) | workbook Activity 3 per standard |
| 1b | **NOTES SUPPORTS ladder**, all 14 standards (frames → cloze+word bank → how-to+model → try-it+self-check) | ✅ committed (this run) | workbook back pages; 205 pp / 0 blank |
| — | **Skill locked** — `build_guided_notes.py` STANDARDS dict now encodes all 14 (cues + supports); engine can build from a reference file | ✅ committed | `.claude/skills/history-hack-unit-content-build/` |
| 4a | **Schedule F self-score** (workbook) | ✅ 89% PASS | `SCHEDULE_F_SELF_SCORE.md` |
| 4b | **Lesson-flow QC** (deck ↔ workbook) | ✅ run, honest count | this report + `DECK_REKEY_PLAN.md` |
| 2 | **Deck re-key** (student deck DI parity + vocab-first) | ⏸ PLAN for sign-off | `DECK_REKEY_PLAN.md` |
| 3 | **Visual asset placement** into decks (21 QA'd assets) | ⏸ PLAN for sign-off | `DECK_REKEY_PLAN.md` placement table |

---

## QC Agent 1 — Lesson-Flow (student-journey) findings

Mechanical pass over the **committed** teacher deck, student deck, and the new workbook:

> **0 blocker · 28 major · 0 minor.**

The 28 majors are **all deck-side**, two patterns, one each per standard:

1. **DI under-coverage / non-parity (×14).** Teacher teaches 4 DI segments (US.51 = 5); the student
   review deck condenses to fewer labeled slides. The workbook's guided Cornell now keys to the
   teacher's "DI N of M," so at-home review can't cleanly resolve every segment. **Fix: deck re-key.**
2. **Vocabulary after direct instruction (×14).** Student deck puts KEY VOCABULARY last; the workbook
   does vocabulary first. **Fix: reorder (mechanical).**

The workbook itself is internally consistent; these findings are the deck's, and the plan owns them.
Target = re-run to **0 blocker / 0 major** after the re-key.

## QC Agent 2 — Schedule F self-score (workbook)

**32 / 36 = 89% — PASS** (bar 80%). Gateway passes (accuracy, alignment, balance).
Four indicators held at 1 on principle, **all additive and all resolved by the deck re-key**:
gradual-release "we do," speaking/listening scaffolds, SSP.03 multi-source synthesis, and SSP.06
geographic (embed the maps). Full breakdown: `SCHEDULE_F_SELF_SCORE.md`.

---

## The honest gaps (what is NOT done)

1. **Student deck is not yet re-keyed** — 28 major flow findings remain until it is. Specified, not executed.
2. **Visuals not yet in the decks** — the 21 QA'd assets are committed under `UNIT6_VISUAL_ASSETS/`
   but not placed on slides. Placement table is in the plan; two maps (US.57, US.58) need a mandatory
   caption caveat.
3. **Workbook's absolute `▶ Deck slide N` refs** (Activities 1,2,5,6,7) still point at the old student-deck
   numbering; they get re-keyed with the deck (the guided Cornell already uses deck-agnostic "DI N of M").
4. **Four Schedule F indicators held at 1** — real content, not yet fully evidenced across all 14; each
   closes with the deck re-key.

None of these is an accuracy or Gateway failure. The workbook ships clean today; the decks need one
approved re-key pass to bring the whole unit to 0/0.

---

## What I recommend you sign off on

1. **Approve the workbook (Targets 1a+1b) as-is** — 89% Schedule F, 0 blank, QC-clean.
2. **Approve `DECK_REKEY_PLAN.md`** so I can execute the student-deck re-key + visual placement in one
   pass, then re-run both agents to 0 blocker / 0 major and re-score Schedule F (expected ≥ 94%).

Say the word and I'll run the deck re-key exactly as specified.
