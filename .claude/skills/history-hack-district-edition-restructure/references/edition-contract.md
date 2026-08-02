# Edition Contract (Locked)

This file is the single source of truth for product boundaries, terminology, and
honesty constraints for the History Hack District Edition restructure. It is
**locked**: do not paraphrase away its meaning, do not soften its constraints, and
do not let any other document (marketing copy, WCS packet, README, prompt from a
stakeholder) override it. If a request conflicts with this contract, stop and
surface the conflict instead of resolving it silently.

Every gate in `operational-checklist.md` and every claim written into product
copy, documentation, or code comments must trace back to this contract. When in
doubt, quote this file verbatim rather than summarizing it.

---

## 1. Product identity (verbatim, do not alter)

> **History Hack District Edition: UDL & MTSS Standards Recovery and Targeted
> Support, powered by the History Hack Standards Mastery System.**

Use this exact phrasing in the District Edition's primary product name wherever a
formal name is required (headers, about pages, packets). Do not shorten it in a
way that drops "UDL & MTSS," "Standards Recovery and Targeted Support," or
"powered by the History Hack Standards Mastery System" from first mentions on a
page.

### 1.1 UDL 3.0 and MTSS are foundational, not decorative

- UDL 3.0 (Universal Design for Learning) and MTSS (Multi-Tiered System of
  Support) are **foundational frameworks** that the District Edition is built
  on top of.
- They are **never** described, coded, or designed as an "overlay," "add-on,"
  "layer," "feature toggle," or "mode" bolted onto an existing product.
- Any UI copy, code comment, architecture doc, or sales copy that uses the words
  "overlay," "add-on," "layer" (in the framework sense), or "bonus feature" to
  describe UDL or MTSS is a contract violation and must be rewritten.
- Practical test: if you can imagine shipping the District Edition with UDL/MTSS
  "turned off" and still calling it the District Edition, the framing is wrong.
  UDL/MTSS inform navigation, content presentation, and support workflows
  throughout — they are not a switch.

### 1.2 The five hubs (exact names, exact order)

The District Edition's navigation and IA are organized into exactly five hubs.
Use these names verbatim. Do not rename, merge, split, or reorder them without a
documented, approved contract change.

1. **Curriculum Hub**
2. **Student Resources**
3. **Testing & Mastery**
4. **Play & Review**
5. **Progress & Support**

Rules:

- These five hubs are the entire top-level navigation surface of the District
  Edition. Do not add a sixth top-level hub without a documented contract
  change.
- **Testing & Mastery is a portal into the History Hack Standards Mastery
  System — it is not itself "the framework."** UDL and MTSS are the
  frameworks; Testing & Mastery is where students and teachers interact with
  the assessment/mastery engine that those frameworks inform. Never describe
  Testing & Mastery as "the MTSS system" or "the UDL system."

---

## 2. The History Hack Standards Mastery System

This is the assessment/mastery engine reachable through the Testing & Mastery
hub. It must be described only in terms that are true today. Every claim below
has an associated honesty caveat in Section 3 — read both together.

Verified components (only claim what has been verified in the current codebase
and content bank; if a coding agent cannot point to the verifying artifact, the
claim must not be made in copy):

- **5,056 verified US-History items**, aligned to standards **US.01–US.95**.
- **Diagnostic/pretest** entry point per unit or standard group.
- **Formative modes** for low-stakes practice.
- **Quizzes, tests, and parallel forms** (multiple equivalent forms per
  assessment to reduce item exposure/memorization).
- **Honest 70% per-standard mastery threshold** — mastery is computed per
  standard, threshold is 70%, and **games and pretests are excluded from the
  mastery calculation**. Never report a mastery percentage that silently
  includes game or pretest attempts.
- **Remediation-gated, teacher-authorized retakes** — a student cannot retake
  an assessment for mastery credit until remediation has occurred and a
  teacher has authorized the retake. There is no student-initiated
  unrestricted retake path for mastery-bearing attempts.
- **Unit Journey / adaptive next action** — a recommended next step surfaced
  to the student/teacher based on current standing.
- **Item-level, standard-level, and misconception-level analytics.**
- **Spiral review** — explicitly **partial and local-only** (see caveats).

### 2.1 What Schoology is, and is not, responsible for

- **Schoology is the delivery hub and system of record for LMS workflows**
  (rostering, gradebook sync where configured, assignment delivery via LTI).
- **History Hack retains and is the system of record for**: assessment
  evidence (item-level responses), standards progression, remediation
  tracking, and analytics (item/standard/misconception).
