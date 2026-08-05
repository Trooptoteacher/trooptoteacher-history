# Student Workbook — Change Spec (Sean batch, Aug 2026)

Reference build: Unit 6 (US.45–US.58) Course Standard. Control document:
`00_START_HERE/STUDENT_WORKBOOK_PLATINUM_STANDARD.md` ("this file wins"). Every change below is
encoded into that spec first, then into the build engine, then propagated to all units + reused by
the other six courses. Palette note: spec §2/§3 still lists the **old** tokens (#1B2A4A/#C89B3C/#F7F5EF)
— migrate to **America 250** (#1F3A5F Heritage Blue · #B22234 · #C9A227 · #F8F5EF · line #9AA0AB) as
part of this pass (CLAUDE.md production guardrail).

Legend: [FILL]=kill white space · [WRITE]=needs ruled lines/redirect · [NEW]=new content ·
[REVERSAL]=changes a currently-LOCKED spec line (Sean-authorized) · [DBQ]=deferred to DBQ book.

## FRONT MATTER
| # | Page | Change | Spec §/code |
|---|---|---|---|
| F1 | "How to Use This Workbook" legend | **Verify + update + [FILL].** Legend must now teach the NEW systems: **Lenses/Dimensions pills** (C/E/G/H/P/T/TCA), **verso supports** model (front=task, back=support; 3 print modes), **Future Ready** callout icon, **self-check keys**, **▶ Deck** keying. Expanding the legend fills the bottom white space. | §4.2 #6, §7.6 front matter; engine front-matter builder |
| F2 | p.4 — TN Standards & SSP Crosswalk | **[FILL]** bottom white space (add the Lenses/Dimensions coverage row or a "how to read the crosswalk" strip). | §4.2 #4 |
| F3 | p.5 — Accessibility/UDL & Accommodation matrix | **[FILL]** bottom white space (extend matrix rows or add the non-replacement guardrail callout + UDL 3.0 note). | §4.2 #5 |

## OPENER (p.7 — first standard page)
| # | Change | Spec §/code |
|---|---|---|
| O1 | **SET YOUR GOAL → SMART goal [NEW][WRITE].** Replace the plain goal line with the guided SMART frame (S·M·A·R·T tagged, ruled lines to write it). This is the per-unit **short-term** goal that ladders to *My SMART Goals*. Fills much of the opener white space. | §7.6 opener; Future Ready SMART system |
| O2 | **PREVIEW & PREDICT [WRITE].** Any remaining opener space → ruled writing room for Preview & Predict. | §7.6 opener, §7.2 |
| G0 | **GLOBAL [WRITE]:** every student write-prompt in the book has ruled lines OR an explicit redirect. Audit all activities. | §7.2 (enforce) |

## ACTIVITY 1 (Vocabulary) — no change. ACTIVITY 2 (Vocab Studio) — no change.

## ACTIVITY 3 (Cornell / Direct Teaching)
| # | Change | Spec §/code |
|---|---|---|
| A3a | **Expand the DOODLE ZONE [NEW][REVERSAL].** §7.6/§7.9 currently say "No separate Doodle Zone — redundant with More Notes." Sean reverses: add/expand a labeled sketch/doodle zone (dual-coding / sketchnoting, UDL). | §7.6, §7.9 (reverse) |
| A3b | **Populate slide numbers [FIX].** The `▶ Deck · DI N of M` cue references must be filled for every standard (relative N-of-M from the deck `_build.json`), not blank. (Absolute `▶ Deck slide N` still waits on decks per §7.8.) | §7.9, build_guided_notes.py |
| A3c | **Q1 locator [FIX].** Progress-Check Q1 ("what does the passage say about characteristics of fascism") must point to where the answer is found (e.g., "→ see cue 2 / your notes"). Add a locator to each Progress-Check item. | §7.6 Act 3 |
| A3d | **"Check Yourself / How am I doing?" boxes for ALL items [FIX].** Currently only item 1 has a rating box; every item needs its own rating options. | §7.6 Act 3 |
| A3e | **Extended writing room for the 12–15 word headline [WRITE][FILL].** If space remains, give more ruled room for the headline/summary. | §7.2, §7.9a |

## ACTIVITY 4 (Close Read)
| # | Change | Spec §/code |
|---|---|---|
| A4a | **Bold the academic vocabulary words** that tie together in the passage. | §7.6 Act 4 |
| A4b | **Teach how to write a thesis statement [NEW].** REC: a compact "How to Write a Thesis" mini-support on the Close-Read→CER bridge — best home = CER Writing Supports verso (Act 7), since the thesis feeds the CER; cross-referenced from Close Read. | §7.6 Act 4/7 |
| A4c | **Too much white space at end [FILL].** Add space between the passage paragraphs (spaced sub-sections, §7.7) AND add key content / a context-matched fill (§5.5 text-source fills). | §7.7, §5 |

## ACTIVITY 5 (Primary Source / HIPPO — p.13)
| # | Change | Spec §/code |
|---|---|---|
| A5 | **Writing opportunity on the support option [WRITE].** The support's writing area has no real room to write. Give adequate ruled space (notebook_table) OR an explicit redirect ("write this on your whiteboard / here"). No stranded prompt. | §7.2 |

## ACTIVITY 6 (Practice Quiz)
| # | Change | Spec §/code |
|---|---|---|
| A6 | **Way too much white space → add the self-check at the bottom [FILL][NEW].** REC (adoption-grade fit for an MCQ set): the **on-page self-check ANSWER KEY** — correct letter **+ one-line rationale** per item ("commit first, then check"), which §7.6/§7.10 already call for. This fills the space AND is the Integrity self-grade move. (The scored CER *rubric* stays on Act 7.) | §7.4 sibling, §7.10 |

## ACTIVITY 7 (CER) — front looks OK.
| # | Change | Spec §/code |
|---|---|---|
| A7 | **Reconcile the CER self-grade [REVERSAL].** §7.4 currently specifies a 1–4 /16 rubric (Claim/Evidence/Reasoning/Conventions). Sean's earlier directive = the **College Board AP-aligned** CER self-grade (A/B/C/D, 6-pt LEQ → 7-pt DBQ). REC: AP-aligned version supersedes §7.4; keep it on the CER verso. | §7.4, §7.6 Act 7 |

## DEFERRED — DBQ book ("next")
| # | Change |
|---|---|
| D1 | **[DBQ]** HIPPO analysis organizer — kill bottom white space, add an **exemplar** (not blank). Governed by `history-hack-dbq-workbook`. |

## CODIFY (the mandate)
All of the above **+** the full Future Ready system (Launch/Debrief/SMART Support/My SMART Goals/CER
Self-Grade/Questions/Money-Math + embedded micro-moments + MCQ self-check rule), the **Lenses/Dimensions**
pills, the **verso supports reverse-document** model, **chart sourcing** rule, and the **annual currency
guardrail** get encoded into: (1) `STUDENT_WORKBOOK_PLATINUM_STANDARD.md`, (2) the build scripts
(`build_guided_notes.py`, `build_backpage_supports.py`, front-matter builder), (3) `SKILL.md` of
`history-hack-unit-content-build`, so re-running the pipeline reproduces every change on any unit and
the pattern is reusable by the other six courses. Then **regenerate all workbooks**. Single skills-only
PR to `main`.
