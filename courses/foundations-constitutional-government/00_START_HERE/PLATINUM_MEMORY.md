# Platinum Build System — Internalized Memory (Government Course)

> "Add this to your memory." This file is the persistent grounding for building
> **Foundations of Constitutional Government** through History Hack's platinum pipeline.
> Source of truth: the `HistoryHack_Platinum/` engine (ported from
> `claude/unit-5-platinum-pilot-jcubu6`) + the course brief. Never invent standards/citations/sources.

## Where the engine lives (ported into this branch)
- `HistoryHack_Platinum/build/` — generators + data contract + preflight:
  - `build_workbook.js` — Student Workbook (7 activities/standard; Cornell paired to the deck; HIPPO; CER; exit tickets; doodle zones; print-safe images)
  - `build_teacher_guide.js` — Teacher How-to-Use & MTSS Guide (SSP + dimension crosswalks, 6-pt CER rubric, answer keys, exit-ticket keys + "What's Next" reteach)
  - `build_assessment_book.js` — Formative checkpoints · Summative Form A/B · Teacher Key/Analysis/Reteach
  - `build_organizer_toolkit.js` — Graphic Organizer Toolkit (also see skill `history-hack-graphic-organizer-workbook`, ported to `.claude/skills/`)
  - `build_cover.js` — sale-ready Cover Wrap (front · spine · back + print/listing spec)
  - `build_student.py` / `build_teacher.py` / `uno_fields.py` (TOC bake → PDF via LibreOffice/uno) / `uno_render.py`
  - `preflight.py` — 11 release checks (see below)
  - `tn_standards_source.json` — US-History standards (reference schema)
  - `unit1_content.json`, `unit1_assessment.json`, `unit1_images.json`, `unit1_exit_tickets.json` — reference data contract

## Standards source schema (replicate as `government_standards_source.json`)
```
CODE → {
  "title":      editorial title (from Teacher Deck STANDARD slide),
  "standard":   VERBATIM official TN standard text (NEVER paraphrase),
  "dimensions": "(C, E, G, H, P, T, TCA)"  — discipline tags, part of the standard,
  "tca":        "(T.C.A. § …)"  — present only when legally required
}
```
`ican` is derived from the verbatim standard ("Explain how…" → "I can explain how…").
**Single true dependency for Government: verbatim GC.01–GC.27 + SSP.01–06 text** (TDOE egress-blocked here).

## Content data contract (per standard, from `unit1_content.json`)
`title · tn (verbatim) · ican · ref(page map) · vocab[3] · sources[2] · cfu{dok,stem,options,key,why} ·
auth{close, tdq[3], frayer[2], quiz[1], cer} · std_source · target · criteria[3] · cues[4]`

## Guardrails (every artifact)
- Source of truth only; **never print "WCS"** (preflight fails on it).
- Standards + "I can" verbatim; dimension tags + TCA citations are part of the standard.
- Print-first, B&W-safe interior; color only when it *encodes* meaning → `colorKey:true`
  (build prints "view full-color on the projection slide"; color original lives in the deck).
- Bilingual EN/ES · WCAG AA · ≥9pt · UDL response choice · grayscale-legible.
- Answer keys + "What's Next" reteach are **teacher-side only**; de-biased answer positions synced across surfaces.
- Assessment items disclose "classroom-formative · pre-field-test."
- Theme: "Teachers power our progress, not technology." SAMR honesty (print when print is best).
- Nothing claims state/waiver approval where external review is pending.
- **TCA legally-required flag: GC.08 only** (T.C.A. § 49-6-1028), per the authoritative source. Other (T) tags = Tennessee *dimension*, not a legal mandate. Course-level compliance also cites T.C.A. §§ 49-6-1011, 49-6-1014 (Freedom Week) and 36 U.S. Code § 106.
- **NEVER mention "WCS" anywhere — in content, teacher materials, matrices, or the site (author-confirmed, absolute).** The "I can" targets originate from the WCS instructional-guide column and contain WCS-local references (e.g., "Williamson County" in GC.29). Carry the target *text* only; strip the WCS label entirely and generalize local references ("your county/district") on every surface. preflight fails on any "WCS".

## preflight.py — 11 release checks (must pass before packaging)
standards verbatim · no answer leak (student side) · de-biased keys · citations + alt text ·
SSP/dimension crosswalks present · pre-field-test disclosure · **no "WCS"** · (+ others — run to enumerate).

## Government-specific adaptations
- Primary Source Spotlight → **Founding-Document / Landmark-Case Spotlight** (Constitution & amendments,
  Federalist Papers, the SCOTUS opinions named in the standards) with full attribution + SSP analysis.
- Skills spine → **SSP.01–SSP.06** (inquiry cycle + historical/geographic awareness) is the SOAPS/HIPP analog.
  Build a practices reference page + per-skill practice tasks; tag each activity with the SSP applied.
- Civic-reasoning skill labels alongside SSPs: constitutional principles · federalism ·
  separation of powers / checks & balances · rights analysis · civic argumentation.

## Web edition (licensable course inside the ONE platform — not a new app)
Register "government" as an entitlement-gated course mirroring U.S. History:
product-edition registry + capability/entitlement; canonical banks
`public/data/government/primary-sources/…` and `…/questions/unit-<N>/dok-<1..4>.json`;
`lib/units` (**7 GC units**), `government-standards`, `lib/question-data`, cornell-notes, vocabulary, spiral, trivia;
wire `app/[subject]/…` routes for "government"; keep route-isolation + CI isolation assertion green;
non-core features behind `lib/feature-flags/optional-features.ts`. See `HistoryHack_Platinum/WEBAPP_LIBRARY_EXTENSION_SPEC.md`.

## Environment notes for this build
- No `CLAUDE.md` in repo → guardrails sourced from `00_START_HERE/playbook.html` + course brief + this file.
- Master skill `history-hack-course-standard-builder` NOT installed → orchestrate manually with the ported engine + installed skills.
- Web-app repo (`history-hack-web-app`) NOT in this session's scope → this run = content-repo half + web-edition spec.
- Egress policy blocks tn.gov / myconnectsuite / district mirrors → verbatim GC standards must be pasted or supplied via an in-scope repo/file.
