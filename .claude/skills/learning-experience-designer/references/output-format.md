# Output Format — Full Reference

When designing a learning experience, provide all nine sections below. This is the standard deliverable format.

---

## Section 1: Experience Overview

| Field | Description |
|---|---|
| **Experience Name** | Descriptive name for the learning experience |
| **Target Audience** | Grade level, course, learner characteristics |
| **TN Standards** | Specific standards addressed (US.XX format) |
| **History Hack Unit** | Which unit this belongs to (Units 1-11) |
| **Estimated Duration** | Total time and per-segment breakdown |
| **Prerequisites** | What students need to know before starting |
| **Experience Type** | Lesson, activity, assessment, review, exploration, etc. |

---

## Section 2: Learner Personas Considered

For each relevant persona, document:

- **Persona name and description** (e.g., "Struggling Reader — 9th grader reading at 6th grade level")
- **Key needs** for this experience
- **Accommodations designed** into the experience
- **Potential barriers** identified and mitigated

Minimum: Address at least 3 distinct personas per design.

---

## Section 3: Experience Map

Provide a visual or structured journey map including:

- Entry point and activation hook
- Core learning segments (numbered, with objectives)
- Decision/branching points
- Scaffolding triggers (when supports activate/deactivate)
- Spaced-review placement (interval math deferred to spaced-repetition-engine)
- Feedback checkpoints
- Assessment moments
- Intentional emotional arc (curiosity → challenge → discovery → mastery → reflection)
- Exit point and transition to next experience

Use ASCII diagrams, flowcharts, or structured lists.

---

## Section 4: Interaction Specifications

For each interaction in the experience, provide:

| Field | Description |
|---|---|
| **Interaction name** | Descriptive label |
| **Type** | Drag-and-drop, timeline, map, document analysis, simulation, annotation, matching, constructed response, etc. |
| **Learning objective** | What this interaction teaches/practices |
| **TN standard** | Specific standard(s) targeted |
| **DOK level** | Webb's Depth of Knowledge level |
| **Instructions shown to student** | Exact text the learner sees |
| **Expected duration** | Minutes for this interaction |
| **Correct response(s)** | What constitutes a correct answer |
| **Feedback — correct** | What the learner sees on success |
| **Feedback — incorrect** | Progressive hint sequence |
| **Accessibility intent** | Keyboard, screen reader, mobile considerations (formal audit → accessibility-qc-agent) |
| **Pedagogical rationale** | Why this interaction type was chosen for this objective |

---

## Section 5: Feedback Design

Document the full feedback system:

- **Immediate feedback** for each interaction (what, when, how detailed)
- **Progressive hint system** (levels of support before revealing answer)
- **Segment summary feedback** (after completing a section)
- **Mastery progress feedback** (standard-level progress tracking)
- **Growth-oriented language** examples used throughout

---

## Section 6: Inclusive-Design Notes (UDL)

Document your UDL *intent* across all three principles — how the design provides multiple means of Engagement, Representation, and Action & Expression, and at least one genuine alternative for each. State intent only; **route the formal UDL 3.0 / CAST audit and checkpoint matrix to udl-cast-expert.**

| Principle | UDL intent in this design | Alternative provided |
|---|---|---|
| Engagement | | |
| Representation | | |
| Action & Expression | | |

---

## Section 7: Accessibility Intent

Specify per-interaction accessibility intent (keyboard operability, screen reader support, color contrast, no color-only meaning, captions/transcripts, touch targets, respects `prefers-reduced-motion`). State intent only; **route the formal accessibility audit to accessibility-qc-agent**, which enforces WCAG 2.2 AA / Section 508 / ADA Title II as the sources of truth.

---

## Section 8: Success Metrics

Define measurable outcomes:

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Completion rate | ≥ 85% | LRS/xAPI event tracking | Weekly |
| Assessment mastery | ≥ 70% score | Post-experience assessment | Per cohort |
| Time-on-task | Within ±20% of estimate | Session duration analytics | Weekly |
| Engagement duration | ≥ 80% active time | Interaction event tracking | Weekly |
| Retry rate | 1-3 attempts average | Attempt count analytics | Monthly |
| Student satisfaction | ≥ 4.0/5.0 | Post-experience survey | Per cohort |

Customize targets and metrics for each experience.

---

## Section 9: Iteration Plan

| Phase | Timeline | Activities |
|---|---|---|
| **Baseline** | Pre-launch | Define metrics, set targets, instrument analytics |
| **Initial data** | Weeks 1-2 | Collect usage data, monitor for critical issues |
| **First review** | Week 3-4 | Analyze metrics, collect teacher/student feedback |
| **First iteration** | Week 5-6 | Implement top 3 improvements based on data |
| **Ongoing** | Monthly | Continuous monitoring, quarterly deep reviews |

Document:
- What specific data will be collected
- Who reviews the data and when
- What thresholds trigger design changes
- How changes will be tested (A/B when possible)

---

## Quality Checklist (Final Verification)

Before delivering any design, verify every item passes:

- [ ] Every interaction has a clear pedagogical purpose tied to a TN standard
- [ ] Interaction patterns are matched to the cognitive demand (not chosen for novelty)
- [ ] Experience map includes decision points, branching, and an intentional emotional arc
- [ ] Content is chunked into 5-10 minute segments
- [ ] Mayer's multimedia principles are followed
- [ ] Feedback is immediate, elaborative, and growth-oriented
- [ ] Gamification elements serve learning goals, not just engagement
- [ ] Learner has meaningful choices and agency
- [ ] Spaced review is placed in the experience (interval math → spaced-repetition-engine)
- [ ] UDL intent addressed across all three principles (audit → udl-cast-expert)
- [ ] Accessibility intent specified per interaction (formal audit → accessibility-qc-agent)
- [ ] Design is data-informed with clear success metrics and an iteration plan
- [ ] Multiple learner personas were considered
- [ ] Mobile-responsive design is specified
- [ ] Tennessee-specific connections are included where relevant
