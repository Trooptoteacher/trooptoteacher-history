# Content Source-of-Truth Consolidation Plan (PROPOSAL)

**Status:** Proposal / assessment only. **Nothing in any build pipeline has been changed.**
**Author:** Claude Code, at Sean's request. **Date:** 2026-08-07.
**Decision owner:** Sean (TroopToTeacher Technologies).

> One-line goal: **one canonical source per asset → many renderers.** Every deliverable
> (Flight Deck, Flight Log / Student Workbook, Cornell Notes, Textbook, Mission Control app)
> renders *from* the canonical sources and never hand-holds its own copy.

---

## 0. Why this plan exists

An audit of **all 9 in-scope repos** found the U.S. History content spread across 4–6
un-synced copies per asset class, with real conflicts (not just duplication). The most
dangerous: the **same quiz item carries a different correct answer** in different files, and
the shipping workbook reads a **`/tmp` file that does not exist in any repo** — so a clean
checkout cannot rebuild Unit 1. The good news: the *right* architecture already exists for
World History (`gen_unit.py` + `course.json` + `unit-NN.source.json` + JSON schemas); the
U.S. flagship simply never migrated onto it.

---

## 1. Canonical source-of-truth decisions (the "who wins")

| Asset | **CANONICAL (single source)** | Becomes *generated* / *retired* |
|---|---|---|
| **Question bank** | **`history-hack-web-app` `public/data/us-history/questions/` (~5,100 items, all 95 standards)** | textbook `question-bank/*.json` (3,209); `trooptoteacher-history/all_questions.json` (answer-key **B** fork); `/tmp/u1_quiz.json` |
| **Standards text (verbatim)** | **`2026-27-Tn.-Social-Studies-Standards/standards/hs-us-history.json`** | inline `tnStandard` copies; textbook `docs/standards.json`; web-app reworded summaries; PS crosswalk copy |
| **Primary sources + images** | **`history-hack-web-app` `public/data/us-history/primary-sources/`** (rights-verified, bilingual) | deck skill `_images.json` (thin); empty `-2026-27-Social-Studies-Primary-Sources` repo |
| **Unit content spine** | **new `content/us-history/unit-NN.source.json`** (authored once) | deck `_build.json` → **generated artifact**, not hand-edited |
| **Build engines + skills** | **`trooptoteacher-history/.claude/skills/` + `print-pipeline/`** | `history-hack-skill-library` zips; `TroopToTeacher-Course-Build` `engine/` + `.claude/skills/` |
| **Item-writer engine** | **promote `tcap-item-writer-v2` into `.claude/skills/`** (canonical) | copies in skill-library + Course-Build |
| **Print distribution** | **`History-Hack-US-History-Workbooks`** (Azure Blob + Drive) — *keep as downstream consumer* | — |

**The web app = Mission Control** hosts the canonical **banks** (questions + primary sources +
images) and is the interactive/runtime renderer (portfolios, spaced repetition, formative/
summative, writing lab). The print side **references** those banks; it never re-copies them.

---

## 2. Target data flow (one spine, one bank, many renderers)

```
        2026-27-Tn Standards (verbatim)        history-hack-web-app / Mission Control
                     │                          ├── questions/  (~5,100 items) ── CANONICAL bank
                     ▼                          ├── primary-sources/ + images/ ── CANONICAL sources
        courses/us-history/course.json ─────────┤
                     │                          └── (runtime: practice, assessments, writing lab)
                     ▼                                          │
        content/us-history/unit-NN.source.json  ◄── authored once (prose + structure)
                     │
                     ▼   gen_unit.py (one generator, seven courses)
        ┌────────────┼───────────────┬───────────────┬────────────────┐
        ▼            ▼               ▼               ▼                ▼
   Flight Deck   Flight Log      Cornell Notes    Textbook        Assessment book
   (.pptx)       (workbook PDF)  (PDF)            (reader)        (from the bank)
        └──────── every quiz / check / practice pulls from the ONE web-app bank ─────────┘
```

---

## 3. Prioritized PR sequence (each self-contained, safe, reversible)

**P0 — Correctness & reproducibility (do first, small):**
1. **Reconcile the answer-key conflict.** Pick the web-app bank as truth; fix/retire
   `all_questions.json` (item `US.01-Q01` etc. where the correct-answer letter differs).
   *Ship blocker under "no known error ships."*
