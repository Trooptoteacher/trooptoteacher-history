# Foundational Frameworks — Full Reference

Read this file when you need detailed guidance on any of the foundational frameworks this skill owns. This is the authoritative reference for applying each to History Hack interactive learning experience designs.

**Re-homed frameworks (do not duplicate here):**
- **UDL 3.0 / CAST** — apply inclusively, but route depth and audits to **udl-cast-expert**.
- **Accessibility (WCAG 2.2 AA / Section 508 / ADA)** — specify intent per interaction, but route the formal audit to **accessibility-qc-agent**.
- **Spaced-review interval math** — place spaced review in the experience, but route the scheduling algorithm to **spaced-repetition-engine**.

---

## 1. Human-Centered Design Thinking (IDEO/Stanford d.school)

Apply the 5-stage process for every new learning experience:

### Stage 1: Empathize

Create and consider these learner personas:

- **Struggling reader** — Below grade-level reading; needs simplified text, audio support, visual aids
- **Advanced learner** — Seeking depth and challenge; needs extension activities, primary source analysis
- **English Language Learner (ELL)** — Needs vocabulary support, visual context, bilingual glossaries
- **Student with IEP** — Specific accommodations (extended time, text-to-speech, simplified assessments)
- **Neurotypical learner** — Standard pathway; benefits from variety and engagement
- **Neurodiverse learner** — May need reduced visual clutter, predictable navigation, sensory considerations

Also consider teacher personas:

- **Tech-comfortable teacher** — Wants data dashboards, customization options, LMS integration
- **Tech-hesitant teacher** — Needs simple setup, clear guides, minimal configuration
- **Standards-focused teacher** — Wants explicit standards alignment, pacing guides, EOC prep tools

### Stage 2: Define

Frame clear problem statements from the learner perspective:

> "[Persona] needs [need] because [insight]."

Example: "A struggling reader needs audio-supported vocabulary previews because encountering unfamiliar terms in dense historical text causes cognitive overload and disengagement."

### Stage 3: Ideate

- Generate multiple solutions before converging on one
- Use "How Might We" (HMW) questions to reframe challenges
- Example: "HMW help ELL students engage with primary source documents without being blocked by archaic language?"

### Stage 4: Prototype

- Start low-fidelity: wireframes, storyboards, paper prototypes
- Then move to digital mockups
- Test the concept before investing in full development

### Stage 5: Test

- Usability testing with actual learners when possible
- Iterate based on data and observation, not assumptions
- Collect both quantitative metrics and qualitative feedback

---

## 2. Gamification & Engagement Psychology

Based on Self-Determination Theory (Deci & Ryan) and Flow Theory (Csikszentmihalyi).

### Core Psychological Needs

- **Autonomy:** Give learners meaningful choices — path selection, topic exploration order, expression format. Choice must be genuine, not cosmetic.
- **Competence:** Progressive difficulty with clear feedback. Mastery-based progression, not time-based. Learners should feel capable and growing.
- **Relatedness:** Social features — collaborative challenges, peer discussion, shared achievements. Learners should feel connected.

### Gamification Elements (Use Purposefully)

| Element | How to Use Well | How NOT to Use |
|---|---|---|
| **Points/XP** | Tied to learning behaviors: completing practice, reviewing errors, helping peers | Awarded only for correct answers |
| **Badges/Achievements** | Milestone-based, recognizing growth and effort | Performance-only rewards |
| **Leaderboards** | Optional; emphasize personal growth; use cooperative boards | Mandatory ranked competition |
| **Streaks** | Encourage consistent practice habits; forgive occasional misses | Punitive streak-breaking |
| **Narrative/Quests** | Embed learning in historical narrative; "mission" framing for units | Superficial story wrapper |
| **Progress Bars** | Visual mastery progress per standard | Vague or meaningless meters |

### Key Principle

Every gamification element must serve a learning goal. If removing a game element would not affect learning, it is decorative — reconsider or remove it.

---

## 3. Microlearning & Chunking Research

### Core Rules

- Chunk content into **5-10 minute** learning segments maximum
- Each microlesson has **ONE clear learning objective**
- Apply **Miller's 7±2 rule**: limit new information elements per screen/interaction to 5-9 items
- Content blocks should be searchable, modular, and reusable

### Microlesson Sequence

| Phase | Duration | Purpose |
|---|---|---|
| **Hook** | ~30 seconds | Capture attention with a question, surprising fact, or visual |
| **Core Content** | 3-5 minutes | Deliver the main concept with multimedia support |
| **Practice** | 2-3 minutes | Active recall, application, or assessment |
| **Reflection** | ~1 minute | Self-assessment, connection to prior knowledge, or preview of next topic |

### Just-in-Time Learning

Support on-demand access: students should be able to search for and access any content block independently, not only through a linear sequence.

---

## 4. Mayer's 12 Multimedia Learning Principles

Apply all 12 principles when designing any multimedia content:

| # | Principle | Guideline |
|---|---|---|
| 1 | **Coherence** | Remove extraneous material — every element must support the learning goal |
| 2 | **Signaling** | Use cues to highlight essential material (headings, bold, color, arrows) |
| 3 | **Redundancy** | Don't add on-screen text to narrated graphics (narration + graphics only) |
| 4 | **Spatial Contiguity** | Place text near corresponding graphics on the same screen |
| 5 | **Temporal Contiguity** | Present narration and graphics simultaneously, not sequentially |
| 6 | **Segmenting** | Break complex lessons into learner-paced segments with continue buttons |
| 7 | **Pre-training** | Teach key vocabulary and concepts before the main lesson |
| 8 | **Modality** | Use spoken narration rather than on-screen text with graphics |
| 9 | **Multimedia** | Use words AND pictures together, not words alone |
| 10 | **Personalization** | Use conversational tone ("you," "let's"), not formal academic register |
| 11 | **Voice** | Use human voice for narration, not machine-generated |
| 12 | **Image** | Speaker's image on screen is not necessarily better — use only if it adds value |

---

## 5. Data-Driven Iteration

### Success Metrics (define for every experience)

| Metric | What It Measures | Target Benchmark |
|---|---|---|
| **Completion rate** | Did students finish the experience? | ≥ 85% |
| **Assessment scores** | Did students learn the targeted content? | ≥ 70% mastery |
| **Time-on-task** | Is the experience appropriately scoped? | Within ±20% of expected duration |
| **Retry rate** | Are students persisting through challenges? | Healthy: 1-3 retries; concerning: 0 or 5+ |
| **Engagement duration** | How long do students stay actively engaged? | ≥ 80% of session time |
| **Drop-off points** | Where do students abandon the experience? | Identify and address any step with >15% drop-off |

### Data Collection Methods

- **xAPI/LRS** — Track granular learning events (started, completed, answered, scored, experienced)
- **A/B testing** — Test design variations with controlled groups when sample size allows
- **Heatmaps/clickmaps** — Identify interaction patterns and confusion points
- **Student surveys** — Collect qualitative feedback on experience quality
- **Teacher observations** — Gather classroom implementation insights

### Iteration Cycle

1. Launch experience with baseline metrics defined
2. Collect data for 2-4 weeks (minimum viable sample)
3. Analyze quantitative metrics + qualitative feedback
4. Identify top 3 improvement opportunities
5. Design and implement changes
6. Measure impact of changes
7. Repeat
