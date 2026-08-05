---
name: spaced-repetition-engine
description: >-
  Research-backed spaced repetition and adaptive spiral review engine for K-12 edtech.
  Designs and implements SM-2/Leitner-hybrid scheduling algorithms, per-student per-standard
  forgetting curve tracking, interleaved retrieval practice, teacher pacing controls,
  and transparent selection logic. Use when building or improving spiral review, daily
  review, retrieval practice, spaced repetition, adaptive quiz scheduling, or any
  review system that should follow evidence-based spacing intervals. Applies Ebbinghaus
  forgetting curve, Rosenshine's Principles 1 and 10, Cepeda optimal gap research,
  Roediger & Karpicke testing effect, interleaving research, and Hattie/Shute formative
  feedback guidelines. For History Hack / TroopToTeacher Technologies K-12 U.S. History platform.
metadata:
  author: TroopToTeacher Technologies
  version: '1.0'
  domain: K-12 EdTech
  platform: History Hack
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, or QC ANY artifact —
> workbook, teacher/student slide deck, graphic organizer, poster, DBQ, assessment or test, worksheet, comic,
> web page, or anything else — from memory, a cached copy, or a prior session. **Re-read the CURRENT version of
> THIS skill from `main` first** — skills are the single source of truth and change only via skills-only PRs.
> Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix, and never read from or write to the protected `us-history` flagship
> on a non-US build. If you cannot confirm you are on the current skill, **STOP and pull it first.**

# Spaced Repetition Engine

## When to Use This Skill

Use this skill when the user asks to:

- Build, improve, or audit a spiral review or daily review feature
- Implement spaced repetition scheduling in an edtech platform
- Design adaptive retrieval practice that adjusts to student performance
- Add teacher pacing controls to a review system
- Make review item selection transparent and explainable
- Expand a question pool for spaced practice
- Track per-student mastery and forgetting curves
- Align a review system to evidence-based research (Ebbinghaus, Rosenshine, SM-2, Leitner)

## Core Research Foundation

Read `references/research-citations.md` for full citations with DOIs, effect sizes, and application guidance. The engine is grounded in these six pillars:

### Pillar 1: The Testing Effect (Retrieval Practice)
Actively recalling information produces stronger long-term retention than passive re-study.
- Roediger & Butler (2011): *d* = 0.50–0.80
- Roediger & Karpicke (2006): Retrieval practice outperformed re-reading by 80% on delayed tests
- **Design rule**: Every review interaction must require active recall (select answer, type response) — never passive display

### Pillar 2: Spaced Repetition (Expanding Intervals)
Distributing review over increasing intervals combats the forgetting curve far more effectively than massed practice.
- Ebbinghaus (1885): 150–200% savings in relearning time with spacing
- Cepeda et al. (2006): *d* = 0.40–0.90, benefit increases with retention interval
- Pashler et al. (2007): Optimal gap depends on target retention date — "review soon, but not too soon"
- **Design rule**: Intervals must expand after each successful recall (1→3→7→14→30 days baseline)

### Pillar 3: Interleaving
Mixing topics within review sessions produces superior transfer and discrimination ability.
- Rohrer & Taylor (2007): 25 percentage-point advantage at 1-week delay (*d* ≈ 0.79)
- Kornell & Bjork (2008): Interleaving improves category/pattern recognition (*d* ≈ 0.70)
- **Design rule**: Never serve 3 questions from the same unit in one session — always interleave across units/standards

### Pillar 4: Rosenshine's Principles of Instruction
- Principle 1 — **Daily Review**: Begin every session with review of prior learning to activate working memory
- Principle 10 — **Weekly and Monthly Review**: Cumulative review at expanding intervals to consolidate long-term memory
- **Design rule**: Daily review (3 questions), weekly review (5–7 questions covering older material), monthly cumulative check (optional)

### Pillar 5: Formative Feedback
- Hattie & Timperley (2007): Feedback *d* = 0.73 — but only when process-level and specific
- Shute (2008): Elaborated feedback > verification-only; immediate for factual recall, delayed for transfer
- **Design rule**: Every response gets elaborated feedback (why the answer is correct, the historical reasoning), not just right/wrong

### Pillar 6: Adaptive Difficulty (Desirable Difficulty)
- Bjork (1994): Learning is optimized at ~80% success rate — challenging enough to strengthen memory, not so hard it causes frustration
- Rosenshine (2012): Target ~80% success during guided practice
- **Design rule**: Track per-student success rate; if consistently >90%, increase DOK level or introduce less-reviewed standards; if <60%, drop back to more recently reviewed or lower-DOK items

