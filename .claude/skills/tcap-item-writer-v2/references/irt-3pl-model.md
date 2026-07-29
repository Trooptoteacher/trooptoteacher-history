# IRT 3-Parameter Logistic Model — Metadata Tagging Guide

Source: [IRT Item & Test Information Functions (TQMP)](https://www.tqmp.org/RegularArticles/vol20-1/p033/p033.pdf)

## Overview

The TCAP uses a 3-parameter logistic (3PL) IRT model to estimate item characteristics. Each item receives three parameter estimates:

| Parameter | Symbol | Name | Description |
|-----------|--------|------|-------------|
| a | a | Discrimination | How well the item differentiates between high- and low-ability students |
| b | b | Difficulty | The ability level at which a student has a 50% chance of answering correctly (adjusted for guessing) |
| c | c | Guessing | The probability that a very low-ability student answers correctly by chance |

## 3PL Formula

P(θ) = c + (1 − c) × [1 / (1 + e^(−a(θ − b)))]

Where θ = student ability on the latent trait scale.

## Parameter Guidelines for Item Writing

### a-parameter (Discrimination)

| Range | Quality | Interpretation |
|-------|---------|----------------|
| < 0.5 | Poor | Item does not differentiate well; likely has a flawed distractor or ambiguous stem |
| 0.5–0.8 | Marginal | Acceptable for field test but may need revision |
| **0.8–2.0** | **Target** | **Good to excellent discrimination; item functions well on the test** |
| > 2.0 | Very high | Item may be too narrow or content-specific; check for cueing |

**Item writing implications**:
- Strong distractors that target specific misconceptions increase discrimination
- Ambiguous stems or "none of the above" options reduce discrimination
- Items where the key is obviously longer or more detailed than distractors show poor discrimination

### b-parameter (Difficulty)

| Range | Interpretation | Student Ability Level |
|-------|---------------|----------------------|
| −3.0 to −2.0 | Very easy | Nearly all students answer correctly |
| −2.0 to −1.0 | Easy | Most students answer correctly |
| −1.0 to 0.0 | Moderate-easy | Above-average success rate |
| **0.0** | **Medium** | **50% of average-ability students answer correctly** |
| 0.0 to +1.0 | Moderate-hard | Below-average success rate |
| +1.0 to +2.0 | Hard | Only high-ability students typically succeed |
| +2.0 to +3.0 | Very hard | Very few students answer correctly |

**Target distribution for a balanced assessment**:
- 20% easy (b < −1.0)
- 60% moderate (−1.0 ≤ b ≤ +1.0)
- 20% hard (b > +1.0)

**Item writing implications**:
- DOK 1 items typically have b < 0.0 (easier)
- DOK 2 items typically have b around 0.0 (moderate)
- DOK 3 items typically have b > 0.0 (harder) — but not always; a DOK 3 item on a well-taught concept can be moderate difficulty
- Difficulty ≠ DOK level. A hard DOK 1 item (obscure fact) is different from an easy DOK 3 item (straightforward evidence evaluation)

### c-parameter (Guessing)

| Range | Quality | Interpretation |
|-------|---------|----------------|
| **< 0.20** | **Target** | **Low guessing probability; distractors working well** |
| 0.20–0.25 | Acceptable | Near the theoretical floor for 4-option MC (1/4 = 0.25) |
| > 0.25 | Problem | One or more distractors may be implausible; students are eliminating options and guessing among remainder |
| 0.00 | Ideal for CR | Constructed response items have c = 0 by definition |

**Item writing implications**:
- 4-option MC theoretical guessing floor = 0.25; good items push below this
- If c > 0.25, at least one distractor is non-functional — revise
- Multiple-select items naturally have lower c-parameters due to combinatorics

## Estimating IRT Parameters at Item Writing Time

Since actual IRT parameters require field test data, item writers assign **estimated** values based on:

1. **Estimated difficulty (b_est)**: Based on DOK level, content familiarity, stem complexity
2. **Estimated discrimination (a_est)**: Based on distractor quality, stem clarity, alignment tightness
3. **Estimated guessing (c_est)**: Based on number of options, plausibility of distractors

### Estimation Heuristics

| DOK Level | Typical b_est Range | Typical a_est Range |
|-----------|--------------------|--------------------|
| DOK 1 | −1.5 to 0.0 | 0.8–1.5 |
| DOK 2 | −0.5 to +1.0 | 1.0–1.8 |
| DOK 3 | 0.0 to +2.0 | 1.2–2.0 |

| Item Type | Typical c_est |
|-----------|--------------|
| MC (4-option) | 0.20 |
| MS (>4 options) | 0.10 |
| CR/ER/DBQ | 0.00 |

These are pre-calibration estimates. Actual values come from field testing. Tag items with `_est` suffix to indicate pre-calibration status.
