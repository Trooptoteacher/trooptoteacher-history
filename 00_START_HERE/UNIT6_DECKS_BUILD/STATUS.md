# Unit 6 — Slide Decks — Build Status

**Files:**
- `Unit6_Student_Deck_CourseStandard.pptx` — Student (Lean) deck, 113 slides, 16:9
- `Unit6_Teacher_Deck_CourseStandard.pptx` — Teacher (Full) deck, 258 slides, 16:9

## Assessment
The uploaded Course Standard decks were already complete, comprehensive, and on-brand
(legend slide + per-standard arc for US.45–US.58: title, content, primary source, progress
check, representation "who benefited/paid/decided", vocabulary). **Recreation was not needed.**

## What changed
Palette unified to the **locked canonical** tokens from the workbook standard
(`STUDENT_WORKBOOK_PLATINUM_STANDARD.md` §3), so deck and workbook read as one product:
- navy `#1A2332` → **`#1B2A4A`**
- gold `#C9A84C` → **`#C89B3C`**
- (teacher) red `#C62828` → **`#B22234`**

Both decks pass `pptx/scripts/office/validate.py` and render cleanly. Student red was already
canonical `#B22234`. The teacher deck's bright amber `#F9A825` accent was left as-is (not an
explicitly deprecated token) — flag for review if full unification to `#C89B3C` is wanted.

## Four-piece Course Standard set — status
1. Student Workbook — ✅ complete (`UNIT6_STUDENT_WORKBOOK_BUILD/`)
2. Teacher How-to-Use & MTSS Guide — ✅ complete (`UNIT6_TEACHER_GUIDE_BUILD/`)
3. Student (Lean) Deck — ✅ finalized (canonical palette)
4. Teacher (Full) Deck — ✅ finalized (canonical palette)

## Remaining
- **Deck ↔ workbook slide-keying** (now unblocked): add `▶ Deck slide N` references to the
  workbook's writing/response activities, keyed to the Student deck's slide numbers, per
  `SLIDE_DECK_PLATINUM_STANDARD.md` §1. Numbers must come from the shared reference map,
  never hardcoded by hand.

## Slide-keying — DONE
Added `▶ Deck slide N` references to every workbook activity header (US.45–US.58, 98 refs),
computed from the Student deck's real slide positions (per-standard block = 2 + 8·k):
- Activity 1 & 2 (Vocabulary) → KEY VOCABULARY slide (base+6)
- Activity 3 (Cornell Notes) & Activity 4 (Close Read) → content/direct-instruction slides (base+1…+3)
- Activity 5 (Primary Source / HIPPO) → SOURCE IT FIRST (base+4)
- Activity 6 (Practice Quiz) → PROGRESS CHECK (base+7)
- Activity 7 (CER) → content + representation slides (base+1…+5)

Numbers derive from the deck's file positions, not hand-guessed. Workbook re-rendered at
190 pp, zero blank pages. Optional follow-on: the reverse deck→workbook "✍ In your workbook"
cue on matching deck slides (edits the decks, not the workbook).
