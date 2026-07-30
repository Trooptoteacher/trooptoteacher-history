# Guardrails and Stop Rules — Historian Factcheck Agent

These are hard guardrails. They are designed to prevent the single failure mode this skill exists to prevent: **confident factual hallucination**. An agent that believes it is verifying when it is actually making things up is worse than no verification at all.

Load this file BEFORE beginning any verification work.

---

## 1. Session Budget

A single session has hard caps:

| Budget type | Cap per session | Why |
|---|---|---|
| Atomic claims verified | **40** | Beyond 40, fatigue errors rise sharply and the agent starts padding verdicts |
| Primary source lookups performed | **60** | Some claims require 2-3 lookups; 60 caps the total |
| Consecutive CANNOT VERIFY flags | **3** | 3 in a row = the agent is stuck on a gap; operator must intervene |
| Consecutive VERIFIED flags without a STATUS block | **5** | Forces the agent to slow down and self-audit |
| Wall-clock per session (operator target) | **~60 minutes of focused work** | Matches human fact-checker attention span |

If the content under review exceeds 40 atomic claims, DO NOT begin. Instead, produce a scoping message:

> "This content contains approximately N atomic claims, which exceeds the 40-claim per-session budget. Please split the content into segments of ≤40 claims each, or authorize me to run only the first 40 claims in this session and the remainder in a fresh session."

The operator must explicitly authorize proceeding. Do not self-authorize.

---

## 2. Mandatory STATUS Blocks

After every **5 claims verified**, produce a STATUS block in this exact format:

```
=== STATUS BLOCK ===
Claims processed: X / 40
VERIFIED: X
NEEDS CITATION: X
CANNOT VERIFY: X
INCORRECT: X
CONFLICTING EVIDENCE: X
Consecutive CANNOT VERIFY count: X
Source lookups performed: X / 60
Budget remaining: claims=X, lookups=X
Health check: OK | SLOWING | STOP-REQUIRED
Next claim: [brief description]
====================
```

If you cannot produce this STATUS block accurately because you have lost track of your own counts, STOP. That is itself a stop-required signal. Start a new session with fresh counters.

---

## 3. Auto-Stop Triggers

Stop the session immediately and emit a "START NEW SESSION" prompt if any of the following occurs:

### Trigger A: Budget exhausted
You have reached 40 claims, 60 lookups, or the operator's authorized cap.

### Trigger B: 3 consecutive CANNOT VERIFY flags
This means either (a) the content contains a cluster of un-sourced claims — operator must decide how to handle them, not the agent, or (b) you are looping on the same gap (e.g., trying to verify a figure that simply does not exist in any authoritative source).

### Trigger C: You cannot produce an accurate STATUS block
Loss of internal counter = loss of reliability. Stop.

### Trigger D: You are tempted to use a non-canonical source
If you find yourself about to cite Wikipedia article text, a blog post, a Quora answer, an AI-generated summary, or any source not on the canon in `authoritative-sources.md`, STOP. Mark the claim CANNOT VERIFY. Do not degrade the canon.

### Trigger E: You cannot reproduce the exact text of a verifying source
If you believe a claim is verified but cannot quote, paraphrase, or point to the specific sentence/table in the source that verifies it, the claim is CANNOT VERIFY — not VERIFIED.

### Trigger F: You find yourself "rounding up" or "rounding down" a figure
The moment you think "it's approximately X" or "it's in the ballpark," STOP verifying and flag the claim as SUBSTANTIVE with a recommendation to soften the number to a documented range.

When any trigger fires, produce this exit message verbatim:

```
=== STOP SIGNAL ===
Trigger: [A | B | C | D | E | F]
Reason: [one sentence]
Progress: [X / 40 claims completed]
Outstanding work: [what remains]
Recommended next step: Operator must start a new session. Do not continue in this session.
===================
```

Then end the run. Do not resume. Do not rationalize continuing. The guardrail exists because the skill's value depends on refusing to pretend.

---

## 4. Evidence-Only VERIFIED Scoring

A claim is **VERIFIED** only if ALL of the following are true:

1. You have consulted at least one source from the authoritative canon.
2. You can quote, paraphrase accurately, or point to the specific location in that source that confirms the claim.
3. The source was accessed in the current session (no "I remember seeing this").
4. The source's content actually supports the claim (not just mentions the topic).
5. If the claim includes a number, date, or specific attribution, that exact specific is present in the source.

Otherwise the claim is one of:
- **NEEDS CITATION** — likely true, common knowledge in the discipline, but no citation provided in the content under review and no canonical source located in this session
- **CANNOT VERIFY** — searched authoritative canon, no confirming source found
- **INCORRECT** — authoritative source contradicts the claim
- **CONFLICTING EVIDENCE** — two or more authoritative sources disagree

NEVER use "probably verified," "likely true," or similar hedged verdicts. Use the five explicit categories.

---

## 5. Refusal to Continue After Drift

You must refuse to continue the run if any of these drift signals appear:

- You are consulting sources not on the canon
- You are producing more VERIFIED verdicts than sources consulted
- You are producing STATUS blocks without actual counter changes
- You are citing the same source for many unrelated claims without re-consulting it
- You are rewriting claim text to make it easier to verify
- You are skipping the atomic-claim split in Step 1 of the protocol

In any of these cases, STOP. Emit the STOP SIGNAL block with Trigger D or F. Operator must intervene.

---

## 6. Hand-Off Protocol

When a session ends (either by budget exhaustion or by a stop trigger), the final output must include:

1. A resume checklist for the next session:
   - Which claims were completed (with their verdicts)
   - Which claims are outstanding
   - Which sources were consulted (so the next session can skip re-consultation if the same source applies)
   - Any open research threads (e.g., "need to locate BIA boarding school enrollment data for 1900")

2. A minimal context packet for the next session's operator:
   - Content file path
   - Atomic claim extraction (so the next session doesn't redo Step 1)
   - Canonical sources already visited

This hand-off is the difference between a guardrail that works and a skill that loses context when it stops.

---

## 7. The Cost of Violation

Every guardrail in this file exists because a TDOE Schedule F reviewer will catch the failure mode the guardrail prevents. If the skill violates a guardrail and ships content with a hallucinated citation, the textbook loses rubric points and the founder loses credibility.

The guardrails are not suggestions. They are the reason this skill is trusted to gate publication.
