"""
build_guided_notes.py — Guided Cornell cues + NOTES SUPPORTS ladder (Course Standard workbook).

Repeatable engine that applies the LOCKED guided-notes design (approved on Unit 6 · US.45) to
every standard in a Course Standard student-workbook `.docx`. Run it AFTER the workbook has the
full 7-activity cycle and zero blank pages (pipeline Phase 1). It does two things per standard:

  FRONT — Activity 3 "Direct Teaching Cornell Notes": seeds the cue column with the standard's
    direct-instruction (DI) segments IN LECTURE ORDER, each keyed to the teacher deck's own
    "N of M" DI slides:  ①navy topic  ·  gold "▶ Deck · DI N of M"  ·  italic guiding question.
    Students always know which lecture segment they're on and what to listen for.

  BACK — "NOTES SUPPORTS — build your notes, your way": a four-rung support ladder so a
    high-need student can produce full notes from the back ALONE (the ceiling never drops):
      ① Sentence frames — finish the thought
      ② Fill-in notes — write just the missing word(s)      (+ word bank)
      ③ How to build your answer — Name it → Define → Example (+ worked model)
      ④ Try it — write one full note on LINED NOTEBOOK PAPER  (+ Quick self-check rubric)

WHY THE PROPAGATION CLONES THE US.45 REFERENCE INSTEAD OF REBUILDING FROM SCRATCH
  Formatting parity is the whole point ("hopefully the formatting is the same"). The safest
  guarantee is to deep-copy the approved US.45 NOTES SUPPORTS block (which preserves every
  shading fill, border, font, and spacing token) and swap only the standard-specific TEXT.
  The cue column is empty in every standard, so it is seeded from scratch with byte-stable helpers.

TWO FORMATTING LESSONS BAKED IN (do not "simplify" these away)
  1. NOTEBOOK PAPER IS A TABLE, NOT STACKED PARAGRAPHS. Empty paragraphs that each carry only a
     `w:bottom` border COLLAPSE in Word/LibreOffice — adjacent identical paragraph borders merge
     and only ONE line renders. Ruled notebook paper MUST be a borderless table whose ROWS each
     carry a bottom border (row/cell borders never collapse). See `notebook_table()`.
  2. ONE `w:spacing` PER PARAGRAPH. Setting space_before/after via python-docx AND then appending
     your own `w:spacing` produces two sibling `w:spacing` elements; Word reads the first and
     silently drops your exact line height. Always build a single merged `w:spacing`.

Usage:
    python build_guided_notes.py IN.docx OUT.docx            # apply to all configured standards
    python build_guided_notes.py IN.docx OUT.docx US.45      # single standard (for iterating)
"""

import copy
import sys
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# ── Canonical brand tokens (LOCKED — must match STUDENT_WORKBOOK_PLATINUM_STANDARD.md §3) ──
NAVY = "1B2A4A"
RED = "B22234"
GOLD = "C89B3C"
DARK = "2B2B2B"
LINE = "9AA0AB"          # writing / notebook line color


# ── Low-level run/paragraph helpers ───────────────────────────────────────────
def _run(p, text, color, half_pt, bold=False, italic=False):
    """Append one Calibri run. half_pt = size in half-points (22 == 11 pt)."""
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    rf.set(qn("w:ascii"), "Calibri"); rf.set(qn("w:hAnsi"), "Calibri")
    rpr.append(rf)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    c = OxmlElement("w:color"); c.set(qn("w:val"), color); rpr.append(c)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(half_pt)); rpr.append(sz)
    r.append(rpr)
    t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = text
    r.append(t)
    p.append(r)
    return r


def _para(before=0, after=40, line=240, rule="auto"):
    """A paragraph carrying exactly ONE w:spacing element (see lesson #2)."""
    p = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), str(before)); sp.set(qn("w:after"), str(after))
    sp.set(qn("w:line"), str(line)); sp.set(qn("w:lineRule"), rule)
    ppr.append(sp)
    p.append(ppr)
    return p


