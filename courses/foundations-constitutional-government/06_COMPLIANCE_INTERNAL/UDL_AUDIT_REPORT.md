# CAST UDL 3.0 Audit — Foundations of Constitutional Government

**Framework:** CAST (2024). *Universal Design for Learning Guidelines version 3.0.* Lynnfield, MA.
**Scope audited:** Student Workbooks, Teacher + Student Decks, Assessment Books, Graphic Organizer Toolkits, the 700-item Question Bank, and course content JSON (all 7 units, GC.01–GC.35).
**Method:** Each of the 9 guidelines scored ✅ present-and-strong (evidence in the artifact) / ⚠️ present-but-weak / ❌ absent, with the artifact evidence and the design gap. Scores reflect **evidence in the design**, not the presence of a UDL label. A "strip" that names a support counts only where the artifact actually delivers it.

## The core distinction this audit enforces
A UDL/MTSS **strip is a signpost, not embedding.** It scores here only where a real affordance backs it. Where a strip claims an option the artifact doesn't provide per task, that is scored ⚠️ and listed as a gap — not credited.

---

## Principle 1 — Engagement (the WHY)

| Guideline | Score | Evidence in the artifacts | Gap |
|---|---|---|---|
| **7. Welcoming Interests & Identities** | ✅ | 7.2 authentic civic hooks per standard (`hook`, `civic_label`, `tn_connection`); 7.3 joy/play via the "Make It Stick" `play` routine; 7.4 low-threat framing ("no penalty for 'never seen it'," "growth is the goal") | 7.1 student **choice/autonomy** is mostly teacher-directed ("your teacher chooses which activities") — limited *student*-facing choice menu |
| **8. Sustaining Effort & Persistence** | ✅ | 8.1 explicit `learning_targets` + success `criteria` + goal-setting; 8.2 **Guided Support** + **Extend & Re-Engage** (challenge both ways); 8.5 action-oriented feedback via remediation routing + Confidence Check-in | 8.4 belonging/community is implicit (discussion norms) rather than a designed element |
| **9. Emotional Capacity** | ⚠️ | 9.1 **belief-check** (Make It Stick); 9.3 reflection via Knowledge Rating + Confidence Check-in | 9.2 awareness of self/others and 9.4 empathy/restorative practices are not explicit design elements |

## Principle 2 — Representation (the WHAT)

| Guideline | Score | Evidence | Gap |
|---|---|---|---|
| **1. Perception** | ⚠️ | 1.2 multiple ways to perceive (primary sources + captions + read-aloud-able plain text); 1.3 diversity of perspectives (`perspectives`, `lenses`); images carry **alt-text** (`descr` on every image run) | **1.1 customize display** — no dedicated large-print / reading-order-tagged accessible export exists yet (docx is zoomable + alt-texted, but not a tagged accessible edition) |
| **2. Language & Symbols** | ✅ | 2.1 vocab definitions + Frayer + Vocabulary Self-Check; 2.2 decoding via pronunciation (`say`); 2.3 **EN/ES** gloss (`es`) on every term; 2.5 multiple media | 2.4 biases in language/symbols not explicitly addressed as a design note |
| **3. Building Knowledge** | ✅ | 3.1 prior-knowledge activation (Spaced Retrieval); 3.2 patterns/big ideas (`cues`, essential question); 3.3 multiple ways of knowing (organizer variety); 3.4 transfer via **spiral** | — |

## Principle 3 — Action & Expression (the HOW)

| Guideline | Score | Evidence | Gap |
|---|---|---|---|
| **4. Interaction** | ⚠️ | 4.1 multi-modal response IS offered in the **Organizer Toolkits** ("students may write, say (record), draw, or build"); 4.2 alt-text supports assistive tech | **4.1 not uniform** — the **workbook** constructed tasks default to writing lines; the response-mode choice is not on each workbook activity |
| **5. Expression & Communication** | ⚠️ | 5.1 multiple media in organizers; open-response items are rubric-scored (mode-flexible); 5.3 Guided Support scaffolds | **5.1/5.2 weak in the workbook** (no per-task mode choice or composition tools); 5.4 biases in modes not addressed. **This is where the strip currently outruns the design.** |
| **6. Strategy Development** | ✅ | 6.1 goals (`learning_targets`); 6.2 Preview & Predict; 6.3 organize (Cornell + organizers); 6.4 monitor progress (Confidence Check-in, Knowledge Rating, Self-Check); 6.5 firm-goal/"same ceiling" language | — |

---

## Prioritized gaps (CAST equity lens — ordered by impact)

