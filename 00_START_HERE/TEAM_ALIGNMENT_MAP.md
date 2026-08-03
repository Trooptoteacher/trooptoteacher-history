# TEAM Alignment Map — History Hack ⇄ TEAM General Educator Rubric

> **Don't just learn history. Hack it.**
> _The curriculum that was built for results, not revenue._
> **Mission over margin.**

_Canonical mapping of the **Tennessee Educator Acceleration Model (TEAM) General Educator Rubric**
to History Hack lesson elements. This is what powers the lesson-plan builder's TEAM feature: when a
teacher assembles a lesson, the builder shows and prints the **TEAM observation evidence** that lesson
generates. The rubric itself is a public TDOE instrument; stored here is the **derived alignment**,
not the rubric text. The builder's machine-readable copy lives in the web app at
`lib/lesson-package/team-alignment.ts` — keep the two in sync._

## The rubric, in one line
Three domains; every indicator scored **5 (Significantly Above) · 3 (At) · 1 (Significantly Below)
Expectations**. History Hack is designed so a teacher running the lesson **naturally produces evidence
for the Instruction and Planning indicators** — the builder makes that evidence explicit and printable.

## Instruction domain — the seven-activity lesson maps almost one-to-one
| TEAM indicator | History Hack evidence |
|---|---|
| **Standards & Objectives** | Warm-Up "Set Your Goal" (I-CAN) tied to the TN standard; objectives referenced throughout. |
| **Motivating Students** | The **Hook** (engagement opener); content made relevant. |
| **Presenting Instructional Content** | **Cornell Notes** direct instruction + the **teacher deck** — visuals, modeling, logical sequencing, internal summaries. |
| **Lesson Structure & Pacing** | The **seven-activity cycle** + the timing table (46 / 43 / 41-min blocks) — coherent beginning/middle/end, prompt start, protected Exit Ticket. |
| **Activities & Materials** | The **seven activities** + UDL/MTSS supports — varied, aligned to objectives, appropriately challenging. |
| **Questioning** | **Close Read** text-dependent questions · **HIPPO** source prompts · **DOK-leveled Practice Quiz**. |
| **Academic Feedback** | The **CER loop** — write → self-grade on the rubric → real-time app feedback → revise. |
| **Grouping Students** | Teacher-directed; the plan documents grouping choices (teacher keeps power). |
| **Teacher Content Knowledge** | Historian-verified content + teacher keys and how-to-use guide. |
| **Teacher Knowledge of Students** | Five-band differentiation + UDL 3.0 + WIDA + IEP/504 supports selected per class. |
| **Thinking** | HIPPO analysis + CER reasoning — students generate and defend ideas (DOK 3–4). |
| **Problem-Solving** | Primary-source/data reasoning and constructed response. |

## Planning domain
| TEAM indicator | History Hack evidence |
|---|---|
| **Instructional Plans** | The **generated lesson plan** itself — objectives, standards, sequence, timing, supports, TEAM evidence. |
| **Student Work** | Workbook activities requiring organization/interpretation/analysis (CER, HIPPO, Close Read). |
| **Assessment** | Formative checks + the **5,041-item IRT-parameterized bank** with per-standard mastery + remediation. |

## Environment domain (context, not auto-evidenced)
Expectations · Managing Student Behavior · Environment · Respectful Culture are about the *room*, not
the materials — the builder surfaces them as **teacher-completed** fields on the plan (the product
supports high expectations via the firm-goal UDL framing, but the observation evidence is the
teacher's, not the materials').

## How the builder uses this
1. The teacher selects activities/segments for the lesson.
2. The builder computes the **union of TEAM indicators** those selections evidence (this map).
3. The preview + printed plan show a **"TEAM Observation Evidence"** panel: *"This lesson provides
   evidence for: Standards & Objectives, Presenting Instructional Content, Questioning, Academic
   Feedback, Thinking …"* — so a teacher walks into a TEAM observation with the evidence documented.
4. Environment-domain and Grouping fields stay **teacher-completed** — the tool never fabricates
   evidence for what only the observer can see. Teacher keeps complete power.

_This is the differentiator: no competitor pre-aligns a printable lesson plan to the TN teacher-
evaluation rubric. It makes the builder valuable to every TN teacher who is observed on TEAM._