def _set_para_text(p, text):
    """Replace a paragraph's visible text while preserving the FIRST run's formatting.

    Multi-run paragraphs with inline bold labels (e.g. 'Model: …') must NOT be flattened;
    for those, edit the specific run's <w:t> directly. This helper is for single-voice lines.
    """
    runs = p.findall(qn("w:r"))
    if not runs:
        _run(p, text, DARK, 21)
        return
    # keep first run, drop the rest, set text on the first run's <w:t>
    for extra in runs[1:]:
        p.remove(extra)
    t = runs[0].find(qn("w:t"))
    if t is None:
        t = OxmlElement("w:t"); runs[0].append(t)
    t.set(qn("xml:space"), "preserve"); t.text = text


# ── Notebook paper (border-collapse-proof) ─────────────────────────────────────
def notebook_table(nrows=5, height_twips=460, color=LINE, grid_twips=9360):
    """Return a borderless table of `nrows` ruled lines. Each ROW carries the bottom
    border, so the lines never collapse the way stacked bordered paragraphs do (lesson #1).
    height_twips 460 == 23 pt line pitch (matches the house writing-line height)."""
    tbl = OxmlElement("w:tbl")
    tblPr = OxmlElement("w:tblPr")
    tw = OxmlElement("w:tblW"); tw.set(qn("w:w"), "5000"); tw.set(qn("w:type"), "pct")
    tblPr.append(tw)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), "none"); e.set(qn("w:sz"), "0"); e.set(qn("w:space"), "0")
        borders.append(e)
    tblPr.append(borders)
    layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed"); tblPr.append(layout)
    tbl.append(tblPr)
    grid = OxmlElement("w:tblGrid")
    gc = OxmlElement("w:gridCol"); gc.set(qn("w:w"), str(grid_twips)); grid.append(gc)
    tbl.append(grid)
    for _ in range(nrows):
        tr = OxmlElement("w:tr")
        trPr = OxmlElement("w:trPr")
        th = OxmlElement("w:trHeight")
        th.set(qn("w:val"), str(height_twips)); th.set(qn("w:hRule"), "exact")
        trPr.append(th); tr.append(trPr)
        tc = OxmlElement("w:tc")
        tcPr = OxmlElement("w:tcPr")
        tcw = OxmlElement("w:tcW"); tcw.set(qn("w:w"), str(grid_twips)); tcw.set(qn("w:type"), "dxa")
        tcPr.append(tcw)
        tcB = OxmlElement("w:tcBorders")
        bot = OxmlElement("w:bottom")
        for k, v in (("w:val", "single"), ("w:sz", "8"), ("w:space", "0"), ("w:color", color)):
            bot.set(qn(k), v)
        tcB.append(bot); tcPr.append(tcB)
        tc.append(tcPr)
        tc.append(_para(after=0, line=240))
        tr.append(tc); tbl.append(tr)
    return tbl


# ── FRONT: seed the guided Cornell cue column ─────────────────────────────────
def _ptext(el):
    return "".join(n.text or "" for n in el.iter(qn("w:t")))


def find_cornell_table(doc, code):
    """Return the Activity 3 Cornell table element for standard `code` (e.g. 'US.45')."""
    kids = list(doc.element.body)
    header = None
    for i, ch in enumerate(kids):
        if ch.tag == qn("w:p") and _ptext(ch).startswith(f"Activity 3 —") and code in _ptext(ch):
            header = i
            break
    if header is None:
        raise ValueError(f"Activity 3 header for {code} not found")
    for ch in kids[header:]:
        if ch.tag == qn("w:tbl") and "Cues (tied" in _ptext(ch):
            return ch
    raise ValueError(f"Cornell table for {code} not found")


