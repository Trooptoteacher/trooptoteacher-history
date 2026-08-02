# Report Template

**Load this reference in the final report-generation step.**

Every QC report must follow this structure exactly. File output location: `/home/user/workspace/compliance/a11y/qc_reports/YYYY-MM-DD_[artifact-type]_QC_Report.md`

---

```markdown
# Accessibility QC Report — [Artifact Type] — [Date]

**Auditor:** Accessibility QC Agent (TroopToTeacher Technologies)
**Requestor:** Sean Reynolds
**Session ID:** [slug]
**Standards Applied:** [comma-separated list from sources-of-truth]
**Artifacts Audited:** [enumerated]
**Artifacts Planned for Next Session:** [if budget reached]

---

## Executive Summary

[≤5 sentences in plain language. State what was audited, what was found, and whether submission-ready. No jargon beyond standard names.]

---

## Overall Grade

**Grade: [A / B / C / D / F / INCOMPLETE]**

**Submission Readiness:** [YES / NO / CONDITIONAL]

[One paragraph explaining the grade, citing the rubric.]

### Grade Rubric Applied

| Grade | Requirements met? |
|---|---|
| A | [✓ or ✗ with reason] |
| B | [✓ or ✗ with reason] |
| C | [✓ or ✗ with reason] |

---

## Blockers (Must Fix Before Submission)

| ID | Severity | Finding | Location |
|---|---|---|---|
| F-001 | Critical | [short] | [path/page/item] |
| F-002 | Critical | [short] | [path/page/item] |

---

## Findings Table

### Critical Findings

| ID | Standard(s) | Location | Finding | User Impact | Remediation | Effort |
|---|---|---|---|---|---|---|
| F-001 | WCAG 2.2 SC 2.1.1 Keyboard (A); also Section 508 E205.4 | [path]:[line] | [one-line] | [one-line] | [one-line] | S/M/L |

### High Findings

[same table structure]

### Medium Findings

[same table structure]

### Low Findings

[same table structure]

### Unverified Items

| ID | Criterion | Why Unverified | Evidence Needed |
|---|---|---|---|
| U-001 | [criterion] | [reason] | [specific evidence request] |

---

## Evidence Appendix

### F-001 — [short title]

**Quoted from [path]:[line]:**

```
[exact code / content quote]
```

**Tool output (if applicable):**

```
[axe-core / jest-axe / eslint output]
```

[Repeat for every Critical and High finding. Medium / Low can share a compact evidence block.]

---

## Action Items

Numbered list of specific, owner-assignable actions.

1. **[F-001]** Replace `<div role="button">` in `DBQCard.tsx:47` with native `<button>`. Restore Enter + Space keyboard handling. Target: before PR #43 merge.
2. **[F-002]** ...

---

## Related Open PRs

[Cite any open PRs remediating findings: #40, #41, #43.]

---

## Standards Coverage Summary

| Standard | Criteria applied | Pass | Fail | Unverified | N/A |
|---|---|---|---|---|---|
| WCAG 2.2 AA | 47 | 38 | 6 | 2 | 1 |
| Section 508 | 12 | 12 | 0 | 0 | 0 |
| ADA Title II | (WCAG 2.1 AA baseline) | by reference | | | |
| ISTE | — | — | — | — | out of scope |

---

## Next Session Candidates

Artifacts noticed but NOT audited this session (scope creep prevention):

- [artifact ID] — [one-line reason it deserves a future audit]

---

## STATUS Block

```
=== ACCESSIBILITY QC STATUS ===
session_date: YYYY-MM-DD
session_id: [slug]
artifact_type: [type]
standards_applied: [list]
artifacts_audited: N
artifacts_in_scope: M
budget_status: [within|reached|exceeded]
findings_critical: N
findings_high: N
findings_medium: N
findings_low: N
unverified_items: N
pass_items: N
overall_grade: [A-F or INCOMPLETE]
submission_ready: [YES|NO|CONDITIONAL]
blockers_count: N
blockers: [F-001, F-002, ...]
next_session_candidates: [list]
tracker_path: /home/user/workspace/compliance/a11y/tracker.md
stop_reason: [budget|completed|user-requested|evidence-missing|refusal-triggered|loop-detected|emergency-stop]
=== END STATUS ===
```

---

## Handoff Instructions

[If budget reached, loop detected, or evidence missing, provide the exact prompt to paste into a new session.]

```
Continue accessibility QC. Tracker at [path]. Next batch: [IDs]. Standards: [list].
```
```

---

## Tracker Format

Maintain a running tracker at `/home/user/workspace/compliance/a11y/tracker.md` with this structure:

```markdown
# Accessibility QC Tracker — History Hack

## Audit History

| Date | Session ID | Artifact(s) | Standards | Grade | Submission-Ready | Findings (C/H/M/L) | Report Path |
|---|---|---|---|---|---|---|---|
| 2026-04-17 | baseline-a11y | full app | WCAG 2.2 AA | C | NO | 6/11/13/8 | [link] |
| 2026-04-18 | code-dbqcard-writinglab | 2 components | WCAG/508/Title II | [grade] | [Y/N/C] | [C/H/M/L] | [link] |

## Open Blockers

- F-001 — [from which report] — [status: open / in-progress / closed-by-PR-XX]
- ...

## Closed Blockers

[Move items here when PR merges or user confirms fix.]

## Next Session Queue

[Artifact IDs not yet audited, in priority order.]
```

---

## File Output Discipline

At the end of every session:

1. Write the report to `/home/user/workspace/compliance/a11y/qc_reports/YYYY-MM-DD_[artifact-type]_QC_Report.md`
2. Update the tracker at `/home/user/workspace/compliance/a11y/tracker.md`
3. `share_file` the report (not the tracker — tracker is internal; report is what Sean and human reviewers read)
4. Emit the STATUS block as the final content in the response
