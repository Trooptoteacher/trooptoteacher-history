# U.S. History Hack — Slide Deck Platinum Standard

**Version:** 1.0 — DRAFT for Sean's review
**Owner:** TroopToTeacher Technologies LLC
**Companion to:** `STUDENT_WORKBOOK_PLATINUM_STANDARD.md` (the two are one system — edit them together)
**Status:** Working master. Edit this file, hand it back, and it becomes the source of truth I encode into the deck build engine and the web viewer.

---

## 0. How this document works (same loop as the workbook standard)

This is the control document for how every U.S. History Hack **teacher/student slide deck** is built. You edit it in plain language; I encode every rule into the deck engine (`build_student.py` / the deck templates) and the web deck viewer. **This file wins** when it and the code disagree.

The deck and the student workbook are a **matched pair.** Neither is finished until it lines up with the other. Where a rule here has a partner rule in the workbook standard, it's marked 🔗.

---

## 1. THE FOUNDATION — deck and workbook are locked together (🔗 non-negotiable)

This is the first principle, above everything else about color or layout:

> **A student must never wonder where a writing task came from.** Every place the workbook asks a student to write, it names the exact deck slide the thinking comes from — and every deck slide that has a matching workbook task shows a "write now" cue. The deck and workbook point at each other, by design, on every standard.

Four rules make this real:

### 1.1 Shared spine: standard code is the key
- The deck and the workbook are both organized by **standard code** (US.01, US.02, …).
- **Every slide carries its standard tag** (the gold `US.xx` chip, top-right). **Every workbook section carries the same code.** That shared code is the backbone of the correlation.

### 1.2 Workbook → deck keying (the part you called out)
- **Every workbook activity that asks for writing prints its source slide reference** in the activity header — e.g. `▶ Deck slide 8` or `▶ Deck slides 4–7`.
- The reference is exact and slide-number-accurate (see §7 on numbering stability).
- This includes: Cornell notes, Close Read, Transfer/Progress Check, primary-source analysis, and the CER/written response. If a student is writing, the workbook tells them which slide to look at.

### 1.3 Deck → workbook cue
- **Every deck slide that has a matching workbook task shows a "✍ In your workbook" cue** naming the activity (e.g. "✍ Workbook — Cornell Notes, US.03").
- Slides with **no** workbook task carry no cue — so the cue reliably means "pick up your pencil."

### 1.4 One-to-one checks
- The deck's **Progress Check** slides and the workbook's **Transfer Check** items are the *same item* (same question ID), so what students rehearse on screen is what they commit to on paper.
- Answers stay **hidden on the student deck** and live only in the teacher key/teacher deck — so the check works as a real check.

> 🔗 The workbook side of every rule above must be mirrored in `STUDENT_WORKBOOK_PLATINUM_STANDARD.md` §4 (page anatomy) and §5 (activities). If the two docs ever disagree on the keying, this §1 governs.

---

## 2. Deck geometry & format

| Parameter | Current value | Notes |
|---|---|---|
| Aspect / size | **16:9 widescreen, 13.33 in × 7.5 in** | Standard projector/really-common classroom display |
| Background | Solid **navy**, full bleed | See palette + the navy decision below |
| Safe margins | ~0.5 in content inset; footer band at ~7.08 in | Keep all text inside the safe area for older projectors |
| Standard tag | Gold `US.xx` chip, **top-right**, every content slide | The correlation key (§1.1) |
| Footer | Unit footer text left, **page/slide number right**, ~9 pt | Slide number is what the workbook references |

> `DECISION NEEDED — two decks or one?`: today there's a **Student (Lean)** deck and a **Teacher** deck per unit. Confirm we keep both (student = clean, answers hidden; teacher = same slides + answers, speaker notes, reveal prompts), and that the workbook keys to the **Student** deck's numbering.

---

## 3. Typography

- **Headlines / titles:** Georgia (serif).
- **Chips, labels, footer:** Trebuchet MS.
- **Body / cards:** Calibri.
- **Font floor:** nothing below **9 pt** anywhere (fixes legacy 8 pt footers). On-slide instructional text should read from the back of a room — titles ~28–30 pt, body ~13–18 pt.

> 🔗 The deck's body floor (9 pt for furniture) is looser than the workbook's (10.5 pt) because decks are projected, not read at a desk. Keep them as separate floors on purpose.

---

## 4. Brand palette

Current deck tokens (from the deck engine):

| Token | Hex | Use |
|---|---|---|
| Navy | `#1A2332` | Slide background |
| Gold | `#C9A84C` | Standard tag, CORE PATH chip, accents |
| Light | `#C7D4E0` | Footer, subtitles on navy |
| White | `#FFFFFF` | Titles, card headers |
| Ink | `#1F2430` | Body text on light cards |
| Green | `#1B5E20` | SUPPORT OPTION |
| Blue | `#002858` | LANGUAGE SUPPORT |
| Red | `#C62828` | RESPONSE CHOICE |
| Purple | `#6A4E9C` | PROGRESS CHECK |
| Deep green | `#2F6F4E` | EXTENSION |

