# Product Model Doctrine — Print-First, SAMR-Driven, Workbook⇄App Flow

> **Don't just learn history. Hack it.**
> _The curriculum that was built to make a difference, not to make money._
> **Mission over margin.**

_Archived product-model decision (owner: Sean / TroopToTeacher). This is the standing answer to
"what is the product, and how does the web platform relate to it?" Read it before designing any
web feature, unit flow, or app screen. When a design question is about **where** something lives —
page or screen — this document settles it. Doctrine + intent here; build detail lives in
`BUILD_STANDARD.md` and the skills._

---

## 1. The one decision: the district is going print-first

The product is a **print product.** Everything is designed for print first: the student workbook is
the spine of the course, and the lesson lives on the page. This is not a compromise or a fallback —
it is the deliberate model the district is adopting. A teacher can run the entire course with the
printed workbook and deck and lose nothing essential.

**Technology is used only when it enhances** — never as decoration, never as a substitute for the
page, never "because it's an app." If a digital feature does not make the learning measurably better
than the paper version of the same moment, it does not ship into the flow.

**The technology-value rule (LOCKED):** _All technology must exclusively bring value — and prove it
with evidence. Print first. High-value technology only. Every function has a purpose; every purpose
is high value; and it is used only if it cannot be done in print. We provide supports where supports
are necessary or needed — never as decoration._ The three-question test that enforces this (can it be
done in print? · what's the value + evidence? · which framework does it serve?) lives in
`FRAMEWORKS_CANON.md` §2.

## 2. Two questions per digital touch — inside the workbook flow

Every place technology enters the lesson answers **two separate questions**, and it must do so
**within the workbook flow** — the workbook sequence is the organizing structure; the app augments
specific moments in it, it does not replace or run alongside a separate "digital course."

**Q1 — What *kind* of integration is this? (descriptor, not proof): SAMR + TPACK.**
SAMR (Puentedura) names the transformation rung — Substitution → Augmentation → Modification →
Redefinition; TPACK (Mishra & Koehler) confirms the technology, pedagogy, and content actually fit
at that spot. **This is descriptive only.** SAMR tells us the *shape* of the integration; it does
**not** prove the feature teaches better. A "Redefinition" feature can still be low-impact. So SAMR
is never our quality bar — it is context.

**Q2 — Does it *prove learning impact*? (the actual value bar): the Educational-Impact Gate.**
This is the bar that matters. A digital function ships only if it clears **both** parts:

1. **Named high-impact strategy + effect size.** The feature must map to a research-validated
   instructional strategy at or above Hattie's hinge point (**d ≈ 0.40**), and preferably well
   above — e.g. **feedback** (d ≈ 0.70), **formative assessment / classroom evaluation**,
   **retrieval practice / spaced repetition** (the testing effect), **concept mapping / graphic
   organizers** (Venn diagrams, d ≈ 0.60). Sources of truth: **Hattie, *Visible Learning***;
   **Rosenshine's Principles of Instruction**; **Marzano's high-yield strategies**; **Black &
   Wiliam** (formative); **Roediger & Karpicke** (retrieval practice).
2. **Print cannot deliver that same benefit.** The strategy's payoff must depend on something paper
   physically can't do — real-time feedback, adaptive spacing, parallel analytics, per-student
   mastery routing, audio access. If print delivers the strategy just as well, it stays on paper.

**Rule of thumb:** if you can't name the high-impact strategy, its effect size, and the reason print
can't match it, the paper version wins. SAMR/TPACK describe the move; the Educational-Impact Gate
proves it earns a screen. Full three-question enforcement test: `FRAMEWORKS_CANON.md` §2.

## 3. What the web platform is for — the value pieces

The web platform is the **amplifier**, not the course. Its value is a small set of things paper
genuinely cannot do:

1. **Testing platform for parallel test-data analytics** — assessment delivery that yields
   comparable, cross-section data (item-, standard-, and cohort-level).
2. **Real-time standard mastery** — live per-student, per-standard mastery (US.01–US.95), not an
   end-of-unit guess.
3. **Reteaching** — targeted reteach surfaced from mastery data (spiral/adaptive review).
4. **Lesson-plan builder** — teacher-side planning that assembles from the same standards spine.
5. **Gamification and read-aloud** — engagement mechanics and audio access (read-aloud is also a
   UDL/MTSS/WIDA access lever, not just engagement).

Anything proposed for the web app should map to one of these five. If it doesn't, question whether
it belongs on paper instead.

## 4. The flow: workbook ⇄ app, handing off multiple times per lesson

The lesson is not "paper, then screen." The student moves **between the workbook and the app several
times within a single lesson**, each handoff chosen because it enhances that specific moment.

**Canonical example — the CER loop:**

1. In the **workbook**, the student writes a **CER** (Claim–Evidence–Reasoning) by hand.
2. Still in the **workbook**, the student **self-grades** it against their printed **rubric**.
3. The student **inputs it into the app** and gets **real-time feedback**.
4. Feedback sends them back to the page to revise.

In one loop the student is **reading, writing, self-assessing, and getting real-time feedback** —
the writing and metacognition happen on paper (where they're strongest), and the app adds the one
thing paper can't: immediate, standard-aligned feedback and a data trail. That handoff pattern —
**page → app → page** — is the shape every unit's flow should take.

## 5. What this means for builders

- **Design the workbook first.** The printed spine is the source of truth; the app keys to it, the
  way the decks key to the workbook. Never design an app screen that has no home on the page.
- **Every app screen names its workbook moment.** A feature should reference the exact workbook
  activity it hands off from and back to (like the CER loop above).
- **Justify every digital touch on SAMR.** State the rung and the functional benefit in the spec.
- **Keep the five value pieces central.** Analytics, real-time mastery, reteach, lesson-plan
  builder, gamification + read-aloud — these are the platform. Feature creep outside them is a
  paper question in disguise.
- **The page must stand alone.** A classroom with no working devices still runs the full lesson.
  The app raises the ceiling; it never lowers the floor.

---

_This doctrine sits under the Adoption Standard (`ADOPTION_STANDARD.md`) and feeds the Build
Standard (`BUILD_STANDARD.md`). Where this and a build guardrail appear to conflict, the decision
rule in `ADOPTION_STANDARD.md` governs: 100% alignment · TDOE Schedule F · best path to adoption._
