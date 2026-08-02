# History Hack — Build Standard (the one spot)

> **Don't just learn history. Hack it.** · **Mission over margin.**
> This is the single front door for building any History Hack curriculum product. It makes the
> product-type distinctions explicit, names one owner per job, and points to the authoritative
> guardrail for each concern. **Decisions + pointers here; detail lives in the referenced files.**
> Reference build (canonical exemplar for everything below): **Unit 6 — WWII (US.45–US.58).**

---

## 1. Product types — name them, don't confuse them

| Product | What it is | Owner skill(s) | Not to be confused with |
|---|---|---|---|
| **Unit Workbook (Course Standard)** — *a.k.a. "chapter / unit workbook"* | The lesson-spine workbook for a **unit's standards**: opener + 7-activity cycle per standard + exit ticket, guided Cornell, NOTES SUPPORTS, deck-aligned. | `history-hack-platinum-unit-builder` (orchestrator) + `history-hack-unit-content-build` (engine: `build_guided_notes.py`) | the DBQ workbook |
| **DBQ Workbook** | A **standalone document-based-question / primary-source investigation** SKU (HIPPO/OPTIC, doc set). A different product from the unit workbook. | `history-hack-dbq-workbook` | the Unit Workbook |
| **Graphic Organizer Toolkit** | Reproducible per-standard organizers; carries the Cornell supports ladder reproducibles. | `history-hack-graphic-organizer-workbook` | either workbook |

**Rule:** when pulling or referencing a build, always say which of the three it is. "Workbook"
alone is ambiguous. The Unit Workbook and the DBQ Workbook are separate SKUs with separate owners.

## 2. Slide decks — guardrails & rules

Authoritative detail: `SLIDE_DECK_PLATINUM_STANDARD.md`.
- **Two decks per unit:** Teacher (lecture) + Student (review). One teacher deck, stored once.
- **Merge, never author from blank** — build both by merging the UDL/supports layer into the
  district's authentic source `.pptx` decks.
- **Vocabulary before instruction.**
- **Student deck = one review slide per teacher DI segment**, captioned **`US.xx · DI k of M`**.
  DI count matches across workbook / teacher deck / student deck.
- Teacher deck carries **`✍ In your workbook · <activity>`** write-cues; per-standard blocks are
  **contiguous** (no interleaving).
- **Engineering:** duplicate slides only with the pptx skill's `add_slide.py` — never python-pptx's
  `add_slide` (orphans a slide part → corrupt package on re-save). Validate + round-trip dup check.
- Brand tokens per `BRAND_PALETTE.md` (America 250).

## 3. Workbook ↔ deck alignment (LOCKED — this is a pass/fail bar)

