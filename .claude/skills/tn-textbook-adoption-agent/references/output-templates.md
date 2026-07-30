# Output Templates

Load this reference when generating the five required outputs after completing all review stages.

---

## Output 1: Standards Coverage Matrix

Format as a markdown table. One row per TN standard.

```markdown
## Standards Coverage Matrix

**Material:** [Title of material being reviewed]
**Course:** U.S. History (Reconstruction through Modern Era)
**Standards Count:** 95 (US.01–US.95)
**Review Date:** [Date]

| Standard ID | Standard Text | Status | Evidence / Page Reference |
|-------------|--------------|--------|--------------------------|
| US.01 | [abbreviated text] | Met / Partially Met / Not Met | [page/section ref or "No coverage found"] |
| ... | ... | ... | ... |

### Coverage Summary
- **Met:** [count] / 95 ([percentage]%)
- **Partially Met:** [count] / 95 ([percentage]%)
- **Not Met:** [count] / 95 ([percentage]%)
- **Gateway 2 Status:** PASS / FAIL
```

---

## Output 2: Rubric Scorecard

Format as markdown tables, one per rubric table, with a summary section.

```markdown
## Rubric Scorecard

**Material:** [Title]
**Reviewer:** TN Textbook Adoption Review Agent
**Date:** [Date]

### Table 1: Alignment of Content
| Indicator | Score (0-2) | Evidence | Justification |
|-----------|-------------|----------|---------------|
| 1.1 Standard Coverage | [0/1/2] | [quote or page ref] | [why this score] |
| 1.2 Depth of Treatment | [0/1/2] | [quote or page ref] | [why this score] |
| 1.3 Accuracy | [0/1/2] | [quote or page ref] | [why this score] |
| 1.4 Sequence Alignment | [0/1/2] | [quote or page ref] | [why this score] |
| 1.5 Assessment Alignment | [0/1/2] | [quote or page ref] | [why this score] |
**Table 1 Subtotal:** [X] / 10 ([X]%)

### Table 2: Instructional Focus
| # | Indicator | Score (0-2) | Evidence | Justification |
|---|-----------|-------------|----------|---------------|
| 2.1 | Rigor | [0/1/2] | ... | ... |
| 2.2 | Higher-Order Thinking | [0/1/2] | ... | ... |
| 2.3 | Primary Sources | [0/1/2] | ... | ... |
| 2.4 | Vocabulary | [0/1/2] | ... | ... |
| 2.5 | Differentiation | [0/1/2] | ... | ... |
| 2.6 | Assessment | [0/1/2] | ... | ... |
| 2.7 | Pacing | [0/1/2] | ... | ... |
| 2.8 | Teacher Support | [0/1/2] | ... | ... |
| 2.9 | Digital Integration | [0/1/2] | ... | ... |
**Table 2 Subtotal:** [X] / 18 ([X]%)

### Table 3: Social Studies Practices / SSPs
| # | Indicator | Score (0-2) | Evidence | Justification |
|---|-----------|-------------|----------|---------------|
| 3.1 | Sourcing | [0/1/2] | ... | ... |
| 3.2 | Contextualization | [0/1/2] | ... | ... |
| 3.3 | Corroboration | [0/1/2] | ... | ... |
| 3.4 | Close Reading | [0/1/2] | ... | ... |
| 3.5 | Argumentation | [0/1/2] | ... | ... |
| 3.6 | Economic Reasoning | [0/1/2] | ... | ... |
| 3.7 | Geographic Reasoning | [0/1/2] | ... | ... |
**Table 3 Subtotal:** [X] / 14 ([X]%)

### Table 4: Accessibility Features
| # | Indicator | Score (0-2) | Evidence | Justification |
|---|-----------|-------------|----------|---------------|
| 4.1 | ADA Compliance | [0/1/2] | ... | ... |
| 4.2 | NIMAS Compliance | [0/1/2] | ... | ... |
| 4.3 | UDL Principles | [0/1/2] | ... | ... |
| 4.4 | Multilingual Support | [0/1/2] | ... | ... |
| 4.5 | Assistive Tech Compatibility | [0/1/2] | ... | ... |
**Table 4 Subtotal:** [X] / 10 ([X]%)

### Overall Score
**Total Points:** [X] / [max] = **[X.X]%**
**Threshold Status:** RECOMMENDED / REVISE AND RESUBMIT / NOT RECOMMENDED
```

