# Skill Consolidation Matrix — Claude ∪ Perplexity → one platinum set

**Goal (Sean):** one platinum-integrity, non-overlapping skill set for a continuous course-build
process — most up-to-date, tight, effective; no skills stepping on each other. Take the best of both
sources. Perplexity source preserved (not active) in `_inbound/perplexity/`. This extends
`SKILLS_RECONCILIATION_PLAN.md`.

**Verdict keys:** **ADOPT** = new capability we lack, bring in. **KEEP** = ours wins / unique.
**MERGE** = both have it, best-of-breed head-to-head before finalizing. **RETIRE** = superseded.

## The headline win

Perplexity brings **real deck GENERATORS we never had** — all session we hand-edited decks because
there was no builder:
- `history-hack-tcap-deck-builder` — builds the **teacher lecture deck** (.pptx) + answer-key PDF +
  usage guide from a JSON data contract (`build_deck.js`, `make_key_pdf.py`).
- `history-hack-lean-deck-builder` — builds the **student review/lean deck** + answer key + web
  viewer manifest (`build_lean_deck.js`, `make_lean_key_pdf.py`, `gen_manifest.py`).

These are the missing engine for the deck side of every future unit.

## ADOPT — new capabilities (vet, then promote)

| Skill (from Perplexity) | Why | Note |
|---|---|---|
| `history-hack-tcap-deck-builder` | teacher lecture deck generator | pair with our lesson-flow-qc gate |
| `history-hack-lean-deck-builder` | student review deck generator + manifest | ditto; enforces vocab-first, DI parity downstream |
| `accessibility-qc-agent` | WCAG 2.2 AA / 508 gate (code + content) | complements `udl-cast-expert` (design) — one does design, one audits compliance |
| `ell-bilingual-review-specialist` | English/Spanish + ELL scaffolding QC | we had WIDA rules but no dedicated reviewer |
| `history-hack-poster-packet-builder` | 24×36 wall posters + station packets SKU | new product |
| `us-history-hack-packet-builder` | TpT / for-sale packaging (front/back matter, copyright) | commercialization |
| `magic-school-created-worksheets` | MagicSchool prompts for genuine content gaps | gap-fill |
| `history-hack-district-edition-restructure` | District Edition / product-edition / route isolation | app-side; keep separate from curriculum builders |
| `wcs-app-approval-qc` | Williamson County app-approval submission gate (COPPA/FERPA) | district submission |

## MERGE — both sources have it (best-of-breed head-to-head required)

| Job | Ours | Perplexity | Direction |
|---|---|---|---|
| Unit workbook | `unit-content-build` (guided-notes engine, verso supports) | `history-hack-course-standard-student-workbook` (Base/Support/EL/Modified/Honors editions, universal Cornell ↔ lean deck) | Merge: our engine + their edition matrix; keep verso supports (panel-locked) |
| Unit builder (orchestrator) | `platinum-unit-builder` (reconciled, references gates) | `platinum-unit-builder` (Unit-1 version) | Reconcile to one — ours references the standalone gates |
| DBQ workbook | `dbq-workbook` | `platinum-workbook` | Merge best-of-breed; keep name `dbq-workbook` |
| End-to-end unit QC | `lesson-flow-qc` + `text-integrity-qc` (runnable gates) | `history-hack-unit-qc` (workflow orchestrator) | Make unit-qc **orchestrate/call** our standalone gates — never duplicate them |
| Fact-check | `historian-factcheck-agent` | `historian-factcheck-agent` | Pick the tighter; one owner |
| Adoption | `tn-textbook-adoption-agent` | `tn-textbook-adoption-agent` | Pick the tighter; one owner |
| Copyright/IP | `copyright-integrity-accreditation` | `copyright-integrity-accreditation` | Pick the tighter; one owner |

## KEEP — ours, unique or already best

`history-hack-platinum-standard` · `history-hack-lesson-flow-qc` · `history-hack-text-integrity-qc` ·
`history-hack-graphic-organizer-workbook` · `tn-assessment-specialist` (absorbs `tcap-item-writer-v2`) ·
`udl-cast-expert` · `instructional-design-specialist` · `tt-education-research-team` ·
`history-hack-course-standard-builder` (new-course orchestrator — rename to end the collision) ·
`history-hack-print-qc-auditor`.

## RETIRE

`tcap-item-writer-v2` → into `tn-assessment-specialist`.

## Honest gap

The **MERGE** rows are not yet compared line-by-line — I've mapped them from each skill's identity,
not a full head-to-head read. Those get the 4-lens panel treatment (UDL · Schedule F · teacher-usability
· architecture) inside the reconciliation PR before a winner is locked, so we adopt the *most effective*
version, not just the newer one. ADOPT rows are new capabilities and can be promoted after a vet pass.

## Result — the canonical continuous-build system

Builders: unit builder + unit engine · **teacher deck builder** · **student deck builder** · DBQ ·
graphic organizers · poster/packet · TpT packaging · MagicSchool gap-fill · district-edition ·
new-course orchestrator. Gates: alignment · text-integrity · **accessibility** · **ELL/bilingual** ·
print · unit-QC orchestrator · **WCS approval** · fact-check · adoption · copyright. Plus mission
(platinum-standard), assessment, UDL, instructional design, research. One owner per job; lands via the
review-first skills-only PR to `main`.

---

## Batch 2 — Course Expansion skills (added 2026-08-02, staged in `_inbound/perplexity/`)

**ADOPT — new capabilities we lack:**
| Skill | Why |
|---|---|
| `spaced-repetition-engine` | retrieval-practice / spacing engine — core learning science (Rosenshine, spaced review); nothing equivalent on our side |
| `tn-content-specialist` | TN-standards content authoring specialist — fills the content-authoring seat |
| `edtech-adoption-specialist` | edtech/district *sales & adoption* — distinct from `tn-textbook-adoption-agent` (TDOE textbook rubric); confirm the two don't overlap, then keep both with clear lanes |

**MERGE — version/overlap (head-to-head required, see guardrail below):**
`tn-assessment-specialist` (Perplexity vs ours vs the #4 v3 — pick/merge the richest) ·
`tcap-item-writer-v2` (still slated to fold into `tn-assessment-specialist`; harvest its psychometric
depth first — Perplexity's copy is 23 KB) · `udl-cast-expert` (Perplexity vs ours) ·
`instructional-design-specialist` (Perplexity vs #4) · `learning-experience-designer` (Perplexity vs ours).

## Best-of-breed VERSION guardrail (never old over best)

Before ANY overlapping skill is promoted from `_inbound/` into active `.claude/skills/`:
1. **Head-to-head compare the candidate versions' content against the mission** — 4-lens panel
   (UDL · Schedule F · teacher-usability · architecture) for anything non-trivial.
2. **Never auto-pick by source, filename, or age.** Newer is not automatically better; older is not
   automatically safer. The winner is the **most effective for students + adoption**. Where each
   version has a unique strength, **MERGE** — take the best of each.
3. **Record the decision + one-line rationale + provenance** in this matrix (which version won, why).
4. **Promote only after** it loads clean, contradicts nothing in the canonical set, and has a
   one-owner registry entry.

This four-step compare **is** the QC process/guardrail that guarantees the best skill wins — it runs
inside the review-first skills-only reconciliation PR, and no skill goes active without it.