The workbook must **exactly follow the deck and guide the student to the precise slide** each
activity's notes come from. Zero guesswork.
- Every workbook activity → an **exact slide**, in order. Cornell notes: **`▶ Deck · DI k of M`**
  (1:1 with the deck's DI segments). Activity headers: **role-based `▶ Deck · <Role>`** refs
  (`Key Vocabulary`, `Direct Instruction`, `Primary Source`, `Progress Check`, `Constructed
  Response`) — deck-agnostic so they never go stale on a re-key. **Never hard slide numbers.**
- **Gate:** `history-hack-lesson-flow-qc` → **0 blocker / 0 major**. It builds the Workbook→Exact-
  Slide matrix, verifies DI parity + vocab-first, and flags any hard slide number or unresolvable ref.

## 4. HTML → print-PDF formatting + white-space guardrails

Authoritative detail: `STUDENT_WORKBOOK_PLATINUM_STANDARD.md` §5 + §7; `history-hack-dbq-workbook/
references/white-space-activity-library.md`.
- **No write area without notebook lines** — ever. Ruled lines = a **borderless table with a per-row
  bottom border** (stacked bordered paragraphs collapse to one line); exactly one `w:spacing` per
  paragraph. Engine: `notebook_table()`.
- **White space is filled by standards-aligned activities, not padding** — banded rule: under ~20%
  unused → leave it (breathing room lowers load); **20–65% → add exactly one context-matched move**
  (spaced-retrieval "3 from before," confidence check, quarter-page CER); a fill may **never** spill
  to a new page; stay under the 120-page cap.
- **Per-activity page isolation** — each activity **front** starts its own page (fixed count), so
  selective printing and the duplex/single-sided support toggle stay reliable.
- **Zero blank pages.** Render and visually confirm every PDF.
- **Gate:** `history-hack-text-integrity-qc` → **0 BLOCKER** (no truncated / clipped / placeholder
  text; render-confirm every MAJOR overflow/elision lead).

## 5. UDL 3.0 / MTSS / CAST framework

Owner: `udl-cast-expert`. Authoritative detail: `STUDENT_WORKBOOK_PLATINUM_STANDARD.md` §7.9.
- **Supports live on the verso, in the student book, default-included** — the ceiling never drops;
  the highest-need / EL student produces full notes from the back alone (CAST 5.3 graduated support;
  MTSS Tier 1 = front, Tier 2/3 = verso). Never gate supports into a teacher-only pack.
- **"Lighter book" = a PRINT FLAG, not gating:** *Duplex = notes + supports (scaffolded); Single-
  sided = notes only (lighter / independent).* One book-level decision.
- **Fade is a content property:** rungs thin across the unit (Guided → Light → Independent).
- WIDA L1–2/L3–4/L5–6 supports; WCAG 2.2 AA accessibility; bilingual parity for student-facing.

## 6. Brand

`BRAND_PALETTE.md` — **America 250 palette** (Heritage Blue `#1F3A5F`, Patriot Red `#B22234`,
Founders Cream `#F8F5EF` background, Muted Gold `#C9A227` sparingly). Retires `#1B2A4A`/`#0A1F3C`/
`#C89B3C`.

## 7. Release gates (all must pass — proven on Unit 6)

1. **Content accuracy** — foundational (TDOE Policy 2.600); `historian-factcheck-agent`. No known error ships.
2. **Alignment** — `history-hack-lesson-flow-qc` 0 blocker / 0 major.
3. **Text integrity** — `history-hack-text-integrity-qc` 0 BLOCKER.
4. **Schedule F self-score** — per section + unit, as-built, ≥ 80%; `tn-textbook-adoption-agent`.
5. **Print** — zero blank pages; notebook lines visible; white-space banded rule satisfied.
6. **UDL/accessibility** — `udl-cast-expert` audit; supports default-included.

## 8. Skills registry (one owner per job)

**Mission/rule:** `history-hack-platinum-standard`.
**Builders:** `history-hack-platinum-unit-builder` (unit workbook + decks, THE builder) ·
`history-hack-unit-content-build` (content engine) · `history-hack-dbq-workbook` (DBQ SKU) ·
`history-hack-graphic-organizer-workbook` (organizers) · `history-hack-course-standard-builder`
(new-course orchestrator — *pending rename to end the name collision*).
**Gates (standalone, runnable):** `history-hack-lesson-flow-qc` · `history-hack-text-integrity-qc` ·
`history-hack-print-qc-auditor`.
**Assessment:** `tn-assessment-specialist` (*absorbs `tcap-item-writer-v2`, pending retirement*).
**Specialist reviewers:** `historian-factcheck-agent` · `tn-textbook-adoption-agent` ·
`udl-cast-expert` · `instructional-design-specialist` · `tt-education-research-team`.

Reconciliation to this canonical set (retirements, renames, standalone-vs-inlined) is specified in
`SKILLS_RECONCILIATION_PLAN.md` and lands via a review-first skills-only PR to `main`.

## 9. Flight logs (build records)

Every build keeps its record so decisions and status are auditable: per-build `STATUS.md`, the
`UNIT6_ALIGNMENT_SIGNOFF_REPORT.md`, `SCHEDULE_F_SELF_SCORE.md`, `DECK_REKEY_PLAN.md`, and the QC
run outputs. These are the flight logs — what was built, what passed, what's held.

## 10. Anti-drift rule (so this never fragments again)

`.claude/skills/` is **main-owned and read-only on work branches.** Skills change only via a
dedicated **skills-only PR merged to `main` first**; content branches rebase and consume skills
read-only. A one-owner skill registry + CI lint (overlap / inlined-gate / retired-name checks)
enforce it. Detail: `SKILLS_RECONCILIATION_PLAN.md`.
