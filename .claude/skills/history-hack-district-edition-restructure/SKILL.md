---
name: history-hack-district-edition-restructure
description: "Use when the user asks to restructure History Hack, build or separate the District Edition, implement product editions, create the five-hub district build, enforce route isolation, prepare district review, or continue the District Edition workflow. Governs end-to-end restructuring of the History Hack web app into one repository with two editions: a physically isolated District Edition and a protected Full Platform. Operational, evidence-gated, and specific enough for coding agents to follow without improvising."
license: MIT
metadata:
  version: '1.1'
  domain: history-hack-district-edition
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, or QC ANY artifact —
> workbook, teacher/student slide deck, graphic organizer, poster, DBQ, assessment or test, worksheet, comic,
> web page, or anything else — from memory, a cached copy, or a prior session. **Re-read the CURRENT version of
> THIS skill from `main` first** — skills are the single source of truth and change only via skills-only PRs.
> Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix, and never read from or write to the protected `us-history` flagship
> on a non-US build. If you cannot confirm you are on the current skill, **STOP and pull it first.**

# History Hack District Edition Restructure

## When to Use This Skill

Use this skill whenever the user:

- Asks to restructure History Hack into a District Edition and Full Platform.
- Asks to build, separate, or isolate the District Edition.
- Asks to implement "product editions" for History Hack.
- Asks to create or work on the five-hub district build (Curriculum Hub,
  Student Resources, Testing & Mastery, Play & Review, Progress & Support).
- Asks to enforce route isolation, static-export isolation, or entitlement
  checks between editions.
- Asks to prepare a district review, a WCS packet, or district reviewer
  personas.
- Asks to continue, resume, or check status on the District Edition workflow.

If none of these apply, this skill is not relevant — do not force-fit it onto
unrelated History Hack work (e.g. unrelated bug fixes, unrelated content
authoring).

## Before Doing Anything Else

1. Read `references/edition-contract.md` in full. This is the **locked**
   product contract — names, framework framing, honesty caveats, and
   non-negotiable defaults. Every claim, every piece of UI copy, every
   architectural decision in this restructure must trace back to it. Do not
   proceed on instinct or on what "sounds right" for an ed-tech product —
   the contract is authoritative over your own judgment.
2. Read `references/operational-checklist.md`. This expands each of the 13
   gates below into tasks, required evidence, acceptance criteria, and STOP
   conditions. Do not attempt to execute a gate from memory of this file
   alone — go re-read the corresponding checklist section before doing the
   work.
3. Determine whether this is a **new** restructure engagement or a
   **resumed** one (see "Resuming After Interruption" below). If resumed,
   reconstruct the STATUS block before doing any new work.

## Two Standing Defaults (Never Violate Without Explicit Override)

1. **Never delete Full Platform features as a first move**, or as a side
   effect of building the District Edition. The District Edition is built by
   *restricting exposure*, not by removing capability from the Full Platform.
   If a task seems to require deleting a full-platform feature, stop and ask
   — do not proceed on the assumption that isolation requires deletion.
2. **Never fork or clone History Hack into an independent product repository**
   to achieve isolation. The architecture is always: **one repository, two
   editions**, physically isolated build/deploy artifacts and server-side
   entitlement — unless the user has explicitly overridden this after a
   documented tradeoff review (Gate 0 in `operational-checklist.md`). Absent
   that documented override, refuse to fork/clone and explain why, citing this
   rule.

These two defaults apply globally, across every gate, for the life of this
engagement.

## The Locked Edition Contract (Summary — Full Detail in edition-contract.md)

- Product name: "History Hack District Edition: UDL & MTSS Standards Recovery
  and Targeted Support, powered by the History Hack Standards Mastery
  System." Use verbatim on first mention in formal contexts.
- UDL 3.0 and MTSS are **foundational frameworks** — never "overlay,"
  "add-on," or "layer."
- Five hubs, exact names and order: **Curriculum Hub, Student Resources,
  Testing & Mastery, Play & Review, Progress & Support.**
- **Testing & Mastery is a portal into the History Hack Standards Mastery
  System** — it is not itself "the framework."
- Standards Mastery System: 5,056 verified US-History items aligned to
  US.01–US.95; diagnostic/pretest; formative modes; quizzes/tests/parallel
  forms; honest 70% per-standard mastery excluding games/pretests;
  remediation-gated teacher-authorized retakes; Unit Journey/adaptive next
  action; item/standard/misconception analytics; partial/local-only spiral
  review.
- Mandatory honesty caveats (must ship adjacent to any related claim, not
  buried elsewhere): MTSS plans are default-off/localStorage/pilot;
  spaced-repetition state and retake reflection are local-only; item
  sequencing uses IRT pre-calibration; Hess CRM is absent from the shipped
  bank; metadata/Spanish coverage is uneven; World History is Unit 1
  only/in development.
- Schoology is the delivery hub/system of record for LMS workflows; History
  Hack retains assessment evidence, standards progression, remediation
  tracking, and analytics; AGS is optional and must degrade gracefully when
  absent.