def ensure_cue_rows(cornell_tbl, n):
    """Expand the Cornell table so there are exactly `n` cue-content rows before the
    'Key terms →' row. The committed workbook ships 3 cue rows, but a standard's guided cues
    need one row per DI segment (4 for most, 5 for US.51). Deep-copies the last content row
    (preserving the ruled 'My notes' cell) and inserts it before the Key-terms row, clearing
    the copied cue cell. Returns the final cue-row count. Call this BEFORE seed_guided_cornell."""
    rows = cornell_tbl.findall(qn("w:tr"))
    kt = next((r for r in rows if "Key terms" in _ptext(r)), None)
    header = rows[0] if rows else None
    content = [r for r in rows if r is not header and r is not kt]
    while len(content) < n and content and kt is not None:
        newrow = copy.deepcopy(content[-1])
        cell0 = newrow.findall(qn("w:tc"))[0]
        for p in cell0.findall(qn("w:p")):
            for r in p.findall(qn("w:r")):
                p.remove(r)
        kt.addprevious(newrow)
        content.append(newrow)
    return len(content)


def seed_guided_cornell(cornell_tbl, cues):
    """Fill the cue column (col 0) of rows 1..len(cues). Call `ensure_cue_rows(tbl, len(cues))`
    first so the table has enough rows. `cues` is a list of
    (topic, deck_marker, guiding_question) triples in LECTURE ORDER. Row 0 is the
    header; the final 'Key terms →' row is left untouched."""
    rows = cornell_tbl.findall(qn("w:tr"))
    for i, (topic, deck, q) in enumerate(cues):
        cell = rows[i + 1].findall(qn("w:tc"))[0]
        for p in cell.findall(qn("w:p")):
            cell.remove(p)
        p1 = _para(before=20, after=20); _run(p1, topic, NAVY, 22, bold=True); cell.append(p1)
        p2 = _para(after=20); _run(p2, deck, GOLD, 17, bold=True); cell.append(p2)
        p3 = _para(after=40); _run(p3, q, DARK, 18, italic=True); cell.append(p3)


# ── BACK: clone the reference NOTES SUPPORTS page and swap standard text ────────
def find_notes_supports_block(doc, code):
    """Return the ordered list of body elements that make up the NOTES SUPPORTS page for `code`
    (title → intro → 4 rungs → notebook table → self-check). Used both to LOCATE the US.45
    reference block for cloning and to find a target block to replace."""
    kids = list(doc.element.body)
    start = None
    for i, ch in enumerate(kids):
        if "NOTES SUPPORTS" in _ptext(ch) and code in _ptext(ch):
            start = i
            break
    if start is None:
        raise ValueError(f"NOTES SUPPORTS block for {code} not found")
    block = []
    for ch in kids[start:]:
        t = _ptext(ch).strip()
        if ch.tag == qn("w:p") and t.startswith("Activity 4"):
            break
        block.append(ch)
    return block


def clone_notes_supports(reference_block, cfg, anchor):
    """Deep-copy the US.45 reference NOTES SUPPORTS `reference_block`, swap in `cfg`'s
    standard-specific text, and insert it immediately BEFORE `anchor` (the standard's
    Activity 4 header) in forward order. The notebook table and self-check line are copied
    verbatim — their formatting is identical for every standard by design.

    cfg keys:
      code, title_tail            e.g. 'US.46', 'build your notes, your way · US.46'
      frames   : [4 strings]      rung ① sentence frames (bullet text WITHOUT the '•  ')
      cloze    : [4 strings]      rung ② fill-in bullets
      wordbank : str              rung ② word bank line (after 'Word bank:  ')
      model    : str              rung ③ worked model (the quoted sentence)
    """
    clones = [copy.deepcopy(el) for el in reference_block]

    def is_bullet(el):
        return el.tag == qn("w:p") and _ptext(el).strip().startswith("•")

    bullets = [el for el in clones if is_bullet(el)]
    frames, cloze = bullets[:4], bullets[4:8]

    # title
    for el in clones:
        if "NOTES SUPPORTS" in _ptext(el):
            _set_para_text(el, f"NOTES SUPPORTS — {cfg['title_tail']}")
            break
    # rung ① frames  /  rung ② cloze  (preserve the leading bullet glyph + tab)
    for el, text in zip(frames, cfg["frames"]):
        _set_para_text(el, f"•   {text}")
    for el, text in zip(cloze, cfg["cloze"]):
        _set_para_text(el, f"•   {text}")
    # word bank + model — each is a SINGLE 'label: body' run in the reference, so rewrite the
    # whole run's text (this preserves the run's rPr/styling; do NOT try to keep a separate
    # label run — there isn't one).
    for el in clones:
        t = _ptext(el)
        if t.startswith("Word bank"):
            _set_para_text(el, f"Word bank:   {cfg['wordbank']}")
        elif t.startswith("Model"):
            _set_para_text(el, f'Model:  "{cfg["model"]}"')

    for el in clones:
        anchor.addprevious(el)


