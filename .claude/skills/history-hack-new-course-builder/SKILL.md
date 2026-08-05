---
name: history-hack-new-course-builder
description: Master cradle-to-grave pipeline for building a NEW licensable History Hack course edition from a set of state standards — feature-for-feature and guardrail-for-guardrail with the U.S. History flagship. Use when asked to build, scaffold, or stand up a new course/subject (e.g., Government/Civics, Economics, World History, Geography) as an entitlement-gated edition inside the existing platform (not a new app, not a fork): standards intake, unit mapping, primary-source + case procurement, content authoring (narrative, Cornell, Frayer vocab, packets, decks, organizer toolkits), TCAP-grade assessment banks with analytics/mastery/remediation, QC gates (Schedule F, print preflight, item-rigor), and web-edition registration. Orchestrates the specialist skills; does not reinvent their logic.
metadata:
  author: Sean Reynolds / TroopToTeacher Technologies LLC
  version: '1.0'
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, or QC ANY artifact —
> workbook, teacher/student slide deck, graphic organizer, poster, DBQ, assessment or test, worksheet, comic,
> web page, or anything else — from memory, a cached copy, or a prior session. **Re-read the CURRENT version of
> THIS skill from `main` first** — skills are the single source of truth and change only via skills-only PRs.
> Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix, and never read from or write to the protected `us-history` flagship
> on a non-US build. If you cannot confirm you are on the current skill, **STOP and pull it first.**

# History Hack — New Course Standard Builder (Platinum Pipeline)

Build a new course to the same platinum bar as U.S. History. **Match feature-for-feature and
guardrail-for-guardrail.** Source of truth only — never invent standards, citations, or sources.

## STEP 0 — Ground yourself every run
0. **Resolve + declare the course, then honor the walls.** This skill OWNS the **Course-Binding Standard**:
   `references/course-binding-and-walls.md` (the 7-course registry, the `course.json` config contract, and the
   hard walls W1–W7). Before anything else, resolve the course id and state it; read standards/content ONLY from
   that course's `standardsFile`/`contentRoots`; emit ONLY its `standardsPrefix` codes; never touch another
   course or the protected `us-history` flagship. Every shared build skill consumes this same wall.
1. Read repo memory/guardrails (`CLAUDE.md` if present) and `00_START_HERE/playbook.html`.
2. Locate the flagship data contracts to mirror: the standards source JSON, a unit `*_content.json`,
   the canonical primary-source bank (`public/data/<subject>/primary-sources/…`), and the question
   bank (`public/data/<subject>/questions/unit-<N>/dok-<1..4>.json`).
3. Load and USE these specialist skills — invoke, don't reinvent:
   - `instructional-design-specialist` — unit architecture, "I can" targets
   - `tn-assessment-specialist` — the authoritative item schema + rigor + QC
   - `udl-cast-expert` — UDL 3.0 / CAST review of every artifact
   - `tt-education-research-team` — evidence base / ESSA tiers for adoption
   - `tn-textbook-adoption-agent` — Schedule F scoring + submission package
   - `historian-factcheck-agent` — claim-by-claim primary-source verification (dates, statutes, cases)
   - `history-hack-platinum-unit-builder` (unit sets) / `history-hack-dbq-workbook` (DBQ SKU) / `us-history-hack-packet-builder` — sale-ready packet builds
   - `history-hack-print-qc-auditor` · `history-hack-teacher-ux-reviewer` · `history-hack-website-builder`

## THE 6-PHASE PIPELINE (gates between phases)
1. **Standards intake** → verbatim standards JSON + unit map + verbatim "I can" targets.
2. **Source + case procurement** → canonical primary-source bank, rights validated, full citations.
3. **Content authoring** → narrative, Cornell notes, Frayer vocab, packets A/B/C, decks, organizer toolkit.
4. **Assessment authoring** → question banks per DOK 1–4 (+ spiral, DBQ/CER) to the item-writer schema.
5. **QC gate** → Schedule F self-assessment, print preflight, item-rigor linter, teacher-UX, fact-check.
6. **Package + deploy** → cover wraps, PDFs, web-edition registration (entitlement-gated), mirror to Drive.

## DATA CONTRACTS (replicate exactly)

### Standards source (`<subject>_standards_source.json`)
```
CODE → { title, standard (VERBATIM), ican (verbatim guide target), dimensions "(C,E,G,H,P,T,TCA)",
         tca "(T.C.A. § …)" when legally required, unit, unit_title, quarter }
```
`ican` derives from the verbatim standard when no guide column exists.

### Unit content (`unit<N>_content.json`) — per standard
`title · tn(verbatim) · ican · vocab[{term,say,es,def}] · sources[{title,who,date,quote,repo,url}] ·
cfu{dok,stem,options,key,why} · auth{close,tdq[3],frayer,quiz,cer} · target · criteria · cues ·
dim_map · hook · civic/skill label · ssp_focus`

### Canonical primary-source bank (`public/data/<subject>/primary-sources/unit-<N>.json`)
Each record: `id·type·title·author·date·repository·url·rights·excerpt·citation_chicago·standards·colorKey`.
Images live in `images/unit-<N>.json` with EN/ES alt text; `colorKey:true` only when color encodes meaning.

### Question bank — use the `tn-assessment-specialist` JSON schema
Every item: `id·standard·secondaryStandard·unit·reportingCategory·dok·blooms·dokRationale·bloomsRationale·
question·stimulus·stimulusAttribution·options·correctAnswer·distractorTags(PK/MC/PE/NE/CA/AN/OG)·
distractorRationales·c3Dimension·sspAlignment·tennesseeSpecific·tcaRequired·contentTags·type·pointValue`.

