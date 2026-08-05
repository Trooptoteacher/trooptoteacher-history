---
name: wcs-app-approval-qc
description: End-to-end quality control gate for Williamson County Schools (WCS) App Approval submission packets for History Hack / TroopToTeacher Technologies. Runs a prioritized 34-item checklist across 11 WCS evaluation areas (policies, COPPA/FERPA, SSO/rostering, LTI interop, instructional materials, hosting/whitelist, VPAT/WCAG, ToU/data practices, data security, AI disclosure, ratings/pledges) plus the DPA framework. Enforces the Unit 1 gold-standard QC discipline (session-budget guardrails, STATUS blocks, evidence-only Pass scoring). Use when the user asks to QC the WCS packet, run a WCS app approval QC, audit the WCS response document, prepare for WCS submission, pre-submission WCS review, or any terminal QC on the WCS-Responses-for-App-Approval document family. Produces Blocker/High/Medium/Low findings and a go/no-go disposition. Sibling to history-hack-unit-qc (content) and accessibility-qc-agent (a11y) — this skill owns district submission readiness.
license: MIT
metadata:
  author: TroopToTeacher Technologies
  version: '1.0'
  sources_of_truth:
    - TCA 49-1-701 et seq. (Tennessee Student Data Accessibility, Transparency and Accountability Act)
    - TCA 47-18-2107 (Tennessee data breach notification, 45-day statutory floor)
    - TCA 49-6-2202(a)(3) (supplemental materials authority)
    - TN Public Chapter 744 of 2022 (Age-Appropriate Materials Act)
    - FERPA 20 U.S.C. § 1232g; 34 CFR Part 99
    - COPPA 15 U.S.C. § 6501 et seq.; 16 CFR Part 312
    - CIPA 47 U.S.C. § 254(h)
    - ADA Title II DOJ Rule (April 2024; WCAG 2.2 AA)
    - Section 508 Refresh
    - WCAG 2.2 Level AA (W3C)
    - VPAT 2.5Rev (ITI, April 2025)
    - 1EdTech LTI 1.3 / LTI Advantage / OneRoster specs
    - SDPC National Data Privacy Agreement (NDPA) v1r7
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, or QC ANY artifact —
> workbook, teacher/student slide deck, graphic organizer, poster, DBQ, assessment or test, worksheet, comic,
> web page, or anything else — from memory, a cached copy, or a prior session. **Re-read the CURRENT version of
> THIS skill from `main` first** — skills are the single source of truth and change only via skills-only PRs.
> Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix, and never read from or write to the protected `us-history` flagship
> on a non-US build. If you cannot confirm you are on the current skill, **STOP and pull it first.**

# WCS App Approval QC

Terminal quality-control gate for Williamson County Schools App Approval submission packets. Last automated check before human and legal review.

## When to Use This Skill

Use this skill when the user asks you to:

- **Run a WCS QC** / **QC the WCS packet** / **audit the WCS responses**
- **Pre-submission WCS review**
- **Evaluate the WCS App Approval document** (usually `WCS-Responses-for-App-Approval.docx` or a variant)
- **Run the WCS gate** before sending to legal counsel
- **Re-QC** a revised WCS packet after remediation
- **Prepare WCS submission packet** from scratch (this skill defines the required shape)

This skill does **NOT** own:

- Content quality of the app itself (use `history-hack-unit-qc`)
- Accessibility testing of live URLs (use `accessibility-qc-agent`)
- Historical fact-checking (use `historian-factcheck-agent`)
- TDOE state-level adoption (use `tn-textbook-adoption-agent`)
- ELL review (use `ell-bilingual-review-specialist`)

Those skills must run separately and their outputs feed into this QC.

## Working Rules

1. **Evidence-only Pass scoring.** Do not mark an item Pass without a verifiable artifact (published URL, signed document, screenshot, or explicit quote from the packet). "Planned" or "in progress" is not Pass.

2. **No fabrication.** Do not invent certifications, URLs, dates, contact info, or compliance claims. If the packet does not state it, mark CANNOT VERIFY.

3. **STATUS block every 10 findings.** After every 10 findings, emit a STATUS block showing: items reviewed, Blockers found so far, High found, elapsed budget. This prevents drift and looping.

4. **Session budget guardrail.** If you have not produced the final scorecard within ~30 tool calls on a single QC run, stop and emit: "Session budget exceeded. Save current state to `wcs_qc_partial.md` and start a fresh session." Do not self-QC your own QC.

5. **Terminal output is a scorecard + action list.** Every run produces the same two deliverables: (a) prioritized findings report, (b) consolidated action list in priority order.

6. **Cite statutes and specs precisely.** TCA § 47-18-2107, 34 CFR § 99.31, 16 CFR § 312.5(c)(10), WCAG 2.2 SC 1.4.3, LTI 1.3, VPAT 2.5Rev — never paraphrase.

7. **Load prior authorization context first.** Before QC'ing a packet, check memory for any existing WCS authorization (e.g., supplemental curriculum authorization under TCA 49-6-2202(a)(3)). The packet must reconcile with prior approvals or clearly state why it is a separate submission.