# ── Per-standard configuration ─────────────────────────────────────────────────
# US.45 is the LOCKED reference (already in the workbook, approved by Sean). For each other
# standard, author the DI segments from that standard's teacher-deck DI slides ("N of M") and
# the four support rungs from the standard's content, then add an entry here.
STANDARDS = {
    "US.45": {
        "cues": [
            ("①  Key Characteristics of Fascism",     "▶ Deck · DI 1 of 4", "What traits make a government fascist?"),
            ("②  Fundamental Tenets of Communism",    "▶ Deck · DI 2 of 4", "What drives history — and who owns property?"),
            ("③  Totalitarianism — Italy, Germany, USSR", "▶ Deck · DI 3 of 4", "How did each regime take total control?"),
            ("④  Factors in Its International Spread", "▶ Deck · DI 4 of 4", "Why did these ideas spread after WWI?"),
        ],
        "supports": {
            "code": "US.45",
            "title_tail": "build your notes, your way · US.45",
            "frames": [
                "Fascism is ______ because it ______.",
                "Communism calls for ______, which means ______.",
                "In ______ (Italy / Germany / USSR), the regime controlled people by ______.",
                "These ideologies spread after WWI because ______.",
            ],
            "cloze": [
                "Fascism = extreme ______ + one all-powerful ______; uses ______ + secret police; blames ______.",
                "Communism = ______ struggle; the ______ owns property; goal is a ______ society.",
                "Totalitarianism = the ______ controls all of public & private life.",
                "Spread = came after ______; fueled by the Great ______, fear, and broken promises.",
            ],
            "wordbank": "nationalism · leader · propaganda · minorities · class · state · classless · government · WWI · Depression",
            "model": "Fascism (name) is rule by one all-powerful leader who glorifies the nation (define) — like Mussolini in Italy (example).",
        },
    },
    # "US.46": { "cues": [...4 triples...], "supports": {...} },  ← author per standard
}

SELF_CHECK = "☐  I named the idea      ☐  I defined it in my own words      ☐  I gave an example      ☐  A reader could follow it"


def apply_standard(doc, code, ref_supports_block):
    cfg = STANDARDS[code]
    # FRONT — expand rows to match the DI-segment count, then seed cues
    tbl = find_cornell_table(doc, code)
    ensure_cue_rows(tbl, len(cfg["cues"]))
    seed_guided_cornell(tbl, cfg["cues"])
    # BACK — clone reference NOTES SUPPORTS unless this standard already has one
    if code != "US.45":
        anchor = None
        for ch in list(doc.element.body):
            if ch.tag == qn("w:p") and _ptext(ch).startswith("Activity 4") and code in _ptext(ch):
                anchor = ch; break
        if anchor is None:
            raise ValueError(f"Activity 4 anchor for {code} not found")
        clone_notes_supports(ref_supports_block, cfg["supports"], anchor)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    only = sys.argv[3] if len(sys.argv) > 3 else None
    doc = Document(src)
    ref_block = find_notes_supports_block(doc, "US.45")  # the locked reference to clone
    codes = [only] if only else list(STANDARDS.keys())
    for code in codes:
        apply_standard(doc, code, ref_block)
        print(f"applied guided notes → {code}")
    doc.save(out)
    print(f"saved {out}  (render + run the QC gate — zero blank pages, notebook lines visible)")


if __name__ == "__main__":
    main()
