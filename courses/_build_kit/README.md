# TroopToTeacher — Course Build Kit

A reusable framework for building **licensable Social Studies course editions** (History Hack /
Government Hack / World History Hack …) to a consistent platinum standard — feature-for-feature
and guardrail-for-guardrail. This repo is the **build system**, not a finished course: the Claude
skills, the platinum build playbook, the brand-locked docx engines, the assessment/question-bank
toolkit, and the compliance templates.

Built and maintained with [Claude Code](https://claude.com/claude-code).

## What's in here

| Folder | What it is |
|---|---|
| `.claude/skills/` | **10 Claude skills** that run the build — course orchestration, curriculum/unit builders, DBQ + graphic-organizer builders, the TCAP item writer + TN assessment specialist, UDL/CAST expert, historian fact-checker, TN adoption agent, and the education-research team. Available automatically to Claude Code in any repo that contains this `.claude/` dir. |
| `playbooks/` | `WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md` — the complete 13-phase workflow with copy-paste prompts, full skills roster, guardrails, primary-source sourcing table, the **workbook brand-lock**, copyright/rights-clearance procedure, a 12-check master QC gate, and Social Studies Suite integration. Plus `HANDOFF_WORLD_HISTORY.md`, the one-page start guide. |
| `engine/` | **Brand-locked docx builders** (docx-js): student workbook, teacher guide, assessment book, cover, graphic-organizer toolkit, plus `render_pdf.py` and `sync_images.py`. The workbook is locked to the U.S. History Hack layout (margins 1224, printable width 9792, Cornell notes, C9C2B4 ruled lines, seven activities/standard). |
| `question_bank_toolkit/` | Subject-agnostic Python toolkit: `consolidate_bank.py`, `bank_qc.py`, `add_udl_remediation.py`, `generate_parallel_tests.py`, `build_inventory.py`. Produces a psychometric item pool (20/standard), equated parallel tests, QC report, inventory + standards crosswalk. |
| `compliance_templates/` | UDL/MTSS framework, Schedule F alignment, and the UDL framework builder. |
| `reference/` | The canonical **brand layout reference** — the actual U.S. History Hack workbook + a README listing the locked-in page settings every course must match. |

## How to use it to build a new course

1. Point Claude Code at this repo (the skills load automatically).
2. Open `playbooks/WORLD_HISTORY_PLATINUM_BUILD_PLAYBOOK.md` and follow it phase by phase, or paste
   its one-shot kickoff prompt. It works for **any** subject — swap the standards, the sourced
   public-domain images, and the content JSON; reuse everything else verbatim.
3. Copy the `engine/` builders into your course's per-unit build folders and repoint the content
   paths. **Verify the brand-lock after copying** (`CW=9792`, margins `1224`, a `cornell()`
   function — see `reference/README.md`).
4. Run the `question_bank_toolkit/` scripts for the assessment pool + parallel tests.
5. Run the **master QC gate** in the playbook before packaging (leak scan, historian fact-check,
   copyright clearance, bank QC, 9/9 UDL audit, accessibility, print QC, brand-lock, Schedule F).

## Guardrails (baked into the playbook)
Source-of-truth only · no cross-edition leakage · teacher keys teacher-side only · genuine
public-domain sources with accurate citations · historically accurate · UDL 3.0 (CAST 2024) + MTSS
evidenced, not just labeled. Assessment items are classroom-formative / pre-field-test.

## Ownership
© 2026 TroopToTeacher Technologies LLC. Proprietary. The `reference/` workbook is a brand asset —
keep this repository **private**.
