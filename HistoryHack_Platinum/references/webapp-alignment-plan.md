# Web App ↔ Print Alignment Plan — Course Standard parity

**Goal:** a student gets the **same core, same names, same rigor** whether they're on paper
(workbook + deck) or on screen (the Next.js web app). © 2026 TroopToTeacher Technologies LLC.

**Principle:** *one canonical activity spec, two renderers.* The print Course Standard is the source
of truth. The web app's 5E "unit journey" is a valid **delivery structure** (it does not conflict with
UDL/MTSS/CER/HIPPO — those are different layers), but it must render the same core activities, under
the same names, at the same rigor, on **every** standard. A parity check keeps them from drifting.

**Main frameworks — must be present on every standard (US.01–US.07), not a pilot:**
- **UDL 3.0 (CAST)** — multiple means of engagement / representation / action & expression on every activity.
- **MTSS** — Tier 1 core + Guided/Light supports + exit‑ticket‑driven reteach ("What's Next") on every standard.
- **CER — the canonical 6‑point rubric** (6 Exemplary · 5 Advanced · 4 Proficient · 3 Adequate · 2 Developing · 1 Beginning).
- **HIPPO — the full 5 elements** (Historical context · Intended audience · Purpose · Point of view · Outside).

**Canonical 7‑activity cycle (per standard):** Vocabulary Word Bank · Vocabulary Studio (Frayer) ·
Direct‑Teaching Cornell Notes (paired to deck) · Close Read · Primary Source / Data (HIPPO‑5) ·
Practice Quiz · Constructed Response (CER, 6‑point) + Exit Ticket. "I can" targets verbatim; answer
positions de‑biased.

---

## Workstream 1 — UDL 3.0 parity (main framework) · **make it universal, not a pilot**

**Current state (evidence).** `lib/feature-flags/us01-udl-mtss-pilot.ts` — UDL is gated to **US.01 only**,
as a **vertical‑slice pilot, OFF by default** in production ("does not change until a district reviewer
turns it on"). Supports exist (read‑aloud, bilingual, reading‑level, sentence frames;
`components/mtss/us01-udl-panel.tsx`, `lib/mtss/`) but only for one standard, behind a flag. The
workbook carries UDL on **every** activity of **every** standard, always on.

**Target.** UDL surfaced on every standard US.01–US.07 (then the rest of the course), on by default,
mirroring the workbook's universal supports: firm learning target + flexible means, RESPONSE CHOICE
(write / say / diagram), LANGUAGE SUPPORT, visuals, and the never‑lower‑the‑bar framing.

**Changes.**
1. Generalize the pilot: replace the `us01`‑scoped flag/panel with a standard‑agnostic
   `UdlSupportPanel` driven by per‑standard data (reuse the existing supports engine).
2. Turn it **on by default** for the shipped units (keep an admin kill‑switch, not an opt‑in gate).
3. Backfill per‑standard UDL data for US.02–US.07 (the workbook already defines these supports —
   reuse the same source rather than re‑author).
**Risk:** M — production‑behavior change; stage per unit. **Effort:** M–L.

---

## Workstream 2 — MTSS parity (main framework) · **tiers + reteach on every standard**

**Current state.** MTSS logic exists (`lib/mtss/decision.ts`, `lib/mtss/unit1-matrix.ts`) but is bound
to the same US.01 pilot flag; the exit‑ticket → reteach loop is **teacher‑side only** and single‑standard.
The teacher guide defines the full MTSS decision cycle for every standard: *Progress check → identify
barrier → select support → reteach → recheck → extend*, with scaffold fading that never displaces
IEP/504.

