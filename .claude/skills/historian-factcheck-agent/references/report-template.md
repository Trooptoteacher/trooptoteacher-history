# Report Template — Historian Factcheck Agent

Every verification run produces a report in this exact structure. The template ensures reports are comparable across units, trackable over time, and usable by operators who won't read every word.

---

# Historian Factcheck Report

**Content audited:** `[file path]`
**Auditor:** Historian Factcheck Agent (History Hack / TroopToTeacher Technologies LLC)
**Session date:** `[YYYY-MM-DD]`
**Session ID:** `[unique ID, e.g. hfc-2026-04-18-001]`
**Scope:** Factual verification only (per skill policy — NOT interpretive/rubric/pedagogical review)
**Policy:** Evidence-only VERIFIED scoring. No verifying source = CANNOT VERIFY, not VERIFIED.

---

## Part 1 — Summary Verdict

| Section | Verdict | Accuracy score (verified / total) |
|---|---|---|
| s1 | [PASS / PASS WITH REVISIONS / FAIL] | X / Y (Z%) |
| s2 | [PASS / PASS WITH REVISIONS / FAIL] | X / Y (Z%) |
| ... | | |

**Overall accuracy score:** X / Y (Z%)
**Total atomic claims reviewed:** Y
**Session budget used:** X / 40 claims, X / 60 lookups

Verdict thresholds:
- **PASS** — 100% of claims VERIFIED, zero NEEDS CITATION / CANNOT VERIFY / INCORRECT / CONFLICTING EVIDENCE
- **PASS WITH REVISIONS** — ≥90% VERIFIED, no INCORRECT, remaining claims have AUTO-APPLY fixes or minor softening
- **FAIL** — any INCORRECT claim OR <90% VERIFIED OR any CANNOT VERIFY claim making a load-bearing factual assertion

---

## Part 2 — AUTO-APPLY Findings

These are mechanical corrections the operator has pre-authorized. Each is a verified fix with a canonical source.

| # | Section | Claim excerpt | Before | After | Verifying source | Notes |
|---|---|---|---|---|---|---|
| 1 | [sX] | [excerpt] | [old text] | [new text] | [URL / archive ID / volume-page] | [2 sentences max] |

---

## Part 3 — SUBSTANTIVE Findings

These require operator decision. Each is flagged with the verdict type and recommended action.

### Finding 1
- **Section:** sX
- **Claim:** [exact text]
- **Type:** [statute | case | date | name | numerical | geographic | event | quote | content]
- **Verdict:** [NEEDS CITATION | CANNOT VERIFY | INCORRECT | CONFLICTING EVIDENCE]
- **Verifying source(s) consulted:** [list with URLs / archive IDs]
- **What the sources say:** [factual summary]
- **Recommended action:** [revise to: ... | soften to range: ... | remove specific figure | add citation: ...]
- **Operator decision required:** YES — [what the operator must decide]
- **Priority:** [CRITICAL / HIGH / MEDIUM / LOW]

(Repeat for each substantive finding.)

---

## Part 4 — CANNOT VERIFY List

Every claim marked CANNOT VERIFY, with:
- Claim text
- Sources consulted (with URLs)
- Why verification failed (source not found, data not in federal records, only secondary-source estimates exist, etc.)
- Recommendation: remove, soften, or add a specific citation

---

## Part 5 — Claim-by-Claim Detail

For operators who want the full audit trail. Format:

```
--- Claim N ---
CLAIM: [exact text]
TYPE: [type]
VERDICT: [verdict]
VERIFYING SOURCE(S):
  - [source 1]
  - [source 2]
NOTES: [notes]
RECOMMENDED ACTION: [action]
```

Repeat for every atomic claim (target: ≤40 per session).

---

## Part 6 — Source Canon Summary

List every source consulted in this session. Confirms no off-canon sources were used.

| Source | Tier | Used for claims | Access date |
|---|---|---|---|
| GovInfo (govinfo.gov) | 1 — Primary statutes | s1, s2, s4 | 2026-04-18 |
| Justia (supreme.justia.com) | 1 — Primary cases | s3 | 2026-04-18 |
| National Native American Boarding School Healing Coalition | 3 — Institutional repository | s2 | 2026-04-18 |
| ... | | | |

---

## Part 7 — Session Telemetry

| Metric | Value |
|---|---|
| Atomic claims extracted | X |
| Claims verified | X |
| Primary source lookups performed | X / 60 |
| STATUS blocks produced | X |
| Consecutive CANNOT VERIFY max | X |
| Stop triggers fired | [none / A / B / C / D / E / F] |
| Session complete? | YES / NO (if NO, see hand-off below) |

---

## Part 8 — Out of Scope (Referred to Other Skills)

Items encountered during this run that are NOT in scope for this skill. Forwarded to other reviewers.

| Item | Recommended reviewer |
|---|---|
| Bilingual translation concerns | `ell-bilingual-review-specialist` |
| Historiographic balance concerns | `tn-textbook-adoption-agent` |
| Accessibility concerns | `accessibility-qc-agent` |
| Pedagogical structure concerns | `instructional-design-specialist` |
| Copyright / OER attribution | `copyright-integrity-accreditation` |

---

## Part 9 — Hand-Off (only if session ended before completion)

### Resume checklist for next session
- Completed claims: [N / total]
- Outstanding claims: [list with section IDs]
- Sources already consulted this session: [list]
- Open research threads: [list]

### Next-session context packet
- Content file path
- Atomic claim extraction (attach)
- Canonical sources already visited (attach)
- Any claim-specific leads found but not pursued

---

## Part 10 — Operator Acknowledgment (sign-off)

```
I, [operator name], have reviewed this fact-check report.
I accept the AUTO-APPLY findings for implementation.
My decisions on each SUBSTANTIVE finding are recorded in:
  [path to DECISIONS file]
Signed: [name]
Date: [YYYY-MM-DD]
```

---

© 2026 TroopToTeacher Technologies LLC. Proprietary. All rights reserved.
