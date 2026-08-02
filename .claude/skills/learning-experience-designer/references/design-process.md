# Design Process — Full Reference

Follow these six steps for every learning experience design. This is the authoritative process reference.

---

## Step 1: Learner Analysis

Before designing anything, answer these questions:

### Target Learners
- What grade level? (History Hack targets high school U.S. History)
- What is the expected reading level range?
- What prior knowledge can be assumed?
- What accessibility needs must be planned for?

### Standards Alignment
- Which TN U.S. History standards (US.01-US.95) does this experience target?
- Which History Hack unit does this belong to?
- What is the EOC blueprint weight for this reporting category?

### Prerequisites
- What concepts/skills must students already have?
- How will you verify prerequisite knowledge (pre-assessment, checkpoint)?

### Common Misconceptions
- What are documented misconceptions for this topic?
- How will the experience surface and address misconceptions?
- What distractor patterns from the question bank apply here?

---

## Step 2: Experience Mapping

Map the full learner journey before designing individual interactions.

### Journey Map Template

```
[Entry Point] → [Hook/Activation] → [Core Learning Segment 1]
    ↓                                        ↓
[Scaffold Check]                    [Practice Activity]
    ↓                                        ↓
[Branch: Needs Support] ←→ [Branch: Ready to Advance]
    ↓                                        ↓
[Remediation Path]              [Core Learning Segment 2]
    ↓                                        ↓
[Rejoin Main Path]              [Application Activity]
    ↓                                        ↓
[Mastery Assessment] → [Reflection/Summary] → [Next Experience Preview]
```

### Key Design Elements

**Decision Points:** Where does the learner or system decide what happens next? Examples:
- Pre-assessment determines starting point
- Practice results trigger scaffolding or advancement
- Learner chooses exploration path

**Feedback Loops:** Where does the learner receive information about their progress?
- After each practice item (immediate feedback)
- After completing a segment (summary feedback)
- At mastery checkpoints (growth-oriented progress report)

**Branching Paths:** What alternative routes exist?
- Remediation path for students who need more support
- Extension path for students who demonstrate early mastery
- Alternative modality paths (read vs. watch vs. listen)

**Scaffolding Entry/Exit:** When do supports activate and deactivate?
- Vocabulary support appears on hover/tap for identified terms
- Hints become available after first unsuccessful attempt
- Scaffolds fade as student demonstrates mastery

**Spaced Review Placement:** Where in the journey does interleaved review of prior standards appear? Design the placement here; **defer the interval algorithm and scheduling math to spaced-repetition-engine.**

### Emotional Arc

Design the emotional journey intentionally:

1. **Curiosity** — Hook sparks a question or presents a mystery
2. **Challenge** — Core content introduces complexity; productive struggle
3. **Discovery** — Learner makes connections, builds understanding
4. **Mastery** — Successful application demonstrates competence
5. **Reflection** — Learner recognizes growth and connects to bigger picture

---

## Step 3: Interaction Design

Select interaction patterns that match the cognitive demand of the learning goal. Never choose an interaction pattern for novelty alone — it must serve the learning objective. This is the core, distinctive job of this skill.

### Interaction Pattern Reference

| Interaction Type | Best For | Example Use |
|---|---|---|
| **Drag-and-drop** | Categorization, sequencing, sorting | Sorting events into chronological order; categorizing causes vs. effects |
| **Timeline** | Chronological reasoning, periodization | Placing events on an interactive timeline; comparing parallel developments |
| **Map interaction** | Geographic/spatial understanding | Identifying regions affected by an event; tracing migration patterns |
| **Document analysis frame** | Primary source work, sourcing, corroboration | Analyzing a political cartoon with guided questions; comparing two source accounts |
| **Debate/perspective-taking** | Multiple viewpoints, argumentation | Taking a historical figure's position; evaluating competing interpretations |
| **Flashcard/spaced repetition** | Factual recall, vocabulary | Key terms, dates, figures; spaced review of previously learned content |
| **Simulation** | Cause-and-effect reasoning, decision-making | Making decisions as a historical actor; modeling economic or political systems |
| **Annotation** | Close reading, evidence identification | Highlighting claims and evidence in a text; marking features of a document |
| **Matching** | Associations, definitions, connections | Matching terms to definitions; connecting causes to effects |
| **Constructed response** | Explanation, argumentation, synthesis | Short-answer analysis; evidence-based claim writing |