## NON-NEGOTIABLE GUARDRAILS (every artifact)
- **Source of truth only. Fabricate nothing** — standards + dimension tags + "I can" verbatim; real cited
  primary sources (National Archives, Library of Congress, Avalon, Congress.gov, pre-1929/gov works).
- **Never print the source-district label** (the instructional-guide district's name/acronym) or district-
  local references anywhere; generalize to "your county/district." Enforce with a build-time guard
  (construct the forbidden token as `"W"+"CS"` so the literal never appears in the repo).
- **Print-first, B&W-safe.** Everything has a print pathway; ≥9pt; color only when it encodes meaning (`colorKey:true`).
- **Bilingual EN/ES · WCAG AA · UDL response choice** (write/draw/record/discuss + access supports).
- **Answer keys + "What's Next" reteach are TEACHER-SIDE ONLY.** De-biased answer positions synced across surfaces.
- **Assessment items disclose** "classroom-formative · pre-field-test" until calibrated.
- Theme: "Teachers power our progress, not technology." SAMR honesty. No claim of state/waiver/Commission approval where review is pending.

## ASSESSMENT RIGOR — enforce, don't hope
Author to the item-writer schema, then run the bundled gate `assets/assessment_rigor_check.py`. It must
report **0 flags** before an item ships. It checks: de-biased keys (even A/B/C/D); **option-length parity
(max/min word ratio ≤ ~1.6; correct answer NOT uniquely longest)**; Option D not weakest; every distractor
**tagged (PK/MC/PE/NE/CA/AN/OG) with a rationale**; complete-question stems; no AOTA/NOTA; no absolute
qualifiers (always/never); dok↔blooms consistency. Historical distractor plausibility is judged by the
assessment skills, not the linter.

## ANALYTICS · MASTERY · REMEDIATION (the product differentiator — build it in)
This is the selling point. Every item carries a **remediation route** (→ its standard's reteach narrative
section + teacher "What's Next" + EN/ES vocab + primary source) and a **per-distractor misconception map**.
Ship a `mastery-config.json`: per-standard mastery tiers (Developing→Approaching→Proficient→Mastered),
DOK-weighted (DOK 3–4 ×1.5), a **remediation trigger** (any standard below Proficient surfaces its reteach
route on the teacher dashboard + student practice queue), and **spiral interleaving** (missed standards
re-enter the 3 spaced-retrieval rounds).

## SCHEDULE F — the QC spine
Score every unit against the TDOE Social Studies rubric: **Gateway** (standards alignment guide in the
scope & sequence; ALL standards addressed), **Table 1** Alignment of Content, **Table 2** Instructional
Focus (inquiry, student-centered, **concepts-before-vocabulary**, multiple perspectives, disciplinary
literacy, connections), **Table 3** SSPs (six practices), **Table 4** Accessibility (digital **+ printable**;
SWD/ELL supports **every** lesson). Keep a per-course `schedule-f-alignment.html` honest and current.

## WEB EDITION — licensable course inside the ONE platform (not a new app)
Register `<subject>` in the product-edition/capability registry (mirror U.S. History) so a district license
unlocks it; keep route isolation + the CI isolation assertion green. Canonical banks + `lib/units`,
`<subject>-standards`, `lib/question-data`, cornell-notes, vocabulary, spiral, trivia — each keyed to the
new standards. Non-core features behind feature flags.

## DEFINITION OF DONE (per unit AND course)
100% standards coverage (every standard → narrative + items across DOK 1–4 + ≥1 primary source/case +
verbatim "I can"); TCA standards flagged; question bank to the item-writer bar (per-distractor rationale,
DOK/Bloom/reporting-category, de-biased, bilingual, **0 rigor-linter flags**); print preflight + WCAG pass;
standards matrix + Schedule F + adoption evidence; web edition CI green, routes resolve, entitlement-gated;
per-unit deliverable + QC checklist reported.

## WORKING METHOD
Unit-by-unit. **One authored source JSON per unit → reproducible generators render every surface** (HTML
chapter, teacher guide, docx packets, question bank). Commit per artifact; PR per phase; keep main clean.

---

## LESSONS & ADDITIONS (what this pipeline adds beyond the original brief)
These were learned building the Government edition and should be standard practice:

1. **Verify the unit map against the authoritative source — never trust the brief.** The Government brief
   said 5 units / GC.01–27; the official instructional playbook was **7 units / GC.01–GC.35** (adding Citizen
   Participation and TN State & Local Government, non-sequential numbering). Always reconcile the intake to
   the real standards document and surface deltas.
2. **Distinguish (T) from TCA.** The `(T)` Tennessee *dimension* is not a legal mandate; only standards
   with a `T.C.A. §` citation are legally required. Flag precisely.
3. **The item-rigor linter is a mandatory gate, not a nicety.** A first-pass bank had the correct answer as
   the longest option in 14/16 items — a classic tell. Enforce length parity mechanically (bundled asset).
4. **Source-of-truth channel:** large chat pastes drop silently and official gov sites are egress-blocked.
   The reliable channel is a **Google Drive folder** (or a pushed repo file). Read standards, guides,
   rubrics, and skills from there; cite the file/fileId for provenance.
5. **Reproducible generators over hand-authored files.** Author one JSON source per unit; render HTML,
   teacher guide, banks, and matrices from it so a standards fix propagates everywhere.
6. **Guard the forbidden token in the build**, and keep answer keys/reteach strictly teacher-side.
7. **Fact-check before packaging** with `historian-factcheck-agent` (dates, statutes, case citations,
   quotations) — evidence-only VERIFIED scoring; no source = CANNOT VERIFY.
8. **Toolchain:** node + `docx` (docx-js) + LibreOffice (`soffice`) render the sale-ready .docx/PDF packets;
   the print-first HTML chapter is the always-verifiable fallback.
