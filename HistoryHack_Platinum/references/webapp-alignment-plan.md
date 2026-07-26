# Web App ↔ Print Alignment Plan — Course Standard parity

**Goal:** a student gets the **same core, same names, same rigor** whether they're on paper
(workbook + deck) or on screen (the Next.js web app). © 2026 TroopToTeacher Technologies LLC.

**Principle:** *one canonical activity spec, two renderers.* The print Course Standard 7‑activity
cycle is the source of truth for names, routines, and rigor. The web app's 5E "unit journey" is a
valid **delivery structure** (it doesn't conflict with UDL/MTSS/CER — those are different layers),
but it must render the same core activities, under the same names, at the same rigor. A parity check
keeps them from drifting again.

**Canonical 7‑activity cycle (per standard US.01–US.07):** Vocabulary Word Bank · Vocabulary Studio
(Frayer) · Direct‑Teaching Cornell Notes (paired to deck) · Close Read · Primary Source / Data
(**HIPPO**, 5 elements) · Practice Quiz · Constructed Response (**CER**) + **Exit Ticket**. Built on
UDL 3.0 + MTSS; "I can" targets verbatim; answer positions de‑biased.

---

## Workstream 1 — HIPPO parity (naming **and** rigor)  ·  highest impact

**Current state (evidence).** The app uses the 4‑letter **`HIPP`** 821× across 89 files and is
internally inconsistent about what it means:
- `app/practice/dbq/dbq-content.tsx:226` — labels a **4‑element** set "HIPPO (Historical context,
  Intended audience, Purpose, Point of view)" — **missing Outside**.
- `dbq-content.tsx:1558–1586, 2074–2078` — expands to Historical Context, Intended Audience, Point
  of View, **Outside Information** — **missing Purpose**.
- `app/units/[id]/unit-journey-client.tsx:257–258` — step 9 desc reads "Analyze historical documents
  with **HIPP**" (EN and ES).

**Canonical (workbook).** `build_workbook.js:330–335` — the complete **5‑element HIPPO**:
H — Historical context · I — Intended audience · P — Purpose · P — Point of view · O — Outside.

**Decision.** Standardize on the workbook's **5‑element HIPPO** everywhere. This is a rigor fix, not a
rename: app students must be prompted for all five moves.

**Changes.**
1. Create one shared definition (e.g., `lib/frameworks/hippo.ts`) exporting the 5 elements + EN/ES
   prompts, and have every surface read from it (journey, DBQ, slides, printables) so it can never
   drift again.
2. `unit-journey-client.tsx` step 9: `HIPP → HIPPO`; scaffold pulls all 5 prompts from the shared def.
3. `dbq-content.tsx`: replace the two inconsistent expansions with the 5‑element set; render all five.
4. Categorized sweep of the 821 `\bHIPP\b` hits — **do not blind‑replace**:
   - Student‑facing (`app/`, `components/`): fix first.
   - Data/scaffolds (`public/data/.../primary-sources/*`, `lib/slides/*`): ensure each carries all 5
     prompts; `lib/slides` already uses full HIPPO, so mostly data backfill of the missing element.
   - Docs/tests/QC (`docs/`, `__tests__/`, `qc/`): update references + snapshot expectations last.
**Risk:** M–L (breadth). Mitigate with the shared def + a codemod + tests. **Effort:** M–L.

---

## Workstream 2 — Add the 3 missing activities to the journey

The journey is defined by `STEPS[]`, `PHASES`, `STEP_TO_STOP`, `STOP_FIRST_STEP` in
`app/units/[id]/unit-journey-client.tsx` (+ `lib/progress-store.ts`). It has **no discrete** Word
Bank, Close Read, or Exit Ticket step — but the underlying data/routes mostly exist.

**Adding a step (mechanics):** append a `StepDef` (`key`, `num`, `label`/`labelEs`, `desc`/`descEs`,
`icon`, `phase`, `framework`, `href`), then update the `PHASES` index arrays, `STEP_TO_STOP`,
`STOP_FIRST_STEP`, and `progress-store` keys. Also fix the stale "10‑step" comment/label — there are
already 11 entries.

