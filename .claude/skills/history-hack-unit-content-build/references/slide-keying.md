# Bidirectional deck ↔ workbook slide-keying

Foundational principle: **a student must never wonder where a writing task came from.** The
workbook names the deck slide; the deck shows a "write now" cue. Both directions, every standard.
(Do this AFTER the decks exist and are numbered — never hardcode a slide number by guess.)

## Build the deck slide map first
Extract slide titles/numbers from the **Student** deck (the one the workbook keys to). It's a
regular block: `base = 2 + 8·k`. Map each activity to the deck slide by role:

| Workbook activity | Deck slide (offset from base) | Deck slide role |
|---|---|---|
| 1 & 2 Vocabulary | base+6 | KEY VOCABULARY |
| 3 Cornell Notes | base+1…+3 | content / DIRECT INSTRUCTION |
| 4 Close Read | base+1…+3 | content / DIRECT INSTRUCTION |
| 5 Primary Source / HIPPO | base+4 | SOURCE IT FIRST |
| 6 Practice Quiz | base+7 | PROGRESS CHECK |
| 7 CER | base+1…+5 | content + THREE PERSPECTIVES |

If a unit's deck block size differs, recompute `base`/offsets from the actual slide map — always
derive numbers from the deck's real file positions.

## Workbook → deck (`▶ Deck slide N`)
Append a gold run to each activity header paragraph:
```python
# gold #C89B3C, ~9pt bold, e.g. "      ▶ Deck slide 14" or "      ▶ Deck slides 11–13"
```
Unit 6 added 98 refs (14 standards × 7 activities). Adding a wrapped header line can tip one tight
page — re-run the QC gate and reclaim space on any spill (Unit 6: shrank US.54's Activity 5 photo).

## Deck → workbook (`✍ In your workbook · <activity>`)
Map deck slides to activities **by title keyword** (works for both decks):
- `KEY VOCABULARY` → Vocabulary (Act 1–2)
- `DIRECT INSTRUCTION` → Cornell Notes & Close Read (Act 3–4)
- `SOURCE IT FIRST` / `PRIMARY SOURCE` → Primary Source & HIPPO (Act 5)
- `PROGRESS CHECK` / `CHECK FOR UNDERSTANDING` → Practice Quiz (Act 6)
- `THREE PERSPECTIVES` / `STUDENT ACTIVITY` → Constructed Response (Act 7)

**Student deck (on-slide, student-facing):** add a gold right-aligned textbox in the top band at
`L≈6.2", T≈0.30", W≈4.9", H≈0.38"` (between the left type-chip and the far-right US.xx chip; clear
of the DI slides' center US.xx chip). Text `✍ In your workbook · <activity>`, ~10.5pt bold gold.
```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
tb=slide.shapes.add_textbox(Inches(6.2),Inches(0.30),Inches(4.9),Inches(0.38))
tf=tb.text_frame; tf.word_wrap=True
for m in ('margin_top','margin_bottom','margin_left','margin_right'): setattr(tf,m,0)
p=tf.paragraphs[0]; p.alignment=PP_ALIGN.RIGHT
r=p.add_run(); r.text=f"✍ In your workbook · {activity}"
r.font.size=Pt(10.5); r.font.bold=True; r.font.name='Calibri'; r.font.color.rgb=RGBColor(0xC8,0x9B,0x3C)
```

**Teacher deck (speaker notes):** the top band is crowded (wide combined title). Add the cue to
`slide.notes_slide.notes_text_frame` instead (append, don't clobber): `✍ Students: <activity> in
the workbook.` Unit 6: 98 on-slide (Student) + 143 notes (Teacher).

Slides with no matching workbook task get **no cue** — so the cue reliably means "pick up your
pencil." Validate + render after; check the cue doesn't collide and the ✍ glyph renders.
