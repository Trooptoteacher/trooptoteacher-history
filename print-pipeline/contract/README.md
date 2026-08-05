# Shared Print Contract — CSS Paged Media (LOCKED)

**Contract version: 1.0.0 · Engine: WeasyPrint (locked) · Owner: `print-pipeline`**

This directory is the **single source of truth for print layout** across every
History Hack page product and every course. One contract, one set of pagination
rules, one brand system — so every file paginates identically and re-flows
correctly on edit. **Nobody hand-aligns a page again.**

## What it governs (four page products)
1. **Textbook** — chapter openers, prose, figures + captions, sidebars, pull-quotes
2. **Student workbook** — 7-activity spine, Cornell notes, write-space
3. **DBQ workbook** — primary-source cards, HIPPO prompts, CER writing space
4. **Graphic-organizer toolkit** — frames, grids, T-chart, Frayer, Venn

> Slide **decks** are a different medium (`.pptx`-native) and are **not** governed here.

## Files
| File | Role |
|---|---|
| `print-contract.css` | **The locked contract.** Every page-layout decision (page size, margins, running headers/footers, page numbers, break rules, and every content primitive). Token-driven; makes no brand decisions. |
| `tokens/us-history.css` | **Brand tokens** for U.S. History (America 250). To brand another course, copy this file and change the values — nothing else. |
| `print-shop.css` | **Optional overlay** — crop marks + 3mm bleed for a commercial print vendor. |
| `fonts/` | Embedded brand fonts (DM Sans / Inter) → self-contained, identical output on any machine, print-shop safe. |
| `fixtures/` | One real proof page per product; also the guardrail's test inputs. |
| `verify_print_contract.py` | **The lock.** Renders all four products, asserts pages render, fonts embed, and the contract's structural invariants hold. Fails the build on any regression. |

## Render
```bash
# from print-pipeline/
python3 render.py contract/fixtures/workbook.json out/workbook.pdf              # teacher/screen PDF
python3 render.py CONTENT.json OUT.pdf --tokens us-history                       # pick a course brand
python3 render.py CONTENT.json OUT.pdf --print-shop                             # crop marks + bleed
```

## The lock (run before shipping any print change)
```bash
python3 print-pipeline/contract/verify_print_contract.py
```

## Rules
1. **All four products render through this one contract.** No product ships its own page rules.
2. **Brand lives in tokens, layout lives in the contract.** New course = new token file, same contract.
3. **The contract is versioned.** Bump `Contract version:` on any layout change and re-run the lock.
4. **Fonts are embedded.** Output PDFs are self-contained and print-shop safe.
5. **Change content → re-render.** Deterministic pagination; never hand-align a page.
