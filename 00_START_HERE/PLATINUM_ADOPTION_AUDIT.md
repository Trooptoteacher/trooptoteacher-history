# Platinum Adoption Audit — the audit trail

**Purpose (Sean):** before building the next ~8 courses, confirm we captured *everything* — every
skill, every guardrail, what it was, whether it's adopted, and **where it lives now** (the crosswalk).
This is the pre-flight checklist for the continuous build.

**Legend:** ⭐ **PLATINUM** (canonical, best-of-best, build to this) · ✅ **ADOPT** (bringing in) ·
🔁 **MERGE** (both/versions exist — best-of-breed compare pending, per the version guardrail) ·
~~**RETIRE**~~ (superseded — crossed out, function moved) · **Active** = live in `.claude/skills/` ·
**Staged** = preserved in `_inbound/perplexity/`, NOT yet active.

**Honest status up front:** the canonical set is *decided*; most of it is not yet *promoted*. Active
skills are live; ADOPT/MERGE skills are staged in `_inbound/` and go active only via the review-first
**skills-only reconciliation PR to `main`** (each passing the version guardrail). Nothing is lost —
everything is either active or staged in the repo.

---

## A. Guardrails & standards (the Platinum reference docs) — all captured, all in `00_START_HERE/`

| Guardrail / standard | What it governs | ⭐ | Located now |
|---|---|---|---|
| `BUILD_STANDARD.md` | the one-spot front door: product types, all guardrails, registry | ⭐ | `00_START_HERE/` |
| `history-hack-platinum-standard` (skill) | mission · decision rule · **Gold vs Platinum** · **future-ready** | ⭐ | `.claude/skills/` (renamed from north-star) |
| `ADOPTION_STANDARD.md` | full doctrine (mission, decision rule, taglines) | ⭐ | `00_START_HERE/` |
| `BRAND_PALETTE.md` | **America 250** palette (retires #1B2A4A/#0A1F3C/#C89B3C) | ⭐ | `00_START_HERE/` |
| `STUDENT_WORKBOOK_PLATINUM_STANDARD.md` | 7-activity spine · §5 white-space banded rule · §7.9 verso supports · notebook lines | ⭐ | `00_START_HERE/` |
| `SLIDE_DECK_PLATINUM_STANDARD.md` | deck guardrails (merge-not-author, vocab-first, DI k of M) | ⭐ | `00_START_HERE/` |
| workbook↔deck alignment (role-based `▶ Deck · <Role>`) | exact-slide guidance, no hard numbers | ⭐ | `BUILD_STANDARD.md` §3 + lesson-flow-qc |
| HTML→PDF / white-space activity library | fill white space with standards-aligned moves | ⭐ | `dbq-workbook/references/white-space-activity-library.md` |
| `SKILLS_RECONCILIATION_PLAN.md` · `SKILL_CONSOLIDATION_MATRIX.md` | the merge blueprint + best-of-breed version guardrail | ⭐ | `00_START_HERE/` |

## B. Skills crosswalk — every candidate → decision → location now → canonical home

### Mission / doctrine
| Skill | What it is | Decision | Located now | Canonical home |
|---|---|---|---|---|
| `history-hack-platinum-standard` | mission + decision rule + Gold/Platinum + future-ready | ⭐ KEEP (renamed) | Active | `.claude/skills/` |

### Builders
| Skill | What it is | Decision | Located now | Canonical home |
|---|---|---|---|---|
| `history-hack-platinum-unit-builder` | THE unit builder (workbook + decks orchestrator) | ⭐ KEEP + 🔁 reconcile (strip inlined gates → reference standalone) | Active + Staged | `.claude/skills/` |
| `history-hack-unit-content-build` | unit content engine (`build_guided_notes.py`) | ⭐ KEEP + 🔁 absorb edition matrix | Active | `.claude/skills/` |
| `history-hack-course-standard-student-workbook` | Base/Support/EL/Modified/Honors editions, universal Cornell | 🔁 MERGE → into unit-content-build | Staged | folds into `unit-content-build` |
| `history-hack-tcap-deck-builder` | **teacher lecture deck generator** (build_deck.js) | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `history-hack-lean-deck-builder` | **student review deck generator** + manifest | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `history-hack-dbq-workbook` | DBQ / primary-source SKU | ⭐ KEEP + 🔁 merge `platinum-workbook` | Active | `.claude/skills/` |
| ~~`history-hack-platinum-workbook`~~ | old name for the DBQ SKU | ~~RETIRE~~ → `dbq-workbook` | Staged | → `history-hack-dbq-workbook` |
| `history-hack-graphic-organizer-workbook` | organizer toolkit (carries Cornell supports reproducibles) | ⭐ KEEP | Active | `.claude/skills/` |
| `history-hack-poster-packet-builder` | 24×36 wall posters + station packets | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `us-history-hack-packet-builder` | TpT / for-sale packaging | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `magic-school-created-worksheets` | MagicSchool prompts for content gaps | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `history-hack-district-edition-restructure` | District Edition / product editions (app-side) | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `history-hack-course-standard-builder` | new-course orchestrator (cradle-to-grave) | ⭐ KEEP (rename to end collision) | Active | `.claude/skills/` |

### Content / learning design
| Skill | What it is | Decision | Located now | Canonical home |
|---|---|---|---|---|
| `tn-content-specialist` | TN-standards content authoring | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `spaced-repetition-engine` | retrieval-practice / spacing engine | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `instructional-design-specialist` | research-based lesson/unit design | 🔁 MERGE (staged vs #4) | Staged | `.claude/skills/` (best version) |
| `learning-experience-designer` | interactive/UX learning design | 🔁 MERGE | Staged | `.claude/skills/` (best version) |
| `udl-cast-expert` | UDL 3.0 / CAST | ⭐ KEEP + 🔁 vs staged version | Active + Staged | `.claude/skills/` (best version) |
| `tt-education-research-team` | ESSA evidence / research foundations | ⭐ KEEP | Active | `.claude/skills/` |

### Gates (QC)
| Skill | What it is | Decision | Located now | Canonical home |
|---|---|---|---|---|
| `history-hack-lesson-flow-qc` | deck↔workbook exact-slide alignment gate | ⭐ KEEP | Active | `.claude/skills/` |
| `history-hack-text-integrity-qc` | no truncated/clipped/placeholder text gate | ⭐ KEEP | Active | `.claude/skills/` |
| `history-hack-print-qc-auditor` | print-defect / classroom-readiness audit | ⭐ KEEP | Available (plugin) | `.claude/skills/` (confirm in-repo) |
| `accessibility-qc-agent` | WCAG 2.2 AA / 508 gate | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `ell-bilingual-review-specialist` | English/Spanish + ELL scaffolding QC | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `history-hack-unit-qc` | end-to-end unit QC workflow | 🔁 MERGE → orchestrate our gates (never duplicate) | Staged | `.claude/skills/` (as orchestrator) |
| `wcs-app-approval-qc` | Williamson County app-approval gate | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `historian-factcheck-agent` | primary-source fact-check (Policy 2.600) | 🔁 MERGE (pick tighter) | Active + Staged | `.claude/skills/` (best version) |
| `tn-textbook-adoption-agent` | TDOE Schedule F / adoption audit | 🔁 MERGE (pick tighter) | Active + Staged | `.claude/skills/` (best version) |
| `edtech-adoption-specialist` | edtech/district sales & adoption (distinct lane) | ✅ ADOPT | Staged | `.claude/skills/` (after vet) |
| `copyright-integrity-accreditation` | IP / licensing / FERPA-COPPA | 🔁 MERGE (pick tighter) | Staged + Available | `.claude/skills/` (best version) |

### Assessment
| Skill | What it is | Decision | Located now | Canonical home |
|---|---|---|---|---|
| `tn-assessment-specialist` | write + psychometric-QC TCAP items | ⭐ KEEP + 🔁 merge richest version | Active + Staged | `.claude/skills/` (best version) |
| ~~`tcap-item-writer-v2`~~ | item-writer (write-only) | ~~RETIRE~~ → absorbed (harvest psychometric depth first) | Active + Staged | → `tn-assessment-specialist` |

---

## C. Audit summary — is everything captured?

- **Guardrails / standards:** ✅ all 9 captured and live in `00_START_HERE/` (⭐ Platinum).
- **Skills:** every candidate is accounted for — **Active** (live) or **Staged** (`_inbound/perplexity/`,
  24 preserved). Nothing dropped.
- **Decisions:** ✅ ADOPT (10 new capabilities) · ⭐ KEEP (11 ours) · 🔁 MERGE (8 best-of-breed pending) ·
  ~~RETIRE~~ (2: `tcap-item-writer-v2`, `platinum-workbook` name).
- **EXECUTED — the reconciliation PR is built** (branch `skill/reconcile-canonical-set`, off `origin/main`,
  awaiting Sean's review before merge). It promoted the 12 ADOPTs, ran the version guardrail on every
  🔁 MERGE (decisions recorded in `SKILL_CONSOLIDATION_MATRIX.md`), rebuilt `platinum-unit-builder` into
  a pure orchestrator (root-cause drift fix), retired the crossed-out names, applied America 250 +
  future-ready, codified the assessment/retrieval cadence (§7.10) and the data-visualization mandate
  (§7.11), and shipped the anti-drift enforcement: `.claude/skills/SKILLS.md` registry +
  `lint_skills.py` + the `skills-lint` CI workflow. Final set: **29 skills, one owner each, lint green.**
- **After merge:** every one of the next ~8 courses builds from this one canonical Platinum set — one
  owner per job, no drift, future-ready.
