---
name: teacher-deck-workbook-aligner
description: >-
  Builds a History Hack PLATINUM TEACHER slide deck that is explicitly aligned to the
  student workbook for direct instruction — every deck slide maps to the workbook page
  students write on, with the DIRECT INSTRUCTION → Cornell notes pairing made visible.
  Layers a teacher intro ("How This Deck Drives the Workbook") and a per-standard
  "LESSON → WORKBOOK MAP" slide onto the AUTHENTIC teacher deck (source slides and
  images never touched), via the same merge pipeline the Course Standard decks use.
  Use whenever the user asks to: "build/build out the platinum teacher deck for Unit N",
  "align the deck with the workbook", "make sure the deck and workbook match for direct
  instruction", "tie the Cornell notes to the slides", or "add the lesson-to-workbook map".
  Pairs with history-hack-course-standard-builder (which builds the workbook + the
  vocab/progress UDL layer); this skill adds the teacher↔workbook alignment map on top.
---

# Teacher Slide Deck ↔ Student Workbook Aligner

**Goal:** a teacher can project the deck top-to-bottom and students always know which
workbook activity to work — and the DIRECT INSTRUCTION slides land, word-for-word, on the
Cornell-note cues students fill in. The deck is the direct-instruction spine; the workbook
follows it.

## The core alignment fact (verify it every time)
History Hack teacher decks run a fixed per-standard cycle:

```
STANDARD divider → QUICK REVIEW → CONFIDENCE CHECK → HOOK
→ DIRECT INSTRUCTION ×3–4 → [KEY FIGURES] → PRIMARY SOURCE ANALYSIS
→ KEY VOCABULARY (Word Wall) → GUIDED PRACTICE → STUDENT ACTIVITY
→ CHECK FOR UNDERSTANDING → ANSWER REVEAL → WRAP-UP
```

The **DIRECT INSTRUCTION slide labels are the workbook's Cornell cues, verbatim**
(`standards[code].criteria` in `unit<N>_content.json`). Units 1 (US.01–07) verified:
US.01/02/05/06 match 3↔3 exactly; US.03/04/07 have a 4th DI slide the workbook folds into
its 3 cues (extra depth — captured in the Cornell "Key terms →" row). `extract_align.py`
prints EXACT / review per standard so you catch any real drift before building.

## What this skill adds (and what it does NOT duplicate)
The authentic teacher deck is already platinum-grade: it has vocabulary (Word Wall),
checks + answer reveals, guided practice, etc. **Do not re-add those.** This skill inserts
only the alignment scaffolding:

1. **Teacher intro** — "How This Deck Drives the Workbook": the 6-row deck→workbook flow
   with the DI→Cornell row highlighted, plus the MTSS decision-cycle strip ("the goal never
   lowers").
2. **One "LESSON → WORKBOOK MAP" per standard**, inserted right after the STANDARD divider.
   Hero block = DECK Direct-Instruction slide (with its real slide number) → WORKBOOK Cornell
   cue students write. Secondary strip maps Primary Source → Act. 4/5, Vocabulary → Act. 1/2,
   Guided/Student Activity → Guided Support + Act. 7 CER, Check + Reveal → Act. 6 + Progress
   Check. TN connection line at the foot.

## Pipeline (merge, never edit-in-place)
Same principle as `references/udl-mtss-deck-merge-pipeline.md` in the course-standard skill:
build the new slides as a pptxgenjs "layer" deck, then MERGE into the authentic deck with
python-pptx so original slides + every embedded image pass through untouched.

```bash
# 0. Inputs: authentic teacher deck (.pptx, in your session — under Drive's 10MB cap, or
#    have the user attach/compress it) and the unit content JSON (unit<N>_content.json).
export NODE_PATH=/workspace/history-hack-web-app/node_modules   # pptxgenjs lives here

# 1. Extract + verify DI↔Cornell parity
python3 scripts/extract_align.py "TEACHER_DECK.pptx" unit<N>_content.json align.json
#    -> reads the "EXACT / review" line for every standard; investigate any "review".

# 2. Build the alignment layer (intro + per-standard maps)
node scripts/build_align_layer.js align.json teacher_align_layer.pptx

# 3. Merge into the authentic deck
python3 scripts/merge_align.py "TEACHER_DECK.pptx" teacher_platinum.pptx align.json teacher_align_layer.pptx

# 4. Render + QC
soffice --headless --convert-to pdf --outdir . teacher_platinum.pptx
pdftoppm -f 1 -l 1 -r 90 -png teacher_platinum.pdf qc_intro    # intro
pdftoppm -f 6 -l 6 -r 90 -png teacher_platinum.pdf qc_map      # a map slide
```

## CONTENT parity — alignment means same content, not just a map slide
A map slide that *points* at the workbook is not enough. The workbook must **teach what
the deck teaches**, per standard. Two fields drift because deck and workbook were authored
separately — check and reconcile both (deck = source of truth):

1. **Cornell cues == DIRECT INSTRUCTION labels** (`standards[code].criteria`). Usually already
   exact; `extract_align.py` / `check_parity.py` flag any drift.
2. **Workbook vocab == KEY VOCABULARY Word Wall** (`standards[code].vocab`). This is the one
   that drifts hard — the deck Word Wall carries ~6 terms/standard (term + pronunciation +
   Spanish + definition); workbooks were often authored with a different subset. Reconcile:
   set `standards[code].vocab` to the deck's Word Wall (adopt term/say/es/def verbatim) and
   point `auth.frayer` at the first two deck terms so Activity 2 uses real deck vocab. Then
   **rebuild the workbook** and re-run the gate.

```bash
python3 scripts/check_parity.py "TEACHER_DECK.pptx" unit<N>_content.json   # exit 0 = aligned
```
Run it after ANY deck or workbook edit. Exit 1 prints every mismatch.

### When the teacher deck is over the 10 MB Drive cap (no binary)
You do NOT need the binary to reconcile vocab. The Drive connector's `read_file_content`
returns a deck's full slide TEXT at any size. Save that result (`{"fileContent": "..."}`) and:
```bash
python3 scripts/wordwall_from_text.py read_file_content.json deck_vocab.json
```
It yields the same `{code:[{term,say,es,def}]}` the binary path produces (Unit 3, US.19–27,
was reconciled this way — 6 terms/standard, verified). Then overwrite `standards[code].vocab`
+ `auth.frayer` from `deck_vocab.json` and rebuild. (check_parity.py still needs the binary;
when you only have text, verify workbook vocab == `deck_vocab.json` instead.)

### Rebuilding the workbook (runs from the unit's build workspace)
The workbook builder reads `analysis/unit<N>_content.json` and writes `deliverables/`. Run it
from the unit workspace (e.g. `/home/user/Unit<N>_Claude_Core/`) so its local `node_modules`
(docx) resolve — `require` resolves from the script path, so also set NODE_PATH to that
workspace's node_modules:
```bash
cd /home/user/Unit<N>_Claude_Core
export NODE_PATH=/home/user/Unit<N>_Claude_Core/node_modules HOME=/home/user
node <repo>/HistoryHack_Platinum/build_unit<N>/build_workbook_u<N>.js
soffice --headless --convert-to pdf --outdir deliverables deliverables/Unit<N>_Student_Workbook_CourseStandard.docx
```

## No white space — fit each activity to a full page (hard rule)
Adopting 6 vocab terms makes **Activity 1 (Word Bank + Language Support + Self-Check)** spill
onto a second, near-empty page. That violates the no-white-space rule. Fit it to ONE full page:
- Word Bank + Self-Check text at 9pt (`size:18`), self-check term at 8pt (`size:16`).
- Drop the trailing "Quick Write" (redundant with Make-It-Yours / Preview-&-Predict / Cornell key terms).
- Give "Make It Yours" `ruled(3)` response lines so the page fills to the margin (not gappy).
Verify with the pagination probe: every standard's Activity 1 must span exactly 1 page
(Activity 2 starts on Activity 1's page + 1) and leave no large bottom gap.

## Design contract (do not drift)
- Canvas 13.333 × 7.5 in. Fonts Cambria (headers), Arial (body).
- Tokens: NAVY `15223E`, GOLD `C89B3C`, GREEN `2E7D46`, RED `B22234`, BLUE `2F5FA6`,
  CREAM `F7F5EF`, INK `1A1A1A`. GOLD marks the DECK side, GREEN marks the WORKBOOK side —
  keep that pairing consistent so teachers read the map at a glance.
- The DI→Cornell block is the hero of every map slide; the activity crosswalk is secondary.
- Teacher-facing, so MTSS/CAST language is allowed (unlike the student deck, which stays
  clean — see the student-deck ruling in the course-standard skill).

## QC checklist (all must pass before delivery)
- [ ] `extract_align.py` prints EXACT (or an understood "review") for every standard.
- [ ] Merged slide count == source + 1 intro + N standards.
- [ ] Every map slide sits immediately after its STANDARD divider (script asserts this).
- [ ] Image count on slides is unchanged vs the source deck (authentic images preserved).
- [ ] Zip integrity OK; intro + one map slide render clean (no truncated/overrun text).
- [ ] Deliver `.pptx` (editable master) + `.pdf` (projection/QC).

## Notes / gotchas
- The 10 MB Drive-connector download cap blocks large teacher decks (e.g., 24 MB). Under the
  cap, pull with the Drive connector; over it, have the user compress (Compress Pictures →
  150 ppi) or attach the `.pptx` to the session.
- `read_file_content` returns full deck TEXT even for oversized decks — useful to verify DI
  labels when you can't get the binary, but you need the binary to merge.
- Slide *file* order ≠ presentation order; always check order via the `sldIdLst`
  (python-pptx `Presentation.slides`), not the media filenames.
