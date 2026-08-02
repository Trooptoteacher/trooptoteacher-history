---
name: history-hack-web-activities
description: "THE product standard for History Hack U.S. History WEB-APP student activities that complement the print unit bundle — the interactive layer that adds variety, instant feedback, practice, and teacher data on top of the printed workbook + decks. Owns three pillars: (1) gamified retrieval practice (term↔definition match, timeline-order, map drag-drop for geography standards, Three-Perspectives sorting), (2) auto-graded formative + summative assessment (per-standard formative from the CFU/exit-ticket bank with instant feedback + reteach; summative from the two parallel Assessment-Book forms with a TCAP-style reporting-category breakdown), and (3) the WRITING LAB for DBQ / CER / HIPP with instant rubric feedback under a LOCKED draft-by-hand-first rule. Use when planning or building web-platform activities, gamification, engagement features, a formative or summative quiz, a writing-feedback tool, or anything that connects a print unit to interactive practice in the history-hack-web-app. Owns the WHAT (the feature set, the flow, and the guardrails) and INVOKES the owner skills for the HOW — `learning-experience-designer` (interactive UX/gamification), `spaced-repetition-engine` (review scheduling), `tn-assessment-specialist` (items + rubrics), `history-hack-website-builder` (the build), `copyright-integrity-accreditation` + `edtech-adoption-specialist` (privacy), `accessibility-qc-agent` (WCAG) — it does not re-implement them."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.0"
  owner_of: "History Hack web-app student-activity feature standard (gamified retrieval, formative/summative delivery, Writing Lab) and how each maps to the print unit"
  build_target: "history-hack-web-app repository"
  companion_to: "history-hack-workbook-print-bundle (print spine) — this is the interactive layer on top of it"
---

# History Hack Web Activities — Interactive Layer Standard

> **Print is the spine; the web is the variety, the instant feedback, and the data.** Every web
> activity is anchored to a real standard, a real item bank, and a real rubric the student already has
> on paper — it never invents parallel content, and it never does the student's thinking for them.

This skill owns the **product decisions and guardrails** for the History Hack web-app student-activity
layer. It **invokes** the owner skills for the how — `learning-experience-designer` (interactive UX +
gamification psychology), `spaced-repetition-engine` (review scheduling), `tn-assessment-specialist`
(items + rubrics), `history-hack-website-builder` (the actual build), `copyright-integrity-accreditation`
+ `edtech-adoption-specialist` (student-data privacy), and `accessibility-qc-agent` (WCAG). It does not
re-implement any of them.

## The print ↔ web model

The printed **workbook + teacher/student decks** carry the teach and the note-taking (see
`history-hack-workbook-print-bundle`). The web layer adds what paper can't: **variety to break the
monotony, instant feedback, spaced practice, and formative data for the teacher.** Every web activity
maps to a specific standard (US.xx) and reuses content that already exists — the question bank, the
Assessment Book forms, and the printed rubrics.

## Pillar 1 — Gamified retrieval practice

Short, replayable games that make *active recall* the fun part, not a worksheet:

- Term ↔ definition match; timeline-ordering; **map drag-drop** (a natural fit for the geography
  standards — e.g. US.50 battles, US.56 Manhattan-Project sites); **Three-Perspectives sorting**
  (Who benefited? / Who bore the costs? / Who decided?).
- **Reward the *doing* of retrieval, not right-answer-only** — light points/streaks/badges for effort
  and completion, so a struggling student still gets reinforced. Gamification supports learning; it
  never becomes the point. Design per `learning-experience-designer`.
- Items and spacing come from `spaced-repetition-engine` (the book seeds; the engine schedules the
  return so vocab and key facts resurface days later).

## Pillar 2 — Auto-graded formative + summative

- **Formative (per standard):** the CFU / exit-ticket items already in the question bank, delivered
  with **instant feedback + a reteach hint** — the digital twin of the workbook's self-grading Practice
  Quiz (Activity 6).
- **Summative (per unit):** the Assessment Book's **two parallel forms (A / B)** as an auto-scored test
  with a **TCAP-style reporting-category breakdown** for the teacher (per-standard mastery, distractor
  routing). Items and psychometrics are owned by `tn-assessment-specialist` — this skill only specifies
  delivery, feedback, and the data view.

## Pillar 3 — The Writing Lab (DBQ / CER / HIPP) — draft-by-hand-first (LOCKED)

Instant, rubric-aligned feedback on student writing — built so it **coaches** authentic writing and
never replaces it.

**The flow:**

1. **Draft on paper first** — in the workbook's ruled CER/HIPP space (Activity 5 HIPP, Activity 7 CER)
   or the DBQ packet. The composing happens in the student's own hand.
2. **Self-score** — the student rates their own draft against the **same rubric printed in the
   workbook**, before the tool sees it.
3. **Type it in → instant feedback** — scored against **that exact rubric** with specific, revise-this
   coaching.
4. **Compare three ways** — *my self-score* vs *the tool's score* vs *the rubric parameters*. This
   comparison builds self-assessment / metacognition (high-leverage per Hattie & Shute).
5. **Revise** (and optionally re-submit).

**LOCKED guardrails:**

- **Draft by hand first.** The tool is a coach, entered *after* the student has written. This is what
  keeps "students actually write" true end to end.
- **The rubric is the authority.** The screen scores against the **same** rubric the workbook prints
  (6-point CER · HIPP for lesson sources · HIPPO for full DBQs) — screen and paper never disagree.
- **Feedback coaches; it never composes.** It points to *where* and *why* against the rubric; it never
  hands the student sentences or rewrites their work.
- **Student writing is student data.** FERPA / COPPA / TN Student Data Act apply — privacy by design,
  not bolted on. Route through `copyright-integrity-accreditation` + `edtech-adoption-specialist`.
- **Accessible by default** — WCAG 2.2 AA, keyboard + screen-reader + text-to-speech; verified by
  `accessibility-qc-agent`.

## Build + QC

- Build in `history-hack-web-app` via `history-hack-website-builder` (project design tokens, brand,
  React/Next stack). Do not fork a new app.
- No feature ships without: correct standard/rubric mapping, the draft-first rule enforced (Writing
  Lab), the privacy review, and the accessibility gate. Content accuracy (Policy 2.600) is
  foundational — the item bank and rubrics are the source of truth; the web layer never invents
  history or parallel rubrics.

## Companion

- `history-hack-workbook-print-bundle` — the print spine this layer sits on top of; each web activity
  names the print activity/standard it complements.
