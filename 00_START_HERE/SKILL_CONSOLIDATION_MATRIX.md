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

---

## Reconciliation decisions — EXECUTED (branch `skill/reconcile-canonical-set`, off `origin/main`)

Recorded per the version guardrail (step 3: decision + rationale + provenance). Byte-identical overlaps
were confirmed with md5 and kept as one owner with no panel needed.

| Overlap | Candidates | Decision | Why (4-lens) |
|---|---|---|---|
| `tn-assessment-specialist` | main v3.0 / mine v2.0 / inbound v1.0 | **main v3.0 base + grafts** | main is a near-superset (all item types + full psychometrics + TCAP schema + quick-quiz + absorbed tcap-item-writer-v2 bundle). Grafted from inbound: UDL/accessibility item rules, performance-task 4-dim rubric, worked CR guide, stimulus-set template; from tcap-item-writer-v2: external-source URL table, PASS/WARN/FAIL labels. No capability lost. |
| `instructional-design-specialist` | main / inbound | **MERGE: inbound base + main grafts** | inbound = deeper learning science (Rosenshine/CLT/UbD-GRASPS/DOK blueprint/Quality Checks). Grafted from main: ASSESS/LEARN/PRACTICE/ENRICH Unit Journey IA, single-lesson drafting mode + 14-part template + curriculum-architect supersession. **Framework roster corrected (Sean): UDL 3.0/CAST 2024 + CER + C3, NO 5E; all output maps to the 7-activity flow.** |
| `learning-experience-designer` | inbound only | **KEEP-SEPARATE (adopt)** | Owns a genuinely unowned job — interactive digital/app UX (interaction patterns, journey/branching, gamification, microlearning, xAPI). Trimmed: UDL section → `udl-cast-expert`; WCAG 2.1 audit → `accessibility-qc-agent` (2.1→2.2); spacing intervals → `spaced-repetition-engine`. |
| `udl-cast-expert` | main / mine / inbound | **KEEP (identical)** | md5-identical across all three; one owner. |
| `historian-factcheck-agent` | main / mine / inbound | **KEEP (identical)** | md5-identical; one owner. |
| `tn-textbook-adoption-agent` | main / mine / inbound | **KEEP (identical)** | md5-identical; one owner. |
| `history-hack-unit-qc` | inbound | **ADOPT as orchestrator** | Added a "gate orchestration" section: it INVOKES lesson-flow-qc / text-integrity-qc / accessibility-qc / ell / print-qc — never duplicates them. |
| `history-hack-platinum-workbook` → `dbq-workbook` | main / mine | **RETIRE name → `dbq-workbook`** | Kept mine's `dbq-workbook` (correct name + product distinction); removed main's `platinum-workbook` dir; repointed all references. |
| `tcap-item-writer-v2` | main / mine / inbound | **RETIRE** | Already absent on main; folded into `tn-assessment-specialist`; all references repointed. |
| `history-hack-platinum-unit-builder` | main v1.2 | **REBUILT to v2.0 orchestrator** | Root-cause drift fix: main INLINED the gates/engine/decision-rule and said "do not invoke the standalones" (violated locked decision #2), and gated NOTES SUPPORTS OFF into the teacher pack (violated locked decision #3). Now a pure orchestrator that invokes `platinum-standard` + `unit-content-build` + `lesson-flow-qc` + `text-integrity-qc`; NOTES SUPPORTS restored to the student-book verso; America 250 palette; North-Star → Platinum. |
| `course-standard-student-workbook` edition matrix | inbound | **ABSORB into `unit-content-build`** | Added the five-edition model (Base / Support / EL / Modified / Honors) as a render flag on one engine, not five books. |

**New capability codified (Sean, mid-reconciliation):**
- **Assessment & retrieval cadence** woven into the 7-activity flow — spaced retrieval + formative + self-assessment + summative, each with a fixed home and owner (STUDENT_WORKBOOK_PLATINUM_STANDARD §7.10; `spaced-repetition-engine` owns the schedule; `tn-assessment-specialist` owns the summative).
- **Data visualization mandate** — original, accurate, sourced charts/graphs built wherever the content warrants, as read-the-data stimulus AND student create/represent move, with citation sidecar + alt text + data-table fallback (§7.11; owner `history-hack-unit-content-build`).

**Anti-drift enforcement shipped:** `.claude/skills/SKILLS.md` (one-owner registry) + `.claude/skills/lint_skills.py` + `.github/workflows/skills-lint.yml` (CI gate on name/dir mismatch, retired refs, inlined gates, registry gaps).