2. **Kill the `/tmp` dependency.** Point the workbook quiz at the canonical web-app bank (a
   committed selection manifest), so a clean checkout builds Unit 1. Retire `/tmp/u1_quiz.json`.

**P1 — Establish the single spine for U.S. History:**
3. **Create `courses/us-history/`** (`course.json` + `standardsFile` → the verbatim TDOE repo),
   mirroring the World History layout.
4. **Author `content/us-history/unit-01.source.json`** and migrate Unit 1 onto **`gen_unit.py`**
   (retire the U.S.-only `gen_unit01.py` fork). Deck `_build.json` becomes a *generated* view.
5. **Add a schema + parity check** for the spine (JSON Schema + a validator that fails the build
   if content is missing/malformed or a renderer's copy drifts from the bank).

**P2 — De-duplicate assets:**
6. **Single image/primary-source source:** deck references web-app IDs; drop the parallel
   `_images.json`. Carry the rights/`commercialUse`/`verifiedAt` fields the print side currently lacks.
7. **Single standards source:** generate every `tnStandard` string from the verbatim repo; delete hand-copies.

**P3 — Consolidate engines/skills:**
8. **One skills home:** `.claude/skills/` is canonical; **promote `tcap-item-writer-v2`** in; retire
   the skill-library zips and the `Course-Build` `.claude/skills/` copy (or make them generated mirrors).
9. **One workbook engine:** decide Python `print-pipeline` vs `Course-Build` JS `engine/`; retire the loser.
10. **Delete the stale web-app deck fork** (`history-hack-web-app/tools/tcap-deck-builder/`).

**P4 — Guardrails so drift can't come back:**
11. **CI "parity check"** on every PR: fail if a renderer reads a non-canonical source, if answer
    keys disagree across surfaces, or if the spine has no schema match.
12. **Reconcile the two `CLAUDE.md` files** so both repos name the same source-of-truth policy.

---

## 4. Decisions — LOCKED by Sean (2026-08-07)

- **D1 — Web app scope → ALL THREE BANKS.** The web app (Mission Control) is home to the
  **question bank, primary sources, and image bank** — all canonical, the platinum standard for
  US History and reusable for other content areas. The **spine references the banks by ID**;
  it never re-copies them. (Two homes, one each: *banks* on the web app; *spine* in the
  curriculum repo — they flow together via ID references.)
- **D2 — Spine authoring home → structured `content/us-history/unit-NN.source.json`.** Prose is
  distilled into the source file; the **Mission (narrative)** and textbook render *from* it.
  (No extraction-from-prose — accuracy-risky.)
- **D3 — Print engine → Python `print-pipeline` + WeasyPrint** (`render.py` + the locked
  `print-contract.css` Paged-Media contract). Retire the `Course-Build` JS `engine/` fork.
- **D4 — Missions → YES, first-class.** **"Mission" replaces "narrative."** Each unit/standard
  has a Mission (its story-driven content) as a spine field that flows into the **Flight Deck**
  and **Flight Log**.

### 4a. Naming canon (LOCKED)

| Term | Meaning |
|---|---|
| **Mission** | The narrative content of a unit/standard (formerly "narrative"/"textbook reader"). |
| **Flight Deck** | The teacher lecture deck (`.pptx`). *(Renamed from "deck.")* |
| **Flight Log** | The student workbook. |
| **Cornell Notes** | The guided note companion. |
| **Mission Control** | The History Hack web app — portfolios, goals, spaced repetition & practice, formative + summative assessments, writing lab; **home to the three canonical banks.** |

> System reads as one metaphor: **Missions** (narrative) → taught via the **Flight Deck**,
> worked in the **Flight Log** + **Cornell Notes**, lived-in on **Mission Control**.
> *(Renames are a naming-canon + docs task; code identifiers change incrementally, not big-bang.)*

---

## 5. What this fixes (traceability to the audit)

- ✅ "Did my updates reach the parity?" → one spine + one bank, with a CI parity check.
- ✅ Reproducible builds (no `/tmp`).
- ✅ No conflicting answer keys reaching students.
- ✅ Verbatim TDOE standards, generated everywhere (no wording drift).
- ✅ One engine/skills home; item-writer promoted to canonical.
- ✅ Mission Control + textbook + print all render from the same truth.