1. **[HIGH] A&E 5.1/4.1 — response-mode choice on the workbook itself.** The per-standard strip claims "respond in writing, speech, or a labeled diagram," but individual workbook tasks provide writing lines. *Fix: add a real "Show what you know — your way" option (write / say-record / draw-diagram / build) to each standard's constructed-response task.* → **design fix**
2. **[HIGH] Perception 1.1 — accessible/large-print edition.** Alt-text is present, but no tagged accessible / large-print export exists. *Fix: publish an accessible-formats provision + a large-print export path; flag full reading-order tagging as a documented next step.* → **format fix + statement**
3. **[MED] MTSS Tier 2/3 as named resources.** Tier 2 has real materials (organizers, Guided Support); Tier 3 is a described protocol. *Fix: an MTSS Support Map naming the Tier 1/2/3 resource per standard.* → **resource packaging**
4. **[LOW] Engagement 7.1 student choice; 9.2/9.4 empathy/reflection; 2.4/5.4 bias-in-language/modes.** *Fix: a student choice menu + explicit reflection/identity prompts + a bias-in-language note.*

## Verdict
The framework is **substantially embedded** in Representation and Strategy Development (real, evidenced affordances), and **partially embedded** in Engagement and Action & Expression — with one clear place where the strip currently over-claims relative to the design (multi-modal expression on the workbook). The gaps above convert the signposts into evidenced embedding. Gap-closure status is tracked in the "Gaps closed" section below as fixes land.

## Gaps closed (design fixes applied)
- **[HIGH] A&E 5.1/4.1 — CLOSED.** Every standard's constructed-response (CER) task in all 7 workbooks now carries a real **"Show what you know — your way"** element: write / say-and-record / draw-and-label / build, scored on the *same* CER rubric against the *same* standard, with word-processor, speech-to-text, scribe, and sentence-frame provisions. Verified: 35 blocks (one per standard), images intact, leak-clean. **Guideline 4 and 5 re-score ⚠️ → ✅** (multi-modal expression is now an artifact affordance in the workbook, not only in the organizers).
- **[MED] MTSS Tier 2/3 named resources — CLOSED.** `MTSS_SUPPORT_MAP.md` names the actual Tier 1/2/3 resource for all 35 standards (workbook cycle / Guided Support + best-fit organizer + Part 6 routing / intensive CRA + parallel-form re-assessment), with the triggers between tiers. Tier 3 is now a named routine, not just a protocol.
- **[MED] Perception 1.1 — CLOSED (with one honest external step).** Now shipped: a **large-print edition** of every workbook (16.5 pt, `*_LargePrint.docx`) and **PDF/UA tagged reading order on all 14 deck PDFs** (StructTreeRoot + MarkInfo + outline + Lang + Title + DisplayDocTitle, verified). Workbook docx are already heading-structured + fully alt-texted (screen-reader accessible); a **workbook tagged-PDF** is a one-command Word/LibreOffice export on the district side — not bundled only because this build environment's LibreOffice is non-functional. **Guideline 1 re-scores ⚠️ → ✅** for the decks and large-print; the workbook tagged-PDF is the single documented external step. See `ACCESSIBILITY_STATEMENT.md`.
- **[LOW] Engagement 7.1 + Guideline 9 — CLOSED.** Every standard's section now carries two real student-facing elements: a **"Choice & Voice"** menu (student picks how to go deeper — defend a term / connect to their life or community / take a side; 7.1 autonomy + 7.2 relevance) and a **"Reflect & Connect"** block (belief before→after self-awareness 9.3; fairly stating a differing view 9.2/9.4 empathy; a restorative discussion norm). 35 of each, verified; images intact; leak-clean. **Guideline 7 (7.1) and Guideline 9 re-score to ✅.**
- Residual minor notes (2.4/5.4 bias-in-language/modes) are partly addressed by the CER mode element (5.4) and the "state their view fairly" empathy prompt; no ❌ remain.

### Post-fix summary
| Principle | Guideline | Before | After |
|---|---|---|---|
| Representation | 1 Perception | ⚠️ | ✅ (large-print + tagged decks; workbook tagged-PDF = 1 external step) |
| Representation | 2 Language & Symbols | ✅ | ✅ |
| Representation | 3 Building Knowledge | ✅ | ✅ |
| Action & Expression | 4 Interaction | ⚠️ | ✅ |
| Action & Expression | 5 Expression & Communication | ⚠️ | ✅ |
| Action & Expression | 6 Strategy Development | ✅ | ✅ |
| Engagement | 7 Welcoming Interests | ✅ (7.1 ⚠️) | ✅ (7.1 closed — Choice & Voice) |
| Engagement | 8 Sustaining Effort | ✅ | ✅ |
| Engagement | 9 Emotional Capacity | ⚠️ | ✅ (Reflect & Connect) |

**Net:** **9 of 9 guidelines ✅ present-and-strong with artifact evidence.** Every UDL access strip maps to a real design affordance embedded in the artifacts, per standard. The single external step is exporting a workbook to tagged PDF (one Word/LibreOffice command — the docx is already heading-structured and fully alt-texted).