## Algorithm Specification

### SM-2 / Leitner Hybrid

The engine uses a modified SM-2 algorithm (SuperMemo 2) combined with Leitner box logic for simplicity in a localStorage environment:

```
For each (student, standard) pair, track:
{
  standardId: string,           // e.g., "US.03"
  box: number,                  // Leitner box 1-5 (determines interval)
  ease: number,                 // SM-2 ease factor, starts at 2.5
  lastReviewed: ISO timestamp,  // when last answered
  nextDue: ISO timestamp,       // when next review is scheduled
  correctStreak: number,        // consecutive correct answers
  totalAttempts: number,        // lifetime attempts on this standard
  totalCorrect: number,         // lifetime correct on this standard
  lastQuestionId: string        // avoid immediate repeats
}
```

### Interval Schedule (Leitner Boxes)

| Box | Base Interval | Description |
|-----|---------------|-------------|
| 1   | 1 day         | New or recently missed — review tomorrow |
| 2   | 3 days        | One successful recall — short spacing |
| 3   | 7 days        | Two consecutive successes — weekly review |
| 4   | 14 days       | Solid recall — biweekly |
| 5   | 30 days       | Mastered — monthly maintenance |

### Promotion / Demotion Rules

- **Correct answer**: Move up one box (max box 5). Multiply interval by ease factor.
- **Incorrect answer**: Move back to box 1. Reset ease factor by -0.2 (minimum 1.3).
- **Ease factor adjustment** (SM-2 style):
  - Correct on first try: `ease = max(1.3, ease + 0.1)`
  - Correct after hesitation (>15s response time, if trackable): `ease = ease` (no change)
  - Incorrect: `ease = max(1.3, ease - 0.2)`

### Daily Question Selection Algorithm

```
function selectDailyReview(studentData, questionPool, count = 3):
  1. Filter questionPool to standards from units student has studied
  2. Compute priority score for each standard:
     - overdueScore = max(0, daysSince(nextDue)) / baseInterval
     - If overdue: priority = overdueScore * 10  (urgent)
     - If due today: priority = 5
     - If not yet due: priority = 0.1
     - Boost: standards with <70% accuracy get +3 priority
     - Boost: standards not seen in 14+ days get +2 priority
  3. Sort standards by priority (descending), break ties randomly
  4. Select top N standards, ensuring:
     - No two questions from same unit (interleaving rule)
     - Don't repeat lastQuestionId for that standard
  5. For each selected standard, pick a question:
     - Prefer questions not recently shown (use questionHistory)
     - Match difficulty to student performance (if accuracy >85%, pick DOK 2-3; if <60%, pick DOK 1)
  6. Return selected questions with metadata for transparency display
```

### New Student Bootstrap

Students with no review history start with:
- All standards from Unit 1 placed in Box 1 (due immediately)
- As the student progresses through units, new standards enter Box 1
- First session shows 3 questions from studied content, cycling through available standards

## Teacher Pacing Controls

Teachers MUST be able to configure:

### 1. Active Units Scope
```typescript
interface TeacherPacingConfig {
  activeUnits: number[];        // Which units are "in scope" for review
  // e.g., [1, 2, 3] means only review Units 1-3
  // Default: all units the student has attempted
  
  focusStandards: string[];     // Standards to prioritize (boost +5 priority)
  // e.g., ["US.03", "US.14"] for upcoming test emphasis
  
  excludeStandards: string[];   // Standards to temporarily exclude
  // e.g., ["US.90"] if not yet covered
}
```

### 2. Interval Aggressiveness
```typescript
interface IntervalConfig {
  preset: "intensive" | "standard" | "maintenance";
  // intensive:    intervals halved (0.5, 1.5, 3.5, 7, 15 days) — pre-test cramming
  // standard:     default intervals (1, 3, 7, 14, 30 days)
  // maintenance:  intervals doubled (2, 6, 14, 28, 60 days) — post-unit long-term
  
  dailyCount: number;           // Questions per day: 3 (default), 5, or 7
  weeklyReviewEnabled: boolean; // Enable Friday cumulative review (5-7 items)
}
```

### 3. EOC Exam Alignment Mode
```typescript
interface EOCPrepConfig {
  enabled: boolean;
  examDate: string;             // ISO date of EOC exam
  // When enabled, algorithm shifts to:
  // - Compress all Box 4-5 standards back to Box 3 (force more frequent review)
  // - Weight question selection toward EOC blueprint reporting categories
  // - Increase daily count to 5
  // - Prioritize standards with lowest mastery scores
}
```

