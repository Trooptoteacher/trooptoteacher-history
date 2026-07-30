# Research Foundations — Annotated Outline & Citation Library
## TroopToTeacher Technologies · Education Research Team

**Load when:** Writing a Research Foundations white paper, building a literature section for a grant or RFP, or verifying that a design-rationale claim is properly grounded and cited.

---

## Purpose of This Document

A "Research Foundations" document for History Hack must accomplish four things simultaneously:

1. Demonstrate that the product design draws on established, peer-reviewed science
2. Accurately represent what the science says (no cherry-picking or overclaiming)
3. Be honest that the cited research is about the underlying pedagogical principles, NOT about History Hack itself
4. Provide enough substance to satisfy a district curriculum director or grant reviewer

The standard to aim for: a curriculum director with a master's degree in education reads this and says "This is honest and solid, not marketing fluff."

---

## Recommended White Paper Structure

```
1. Executive Summary (1 page)
2. Introduction: Why Evidence-Grounded Design Matters
3. The Learning Science Behind History Hack
   3.1 Retrieval Practice and the Testing Effect
   3.2 Spaced Repetition and Distributed Practice
   3.3 Rosenshine's Principles of Instruction
   3.4 Cognitive Load and Instructional Scaffolding
   3.5 Mayer's Multimedia Learning Principles
   3.6 Universal Design for Learning (UDL)
   3.7 Culturally Responsive Pedagogy
4. Design-to-Research Alignment Table
5. Honest Limitations: What This Document Does NOT Claim
6. Logic Model and Evidence Roadmap
7. References (APA 7th)
```

---

## Section 3: Annotated Literature

### 3.1 Retrieval Practice and the Testing Effect

**Core claim (design rationale):** History Hack's question bank activates retrieval practice, one of the most robust and well-replicated learning strategies in cognitive psychology.

**Key studies:**

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249-255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Classic RCT showing retrieval practice produces better long-term retention than restudying
- Effect robust across content areas including fact-based material (relevant to history)

Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4-58. https://doi.org/10.1177/1529100612453266
- Meta-analysis rating 10 learning strategies on utility; practice testing rated **HIGH utility**
- Distributed practice also rated HIGH; elaborative interrogation and self-explanation rated MODERATE
- This is the single most useful citation for claiming retrieval practice is evidence-based

Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. *Review of Educational Research, 87*(3), 659-701.
- Meta-analysis of 272 studies; d = 0.50 average effect of practice testing vs. restudying
- Effect holds across age groups, formats, and retention intervals

**Honest framing in the document:**
> "Extensive research demonstrates that retrieval practice — answering questions from memory — produces stronger long-term retention than passive review (Dunlosky et al., 2013; Roediger & Karpicke, 2006). History Hack is designed to leverage this principle through frequent, low-stakes questions embedded throughout each unit. This is a design-rationale claim; a formal study has not yet evaluated whether History Hack students achieve greater retention gains than peers using other materials."

---

### 3.2 Spaced Repetition and Distributed Practice

**Core claim (design rationale):** History Hack's unit structure distributes practice across multiple sessions rather than concentrating it in single lessons.

**Key studies:**

Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354-380. https://doi.org/10.1037/0033-2909.132.3.354
- Meta-analysis; distributed practice superiority replicates across virtually all verbal learning tasks
- Effect size depends on retention interval; longer gaps require longer spacing

Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585-592.
- Spacing benefits extend to category learning (relevant to conceptual history understanding)

**Caution — do NOT claim:** That History Hack implements an algorithmic spaced-repetition system (e.g., like Anki's SM-2 algorithm). The current platform distributes content across units by curriculum design, not by a real-time algorithm tracking individual student forgetting curves. This distinction matters if a district asks.

---

### 3.3 Rosenshine's Principles of Instruction

**Core claim (design rationale):** History Hack's lesson structure reflects multiple Principles of Instruction derived from both cognitive science and observational studies of effective teachers.

**Key citation:**

Rosenshine, B. (2012). Principles of instruction: Research-based strategies that all teachers should know. *American Educator, 36*(1), 12-19. https://www.aft.org/sites/default/files/Rosenshine.pdf
- 17 principles; freely available; highly readable
- ALSO cited in: Sherrington, T. (2019). *Rosenshine's Principles in Action.* John Catt Educational. (accessible practitioner version)

**Most applicable principles for History Hack:**

| Principle | # | Application to History Hack |
|---|---|---|
| Begin a lesson with a short review | 1 | Review questions at unit start |
| Present new material in small steps | 2 | Chunked unit modules |
| Ask a large number of questions | 3 | Embedded question bank throughout lessons |
| Provide models / worked examples | 6 | Worked example documents [NEEDS VERIFICATION] |
| Guide student practice | 7 | Scaffolded practice before independent work |
| Check for student understanding | 8 | Formative quiz checkpoints [NEEDS VERIFICATION — confirm feature] |
| Obtain a high success rate | 9 | Scaffolded questions before harder items |
| Provide scaffolds for difficult tasks | 11 | Vocabulary support, chunked content |
| Require and monitor independent practice | 16 | End-of-unit independent questions |
| Engage in weekly and monthly review | 17 | TCAP review decks across units |

---

### 3.4 Cognitive Load Theory

**Core claim (design rationale):** History Hack's design minimizes extraneous cognitive load and supports germane load through scaffolding and chunking.

**Key citations:**

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257-285.
- Foundational paper introducing cognitive load theory

Sweller, J., van Merrienboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296.
- Distinguishes intrinsic, extraneous, and germane load
- Scaffolding and worked examples reduce extraneous load

van Merrienboer, J. J. G., & Sweller, J. (2005). Cognitive load theory and complex learning: Recent developments and future directions. *Educational Psychology Review, 17*(2), 147-177.
- Applied framework for complex domain instruction (relevant to multi-era history curriculum)

**Application note:** If History Hack materials display text and image simultaneously in ways that could cause split-attention effect, this is a design issue — flag to `instructional-design-specialist`.

---

### 3.5 Mayer's Multimedia Learning Principles

**Core claim (design rationale):** Where History Hack uses text alongside images, maps, or diagrams, the design can be evaluated against Mayer's evidence-based principles.

**Key citation:**

Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). Cambridge University Press.
- 12 principles of multimedia learning, each backed by experimental evidence
- Most relevant: coherence principle (remove extraneous material), signaling (highlight key ideas), segmenting (user-paced segments), spatial contiguity (place text near related graphics)

