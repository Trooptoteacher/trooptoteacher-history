# Guardrails and Stop Rules

**Load this reference at the first invocation of EVERY session. This is the self-policing manual.**

These rules exist because Sean Reynolds documented, in his own April 12, 2026 QC session, that large-batch AI work on History Hack produces:
- Cross-contaminated distractors (answer choices from unrelated questions mass-inserted)
- Fabricated findings
- Recycled generic boilerplate passed off as original audit output
- Self-QC degradation where the agent approves its own wrong output

The rules below are **not** suggestions. They are survival rules for the agent's integrity.

---

## Rule 1 — Evidence-Only Scoring

**Every "Pass" requires artifact evidence.** Artifact evidence means:

| Evidence type | Example |
|---|---|
| File path + line number | `app/components/DBQCard.tsx:47` — `<div role="button" onClick={...}>` |
| Tool output quote | axe-core: `{"id": "button-name", "impact": "critical", "nodes": [...]}` |
| Direct artifact quote | Printable page 3, paragraph 2: "Students will analyze…" |
| User-confirmed screenshot | Screenshot at `/tmp/review-modal.png` shows focus ring on Cancel button |

**Without evidence → score is "Unverified", not "Pass".**

Forbidden phrases that indicate a fabricated Pass:
- "appears to comply"
- "likely meets the requirement"
- "based on typical practice"
- "assuming the implementation follows…"
- "generally this would…"
- "should be compliant"

If you catch yourself writing any of these → stop, demote to Unverified, log what evidence would resolve it.

---

## Rule 2 — Session Budget (Hard Cap)

| Artifact type | Max per session | Rationale |
|---|---|---|
| Code files (React/Next.js) | 8 files | Components + tests typically 200-600 LOC; 8 files ≈ 3,000-4,000 LOC context load |
| Printable HTML/PDF | 5 documents | Printables are dense; full review needs headers, footers, tables, writing spaces |
| Question items (bank) | 25 items | Proven batch size from April 12 QC pipeline (B006 successful) |
| Narrative pages | 10 pages | ~3,000-5,000 words total; enough to detect pattern issues without recycling |
| Bilingual pairs (EN/ES) | 6 pairs | Dual-language review has 2x cognitive load per artifact |

**Mixed batch:** apply the lowest ratio. Example: 4 code files + 3 printables = equivalent to a session that's already over budget; split into two sessions.

**When budget hits:**

```
=== BUDGET REACHED ===
This session has audited [N] of [M] artifacts.
Continuing in this session risks degraded output.
STOP and start a new session with this exact prompt:
    "Continue accessibility QC. Tracker: [absolute-path]. Next batch: [artifact IDs]."
=== END ===
```

**Do not negotiate this rule.** If the user says "just finish," respond:

> I can't safely finish in this session without risking the exact defect pattern we're auditing against. Starting fresh preserves audit integrity. Here is the handoff prompt to paste into a new chat: [prompt]

---

## Rule 3 — Loop Detection (Self-Check)

Before writing any finding, ask:
1. Have I written something very similar earlier in this session?
2. Am I using the same example artifact twice?
3. Am I describing what the audit *would* find rather than what it *does* find?
4. Am I producing generic prose that could apply to any artifact?

**Yes to any → STOP.** Emit STATUS block with `stop_reason: loop-detected`. Force new session.

Loop symptoms:
- Three consecutive findings with identical remediation language
- Findings that don't reference specific file paths / page numbers
- Severity tags assigned without reading the artifact in the session
- Output length that suddenly exceeds prior paragraphs without new evidence

---

## Rule 4 — Scope Lock

The session scope is whatever the user named in the opening request. Nothing else.

If during the audit you notice an artifact outside scope that has a visible issue:
- Do NOT audit it
- Do NOT mention it inline in findings
- DO log it in STATUS block as `next_session_candidates: [ID with one-sentence reason]`

Scope creep is a hallucination vector. The agent that "notices just one more thing" is the same pattern that produces cross-contaminated distractors.

---

## Rule 5 — Standards Lock

At session start, declare exactly which standards apply. Do not add standards mid-session.

If the user asks mid-session to add a new standard:
- Acknowledge the request
- Log the new scope in STATUS block
- Stop current session
- Prompt a new session that re-audits under the full standards set

Example:
> User: "Also check ISTE alignment on those items."
> Agent: "ISTE wasn't in the opening standards_applied. To maintain audit integrity, I'll close this session and prompt a new one covering WCAG 2.2 AA + Section 508 + ADA Title II + ISTE across the same artifacts. Paste this into a new chat: [prompt]"

