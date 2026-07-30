# Government Question Bank & Parallel-Test Generator

A deep, psychometrically-tagged item pool for **Foundations of Constitutional Government**
(Government Hack edition), built to mirror the U.S. History flagship bank (`all_questions.json`)
and to generate as many **equated parallel tests of equal rigor** as needed.

## Contents
- `government_question_bank.json` — the consolidated pool: **700 items**, 35 standards × 20
  (GC.01–GC.35). Superset schema = flagship fields (`id, standard, unit, question_number, type,
  dok, level, question, options, correct_answer, tennessee_specific, topics`) **+** psychometrics
  (`blooms, hess_crm_cell, irt_a/irt_b/irt_c, c3_dimension, ssp, distractor_tags, key_rationale,
  dok_rationale, blooms_rationale, bias_flag, reporting_category, tcap_format, field_test_ready,
  rubric_id/rubric_name`) **+** `udl_supports` (CAST 3.0) and `remediation` (distractor-based,
  MTSS Tier 2/3). Authored via the `tn-assessment-specialist` + `tcap-item-writer-v2` skills;
  UDL/remediation added by `add_udl_remediation.py`.
- `QUESTION_BANK_INVENTORY.md`, `standards_crosswalk.csv`, `item_inventory.csv` — full inventory
  and per-standard crosswalk (coverage, DOK/type mix, TN-specific, SSP/C3, verbatim standards),
  from `build_inventory.py`.
- Per-unit source pools live at `BUILD/unitN/analysis/unitN_item_bank.json`.
- `generated_tests/` — sample output (4 equated course-wide forms + equating report).

## Depth per standard
20 items each (Q01–Q20): a base set + a DOK-3-weighted extension. Bank-wide DOK \u2248 20/35/45. Every standard has DOK-3 multiple-choice items so parallel forms carry deep objective rigor. MC answer keys debiased across A/B/C/D.
(short-answer, CER, and a document-based or extended-response item citing a genuine public-domain
source). Bank-wide DOK ≈ **20 / 40 / 40**. MC answer keys debiased across A/B/C/D.

## Tools
```bash
# 1. Rebuild the consolidated bank from the per-unit pools
python3 08_QUESTION_BANK/consolidate_bank.py

# 2. Run the rigor/QC report (coverage, DOK/type/Bloom's, key balance, IRT spread,
#    duplicate-stem detection, required fields, forbidden-string leak scan)
python3 08_QUESTION_BANK/bank_qc.py

# 3. Generate N equated parallel tests
python3 08_QUESTION_BANK/generate_parallel_tests.py \
    --forms 4 --scope all --per-standard 1 --title Government_EOC_Practice
#   --scope all | unit3 | GC.01,GC.02,...     --per-standard 2  (longer tests)
```

## How equating works
For each standard the generator interleaves items by DOK (recall→reasoning→analysis) and assigns
them to forms with a rotating per-standard offset. Result: every form carries the **same DOK
profile** and the forms' **mean IRT difficulty converges** (the `EQUATING_REPORT.md` prints the
max−min spread; ≤0.35 = tightly equated). Distinct items are used per form until the pool is
exhausted, then reuse is reported. With 7 MC/standard you can build up to ~7 fully-distinct
MC parallel forms; deeper pools (raise items/standard) yield more.

## Guardrails
Answer keys are written to a **separate teacher-key file only**; student forms carry stems +
options. IRT parameters are **pre-field-test design-time estimates**, to be calibrated on response
data. No US-History content, no source-district names, genuine public-domain sources only.