### Interaction Design Checklist

For each interaction, document:

- [ ] **Learning objective:** What specific skill or knowledge does this interaction build?
- [ ] **TN standard:** Which standard(s) does this target?
- [ ] **Cognitive demand:** What DOK/Bloom's level is required?
- [ ] **Instructions:** Are directions clear, concise, and visible?
- [ ] **Feedback:** What happens when the learner responds (correctly and incorrectly)?
- [ ] **Accessibility intent:** Can this interaction be completed via keyboard, screen reader, and touch? (Formal audit → accessibility-qc-agent.)
- [ ] **Mobile:** Does this interaction work on mobile screens?
- [ ] **Time estimate:** How long should this interaction take?

---

## Step 4: Feedback Design

Feedback is one of the most impactful elements of a learning experience. Design it intentionally.

### Feedback Types

| Type | When | What | Example |
|---|---|---|---|
| **Immediate** | After each response | Right/wrong + brief explanation | "Correct! The 14th Amendment did establish birthright citizenship." |
| **Elaborative** | After each response | WHY the answer is right/wrong | "Not quite. While the Freedmen's Bureau did provide education, it was the 14th Amendment that established citizenship rights." |
| **Progressive hints** | After incorrect attempts | Nudge → Clue → Full explanation | Attempt 1: "Think about which Reconstruction amendment addressed citizenship." → Attempt 2: "It was ratified in 1868." → Attempt 3: Full explanation |
| **Summary** | After completing a segment | Performance overview | "You mastered 4/5 objectives in this section. Review: distinguishing Reconstruction amendments." |
| **Mastery** | At checkpoints | Progress toward standard mastery | "You've improved from 60% to 80% on standard US.14. Two more practice sets to reach mastery." |
| **Growth-oriented** | Always | Emphasize progress and effort | "Great persistence! You've attempted this 3 times and improved each time." |

### Feedback Language Guidelines

- Use conversational, encouraging tone
- Reference specific content, not generic praise ("You correctly identified the cause" not "Good job!")
- Frame errors as learning opportunities ("Not yet — here's a clue" not "Wrong")
- Show progress over time when possible
- Avoid language that attributes success/failure to fixed traits

---

## Step 5: Inclusive-Design Check (UDL)

Design inclusively from the start: provide multiple means of Engagement, Representation, and Action & Expression, and confirm no learning goal depends on a single modality. Document your UDL *intent* for each of the three principles as part of the design.

**Route the formal UDL 3.0 / CAST audit to udl-cast-expert.** Do not restate the CAST framework or run the full checkpoint matrix here — this skill specifies inclusive-design intent; udl-cast-expert owns the audit and CAST alignment.

Minimum bar before handoff:

- At least ONE genuine alternative is provided for each of the 3 principles
- No principle is completely unaddressed
- The design does not rely exclusively on a single modality

---

## Step 6: Accessibility Intent

Specify accessibility *intent* for every interaction so the design is accessible-by-construction:

- Keyboard operability (Tab / Enter / Escape / Arrow keys), no keyboard traps
- Screen reader support (heading hierarchy, ARIA labels, live regions)
- Sufficient color contrast and no color-only meaning
- Touch targets sized for mobile
- Captions/transcripts for any audio or video
- Respects `prefers-reduced-motion`; no excessive flashing

**Route the formal accessibility audit to accessibility-qc-agent**, which enforces WCAG 2.2 AA, Section 508, and ADA Title II as the sources of truth. This skill states intent; accessibility-qc-agent is the terminal audit gate.