### Storage
Teacher config stored in localStorage under `teacherPacingConfig`. Default config applied if none set. Config UI in Teacher Tools section.

## Transparency Requirements

### For Students
Each spiral review question MUST display (after answering):
- "Why this question?" tooltip/badge showing:
  - "Last reviewed: [X days ago]"
  - "Your accuracy on this standard: [X]%"
  - "Next review scheduled: [date]" (after answering)
- Mastery progress bar per standard (Box 1-5 visualization)

### For Teachers
Teacher Tools dashboard MUST show:
- Class-level heatmap: standards × students showing mastery levels (Box 1-5 colors)
- "At risk" standards: any standard where >30% of class is in Box 1-2
- Review schedule forecast: what standards are coming due this week for the class
- Individual student drill-down: full review history with accuracy trends

### For Administrators/Reviewers (Accreditation Transparency)
Document in-app or in docs:
- Algorithm description (this skill document serves as the source)
- Research citations justifying each design decision
- How intervals were chosen and what research supports them
- That teacher override capability exists

## Question Pool Requirements

### Minimum Pool Size
For genuine spaced repetition to work without excessive repetition:
- **Minimum**: 5 questions per standard (allows variety across review cycles)
- **Target**: 8-10 questions per standard
- **Current state**: 30 total (3 per unit) — INSUFFICIENT for true spaced repetition
- **Required expansion**: Scale to 150-300 items covering all TN standards US.01-US.95

### Question Metadata
Every question in the pool must have:
```typescript
interface SpiralQuestion {
  id: string;
  standardId: string;           // TN standard (e.g., "US.03")
  unitNum: number;
  dok: 1 | 2 | 3;              // Webb's Depth of Knowledge
  stem: string;
  stemEs: string;
  choices: { id: string; text: string; textEs: string }[];
  correctId: string;
  feedback: string;             // Elaborated feedback (WHY, not just WHAT)
  feedbackEs: string;
  distractorFeedback?: Record<string, string>;  // Per-distractor misconception feedback
  distractorFeedbackEs?: Record<string, string>;
  tags: string[];               // e.g., ["economic", "cause-effect", "primary-source"]
}
```

## Implementation Architecture (History Hack Web App)

### File Structure
```
lib/
  spaced-repetition/
    engine.ts            — Core SR algorithm (box promotion/demotion, interval calc, selection)
    types.ts             — TypeScript interfaces for SR state, config, questions
    storage.ts           — localStorage read/write for student SR state
    teacher-config.ts    — Teacher pacing config read/write
    transparency.ts      — Helper functions for "why this question" display data
    
data/
  spiral-questions/
    unit1.ts through unit10.ts  — Expanded question pools per unit (8-10 per standard)
    index.ts                     — Aggregates and exports full pool
    
app/
  dashboard/
    spiral-review-section.tsx    — Refactored spiral review UI component
  teacher-tools/
    spiral-config/
      page.tsx                   — Teacher pacing control UI
    spiral-analytics/
      page.tsx                   — Class mastery heatmap and analytics
```

### localStorage Keys
```
sr_state_{standardId}    — Per-standard review state (box, ease, timestamps)
sr_history               — Array of last 100 review attempts (for analytics)
sr_teacher_config        — Teacher pacing configuration
sr_daily_session         — Today's date + questions served (prevent re-serving on refresh)
```

### Migration from Current System
The current `getSpiralQuestions()` in `lib/spiral-review-data.ts` must be replaced:
1. Keep the existing 30 questions as seed data
2. Add new questions to reach minimum pool size
3. Replace the day-of-year random selection with the SR engine
4. Migrate the dashboard `SpiralReview` component to use the new engine
5. The old `spiral-review-data.ts` file can be deprecated after migration

## Quality Checks

Before any implementation is considered complete, verify:

- [ ] Intervals follow the Leitner box schedule (1, 3, 7, 14, 30 days)
- [ ] Incorrect answers always demote to Box 1
- [ ] Questions from the same unit never appear consecutively in a session (interleaving)
- [ ] Every question shows elaborated feedback after answering
- [ ] Student can see "why this question" transparency data
- [ ] Teacher can configure active units, focus standards, and interval preset
- [ ] New students get a reasonable bootstrap experience (not empty state)
- [ ] localStorage state persists across sessions
- [ ] Daily session is stable (refreshing page doesn't change the 3 questions)
- [ ] Question pool has sufficient variety to avoid repetition within a 2-week cycle
- [ ] Spanish translations exist for all new questions, feedback, and UI labels
- [ ] Accessibility: all new UI elements have proper ARIA labels, keyboard navigation