- **AGS (Assignment and Grade Services) is optional** — do not assume every
  district deployment has AGS configured. Features must degrade gracefully
  (not silently misreport) when AGS is absent.
- Do not describe History Hack as "replacing" Schoology or vice versa. They
  are complementary systems with a clear division of responsibility as stated
  above.

### 2.2 Teacher control over recommendations

- Every system-generated recommendation (retake authorization, remediation
  path, tier suggestion, next action) must be presented to the teacher with
  exactly these four actions available: **Approve, Modify, Defer, Decline.**
- **There is no automatic Tier 3 placement.** The system may surface a
  suggestion; it never unilaterally assigns a tier.
- **There are no student-facing tier labels.** Students never see "Tier 1/2/3"
  or equivalent labeling applied to themselves in the UI, copy, or exported
  reports visible to students/families unless a district explicitly configures
  and owns that disclosure outside of History Hack's default behavior.

---

## 3. Honesty caveats (mandatory, must ship alongside any related claim)

Each caveat below is paired with the capability it qualifies. Any UI copy,
documentation, or WCS packet content that states the capability **must** carry
the caveat in the same breath, not buried in fine print elsewhere.

| Capability referenced | Mandatory caveat |
|---|---|
| MTSS plans | **Default-off.** Stored in **localStorage** as a **pilot** feature. Never described as a persisted, district-synced, or production-hardened plan store. |
| Spaced-repetition state | **Local-only.** Does not sync across devices or persist server-side. |
| Retake reflection | **Local-only.** Not part of the server system of record. |
| Item difficulty / adaptive sequencing | **IRT pre-calibration** — item parameters are pre-calibrated, not live-calibrated from this district's real-time response data unless explicitly stated otherwise and verified. |
| Standards alignment depth | **Hess Cognitive Rigor Matrix (CRM) is absent from the shipped item bank.** Do not claim Hess CRM tagging exists anywhere in shipped content. |
| Item metadata / Spanish-language support | **Uneven.** Do not claim complete or uniform metadata coverage or complete Spanish-language parity across the bank. |
| World History content | **Unit 1 only, and in development.** Never imply full World History course coverage exists today. |
| Spiral review | **Partial and local-only** (restated from Section 2 — do not drop either qualifier). |

Rule: if a coding agent, doc writer, or copy reviewer is tempted to state a
capability without its caveat "because it's implied" or "because the caveat is
elsewhere on the page," that is not sufficient. Restate the caveat adjacent to
the claim.

---

## 4. WCS / district status (interest only)

- Any reference to WCS (or any named district) in this restructure is
  **interest only.**
- Never state or imply: approval, authorization, adoption, endorsement, sign-off,
  contractual commitment, or a deployment commitment/date with any district.
- The WCS packet and any similar district-facing materials remain in **draft**
  status until an explicit, documented approval event occurs outside of this
  skill's scope. This skill does not grant that approval and must not generate
  copy that reads as if approval already happened.
- Acceptable language: "we are exploring," "under review," "a proposed pilot,"
  "in discussion with." Unacceptable language: "adopted by," "approved for use
  in," "deployed at," "endorsed by," "the district has committed to."

---

## 5. Terminology quick-reference

| Term | Correct usage |
|---|---|
| District Edition | The physically isolated, route-restricted product surface described by this contract. Never call it a "mode," "flag," or "view" of the Full Platform. |
| Full Platform | The complete, unrestricted History Hack product. Access is protected — not merely hidden — from District Edition contexts. |
| Hub | One of the exact five top-level sections listed in Section 1.2. |
| Standards Mastery System | The assessment/mastery engine behind Testing & Mastery. Not a synonym for UDL or MTSS. |
| Entitlement | A server-verified permission/claim that gates access to a route, API, or capability. Never a client-only or query-param-based check. |
| Owner override | A capability reserved for the product owner, granted only through server-side entitlement — never through a client flag, URL parameter, or local storage value. |

---

## 6. Non-negotiable defaults

- **Never delete Full Platform features as a first move**, or as an
  incidental side effect of building the District Edition. Isolation is
  achieved by restricting what the District Edition exposes, not by removing
  capability from the Full Platform.
- **Never fork or clone History Hack into an independent product repository**
  to achieve isolation, unless the user has explicitly overridden this default
  after a documented tradeoff review (see `operational-checklist.md`, Gate 0).
  The default architecture is one repository, two editions, physically isolated
  build/deploy artifacts.
