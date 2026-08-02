# Slide-Native 12-Item QC Checklist — History Hack Slide-Deck Subsystem

Authoritative checklist for QC'ing slide decks (and their backing primary-source catalog) in `history-hack-web-app`. **Use this — NOT the 18-item textbook checklist — for any slide-deck or primary-source-catalog QC. Unit 1 is the reference state.**

Established April 22, 2026 with `docs/qc/unit-1-slide-qc-round-1.md` as the Unit 1 reference.

---

## Scope

This checklist covers:
- The slide-deck subsystem code, schema, scripts, and renderers (`lib/slides/*`, `components/slides/*`, `scripts/check-deck-*`, `scripts/generate-a11y-evidence.mjs`, `app/api/decks/[deckId]/export/route.server.ts`)
- The per-unit primary-source catalog (`public/data/primary-sources/unit-{N}.json`) — every deck cites this
- CI gates: `npm run check:decks` (citations + permalinks) and `npm run check:a11y-evidence`

This checklist does NOT cover:
- Textbook narrative, I Can, vocabulary, printables, Cornell notes, pacing — use the 18-item checklist for those
- Authored deck instances stored in Azure SQL / localStorage — once those exist per-unit, a Round 2 per-deck content QC is required

---

## The 12-Item Checklist

### Critical (4) — ship blockers

**C1 · No first-person impersonation of real historical figures**
- Audit every `excerpt` in `public/data/primary-sources/unit-{N}.json`
- First-person is LEGITIMATE when the author is a real historical figure AND the quote comes from a documented primary source (testimony, speech, published book, letter)
- First-person is a BLOCKER when the "quote" is invented (patterns like "My name is X, and..." with no primary-source URL, or dated telegrams/letters not in any archive)
- Contrast reference: `docs/qc/standards-slides-qc-round-1.md` blocker B-1 (15+ impersonations of Carter Glass, Ida Tarbell, Rose Schneiderman, etc.)

**C2 · No fabricated/unverifiable dated primary-source quotations**
- Every dated quote (`"date": "YYYY"` + `"excerpt": "..."` + `"author": "Named Person or Publication"`) must verify against a primary-source URL
- Apocryphal / folk sayings / oral traditions must be labeled as such — never dated as if a single document
- If `sourceUrl` is a general presentation page (not a direct permalink to the document), flag
- Litmus test: 10 minutes of Google searching across the catalog should find zero quotes that couldn't exist (paper founded later, person dead, statute text misquoted)

**C3 · No duplicate or mis-assigned unit catalog files**
- Run `md5sum public/data/primary-sources/unit-*.json` — all 10 hashes must be unique
- Each entry's `unitId` must match its filename
- Contrast reference: standards-stories round-1 blocker B-2 (unit-5.json = unit-4.json byte-identical)

**C4 · Every unit standard has at least one primary-source catalog entry**
- Audit `standardId` coverage across the unit's catalog
- Unit ranges (per textbook reference state):
  - Unit 1: US.01–US.07
  - Unit 2: US.08–US.18
  - Unit 3: US.19–US.24
  - Unit 4: US.25–US.38
  - Unit 5: US.39–US.44
  - Unit 6: US.45–US.55
  - Unit 7: US.56–US.67
  - Unit 8: US.68–US.77
  - Unit 9: US.78–US.88
  - Unit 10: US.89–US.95
- Gaps are scope questions for the operator — confirm range before flagging as blocker

### High (4) — TDOE submission blockers

**H5 · Zod schema compliance on save + export**
- Run `npx vitest run __tests__/lib/slides/schema.test.ts` → must be 21/21 passing
- Schema hard gates: ≤5 bullets/slide, ≤14 words/bullet, ≤400 chars/quote, `US\.\d+` standard codes, unit-id restricted to unit-1..unit-11, provenance required on primary-source slides, DOK required on CFU slides, structured SpeakerNotes required for new decks

**H6 · `npm run check:decks` green**
- Two scripts: `check-deck-citations.mjs` (offline, static) and `check-deck-permalinks.mjs` (live HEAD)
- Citations: every PS slide declares `quote + attribution + citation`; every `citationIds` entry resolves; every PS record has `sourceUrl` on scholarly allowlist; no duplicate ids; 4-digit year between 1600 and current year + 1; zero TBD/TODO/FIXME
- Permalinks: no 404 or soft-404. 403 from federal domains (.loc.gov, archives.gov) may be bot-block — manually verify in browser; swap to Internet Archive or alternate permalink if truly dead
- Known allowlisted non-error deferrals: cross-unit id collisions on `ps-us84-1`/`ps-us84-2` (tracked in RUNBOOK-slides)

**H7 · `npm run check:a11y-evidence` green, zero Unverified**
- Must print "No Unverified rows. Fragments are VPAT-ready."
- 5 renderer catalogs (title, bullets, two-column, primary-source, check-for-understanding) × 18 WCAG 2.2 AA success criteria
- Every row must be `Supports` (source:line + test anchor) or explicit `Not Applicable` (with rationale)
- Any `Unverified` row is a fail-closed blocker under `accessibility-qc-agent` Rule 5

