# Prompt — fold the Unit 6 pipeline into the Platinum Unit Builder

> Paste this into an agent working in this repo. It wires everything proven on Unit 6 (WWII,
> US.45–US.58) into `history-hack-platinum-unit-builder` so the builder produces **and gates** the
> complete unit set. Cross-reference the sibling skills — do not duplicate their logic.

---

Update the **`history-hack-platinum-unit-builder`** skill so its authoritative components, when-to-use
triggers, and Platinum QA release gates include everything we proved on Unit 6. Keep every existing
platinum rule intact (branding, one teacher deck, editable-Word-authoritative, three schedule
variants, exit-ticket protection, English/Spanish parity, draft-branch/PR gate, verified standards
source). Follow the Platinum Standard decision rule at every fork: **(1) 100% alignment → (2) TDOE Schedule F
→ (3) best path to state adoption / highest quality** (`history-hack-platinum-standard`). Content accuracy
(TDOE Policy 2.600) is foundational — no known error ships.

## 1. Add these authoritative components to the unit product definition

- **Student Workbook** — the 7-activity lesson spine per standard **plus**:
  - Guided **Cornell notes** (Activity 3) whose cue column is keyed to the teacher deck's direct-
    instruction segments, one row per segment, marked `▶ Deck · DI k of M`.
  - The four-rung **NOTES SUPPORTS** back-page ladder: ① sentence frames → ② fill-in cloze + word
    bank → ③ how-to + worked model → ④ try-it on ruled notebook paper + a self-check rubric. Front/
    back print rule: notes on recto, supports on verso, page-matched.
  - Built with **`history-hack-unit-content-build`** (engine: `scripts/build_guided_notes.py`, which
    encodes cues + supports per standard and clones a locked reference block for formatting parity).
- **Teacher (lecture) Deck + Student (review) Deck**, aligned to the workbook:
  - **Vocabulary before direct instruction** in both decks (matches workbook Activity 1–2).
  - Student deck = **one review slide per teacher DI segment**, captioned `US.xx · DI k of M` so a
    student resolves each guided-Cornell cue to an exact slide; student deck = teacher deck minus
    teacher-only slides; DI count (student) == DI count (teacher) == workbook Cornell segments.
  - Teacher deck carries a gold **“✍ In your workbook · <activity>”** cue on every write moment
    (Vocab 1–2, Cornell & Close Read 3–4, Primary Source 5, Practice Quiz 6, CER 7).
  - Per-standard blocks are contiguous (divider → quick review → confidence → hook → vocab → DI×M →
    people → primary source → guided practice → student activity → check → answer reveal → wrap-up →
    vocab review → progress check).
- **Teacher Guide & MTSS**, **Teacher Answer Key**, and a **Visual Asset package** — commercial-use-
  safe only (PD / US-gov / CC0 / CC-BY; no share-alike, no permission-gated), each asset with a
  citation sidecar (creator, date, source, license, caveat) + alt text. Never build political/
  boundary/troop-movement maps in-house; point-location schematics on a PD Census basemap are fine.

## 2. Add these to Platinum QA as hard release gates

- **Lesson-flow QC** (`history-hack-lesson-flow-qc`) → must return **0 blocker / 0 major**. Produces
  the Workbook→Exact-Slide matrix; verifies every activity maps to a specific slide, in order, DI
  counts match, vocab-first, student review deck covers 100% of what was taught.
- **Text-integrity QC** (`history-hack-text-integrity-qc`) → must return **0 BLOCKER**. Catches
  truncated / clipped / placeholder text (the "…the Sudetenland from…" class). Render-confirm its
  MAJOR overflow/elision leads.
- **Schedule F self-score** for every section and for the unit — scored **as-built**, honestly, held
  low on principle where unproven; target ≥ 80%. Author = TroopToTeacher Technologies LLC;
  supplemental under T.C.A. §49-6-2202(a)(3).
- **Zero blank pages** on every rendered PDF; notebook lines visible.

## 3. Add these engineering guardrails (reference doc)

- **.pptx slide duplication:** use the pptx skill's `scripts/add_slide.py` — **never** python-pptx's
  `add_slide` for duplication; it can orphan a slide part and make a later re-save duplicate a
  partname and corrupt the package. After any deck edit, run `scripts/office/validate.py` **and** a
  python-pptx load→save round-trip and check the zip has no duplicate entries.
- **Notebook paper** = a borderless table with a bottom border on each row (stacked bordered
  paragraphs collapse to one line). Exactly one `w:spacing` element per paragraph.
- Render-and-QC gate after every structural change; pixels are authoritative for what a student sees.

## 4. Deliverable

Edit `history-hack-platinum-unit-builder/SKILL.md` (component list + when-to-use + non-negotiables +
QA gates) and add `references/unit-content-and-qc-integration.md` capturing sections 1–3 with links
to the sibling skills. Do **not** re-implement those skills' logic here — reference and invoke them.
Commit on a draft branch / PR per the builder's own release rule, then report what changed.
