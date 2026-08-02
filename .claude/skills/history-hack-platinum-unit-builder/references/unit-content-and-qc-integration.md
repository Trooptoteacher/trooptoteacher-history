# Unit Content & QC Integration (Platinum, proven on Unit 6 · US.45–US.58)

The authoritative spec for the Unit 6 platinum components and the hard release gates
referenced by `SKILL.md`. **Reference and invoke the sibling skills named here — do not
re-implement their logic in this skill.** If a sibling skill is not installed in the
environment, invoke it where available and record the gap in the completion report.

## Decision rule — north star (default every fork)

`history-hack-north-star`, in strict order: **(1) 100% standards alignment → (2) TDOE
Schedule F → (3) best path to adoption.** Accuracy is foundational (**Policy 2.600**) and
is never traded for adoption appeal — a lower-accuracy option is out regardless of rank.

---

## 1. Student Workbook — 7-activity spine + guided Cornell

- **7-activity spine** per standard (the established platinum sequence), unchanged.
- **Guided Cornell notes keyed to the teacher deck's Direct-Instruction (DI) segments.**
  Each notes block is captioned **`▶ Deck · DI k of M`** so the student page and the slide
  the teacher is on are unambiguously paired.
- **Four-rung NOTES SUPPORTS ladder** (gradual release):
  1. **Frames** — sentence/heading frames only.
  2. **Cloze + word bank** — fill-in with a provided bank.
  3. **How-to + worked model** — a completed exemplar to imitate.
  4. **Try-it on ruled paper + self-check** — independent, with a self-check key.
- **Layout: notes on the recto (right), supports on the verso (left)** so a student sees
  the note and its support rung together across the spread.
- **Built by `history-hack-unit-content-build`** (engine `build_guided_notes.py`). Do **not**
  hand-author the ruled notebook tables — the engine emits print-correct tables (see
  Engineering guardrails).

## 2. Aligned Teacher (lecture) + Student (review) decks

- **Vocabulary BEFORE instruction** — vocab slides precede the DI slides for a standard.
- **Student deck = one review slide per teacher DI segment**, captioned **`US.xx · DI k of M`**.
- **DI count matches across all three artifacts** — workbook notes blocks, teacher DI slides,
  and student review slides all report the same `M` per standard.
- **Teacher deck write-cues** — each DI segment that maps to a workbook activity shows
  **`✍ In your workbook · <activity>`** so the teacher directs students to the exact page.
- **Contiguous per-standard blocks** — a standard's slides are one unbroken run; never
  interleave standards.

## 3. Teacher Guide & MTSS · Answer Key · Visual Asset package

- **Teacher Guide & MTSS** and **Teacher Answer Key** per the platinum structure.
- **Commercial-use-safe Visual Asset package** — every image is **Public Domain, US-Government,
  CC0, or CC-BY** only. Each asset ships a **citation sidecar** (source, creator, date,
  repository, license, URL) **and alt text**.
- **Never build political or boundary maps in-house** — accuracy and neutrality risk. Source
  them from an authoritative repository (LoC, NARA, Census, NPS, USGS, etc.).

---

## Hard release gates (all must pass — a unit that fails any is not platinum)

| Gate | Skill / check | Pass condition |
|---|---|---|
| Lesson flow | `history-hack-lesson-flow-qc` | **0 blocker / 0 major.** Emits the workbook→exact-slide matrix; verifies DI-segment parity (workbook = teacher = student) and vocab-before-instruction. |
| Text integrity | `history-hack-text-integrity-qc` | **0 BLOCKER.** No truncated, clipped, or placeholder text; render-confirm every MAJOR. |
| Schedule F | `tn-textbook-adoption-agent` self-score | **≥ 80% as-built**, per section **and** per unit — score what actually renders, not a design-time estimate. |
| Print integrity | render check | **Zero blank pages** on every rendered PDF; **notebook lines visible** on every ruled page. |

## Engineering guardrails

- **`.pptx` slide duplication:** use the **`pptx` skill's `add_slide.py`**. **Never call
  `python-pptx` `add_slide`** — it can orphan a slide part and corrupt the package on re-save.
  After duplicating, **validate with a load/save round-trip dup check** (open, save, reopen;
  confirm slide count + no orphaned parts).
- **Notebook paper (ruled tables):** a **borderless table with a per-row bottom border** (the
  ruled line), and **exactly one `w:spacing` per paragraph** — multiple `w:spacing` runs
  collapse or double lines and break the ruled rhythm.

## Sibling skills (reference, don't re-implement)

- `history-hack-north-star` — the decision rule.
- `history-hack-unit-content-build` — content JSON + `build_guided_notes.py`.
- `history-hack-lesson-flow-qc` — flow gate.
- `history-hack-text-integrity-qc` — text-integrity gate.
- `tn-textbook-adoption-agent` — Schedule F self-score.
- `pptx` — slide duplication (`add_slide.py`).