> `DECISION NEEDED — ONE canonical navy + gold (IMPORTANT, 🔗)`: the deck navy (`#1A2332`) does **not** match the print/workbook navy (`#1B2A4A`) or the web navy (`#0A1F3C`); deck gold (`#C9A84C`) differs from print gold (`#C89B3C`). For deck and workbook to look like one product in a student's hands, **these must be unified.** Pick one navy + one gold and I'll set deck, workbook, and web to all three. This is the same decision flagged in the workbook standard §3 — decide once, applies everywhere.

**Grayscale/contrast:** keep enough contrast that the deck is legible on a weak projector; never encode meaning by color alone (the chip labels carry the meaning, not just the color).

---

## 5. The UDL · MTSS chip system (built in, not decorative)

Every deck opens with a **legend slide** explaining these, and the chips appear throughout:

| Chip | Meaning |
|---|---|
| **CORE PATH** | The essential instruction every student receives |
| **SUPPORT OPTION** | An optional scaffold that keeps the goal, not lowers it |
| **LANGUAGE SUPPORT** | Vocabulary, pronunciation, Spanish cognates for access |
| **RESPONSE CHOICE** | Show learning by writing, saying/recording, or diagramming |
| **PROGRESS CHECK** | A quick DOK-2/3 check to guide reteach or extend |
| **EXTENSION** | A deeper challenge once the goal is met |

Guardrail (🔗, matches workbook): supports work **alongside — never in place of** — required IEP/504 accommodations. State it on the legend slide.

---

## 6. Per-standard slide sequence

Each standard runs the same repeatable arc so students always know what's next — and so the workbook can key to it predictably:

1. **Standard title / hook** (gold `US.xx` tag; essential question).
2. **Key Vocabulary · Language Support** (say-it / cognate / definition). 🔗 → workbook Vocabulary.
3. **Content / close-read / data slides.** 🔗 → workbook Cornell Notes + Close Read.
4. **Primary source + analysis** (HIPP for lessons; OPTIC for standalone visual sources). 🔗 → workbook source analysis.
5. **Representation** (whose story — reached and left out).
6. **Progress Check** (DOK 2/3, answer hidden, RESPONSE CHOICE prompt). 🔗 → workbook Transfer Check (same item ID).

Deck-level bookends: a **How-This-Deck-Works legend** at the front and a **Representation close** at the end.

---

## 7. Numbering stability (why the keying doesn't rot)

The workbook references slides *by number*, so numbers must be trustworthy:
- Slides are **renumbered to file position** on every build (two-pass), and the workbook's slide references are regenerated from the **same** map in the same build — so an inserted slide never leaves a stale reference.
- Never hardcode a slide number in the workbook by hand; it comes from the shared reference map.
- 🔗 This mirrors the workbook's two-pass TOC/crosswalk reconvergence rule (workbook standard §6).

---

## 8. Accessibility

- **Descriptive alt text** on every image (no file paths / no `.jpg` as alt).
- Read-aloud-friendly reading order; high contrast on navy.
- Progress-check options **de-biased** (no "all of the above," balanced option lengths).
- Teacher deck carries **speaker notes** and reveal prompts; student deck does not expose answers.

---

## 9. Where each value lives (my encode targets)

| You change… | I update… |
|---|---|
| Slide size / margins / footer position | deck engine geometry (`build_student.py`) + web deck viewer |
| Palette / canonical navy+gold | deck color constants + workbook engine + web tokens (one change, three places) |
| Chip system / legend | the legend + chip helpers in the deck engine |
| Per-standard sequence | the deck build order + the workbook's slide-reference map (kept in sync) |
| Slide↔workbook keying rules | the shared reference map used by BOTH `build_student.py` and `build_workbook.py` |

---

## 10. Open decisions (put your call next to each)

1. **ONE canonical navy + gold** across deck / workbook / web — §4. ← most important, shared with workbook standard
2. **Keep two decks** (Student + Teacher), workbook keys to Student numbering — §2.
3. **Cue style** — how the "✍ In your workbook" cue and the `▶ Deck slide N` reference should look/word — §1.2–1.3.
4. Anything from the **Unit 6 Core Standard sample deck** once it's out of the zip (see below).

---

## 11. What's still blank — and why

The **structure** above is set. The **sample-specific specifics** (exact slide count per standard, the Unit 6 cover/format details, the real per-standard slide map) come from the **Unit 6 Core Standard Edition sample deck**, which is still sealed inside `HH_Unit6_Sample.zip` (22 MB; the Drive connector caps downloads at 10 MB). The moment that deck (and its workbook) are extracted, I'll:
1. Fill in the sample-derived specifics here,
2. Verify the deck and workbook key to each other correctly, and
3. Lock both this doc and the workbook standard against that one reference unit.

That's the "recreate them together" step — deck and workbook finalized as a matched pair, using Unit 6 as the shared reference implementation.