**Target.** The same decision cycle available on every standard: a formative check (the Exit Ticket,
Workstream 5) drives an evidence‑gated support recommendation and a "What's Next" reteach route, with
Tier 3 only ever a team‑reviewed state (already the pilot's rule — generalize it).

**Changes.**
1. Generalize `lib/mtss/unit1-matrix.ts` → a per‑standard matrix for US.01–US.07 (reuse the teacher
   guide's reteach routing as the data source — single source of truth).
2. Wire the student Exit Ticket (Workstream 5) into `lib/mtss/decision.ts` so a miss produces the same
   reteach move the workbook/teacher guide prescribes.
3. Keep de‑no‑deficit language + the "supports never lower the bar / never replace IEP‑504" rule.
**Risk:** M. **Effort:** M.

---

## Workstream 3 — CER rubric parity · **4‑point → the canonical 6‑point**

**Current state.** `app/practice/constructed-response/constructed-response-content.tsx` uses
`STANDARD_RUBRIC` = a **4‑point** scale (4 Exemplary → 1 Beginning) shown to students. The
workbook/teacher guide (`build_teacher_guide.js §15`) use the canonical **6‑point** scale; student
materials show simple **Full / Developing / Beginning per part**, teachers score on the 6‑point guide.

**Target (verbatim from the teacher guide).**
6 Exemplary · 5 Advanced · 4 Proficient · 3 Adequate · 2 Developing · 1 Beginning.

**Changes.**
1. Replace `STANDARD_RUBRIC` with the 6‑point scale from a shared `lib/frameworks/cer.ts`.
2. Keep the student surface simple (Full / Developing / Beginning per part) exactly as the workbook does;
   expose the 6‑point guide on the teacher view.
3. Point any auto‑scoring / mastery mapping at the 6‑point scale so print and app grade on one scale.
**Risk:** L–M (scoring/mastery thresholds may reference 1–4). **Effort:** M.

---

## Workstream 4 — HIPPO parity · **inconsistent 4‑element → full 5‑element (rigor fix)**

**Current state.** The app uses 4‑letter **`HIPP`** 821× and is internally inconsistent:
`dbq-content.tsx:226` → H‑I‑P‑P (no **Outside**); `:2074‑2078` → H‑I‑P‑O (no **Purpose**);
`unit-journey-client.tsx:257` step 9 → "with **HIPP**". Workbook (`build_workbook.js:330‑335`) has the
complete **5 elements**: Historical context · Intended audience · Purpose · Point of view · Outside.
So app students can be prompted for only 4 of 5 analysis moves — a real rigor gap.

**Changes.** Shared `lib/frameworks/hippo.ts` (5 elements, EN/ES) that every surface reads; fix the
journey + DBQ; then a **categorized** sweep of the 821 `\bHIPP\b` hits (student‑facing → data/scaffolds
→ docs/tests), backfilling the missing element. **Risk:** M–L (breadth). **Effort:** M–L.

---

## Workstream 5 — Add the 3 missing journey activities

`STEPS[]` / `PHASES` / `STEP_TO_STOP` in `app/units/[id]/unit-journey-client.tsx` (+ `lib/progress-store.ts`)
has no discrete Word Bank, Close Read, or Exit Ticket. Data/routes mostly exist. (Also fix the stale
"10‑step" label — there are 11 entries.)
- **Word Bank (Act 1):** a "Word Bank" tab inside the Vocabulary step — data exists. **S.**
- **Close Read (Act 4):** add a journey step routing to the existing `app/textbook/[unit]` close‑read
  content (`closeReadingProtocol`), currently orphaned from the path. **M.**
- **Exit Ticket (Act 7 closer):** add a **student** per‑standard exit ticket after CER, feeding
  progress/mastery + the MTSS reteach route (Workstream 2). Today it's teacher‑side only. **M.**

---

## Workstream 6 — De‑bias enforcement (assessment integrity)

**Current state.** Print balances correct‑answer positions at build; the app stores fixed
`correctAnswer` letters + a `biasFlag` QC field but **no balancer**. **Change:** a build‑time balancer
over the shared `public/data/us-history/questions/unit-*/dok-*.json` that reorders options (keeping each
distractor explanation bound), updates `correctAnswer`, sets `biasFlag`, and runs as a CI gate — and the
**print builder consumes the same balanced JSON** so they can't diverge. **Effort:** M.

---

## Parity guardrail (so it stays aligned)

A shared **Course Standard parity spec** (one module listing the 7 activities × canonical names ×
UDL/MTSS presence × CER‑6 × HIPPO‑5 × de‑bias target) plus an automated check that both surfaces:
expose all 7 activities per standard under the canonical names; surface UDL + MTSS on every standard;
score CER on the 6‑point scale; carry all 5 HIPPO prompts; pass the de‑bias target. Wire into the **app
test suite** and the print **`preflight.py`** so breaking parity fails CI.

---

## Recommended sequencing

| # | Step | Why | Effort |
|---|------|-----|--------|
| 1 | Shared frameworks module (UDL supports map · MTSS cycle · CER‑6 · HIPPO‑5 · de‑bias target) | Single source both surfaces read | S–M |
| 2 | **W1 UDL** + **W2 MTSS** — generalize the US.01 pilot to all standards, on by default | Main frameworks; biggest coverage gap | M–L |
| 3 | **W3 CER** 4→6 point + **W4 HIPPO** 4→5 element | Names + rigor match the workbook | M |
| 4 | **W6 de‑bias** in shared data | Integrity; benefits print + app | M |
| 5 | **W5** add Word Bank / Close Read / Exit Ticket steps | Journey surface parity (Exit Ticket also feeds MTSS) | M |
| 6 | Parity guardrail test in app + preflight | Prevents re‑drift | S–M |

**Net:** the 5E journey stays. We make it carry the **main frameworks (UDL 3.0 + MTSS) on every
standard**, score **CER on the 6‑point rubric**, prompt the **full 5‑element HIPPO**, run **de‑biased**
items, and expose all seven activities under the same names — then lock parity with a test. Same core,
same names, same rigor — paper or screen.