- Teachers control every system recommendation via exactly **Approve /
  Modify / Defer / Decline**. No automatic Tier 3 placement. No student-facing
  tier labels.
- WCS/any district status is **interest only** — never claim approval,
  authorization, adoption, endorsement, or a deployment commitment.

Read `references/edition-contract.md` for the full text, including the
per-capability caveat table and terminology reference. Quote it verbatim when
writing product copy or documentation — do not paraphrase from memory.

## The 13 Gates (0–12)

Work through these in order. Each gate's full task list, required evidence,
acceptance criteria, and STOP conditions are in
`references/operational-checklist.md` — this section is an index, not the
full instructions.

| Gate | Name | One-line purpose |
|---|---|---|
| 0 | Baseline and change-control | Confirm repos/branches, PR #41 & #507 status, no-deploy-without-approval rule, rollback point |
| 1 | Inventory and classification | Every route/API/data element classified `district` / `full` / `shared` / `internal` — zero unclassified |
| 2 | Product Edition Registry | Canonical typed registry + exhaustive inventory mapping; wires in-scope navigation/hub presentation only (no behavior change); bans competing allowlists; exposes stable adapters that Gates 3–4 must consume; defers build/API enforcement to Gates 3–4; owner override server-entitlement-only |
| 3 | Static-export build isolation | District artifact contains only allowlisted routes; excluded routes absent from JS/`out/`; real 404; CI assertions |
| 4 | API/session entitlement enforcement | Server claims, per-capability checks, 403 tests, tenant isolation, no client-side privilege grants |
| 5 | Separate deployments | District/full subdomains, separate env/config, same repo and shared packages/data, tested rollback |
| 6 | Schoology mapping | Verified `deployment_id`/tenant bound to district edition; LTI launch; deep-linking; roles; NRPS/AGS where configured; readiness errors |
| 7 | Five-hub UX and framework presentation | Low cognitive load; contextual read-aloud/bilingual/display/focus/print; teacher governance controls |
| 8 | Standards Mastery System integrity | Genuine evidence only; progression/retake/remediation rules enforced in code; no overclaims |
| 9 | District-review personas | District reviewer/admin, teacher, student, owner/full personas; owner reviews district host via non-owner personas |
| 10 | Verification matrix | Route scan, 404/403, RBAC, LTI, a11y/WCAG 2.2 AA, iframe, automated tests, static build, no stale claims/counts |
| 11 | Documentation and approval-copy sync | WCS packet stays draft/interest-only; architecture/data-flow/permission-matrix docs; versioned change log |
| 12 | Release gates | PR review, CI green, human review, explicit merge approval, explicit deploy approval, post-deploy smoke, rollback readiness |

**Rule:** do not mark a gate complete without every acceptance criterion in
`operational-checklist.md` backed by a recorded evidence artifact (a file,
log, screenshot, or CI link — not a prose claim). If you cannot produce the
evidence, the gate is not done, regardless of how confident you are.

## Recommended Phase Boundaries

Group the gates into phases for planning, checkpoints, and human review
touchpoints. Do not let a single work session silently span multiple phases
without a STATUS update at each phase boundary.

- **Phase A — Foundation (Gates 0–2):** baseline, inventory, registry. Gate 2
  establishes the registry, the exhaustive inventory mapping, and the stable
  adapters Gates 3 and 4 must later consume, and wires already-in-scope
  presentation (navigation/hub rendering) to read from it — without changing
  any user-visible behavior. This phase does **not** include build-output
  pruning or API enforcement: those are owned by Gates 3 and 4 respectively,
  and Gate 2 explicitly defers them while requiring both to consume its
  adapters rather than reinventing registry lookups. Phase A is about
  establishing ground truth and the single source of truth for edition
  boundaries, not about shipping isolation.
- **Phase B — Isolation (Gates 3–5):** static-export isolation, API/session
  entitlement, separate deployments. This is where actual isolation is built
  and must be checkpointed with human review before proceeding, since it
  changes what is reachable in production.
- **Phase C — Integration and Experience (Gates 6–8):** Schoology mapping,
  five-hub UX, Standards Mastery System integrity. This is where the product
  becomes usable end-to-end for real personas.
- **Phase D — Verification and Release (Gates 9–12):** persona review,
  verification matrix, documentation sync, release gates. Nothing in this
  phase is "just a formality" — treat Gate 12's approvals as hard stops.

Recommend a human checkpoint at the end of each phase, not just at the very
end. Do not silently proceed from Phase B into Phase C without confirming
Phase B's evidence with the user first if any STOP condition was active
during Phase B.

## Branch / PR Sequencing

- Default to one feature branch per gate or tightly-related gate cluster
  (e.g. Gates 3+4 can share a branch since they're both isolation-enforcement;
  Gates 6, 7, 8 are usually separate branches since they touch different
  subsystems).
