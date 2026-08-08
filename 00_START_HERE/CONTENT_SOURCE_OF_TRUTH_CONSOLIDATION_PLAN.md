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

**P0 — Correctness & reproducibility (do first, small):** *(scope refined by the 2026-08-07 sweep — see §6)*
1. **Canonicalize on the web-app bank; quarantine `all_questions.json` from U.S. History.** The
   sweep showed the web-app bank and the textbook bank **agree on every matched answer**; all 110
   text conflicts trace to `all_questions.json`, which **no U.S. History builder reads** (only the
   Government course does). So the fix is to **mark it non-canonical for U.S. History** (dissolves
   the conflicts) — *not* hand-editing 110 keys. Coordinate the Government coupling separately.
2. **Wire the quiz at the BANK level, not into the dying `/tmp` path.** The workbook is being
   restructured into a *source* for the Flight Logs (see §4a), so do **not** patch
   `gen_unit01.py`'s `/tmp/u1_quiz.json`. Instead build a single **bank-feed** (select canonical
   items from the web-app bank by standard) that the **new Flight-Log pipeline consumes into the
   Flight-Log appendix**. This kills the `/tmp` dependency by construction and survives the restructure.

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
| **Workbook** | An authored **source** (lesson content). *Feeds the Flight Log — it is not itself the student deliverable.* |
| **Flight Log** | The student-facing deliverable, **generated from the Workbook**, **+ a Flight-Log appendix** (the bank-fed practice/assessment section). |
| **Cornell Notes** | The guided note companion. |
| **Mission Control** | The History Hack web app — portfolios, goals, spaced repetition & practice, formative + summative assessments, writing lab; **home to the three canonical banks.** |

> **Workbook → Flight Log flow (refined 2026-08-07):** Workbook (authored source) **generates** the
> Flight Log (+ appendix); the **canonical question bank feeds the Flight-Log appendix**. Earlier
> shorthand "Flight Log = the workbook" is superseded.

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

---

## 6. P0 answer-key sweep — results (2026-08-07, read-only)

Compared three banks by **resolving every answer letter to its option text** (a letter mismatch
alone is meaningless — options are reordered across banks): web-app **5,041** (canonical), textbook
v5 **3,209**, `all_questions.json` **736**.

| Finding | Count | Meaning |
|---|---|---|
| Answer-**text** conflicts | **110** | **All 110 involve `all_questions.json`.** Web-app vs textbook: none (the 2 flagged are same answer + letter, reworded option text). |
| Same ID, **different question** | 201 | ID scheme is not stable across banks — the root cause of undetected drift |
| Unresolved keys | 388 | A stored letter didn't map to an option (mostly in the fork) |
| Position-only diffs | 193 | Same answer, different letter slot — the de-bias-position sync, not correctness |

**Conclusions:**
- The feared "same question graded differently could reach a student" risk is **not live** in the
  canonical U.S. History path — the web-app and textbook banks agree, and `all_questions.json`
  (the sole divergent source) is read only by the **Government** course, not U.S. History.
- Real structural problem = **no stable cross-bank item identity** (only 70–736 IDs match across
  banks of 736–5,041). Fixed in P1 by the schema + stable IDs.
- The P0 fix is therefore **quarantine one orphan file + stand up the bank-feed**, not per-item
  re-keying. Two items to human-eyeball (both actually the same answer): `US.02-Q05`, `US.05-Q02`.
- Full receipts: sweep detail JSON (110 conflicts, 201 collisions, 388 unresolved, 193 position-only).