- **Word Bank (Activity 1).** Data exists (`lib/worksheet-band-helpers.ts`, `geographic-reasoning-data.ts`,
  `wordBankEn/Es`). It's the *reference* half of vocabulary. **Recommend a "Word Bank" tab inside the
  existing Vocabulary step (3)** rather than a new journey step — exposes it by name without bloating
  the path. **Effort:** S.
- **Close Read (Activity 4).** Content exists via `closeReadingProtocol` (`schemas/textbook_unit.schema.json`,
  `public/data/us-history/textbook/unit-*.json`) and the `app/textbook/[unit]` route, but it's **not a
  journey step**. Add a **"Close Read" step** in the Build Knowledge / Apply phase routing to the
  textbook close‑read view (or a thin `/practice/close-read?unit=` wrapper). **Effort:** M.
- **Exit Ticket (Activity 7 closer).** Only teacher‑side today (`lib/mtss/unit1-matrix.ts`,
  `lib/lesson-package/*`). Add a **student Exit Ticket** as the per‑standard closer (after the CER /
  `writing` step): a short check that pulls the standard's exit‑ticket item, writes to progress/mastery,
  and routes a miss into the MTSS reteach path (parity with the workbook's Exit Ticket + "What's Next").
  **Effort:** M (new student surface; data exists teacher‑side).

---

## Workstream 3 — De‑bias enforcement (parity of assessment integrity)

**Current state.** The print pipeline balances correct‑answer positions (the de‑biased sequence, e.g.
B·D·C·A·D·B·A) at build time. The app stores **fixed `correctAnswer` letters** in
`public/data/us-history/questions/unit-*/dok-*.json` with a `biasFlag: none|review|flagged` QC field
(`lib/slides/types.ts`, `lib/question-data/index.ts`) but **no build‑time or runtime position balancer**.

**Decision.** Enforce de‑bias **once, in the shared question data**, so both surfaces inherit it.
**Changes.**
1. A build‑time balancer script over the question JSON that (a) measures correct‑answer position
   distribution per form, (b) re‑orders options to hit the de‑biased target, (c) updates
   `correctAnswer` **and keeps each distractor explanation attached to its option**, (d) sets `biasFlag`.
2. Run it as a **data QC gate** (npm script + CI). The print builder consumes the **same balanced JSON**
   (single source), so print and app can't diverge.
3. Keep `biasFlag` as the audit signal.
**Risk:** M — option reorder must preserve distractor↔explanation binding (needs tests). **Effort:** M.

---

## Parity guardrail (so it stays aligned)

Add a shared **Course Standard parity spec** (one JSON/TS list of the 7 activities × their canonical
names × the 5‑element HIPPO × the de‑bias target) and an automated check that:
- both surfaces expose all 7 activities per standard under the canonical names,
- every primary‑source scaffold carries all 5 HIPPO prompts,
- answer positions pass the de‑bias target.
Wire it into the **app test suite** and the **print `preflight.py`** so a future change to either surface
fails CI if it breaks parity.

---

## Recommended sequencing

| # | Step | Why first | Effort |
|---|------|-----------|--------|
| 1 | Lock the canonical spec (names + HIPPO‑5 + de‑bias target) as one shared module | Everything references it | S |
| 2 | Workstream 1 — HIPPO to 5 elements everywhere | Biggest rigor gap; student‑facing | M–L |
| 3 | Workstream 3 — de‑bias in shared data | Integrity; benefits print + app at once | M |
| 4 | Workstream 2 — add Word Bank tab, Close Read step, Exit Ticket step | Journey surface parity | M |
| 5 | Parity guardrail test in app + preflight | Prevents re‑drift | S–M |

**Net:** the 5E journey stays — it's a fine delivery model and doesn't fight UDL/MTSS/CER. We make it
render the same seven activities, under the same names, with the full 5‑element HIPPO and de‑biased
items, and lock parity with a test. Same core, same names, same rigor — paper or screen.
