# New-Course Build Prompt — a History Hack course EDITION

_Paste this into a fresh Claude Code session (in an environment that has the History Hack
skills installed). It builds a new, licensable course **inside the existing platform** —
not a new app. Filled in for **Foundations of Constitutional Government** (TN U.S.
Government & Civics). Swap the COURSE block to run it for another course._

> **Architecture decision (settled):** the app is already multi-course. `government` is a
> pre-registered subject in `lib/subjects.ts` with `contentReady:false`. Building this course
> = **populate content + flip one flag + gate by license entitlement** on the same engine
> (auth/SSO, analytics, SAMR, print-first, the Technology Promise, the "Teachers power our
> progress, not technology" theme, compliance). Do NOT build a new system or fork the app.

---

## STEP 0 — Ground yourself (every run)
1. Read `CLAUDE.md` (guardrails + the platinum system) and `00_START_HERE/playbook.html`
   in the content repo (course architecture + pedagogy).
2. In the web app read: `lib/subjects.ts` (subject registry + the "Adding a new subject"
   checklist), `lib/product-edition/` (edition membership + capability entitlement + the CI
   isolation assertion), `app/[subject]/…` (the subject-parameterized routes),
   `scripts/scaffold-world-history.mjs` (the scaffolder template), and
   `public/data/us-history/**` (the JSON shapes to mirror).
3. Load & USE these skills (invoke — don't reinvent): `history-hack-course-standard-builder`
   (master platinum pipeline), `history-hack-curriculum-architect`,
   `instructional-design-specialist`, `history-hack-question-forge`,
   `copyright-integrity-accreditation`, `history-hack-print-qc-auditor`,
   `history-hack-teacher-ux-reviewer`, `tn-textbook-adoption-agent`,
   `history-hack-website-builder`, (optional) comic + `learning-experience-designer`.

## STEP 1 — Branch, never main (both repos)
`git checkout -b course/foundations-constitutional-government` in the content repo AND the
web app. Commit per artifact; PR per phase; keep `main` clean; validate via CI (District
Edition build + isolation, vitest, axe-core).

## NON-NEGOTIABLE GUARDRAILS (from CLAUDE.md — every artifact)
Source-of-truth only (never invent standards, citations, or sources); print-first & B&W-safe
(`colorKey:true` when color encodes meaning); bilingual EN/ES · WCAG AA · ≥9pt · UDL choice;
answer keys + reteach TEACHER-SIDE ONLY; de-biased keys synced across surfaces; verify by
rendering + preflight before packaging; items "classroom-formative · pre-field-test"; theme
"Teachers power our progress, not technology"; SAMR honesty (print when print is best); no
claim of state/waiver approval where review is pending. **Tag TCA legally-required standards**
(GC.08 §49-6-1028; T-tagged GC.11/14/21/22/23–27) as "legally required to teach."

## THE COURSE — Foundations of Constitutional Government (TN GC, 9–12; supplemental, TCA §49-6-2202(a)(3))
Standards source of truth already committed: **`lib/standards/government-standards.ts`**
(SSP.01–06 practices spine + GC.01–27, strands, TCA flags, unit assignments, landmark-case
index; `iCan` fields are `null` — fill VERBATIM from the TDOE instructional guide).

Unit map (5 units): U1 Foundations GC.01–09 · U2 Legislative GC.10–15 · U3 Executive
GC.16–18 · U4 Judicial GC.19–22 · U5 Civil Liberties GC.23–27. Practices SSP.01–06 apply all
year (the SOAPS/HIPP analog — build a practices reference page + per-practice tasks).

## PER-UNIT DELIVERABLES (match History Hack exactly)
Student Workbook · Teacher Guide · Student Deck · Teacher Deck · Graphic Organizer Toolkit ·
Unit Assessment Book · sale-ready Cover Wrap — PLUS the web content set: unit narrative/chapter
· Cornell notes · vocabulary (Frayer) · question bank (DOK 1–4) · 3 spaced-retrieval rounds ·
**Founding-Document + Landmark-Case Spotlight** (Constitution/amendments, Federalist, and the
SCOTUS opinions named in the standards — full attribution + SSP analysis) · reference pages
(Constitution, amendments, the three branches, case index) · formative items · summative
DBQ/CER with synthesis trigger.

## PER-UNIT ANATOMY (from the playbook)
Banner (standards · essential question · SSP skill) → concept-before-vocabulary launch → core
narrative (2–4 sections) → Founding-Document/Case Spotlight (SSP.01–.03; 4–5 text-dependent Qs)
→ analysis activity (DOK 2–3) → 3 spaced-retrieval rounds → Open Inquiry Task (curated source
menu + product choice; SSP.04) → formative items → summative DBQ/CER → teacher guidance
(pacing, Priority Teaching Guide, exemplars, misconceptions). Civic-reasoning skill labels
(constitutional principles, federalism, separation of powers/checks & balances, rights
analysis, civic argumentation) alongside the SSPs.

## 6-PHASE PIPELINE (gates between; use the platinum skill's cradle-to-grave-workflow + prompt-library)
1 Standards intake → unit map + verbatim "I can". 2 Source procurement + rights validation
(docs + SCOTUS opinions). 3 Content authoring (narrative, Cornell, vocab, packets A/B/C, decks,
organizer toolkit). 4 Assessment authoring (banks per DOK, spiral, DBQ/CER). 5 QC gate (print
preflight, teacher-UX, standards matrix/EOC/compliance). 6 Package + deploy (cover wraps, PDFs,
web edition, mirror to Drive).

## WEB APP COURSE EDITION — exact steps (the platform already supports this)
1. **Standards source** — DONE: `lib/standards/government-standards.ts`. (If you regenerate from
   the TDOE PDF, adapt `scripts/generate_us_history_truth_data.py`.)
2. **Scaffold** — run `node scripts/scaffold-government.mjs` (already committed; STANDARDS/UNITS
   pre-filled). It emits `public/data/government/**` skeletons (textbook, questions, vocabulary,
   factcards, ican, standard-stories, standard-summaries + pacing-guide.json), each stamped
   `"subject":"government"` + `"scaffold":true`, with overwrite protection for authored files.
3. **Populate JSON** (mirror `public/data/us-history/**` shapes; keep `"subject":"government"`):
   ican, vocabulary (with `frayer`), textbook (validate: `scripts/validate-textbook-unit.mjs
   --gold`), factcards (+ `scripts/tag-fact-card-strands.mjs`), primary-sources (+ `/images` —
   heavy on founding docs + the named SCOTUS opinions), tiered-questions, standard-stories,
   standard-summaries, study-guides, biographies, and `questions/manifest.json` +
   `questions/unit-{N}/dok-{1..4}.json`.
4. **5-unit fix** — Government is **5 units** (US History is 10). Add a Government units source
   (or make the units source subject-aware) and update the `UNIT_IDS` arrays in
   `app/[subject]/units/[id]/page.tsx` and `app/[subject]/textbook/[unit]/page.tsx` to unit-1..5.
5. **In-TS content currently US-only** — make Government equivalents IF in scope, following the
   World History precedent (JSON, not TS): `lib/cornell-notes-data.ts`, `lib/spiral-review-data.ts`,
   `lib/this-day-in-history.ts`, `lib/content-translations-data.ts`. (WH moved Cornell to
   `public/data/world-history/cornell/`.)
6. **Flip + license** — set `SUBJECTS.government.contentReady = true` in `lib/subjects.ts`
   (routes go live + pre-render) ONLY after content is authored + QC'd; update
   `__tests__/lib/subjects.test.ts` counts. Gate the course via a product-edition
   capability/entitlement so a district's license unlocks it (per-course SKU).
7. **Green CI** — District Edition build + isolation, vitest, axe-core all green; new course
   routes resolve; print-first + SAMR honored; TCA standards flagged.

## DEFINITION OF DONE (per unit + course)
100% standards coverage (every GC/SSP → narrative + items across DOK + ≥1 primary source/case +
verbatim "I can"); TCA standards flagged; question bank scaled to the US-History bar (MCQ+CR+DBQ,
per-distractor rationale, DOK/Bloom/reporting-category, de-biased, bilingual); print preflight +
accessibility pass; standards-alignment matrix + EOC/adoption evidence (`tn-textbook-adoption-agent`);
web edition CI green + entitlement-gated; per-unit deliverable + QC checklist reported.

## METHOD
Unit-by-unit; platinum `prompt-library.md` phase prompts (guardrail preamble); commit per
artifact; PR per phase; main stays clean. Start: STEP 0 → branch → confirm the 5-unit map →
run `scaffold-government.mjs` → Phase 1.
```