## Inputs

| Input | Required | Notes |
|---|---|---|
| WCS response document | ✅ | Usually `.docx` or `.md`. Expect a scorecard, criterion-by-criterion tables, submission checklist, and DPA. |
| Product name | ✅ | Typically "History Hack" |
| Vendor legal entity | ✅ | Typically "TroopToTeacher Technologies, LLC" |
| Academic year target | ✅ | Must match current submission cycle. Reviewer rejects stale years. |
| WCS evaluation form version | Recommended | If user has the current WCS form, cross-reference every field. Otherwise use the 11 evaluation areas listed below. |
| Prior WCS authorizations (if any) | Recommended | Check memory. Packet must reconcile. |

## The 11 WCS Evaluation Areas

This QC enforces every area below. A packet missing any area = Blocker.

1. **Policies** — Terms of Use URL + Privacy Policy URL (live, public, stable)
2. **COPPA / FERPA Compliance** — statements with School Official prongs
3. **Account Management** — SSO (ClassLink, Entra ID), rostering, account creation flow
4. **Interoperability** — Schoology LTI 1.3, LTI Advantage (AGS, NRPS, Deep Linking)
5. **Instructional Materials & Content Governance** — scope-and-sequence, citation policy, district content controls
6. **Installation / Hosting / Whitelist URLs** — all FQDNs, CDN endpoints, video hosts
7. **Accessibility** — VPAT 2.5Rev against WCAG 2.2 AA; iframe accessibility inside Schoology
8. **Terms of Use / Data Practices** — data collected, sharing, retention, IP ownership
9. **Data Security** — encryption (TLS 1.2+, AES-256), US storage, breach notification, export
10. **AI Disclosure** — every AI system, data flows, training opt-out, human review
11. **Ratings / Pledges** — Common Sense Privacy, 1EdTech TrustEd Apps (separate from LTI cert)

Plus the **DPA framework** (14 articles, reviewed as one unit).

## The 34-Item QC Checklist

Load `references/wcs-qc-checklist.md` when starting a QC. It defines the 34 items with pass criteria and common-failure modes.

## The Four Structural Checks (run first)

Before criterion-level review, run these four structural checks. Any failure here is an automatic Blocker and the rest of the QC proceeds in parallel, but the report must lead with it.

### S1. Academic year currency
- Header, section titles, and footer all show **current or upcoming AY**
- Today is April 19, 2026 → packets should read **AY 2026–27**, not 2025–26
- Check every occurrence, not just the header

### S2. Tech-stack internal consistency
- Does the document claim web-only, mobile-only, or both?
- Do App Store / Google Play references appear if product is web-only?
- Does cloud provider claim (Azure vs Railway vs AWS) match the vendor's actual infra?
- For History Hack, the baseline is: **web app on Azure (Node.js, React, TypeScript, Azure SQL Central US)**. Any deviation must be justified.

### S3. Reconciliation with prior WCS authorizations
- Run `memory_search` for prior WCS authorization records
- If authorization exists (e.g., Aug 2026 supplemental-curriculum approval under TCA 49-6-2202(a)(3)), confirm the packet either:
  - (a) is updating an existing approval, OR
  - (b) is a distinct gate (e.g., full district deployment vs. pilot)
- Reviewers will reject packets that contradict known prior approvals

### S4. Placeholder-token sweep
Search the document for any of these tokens — **every one is a Blocker**:
- `[insert `, `[INSERT `, `INSERT `
- `TBD`, `TODO`, `XXX`, `FIXME`
- `<placeholder>`, `{{`, `}}`
- Any bracketed guidance like `[e.g., ...]` that leaked into final prose

## Severity Scale

| Symbol | Severity | Meaning |
|---|---|---|
| 🛑 | **Blocker** | Submission will be rejected or misrepresents the vendor. Fix before any submission. |
| 🔴 | **High** | Likely to trigger clarification request or conditional approval. |
| 🟡 | **Medium** | Weakens response quality. Document workaround if not fixed. |
| 🟢 | **Low** | Polish or consistency. Ship without, but improves credibility. |

**Disposition thresholds:**
- Zero Blockers AND ≤2 High = ✅ READY (pending legal review)
- 1+ Blockers OR >2 High = ❌ NOT READY

## Workflow

### Phase 1 — Intake (2 tool calls max)
1. Read the WCS packet (prefer `parsed.*.txt` version if available)
2. Run `memory_search` for: "WCS authorization History Hack", "WCS compliance packet", "LTI 1.3 plan", "accessibility audit History Hack"
3. Confirm with the user (if ambiguous) which version / AY they are targeting

### Phase 2 — Structural checks (S1–S4)
Run all four in parallel. Emit a STATUS block after.

### Phase 3 — Criterion-by-criterion QC
Walk the 11 evaluation areas + DPA against `references/wcs-qc-checklist.md`. For each finding:
- Cite exact location (section, page/line)
- Quote the problem text verbatim (≤30 words)
- State the rule being violated (with statute/spec citation)
- Provide a specific fix (exact replacement language where possible)
- Assign severity