**H8 · DOK coverage on CFU slides**
- Schema level: `dokLevelSchema = z.union([z.literal(1), z.literal(2), z.literal(3), z.literal(4)])` on every CFU meta
- Audit in authored decks: every CFU slide must declare DOK 1–4, Bloom, TCAP level, optional Hess CRM cell
- Distribution target across a unit: balanced 1–4, not concentrated on DOK 1–2

### Medium (3) — quality and coverage

**M9 · Bilingual coverage**
- Every catalog entry has full Spanish parallel fields: `excerptEs`, `explanationEs`, `questionEs`, `documentTitleEs`, `standardDescriptionEs`, `historicalContextEs`, `excerptEvidenceEs`
- `deck.locale` honored (`"en" | "es" | "en-es-split"`) in renderers
- Chrome localization via `t(deck, "<key>")`; outer element has `slideLangAttr(deck)`
- Inline `lang="es"` on embedded Spanish fragments of English decks
- Register: WIDA ELD 2020 + College Board AP Spanish rubric

**M10 · Speaker notes present and meaningful on every slide**
- New decks REQUIRE structured `SpeakerNotes` (not string fallback)
- Primary-source slides: `hippoScript` + `provenanceNote` required (Zod refinement)
- CFU slides: `misconceptions` array (up to 6); timing; optional differentiation by band (below/approaching/on-level/advanced/exceeds)
- Run `npx vitest run __tests__/lib/slides/speaker-notes.test.ts` — must pass

**M11 · PPTX export round-trip clean**
- Run `npx vitest run __tests__/lib/slides/pptx-export.test.ts` → must be 4/4 passing
- `validateDeck` pre-flight throws before writing a byte on any Zod failure
- Output is Google-Slides-safe: Calibri, PNG only, no SVG, no SmartArt, no animations
- Every export logged to `slide_deck_exports` table

### Low (1)

**L12 · SlideFrame standards badge + ARIA**
- `components/slides/slide-frame.tsx` must have `role="group"` on outer `<section>`, `aria-label` with headline fallback, `StandardsBadge` component mounted top-right when codes exist
- Inner `<div>` uses `role="presentation"` to avoid landmark double-up
- Badge has its own localized `aria-label`: `"Tennessee standards: US.01, US.02"` via `t(deck, "slide.standardsBadge.aria")`

---

## Execution Workflow

Same discipline as the 18-item textbook QC:

1. **Audit first** — run gate scripts and enumerate catalog entries before any edits
2. **Todo list** — one item per PARTIAL/TODO finding
3. **Priority-band commits** — Critical batch, High batch, Medium batch, Low batch
4. **Evidence-only PASS** — no source / no test = not PASS
5. **STATUS blocks** — Disposition (PASS / CONDITIONAL / FAIL), Scorecard table, per-item detail with evidence
6. **Credit-conscious** — local edits, no subagents for catalog work, batch commits

---

## Report Template

Write reports to `docs/qc/unit-{N}-slide-qc-round-{R}.md`. Required sections:

1. **Executive Summary** — Disposition (PASS / CONDITIONAL / FAIL), Scorecard table (12 items × status)
2. **Checklist Detail** — per-item evidence, test output, audit results
3. **Findings Requiring Operator Decision** — numbered F-1..F-N, each with severity + recommendation + auto-applyable flag
4. **What This Report Does NOT Cover** — authored deck instances, live human-in-the-loop PPTX review, out-of-scope cross-unit work
5. **Recommended Sequence** — numbered action sequence
6. **TDOE Policy 2.600 / Schedule F Traceability** — table mapping checklist items to rubric areas

---

## Git Commit Messages

```
Unit {N} slide QC Round {R}: {X}/12 PASS, {Y} CONDITIONAL/FAIL

Slide-native 12-item checklist (Critical 4 / High 4 / Medium 3 / Low 1).
Findings: {summary}.

Gates: schema {X}/{Y}, pptx {X}/{Y}, check:deck-citations {N} errors,
check:a11y-evidence {status}.
```

Auto-apply commits:
```
Unit {N} slide QC Round {R} auto-apply: {brief}

Addresses F-{N} from docs/qc/unit-{N}-slide-qc-round-{R}.md.
```

---

## Progress Register

| Unit | Round | Date | Disposition | Report |
|---|---|---|---|---|
| 1 | 1 | 2026-04-22 | CONDITIONAL PASS (11/12, F-1 apocryphal quote) | `docs/qc/unit-1-slide-qc-round-1.md` |
| 2 | — | pending | — | — |
| 3 | — | pending | — | — |
| 4 | — | pending | — | — |
| 5 | — | pending | — | — |
| 6 | — | pending | — | — |
| 7 | — | pending | — | — |
| 8 | — | pending | — | — |
| 9 | — | pending | — | — |
| 10 | — | pending | — | — |