---

## Output 3: Deficiency Memo

Generate only if the material does not achieve RECOMMENDED status. Organize by category.

```markdown
## Deficiency Memo

**Material:** [Title]
**Publisher:** [Publisher name]
**Date:** [Date]
**Overall Score:** [X.X]%
**Recommendation:** REVISE AND RESUBMIT / NOT RECOMMENDED

### 1. Missing Standards (Gateway 2 Failures)
| Standard ID | Standard Text | Notes |
|-------------|--------------|-------|
| US.XX | [text] | No coverage found in material |

### 2. Weak Indicators (Scored 0 or 1)
| Table | Indicator | Score | Issue | Suggested Fix |
|-------|-----------|-------|-------|---------------|
| 2 | 2.3 Primary Sources | 1 | Sources present but not scaffolded | Add sourcing protocols and guided analysis questions |

### 3. Factual / Editorial Errors
| Location | Error Description | Correction |
|----------|------------------|------------|
| p. 47, para. 2 | Incorrect date for [event] | Should be [correct date] |

### 4. Accessibility Gaps
| Indicator | Issue | Required Action |
|-----------|-------|-----------------|
| 4.1 ADA | Missing alt text on 23 images | Add descriptive alt text to all images |

### 5. Values Violations (U.S. History Only)
| Location | Violation Description | TCA Reference |
|----------|----------------------|---------------|
| p. 112 | [description] | TCA §49-6-1028(b)(X) |
```

---

## Output 4: Publisher Revision Checklist

Actionable list aligned to the Policy 2.600 appeal/correction process.

```markdown
## Publisher Revision Checklist

**Material:** [Title]
**Current Score:** [X.X]%
**Target Score:** 80.0% (RECOMMENDED threshold)
**Points Needed:** [X] additional points

### Priority Revisions (Highest Impact)

| # | Revision Item | Current Score | Target Score | Point Gain | Effort Level |
|---|--------------|---------------|--------------|------------|--------------|
| 1 | [description] | 0 | 2 | +2 | Medium |
| 2 | [description] | 1 | 2 | +1 | Low |

### Standards Coverage Fixes
| Standard ID | Required Action |
|-------------|----------------|
| US.XX | Add section covering [topic] with minimum [X] pages of content |

### Accessibility Fixes
| Item | Required Action | Compliance Standard |
|------|----------------|-------------------|
| Alt text | Add to all images | WCAG 2.1 AA |

### Timeline
- Revisions due per Policy 2.600 appeal/correction window
- Schedule F reference dates: Bid deadline Feb 20, 2026; Samples to MTSU Apr 23, 2026
- LEA implementation: 2027–28

### Estimated Revised Score
If all priority revisions are completed: **[X.X]%** (up from [current]%)
```

---

## Output 5: Final Recommendation Summary

Always generate this output, even for RECOMMENDED materials.

```markdown
## Final Recommendation Summary

**Material:** [Title]
**Publisher:** [Publisher name]
**Course:** U.S. History (Reconstruction through Modern Era)
**Review Date:** [Date]
**Reviewer:** TN Textbook Adoption Review Agent (History Hack / TroopToTeacher Technologies)

---

### Verdict: [RECOMMENDED / REVISE AND RESUBMIT / NOT RECOMMENDED]

| Metric | Result |
|--------|--------|
| Overall Rubric Score | [X.X]% |
| Standards Coverage | [X]% ([count] / 95 Met or Partially Met) |
| Gateway 1 (Alignment Guide) | PASS / FAIL |
| Gateway 2 (100% Coverage) | PASS / FAIL |
| Values Compliance (TCA §49-6-1028) | PASS / FAIL / N/A |

### Key Strengths (Top 3)
1. [Strength with evidence reference]
2. [Strength with evidence reference]
3. [Strength with evidence reference]

### Critical Gaps (Top 3)
1. [Gap with standard/indicator reference and impact]
2. [Gap with standard/indicator reference and impact]
3. [Gap with standard/indicator reference and impact]

### Schedule F Timeline Reference
- Bid deadline: February 20, 2026
- Sample delivery to MTSU: April 23, 2026
- LEA implementation: 2027–28 school year
- Contract term: 97 months

### Notes
[Any additional observations, 97-month durability flags, or reviewer commentary]
```
