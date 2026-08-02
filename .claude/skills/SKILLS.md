# Canonical Skill Registry — one job, one owner

**This is the anti-drift contract.** `.claude/skills/` is **main-owned and read-only on work branches.**
Skills change **only** via a dedicated skills-only PR to `main`; content/unit branches then rebase and
consume skills read-only. No feature branch carries its own skill variant. Every skill below has **one
job and one owner** — if two skills would do the same job, they are merged or one is retired. The CI lint
(`.claude/skills/lint_skills.py`, wired in `.github/workflows/skills-lint.yml`) fails the build on a
name/dir mismatch, a dangling skill reference, an un-annotated retired name, or a builder that inlines a
gate/engine instead of invoking it.

Load `history-hack-platinum-standard` at the start of any build — it owns the mission, the Gold-vs-Platinum
tier convention, the future-ready principle, and the decision rule (100% alignment → TDOE Schedule F →
best path to adoption).

## Mission / doctrine
| Skill | The one job it owns |
|---|---|
| `history-hack-platinum-standard` | Mission, Gold-vs-Platinum tier, future-ready principle, decision rule. Invoked by everything; owns no build step. |

## Builders — units & courses
| Skill | The one job it owns |
|---|---|
| `history-hack-platinum-unit-builder` | **Orchestrator** for a Course Standard unit set. Invokes the engine + gates; does not inline them. |
| `history-hack-unit-content-build` | The 7-activity content **engine** (`build_guided_notes.py`, verso NOTES SUPPORTS, deck-keying, five editions). |
| `history-hack-new-course-builder` | Cradle-to-grave **new-course** orchestrator (Government, Economics, World History…). Calls the unit builder; never re-implements it. |
| `history-hack-dbq-workbook` | Standalone **DBQ / primary-source SKU** — a different product from the unit workbook. |
| `history-hack-graphic-organizer-workbook` | Reproducible **graphic-organizer** toolkit (carries the Cornell supports reproducibles). |

## Print layout — unit workbooks
| Skill | The one job it owns |
|---|---|
| `history-hack-workbook-print-bundle` | The unit student-workbook **print-bundle LAYOUT standard** — duplex activity/supports rhythm, exact bidirectional deck↔workbook slide-keying, all-writing-ruled + no-bleed + breathing-room guardrails, and per-activity print rules. Invoked by the content engine/orchestrator; owns layout, not content. |

## Deck generators
| Skill | The one job it owns |
|---|---|
| `history-hack-tcap-deck-builder` | Generates the **teacher (lecture) deck** .pptx + answer-key PDF + usage guide. |
| `history-hack-lean-deck-builder` | Generates the **student (review/lean) deck** .pptx + answer key + web viewer manifest. |

## Product packaging & gap-fill
| Skill | The one job it owns |
|---|---|
| `history-hack-poster-packet-builder` | 24×36 wall posters + station packets SKU. |
| `us-history-hack-packet-builder` | TpT / for-sale packaging (front/back matter, brand strip, copyright, encryption). |
| `magic-school-created-worksheets` | MagicSchool prompt packets for genuine content gaps. |
| `history-hack-district-edition-restructure` | App-side District Edition / product-edition isolation. |
| `history-hack-web-activities` | The web-app **interactive layer** on top of the print bundle — gamified retrieval, auto-graded formative/summative, and the draft-first **Writing Lab** (DBQ/CER/HIPP). Owns the feature set + guardrails; invokes the UX/assessment/privacy owners. |

## Content & learning design
| Skill | The one job it owns |
|---|---|
| `instructional-design-specialist` | **Print-first pedagogical architecture** of lessons/units/sequences + assessment design. Anchored on UDL 3.0/CAST 2024 + CER + C3; maps to the 7-activity flow. |
| `learning-experience-designer` | **Interactive digital/app student-facing UX** — interaction patterns, journey/branching, gamification, microlearning. (Distinct lane from print design.) |
| `udl-cast-expert` | **UDL 3.0 / CAST** design authority. The single owner of UDL principle depth. |
| `tt-education-research-team` | ESSA evidence tiering / research foundations. |
| `tn-content-specialist` | TN-standards **content authoring** (narrative prose, lesson narratives). |
| `spaced-repetition-engine` | Spiral/retrieval **scheduling algorithm** (SM-2/Leitner, forgetting curve). The book seeds; this owns the schedule. |

## Assessment
| Skill | The one job it owns |
|---|---|
| `tn-assessment-specialist` | **All** TCAP assessment items + tests (every type, full psychometrics, TCAP JSON, QC + quick-quiz modes). Supersedes retired `tcap-item-writer-v2` and `history-hack-question-forge`. |

## Gates & QC
| Skill | The one job it owns |
|---|---|
| `history-hack-lesson-flow-qc` | Release gate: workbook↔deck **exact-slide alignment**, DI parity, vocab-first. |
| `history-hack-text-integrity-qc` | Release gate: no **truncated/clipped/placeholder** text. |
| `accessibility-qc-agent` | Final **WCAG 2.2 AA / 508 / ADA Title II** gate (code + content). |
| `ell-bilingual-review-specialist` | English/Spanish + **ELL scaffolding** QC (WIDA/ELPA21). |
| `history-hack-unit-qc` | End-to-end **web-app unit QC workflow** (18-item checklist). **Orchestrates** the gates above — never duplicates them. |
| `wcs-app-approval-qc` | **District-submission readiness** (Williamson County app-approval packet). |
| `historian-factcheck-agent` | Primary-source **fact-check** (Policy 2.600). |
| `tn-textbook-adoption-agent` | TDOE **Schedule F / adoption** panel review. |
| `copyright-integrity-accreditation` | IP / licensing / **FERPA-COPPA** review. |
| `edtech-adoption-specialist` | EdTech district/state **sales & adoption** process (distinct lane from the Schedule F rubric). |

## External (not in this repo)
| Skill | Where |
|---|---|
| `history-hack-print-qc-auditor` | Print-defect / classroom-readiness audit — available as a plugin; referenced, not vendored here. |

## Retired (do not reintroduce)
| Retired name | Replaced by |
|---|---|
| `history-hack-north-star` | `history-hack-platinum-standard` |
| `history-hack-platinum-workbook` | `history-hack-dbq-workbook` |
| `tcap-item-writer-v2` | `tn-assessment-specialist` |
| `history-hack-question-forge` | `tn-assessment-specialist` |
| `history-hack-course-standard-builder` | `history-hack-platinum-unit-builder` (unit) / `history-hack-new-course-builder` (new course) |