Emit STATUS block every 10 findings.

### Phase 4 — Verify any factual claims in the packet
Use `search_web` or primary-source lookup to verify:
- Statutory citations (TN code, federal regs) are current
- VPAT version claim matches current ITI revision (currently 2.5Rev, April 2025)
- WCAG version claim matches current ADA Title II requirement (2.2 AA)
- TN breach-notification timeline matches TCA 47-18-2107 (45 days)
- Any claim of "certified" / "compliant" has an actual artifact behind it

### Phase 5 — Produce deliverables
Write to `/home/user/workspace/wcs_qc_findings_{YYYYMMDD}.md`:

1. **Executive Summary** — 3-paragraph disposition, counts by severity, three structural problems (if any)
2. **Blockers section** — every Blocker with location, quote, rule, fix
3. **High section** — same structure
4. **Medium section** — same structure
5. **Low section** — same structure
6. **Consolidated Action List** — priority-ordered, grouped by week (Week 1 / Week 2 / Week 3)
7. **QC Summary Scorecard** — table by review area × severity counts
8. **Disposition** — READY / NOT READY with exact criteria met/missed

Share the file with `share_file`.

## Output Template

```markdown
# QC Report — WCS Responses for App Approval

**Document under review:** [filename]
**Vendor:** TroopToTeacher Technologies, LLC
**Product:** History Hack
**QC date:** [date]
**QC skill applied:** wcs-app-approval-qc v1.0
**Reviewer disposition:** [✅ READY / ❌ NOT READY] — [N] Blockers, [N] High, [N] Medium, [N] Low

## Executive Summary
[3 paragraphs]

## 🛑 BLOCKERS ([count])
### B1. [title]
**Location:** [section, line]
**Issue:** [quote + explanation]
**Rule:** [statute/spec citation]
**Fix:** [specific replacement]

[... repeat for each]

## 🔴 HIGH ([count])
[... same structure]

## 🟡 MEDIUM ([count])
[... same structure]

## 🟢 LOW ([count])
[... same structure]

## Consolidated Action List
### Before any editing
- [ ] [structural fix]

### Week 1 — Policies & published URLs
- [ ] ...

### Week 2 — Compliance artifacts
- [ ] ...

### Week 3 — Final QC & submission
- [ ] ...

## QC Summary Scorecard
| Review Area | Status | Blockers | High | Medium | Low |
|---|---|---|---|---|---|
[... 11 areas + DPA + doc polish]

**Disposition:** [READY / NOT READY with rationale]
```

## STATUS Block Format

Emit every 10 findings and at phase boundaries:

```
--- STATUS ---
Phase: [1-5]
Items reviewed: [N] / 34
Blockers: [N]
High: [N]
Medium: [N]
Low: [N]
Tool calls used: [N] / ~30
Next: [action]
--- END STATUS ---
```

## Re-QC After Remediation

When the user says "re-QC" or "run again on revised packet":

1. Load the previous QC report from workspace (`wcs_qc_findings_*.md`)
2. Load the revised packet
3. For each prior Blocker and High, verify fix was applied
4. Run full S1–S4 structural checks again (these can regress)
5. Spot-check Medium and Low items
6. Produce delta report: Fixed / Still Open / New Findings

## Known Gotchas (from April 2026 baseline QC)

These are the most common failure patterns observed:

1. **AY drift** — document written in fall of one AY, submitted in spring of the same AY (stale). Always date-check.
2. **Tech-stack template pollution** — mobile-app boilerplate left in web-only packets.
3. **VPAT 2.4 / WCAG 2.1** — both outdated. Use 2.5Rev / 2.2 AA.
4. **72-hour breach window cited as TN law** — it's GDPR. TN is 45 days.
5. **COPPA statement + grade 7 scope** — grade 7 includes 11-year-olds. Reconcile.
6. **FERPA School Official prongs missing** — direct-control language required.
7. **Subprocessor list empty** — must enumerate Azure, ElevenLabs, HeyGen, etc.
8. **Survival clause incomplete** — must include Data Portability (Article 11) and Governing Law (Article 14).
9. **Whitelist URLs missing** — network admins cannot deploy without them.
10. **AI disclosure undersells footprint** — list every AI system touching the product.

## Sibling Skill Coordination

After this QC passes, the following must run before submission:

| Step | Skill | Output |
|---|---|---|
| 1 | `wcs-app-approval-qc` (this) | Packet structurally sound |
| 2 | `accessibility-qc-agent` | VPAT-ready a11y audit on all live URLs |
| 3 | `copyright-integrity-accreditation` | Citation + licensing sweep |
| 4 | `ell-bilingual-review-specialist` | Bilingual coverage statement |
| 5 | Human legal counsel | Final redline |
| 6 | Submit |

## References

- `references/wcs-qc-checklist.md` — the 34-item checklist with pass criteria
- `references/wcs-evaluation-areas.md` — detailed spec for each of the 11 areas
- `references/known-gotchas.md` — extended failure-mode catalog
- `references/citation-bank.md` — statute and spec citations for quick reuse