Mayer, R. E., & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. *Educational Psychologist, 38*(1), 43-52.
- Applied guide; useful for designers reviewing History Hack visuals

**Caution:** Only apply these principles to materials that actually use multimedia. If units are predominantly text-based, do not overclaim multimedia learning alignment.

---

### 3.6 Universal Design for Learning (UDL)

**Core claim (design rationale):** History Hack is designed with UDL principles in mind to serve diverse learners, including students with IEPs/504s and English Language Learners.

**Key citations:**

CAST. (2018). *Universal design for learning guidelines version 2.2.* https://udlguidelines.cast.org
- Three principles: Multiple Means of Representation, Multiple Means of Action & Expression, Multiple Means of Engagement
- Free, authoritative, updated reference

Rose, D. H., & Meyer, A. (2002). *Teaching every student in the digital age: Universal design for learning.* ASCD.

**Caution:** UDL alignment requires that the product actually provides multiple means of representation (e.g., text alternatives, varied formats). Verify specific accessibility features against the repo and with `accessibility-qc-agent` before claiming UDL alignment.

---

### 3.7 Culturally Responsive Pedagogy

**Core claim (design rationale):** History Hack's curriculum includes diverse historical perspectives and content relevant to students of varied backgrounds.

**Key citations:**

Gay, G. (2000). *Culturally responsive teaching: Theory, research, and practice.* Teachers College Press.
- Foundational text; defines CRP as using cultural knowledge, prior experiences, and frames of reference to teach effectively

Ladson-Billings, G. (1995). Toward a theory of culturally relevant pedagogy. *American Educational Research Journal, 32*(3), 465-491. https://doi.org/10.3102/00028312032003465
- Landmark study identifying effective practices with Black students; broadly applied to all underserved groups

Hammond, Z. (2015). *Culturally responsive teaching and the brain.* Corwin.
- Accessible practitioner text; widely used in TN district professional development

**Important boundary:** Culturally responsive claims must be grounded in what the curriculum actually contains. Do NOT claim CRP alignment generically. Verify specific units, perspectives, and representation with `historian-factcheck-agent` before making any CRP-based claim publicly.

---

## Section 4: Design-to-Research Alignment Table Template

| History Hack Feature | Research Principle | Key Citation | Claim Level |
|---|---|---|---|
| Embedded review questions throughout units | Retrieval Practice | Dunlosky et al. (2013) | Design Rationale |
| Questions distributed across multiple unit sessions | Spaced/Distributed Practice | Cepeda et al. (2006) | Design Rationale |
| Short review at lesson start | Rosenshine Principle #1 | Rosenshine (2012) | Design Rationale |
| Chunked content in small modules | Cognitive Load — intrinsic | Sweller et al. (1998) | Design Rationale |
| TCAP-aligned question bank | Standards-aligned assessment | TN Academic Standards | Design Rationale |
| Scaffolded vocabulary support [NEEDS VERIFICATION] | Rosenshine Principle #11 / Cognitive Load | Rosenshine (2012) | Design Rationale |
| Multiple content formats [NEEDS VERIFICATION] | UDL Representation | CAST (2018) | Design Rationale |

---

## Section 5: Honest Limitations Boilerplate

Include verbatim or adapted in every Research Foundations document:

> **Important note on the scope of this document:**
>
> The research cited in this document supports the theoretical rationale for History Hack's design choices. The studies referenced are about the underlying learning principles — retrieval practice, spaced repetition, cognitive load management, and others — not about History Hack itself. No outcome study has yet evaluated whether students using History Hack achieve greater learning gains, higher TCAP scores, or other measurable outcomes compared to students using other materials.
>
> TroopToTeacher Technologies is committed to building an honest evidence base. This document represents ESSA Tier 4 (Demonstrates a Rationale) evidence. A pilot study is planned to generate outcome data. We will update this document as evidence accumulates and will never claim a level of evidence we have not earned.

---

## APA 7th Edition Quick-Reference Rules

- **Journal article:** Author, A. A., & Author, B. B. (Year). Title of article. *Title of Periodical, volume*(issue), page range. https://doi.org/xxxxx
- **Book:** Author, A. A. (Year). *Title of work: Capital letter also for subtitle* (edition if not first). Publisher.
- **Website/report:** Author, A. A. (Year, Month Day). *Title of page.* Site Name. URL
- DOIs: always include if available; use https://doi.org/ format
- Never fabricate a DOI — if uncertain, omit and note [DOI not confirmed]

---
*Research Team · TroopToTeacher Technologies LLC · Integrity-first, always.*