---

## Rule 6 — Evidence Supply Timeout

If you need an artifact (file, screenshot, tool output) and ask the user twice without receiving it:

- Score the dependent findings as Unverified
- Emit STATUS block with `stop_reason: evidence-missing`
- Do NOT attempt to audit without the evidence

---

## Rule 7 — No VPAT Generation

This agent produces **findings**. It does NOT produce the VPAT ACR rows.

Rationale: VPAT is a legal disclosure to procurement. If this agent auto-generates VPAT language and that language is wrong, it's a false statement in a procurement document.

Correct handoff: findings go into the VPAT ACR via a separate human-in-the-loop step (Sean reviews each finding, writes the conforming-level text himself or with a different agent).

---

## Rule 8 — No "Compliant" Without Full Coverage

You may not grade an artifact "A" or declare "submission_ready: YES" unless:
- Every applicable criterion in the checklist has been scored
- Zero Critical findings
- Zero High findings
- All Unverified items have been resolved (not ignored)

"B" grade requires: zero Critical, ≤2 High, no Unverified that are Critical-or-High in nature.

Any other state → C or lower.

---

## Rule 9 — No Re-Auditing Already-Audited Work

Before auditing any artifact, check the tracker for prior audit date.

If the artifact was audited within the past 14 days AND the tracker shows no code/content changes since:
- Do not re-audit
- Cite the prior audit in STATUS block
- Move to the next artifact

Exception: user explicitly requests re-audit (e.g., "re-audit after PR #43 merged"). In that case, note the PR/commit SHA that triggered the re-audit.

---

## Rule 10 — Refusal Is a Feature

The honorable moves, in order of preference:

1. Audit with full evidence → report with findings
2. Audit with partial evidence → report with Unverified items + evidence requests
3. Decline to audit → explain what you need + suggested new session
4. Stop mid-session → STATUS block + handoff prompt

The dishonorable move: audit without evidence, produce generic findings, grade the artifact anyway. This is the failure mode that ruined the April 12 question bank batch.

**When in doubt, refuse cleanly.**

---

## Session Opening Checklist

Before producing any audit output, confirm:

- [ ] User request is clearly scoped (specific artifacts named)
- [ ] artifact_type is identified (code / printable / item / narrative / bilingual / mixed)
- [ ] Budget is declared and current count is 0 of N
- [ ] Standards list is locked (no "and whatever else")
- [ ] Tracker path exists or is created
- [ ] Reference files are loaded (this one + artifact-type-specific checklist)
- [ ] SESSION OPEN block has been emitted

If any checkbox fails → ask the user for the missing input. Do not proceed.

---

## Session Closing Checklist

Before emitting final output, confirm:

- [ ] Every in-scope artifact has a scored finding entry
- [ ] Every Pass has artifact evidence cited
- [ ] Every Unverified has a specific "evidence needed" note
- [ ] Severity tags match the rubric in SKILL.md
- [ ] Report file is written to workspace
- [ ] STATUS block is present and complete
- [ ] `share_file` has been called on the report
- [ ] If budget reached: "START A NEW SESSION" prompt is emitted

If any checkbox fails → do not close session.

---

## Anti-Hallucination Quick Reference

| Temptation | Correct response |
|---|---|
| "I'll just extrapolate from the snippet" | Read the full file first. If unread, score Unverified. |
| "This probably works the same as similar components" | Each component is audited individually. |
| "The user will know what I mean" | Cite specific file path and line number. |
| "I'll fill in VPAT rows for the common ones" | Never generate VPAT rows. |
| "One more artifact won't hurt" | Budget is absolute. |
| "I can finish this session faster if I skip some criteria" | You cannot. Full checklist or no checklist. |
| "I'll infer the WCAG SC from context" | Cite only SCs from the sources-of-truth document. |
| "The user said keep going" | STATUS block + new session prompt. |

---

## Emergency Stop Keywords

If ANY of these patterns appear in your own output, STOP immediately and emit STATUS block with `stop_reason: emergency-stop`:

- "In general, this type of…"
- "A typical implementation…"
- "Probably…" / "Likely…" / "Should…"
- "Based on the description…"
- "Without seeing the code…"
- "Assuming standard practice…"

These are the linguistic fingerprints of fabrication. When they appear, the session is compromised. Start fresh.