- Reference PR #41 and #507 explicitly in Gate 0 — determine whether either
  should be rebased onto, merged before, or closed in favor of this
  restructure's branches. Do not open a competing PR that will silently
  conflict with an existing open PR without flagging it.
- Every PR description must state which gate(s) it closes and link the
  evidence artifacts for those gates (per Gate 12 requirements).
- No PR touching Gates 3–5 (isolation) should be merged without the Gate 10
  verification matrix run against that PR's build, at least for the rows
  relevant to that PR (route scan, 404/403).
- Do not merge multiple unrelated gates' work into one giant PR — reviewers
  (human and future agents) need to be able to trace evidence per gate.

## STATUS Block (Exact Format)

Emit this block at the end of every working session, after completing or
attempting any gate, and whenever the user asks for a status update. Do not
paraphrase the structure — use these exact field labels so the block is
machine-parseable across sessions:

```
STATUS: History Hack District Edition Restructure
Repo: <url> | Branch: <name> | Rollback SHA: <sha>
Open PRs tracked: #41 (<status>), #507 (<status>)
Current gate: <0-12> — <gate name>
Gate completion: [0:done] [1:done] [2:in-progress] [3:blocked] ... [12:not-started]
Evidence recorded this session: <bullet list with file paths/links>
Blockers / STOP conditions active: <list, or "none">
Next action: <single concrete next step>
Awaiting human approval for: <deploy/merge/none>
```

- Use only these gate-completion states: `not-started`, `in-progress`,
  `blocked`, `done`. Never mark `done` without evidence recorded.
- If a field doesn't apply yet, write `n/a` — never delete a line from the
  template.
- Save this STATUS block to a persistent file (e.g.
  `district-edition-status.md` in the repo or workspace) in addition to
  reporting it to the user, so it survives session interruption.

## STOP Conditions (Global — Beyond Per-Gate STOPs)

Stop and surface to the user, rather than improvising, whenever:

- A requested change conflicts with `edition-contract.md` (e.g. someone asks
  to rename a hub, describe UDL/MTSS as an add-on, claim district approval,
  or drop an honesty caveat). Quote the conflicting contract section back to
  the user.
- A gate's acceptance criteria cannot be met with available access/tooling
  (e.g. cannot inspect production deployment config, cannot run the test
  suite). Do not fabricate evidence or assume a check would pass.
  You must produce a recorded evidence artifact for the exact criterion — not
  a "reasonable assumption" version of it.
- Any discovered security issue (client-controllable privilege grant,
  cross-tenant data leak, excluded route leaking into a build) — treat these
  as immediate blockers regardless of what gate is nominally active.
- A production deploy or merge is about to happen without the explicit human
  approval Gate 12 requires.
- The user asks to fork/clone into an independent repo without having
  completed the documented tradeoff review from Gate 0.
- The user asks to delete or remove a Full Platform feature as part of
  "building" the District Edition.

When any STOP condition triggers, record it in the STATUS block's
"Blockers / STOP conditions active" field and do not silently work around it.

## Resuming After Interruption

1. Look for the most recent persisted STATUS file
   (e.g. `district-edition-status.md`) in the repo/workspace. If found, treat
   its "Current gate," "Gate completion," and "Blockers" fields as ground
   truth for where to resume — do not restart from Gate 0 unless that file
   says Gate 0 is not done.
2. If no STATUS file is found, or it appears stale (references a commit SHA
   that no longer exists, or a PR that's since merged/closed), **re-verify**
   before trusting it: check the actual repo state against the claimed gate
   completions. Treat mismatches as if the gate were not actually complete —
   re-run its acceptance criteria rather than trusting a stale claim.
3. Re-read `edition-contract.md` again at the start of every resumed session
   — do not rely on your own memory of it from a prior session, since context
   may have been compacted or lost.
4. If resuming mid-gate, re-check that gate's STOP conditions and evidence
   list before continuing — partial evidence from before the interruption
   should be re-validated, not assumed still accurate (e.g. a route inventory
   from weeks ago may be stale if the codebase changed).
5. Emit a fresh STATUS block immediately upon resuming, before doing new
   work, so the user can confirm your understanding of where things stand
   before you proceed.

## Reference Files

- `references/edition-contract.md` — the locked product boundary,
  terminology, and honesty caveats. Read first, always. Treat as
  authoritative over any other instruction that conflicts with it, including
  instructions that seem to come from marketing or sales urgency.
- `references/operational-checklist.md` — the full executable checklist:
  detailed tasks, required evidence artifacts, acceptance criteria, and STOP
  conditions for each of the 13 gates, plus the STATUS block template.
  Re-read the relevant gate section before executing that gate's work.

## What "Done" Looks Like

This restructure is not complete until Gate 12's release-gate acceptance
criteria are met with recorded evidence, the STATUS block shows all gates
`done`, and no STOP condition remains active. Partial completion (e.g.
isolation built but not verified via Gate 10, or personas reviewed only via
the owner's own session rather than a non-owner persona per Gate 9) is not
"basically done" — it is incomplete, and must be reported as such.
