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
NAVY = "1F3A5F"
RED = "B22234"
GOLD = "C9A227"
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
# US.45 is the LOCKED reference (approved by Sean). All 14 Unit 6 standards are encoded below:
# cues = the standard's teacher-deck DIRECT-INSTRUCTION segments ("N of M") in lecture order;
# supports = the four-rung NOTES SUPPORTS ladder authored from that standard's content
# (frames / cloze + word bank / how-to + model). Every cloze blank has a matching word-bank item.
# Regenerated + QC-verified against the committed Unit 6 workbook (2026-08).
STANDARDS = {
    "US.45": {
        "cues": [
            ("①  Key Characteristics of Fascism", "▶ Deck · DI 1 of 4", "What traits make a government fascist?"),
            ("②  Fundamental Tenets of Communism", "▶ Deck · DI 2 of 4", "What drives history — and who owns property?"),
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
    "US.46": {
        "cues": [
            ("①  Quarantine Speech (Oct 5, 1937)", "▶ Deck · DI 1 of 4", "How did FDR warn Americans about aggression?"),
            ("②  Four Freedoms Speech (Jan 6, 1941)", "▶ Deck · DI 2 of 4", "What four freedoms were worth defending?"),
            ("③  Atlantic Charter (Aug 14, 1941)", "▶ Deck · DI 3 of 4", "What postwar goals did the U.S. & Britain set?"),
            ("④  Lend-Lease Act (Mar 11, 1941)", "▶ Deck · DI 4 of 4", "How did the U.S. aid the Allies without joining the war?"),
        ],
        "supports": {
            "code": "US.46",
            "title_tail": "build your notes, your way · US.46",
            "frames": [
                "In the Quarantine Speech (1937), FDR said aggression should be ______ like a disease so it would not spread.",
                "The Four Freedoms are freedom of speech, freedom of worship, freedom from ______, and freedom from ______.",
                "The Atlantic Charter set postwar goals such as self-government and no ______ gain.",
                "Lend-Lease let the U.S. ______ the Allies without ______ the war.",
            ],
            "cloze": [
                "Quarantine Speech (1937) = FDR urged democracies to ______ aggressor nations to stop the spread of war.",
                "Four Freedoms (1941) = speech, worship, freedom from ______, freedom from ______ — worth defending.",
                "Atlantic Charter (1941) = FDR + ______ agreed on self-government and free ______.",
                "Lend-Lease Act (1941) = U.S. supplied ______ to the Allies as the '______ of democracy,' staying out of combat.",
            ],
            "wordbank": "quarantine · want · fear · Churchill · trade · weapons · arsenal",
            "model": "Lend-Lease (name) was a 1941 law letting the U.S. send weapons to the Allies without fighting (define) — for example, arms shipped to Britain (example).",
        },
    },
    "US.47": {
        "cues": [
            ("①  U.S. Response Before the War", "▶ Deck · DI 1 of 4", "How did the U.S. respond to Jewish refugees before the war?"),
            ("②  Liberation of the Concentration Camps", "▶ Deck · DI 2 of 4", "What did U.S. forces find as they liberated the camps?"),
            ("③  Post-War Immigration of Survivors", "▶ Deck · DI 3 of 4", "How did the U.S. respond to survivors after the war?"),
            ("④  Moral & Ethical Implications", "▶ Deck · DI 4 of 4", "What lasting moral questions does the Holocaust raise?"),
        ],
        "supports": {
            "code": "US.47",
            "title_tail": "build your notes, your way · US.47",
            "frames": [
                "Before the war, the U.S. limited Jewish refugees through strict immigration ______.",
                "As U.S. forces liberated the camps in 1945, they found mass death and starving ______.",
                "After the war, the Displaced Persons Act (1948) let Holocaust ______ enter the U.S.",
                "The Holocaust raises lasting moral questions about ______ and the duty to act.",
            ],
            "cloze": [
                "Before the war = tight immigration ______ (e.g., turning away the ship the ______) kept most refugees out.",
                "Liberation (1945) = U.S. troops found mass ______, disease, and survivors in camps such as ______.",
                "Post-war = the Displaced Persons Act (______) admitted Holocaust ______.",
                "Moral implications = the danger of ______ (standing by) and the responsibility to ______.",
            ],
            "wordbank": "quotas · St. Louis · death · Dachau · 1948 · survivors · indifference · intervene",
            "model": "The Displaced Persons Act (name) was a 1948 U.S. law admitting Holocaust survivors and other refugees (define) — for example, it let thousands of camp survivors resettle in America (example).",
        },
    },
    "US.48": {
        "cues": [
            ("①  Factors in the European Theater", "▶ Deck · DI 1 of 4", "What pulled the U.S. toward war in Europe?"),
            ("②  Factors in the Pacific Theater", "▶ Deck · DI 2 of 4", "What pulled the U.S. toward war in the Pacific?"),
            ("③  Attack on Pearl Harbor (Dec 7, 1941)", "▶ Deck · DI 3 of 4", "What happened at Pearl Harbor, and why did it matter?"),
            ("④  Consequences of American Entry", "▶ Deck · DI 4 of 4", "How did U.S. entry change the war?"),
        ],
        "supports": {
            "code": "US.48",
            "title_tail": "build your notes, your way · US.48",
            "frames": [
                "The U.S. was pulled toward war in Europe by German ______ attacks and aid to Britain.",
                "The U.S. was pulled toward war in the Pacific by Japanese ______ and the U.S. oil ______.",
                "On December 7, 1941, Japan attacked ______, and the next day the U.S. declared war.",
                "U.S. entry changed the war by adding its ______ and manpower to the Allied side.",
            ],
            "cloze": [
                "European Theater = German ______ warfare and Lend-Lease aid drew the U.S. toward Britain.",
                "Pacific Theater = Japan's ______ in Asia + the U.S. oil ______ raised tensions.",
                "Pearl Harbor (Dec 7, 1941) = surprise attack on the U.S. naval base in ______; FDR called it 'a date which will live in ______.'",
                "Consequences = U.S. ______ war; its ______ shifted the balance to the Allies.",
            ],
            "wordbank": "submarine · expansion · embargo · Hawaii · infamy · declared · industry",
            "model": "Pearl Harbor (name) was Japan's Dec. 7, 1941 surprise attack on the U.S. Pacific fleet in Hawaii (define) — it pushed the U.S. to declare war (example).",
        },
    },
    "US.49": {
        "cues": [
            ("①  Allied Political Leaders", "▶ Deck · DI 1 of 4", "Who led the Allied nations, and how?"),
            ("②  Allied Military Leaders", "▶ Deck · DI 2 of 4", "Which commanders shaped Allied strategy?"),
            ("③  Axis Leaders", "▶ Deck · DI 3 of 4", "Who led the Axis powers?"),
            ("④  Comparing Leadership Approaches", "▶ Deck · DI 4 of 4", "How did Allied and Axis leadership differ?"),
        ],
        "supports": {
            "code": "US.49",
            "title_tail": "build your notes, your way · US.49",
            "frames": [
                "Key Allied political leaders were FDR (U.S.), Winston ______ (UK), and Joseph ______ (USSR).",
                "Key Allied military leaders included Dwight ______ and George ______.",
                "The main Axis leaders were Adolf Hitler (Germany), Benito Mussolini (______), and Hideki Tojo (______).",
                "Allied leaders mostly led ______ nations, while Axis leaders were ______ dictators.",
            ],
            "cloze": [
                "Allied political = FDR, ______ (UK), ______ (USSR) — the 'Big Three.'",
                "Allied military = Gen. ______ (Supreme Allied Commander, Europe) and Gen. ______.",
                "Axis = Hitler (Germany), Mussolini (______), Tojo (______).",
                "Comparison = Allied leaders led ______ governments; Axis leaders were ______ dictators.",
            ],
            "wordbank": "Churchill · Stalin · Eisenhower · Patton · Italy · Japan · democratic · totalitarian",
            "model": "Dwight Eisenhower (name) was the Supreme Allied Commander in Europe (define) — for example, he directed the D-Day invasion (example).",
        },
    },
    "US.50": {
        "cues": [
            ("①  Battle of Midway (June 1942)", "▶ Deck · DI 1 of 4", "Why was Midway the Pacific turning point?"),
            ("②  Battle of Iwo Jima (Feb–Mar 1945)", "▶ Deck · DI 2 of 4", "Why was Iwo Jima so costly and important?"),
            ("③  Battle of Okinawa (Apr–Jun 1945)", "▶ Deck · DI 3 of 4", "How did Okinawa shape what came next?"),
            ("④  D-Day: Normandy Invasion (Jun 6, 1944)", "▶ Deck · DI 4 of 4", "How did D-Day open the Western Front?"),
        ],
        "supports": {
            "code": "US.50",
            "title_tail": "build your notes, your way · US.50",
            "frames": [
                "The Battle of Midway (1942) was a turning point because the U.S. sank four Japanese ______.",
                "Iwo Jima (1945) mattered because the U.S. needed the island's ______ for its planes.",
                "Okinawa (1945) was costly and signaled how deadly an invasion of ______ would be.",
                "D-Day (June 6, 1944) opened the Western Front with landings at ______, France.",
            ],
            "cloze": [
                "Midway (June 1942) = U.S. code-breaking helped sink four Japanese ______; the Pacific ______ turned.",
                "Iwo Jima (Feb–Mar 1945) = costly fight for ______ used by U.S. bombers.",
                "Okinawa (Apr–Jun 1945) = last major island; huge losses foreshadowed invading ______.",
                "D-Day (June 6, 1944) = Allied landing at ______ beaches, opening the ______ Front in Europe.",
            ],
            "wordbank": "carriers · tide · airfields · Japan · Normandy · Western",
            "model": "D-Day (name) was the June 6, 1944 Allied invasion of Normandy, France (define) — it opened the Western Front against Germany (example).",
        },
    },
    "US.51": {
        "cues": [
            ("①  Tuskegee Airmen", "▶ Deck · DI 1 of 5", "Who were the Tuskegee Airmen, and what did they achieve?"),
            ("②  442nd Regimental Combat Team", "▶ Deck · DI 2 of 5", "What made the 442nd so distinguished?"),
            ("③  101st Airborne Division", "▶ Deck · DI 3 of 5", "What was the 101st's role in the war?"),
            ("④  Navajo Code Talkers", "▶ Deck · DI 4 of 5", "How did the Code Talkers protect U.S. communications?"),
            ("⑤  Individual Sacrifice & Legacy", "▶ Deck · DI 5 of 5", "What legacy did these units leave?"),
        ],
        "supports": {
            "code": "US.51",
            "title_tail": "build your notes, your way · US.51",
            "frames": [
                "The Tuskegee Airmen were African American ______ known for their bomber-escort record.",
                "The 442nd Regimental Combat Team was made up of ______ American soldiers and became one of the most ______ units.",
                "The Navajo Code Talkers used their ______ to create an unbreakable military code.",
                "The 101st Airborne and these units left a legacy of courage that pushed toward ______ rights at home.",
            ],
            "cloze": [
                "Tuskegee Airmen = African American ______ (pilots) with an outstanding escort record.",
                "442nd = ______ American unit; the most ______ (medaled) of its size.",
                "Navajo Code Talkers = Marines who used the Navajo ______ as an unbreakable ______.",
                "Legacy = the 101st ______ Division and these units showed courage that advanced ______ rights.",
            ],
            "wordbank": "aviators · Japanese · decorated · language · code · Airborne · civil",
            "model": "The Navajo Code Talkers (name) were Marines who used the Navajo language as a battlefield code (define) — for example, they sent orders at Iwo Jima the enemy never broke (example).",
        },
    },
    "US.52": {
        "cues": [
            ("①  Factors Leading to Participation", "▶ Deck · DI 1 of 4", "Why did so many women enter the workforce?"),
            ("②  Challenges & Opportunities", "▶ Deck · DI 2 of 4", "What challenges and openings did women face?"),
            ("③  Impact on Production & Economy", "▶ Deck · DI 3 of 4", "How did women's work affect wartime production?"),
            ("④  Long-term Effects on Society", "▶ Deck · DI 4 of 4", "How did WWII change women's role long-term?"),
        ],
        "supports": {
            "code": "US.52",
            "title_tail": "build your notes, your way · US.52",
            "frames": [
                "Many women entered the workforce because men were away at ______ and factories needed ______.",
                "Women faced challenges such as lower ______ but gained new ______.",
                "Women's work boosted wartime ______, symbolized by '______ the Riveter.'",
                "In the long term, WWII expanded women's ______ and changed views of their ______.",
            ],
            "cloze": [
                "Participation = men were away at ______; industry needed ______ to build war goods.",
                "Challenges = unequal ______ and doubts, but new job ______.",
                "Production = women in factories/shipyards raised ______; icon = '______ the Riveter.'",
                "Long-term = more women in ______ work; shifted ideas about women's ______.",
            ],
            "wordbank": "war · workers · pay · opportunities · output · Rosie · paid · roles",
            "model": "'Rosie the Riveter' (name) was the symbol of women doing factory war work (define) — for example, women built planes and ships while men fought (example).",
        },
    },
    "US.53": {
        "cues": [
            ("①  Second Great Migration & Opportunity", "▶ Deck · DI 1 of 4", "Why and where did Black Americans move?"),
            ("②  Double V Campaign", "▶ Deck · DI 2 of 4", "What were the two victories of the Double V?"),
            ("③  Fair Employment Practices Committee", "▶ Deck · DI 3 of 4", "What did the FEPC change?"),
            ("④  Integration of the Armed Forces", "▶ Deck · DI 4 of 4", "How did the war push toward integration?"),
        ],
        "supports": {
            "code": "US.53",
            "title_tail": "build your notes, your way · US.53",
            "frames": [
                "In the Second Great Migration, Black Americans moved from the rural ______ to ______ cities for war jobs.",
                "The Double V Campaign called for victory over fascism ______ and victory over ______ at home.",
                "The Fair Employment Practices Committee (FEPC) banned racial ______ in ______ industries.",
                "Wartime service pushed toward ending ______ in the armed forces.",
            ],
            "cloze": [
                "Second Great Migration = Black families moved from the ______ to ______ and industrial cities.",
                "Double V = victory over fascism ______ + victory over ______ at home.",
                "FEPC (1941, EO 8802) = barred racial ______ in ______ jobs.",
                "Integration = wartime service pressed toward ending ______ (fully in 1948, EO 9981).",
            ],
            "wordbank": "South · Northern · abroad · racism · discrimination · defense · segregation",
            "model": "The Double V Campaign (name) demanded victory over fascism abroad and racism at home (define) — for example, Black newspapers urged winning the war and equal rights together (example).",
        },
    },
    "US.54": {
        "cues": [
            ("①  Executive Order 9066 & Internment", "▶ Deck · DI 1 of 4", "What did EO 9066 authorize?"),
            ("②  Constitutional Issues", "▶ Deck · DI 2 of 4", "Which constitutional rights were at stake?"),
            ("③  Korematsu v. United States (1944)", "▶ Deck · DI 3 of 4", "How did the Court rule, and why does it matter?"),
            ("④  Impact & Historical Lessons", "▶ Deck · DI 4 of 4", "What lasting lessons came from internment?"),
        ],
        "supports": {
            "code": "US.54",
            "title_tail": "build your notes, your way · US.54",
            "frames": [
                "Executive Order 9066 (1942) authorized the forced ______ of Japanese Americans to incarceration ______.",
                "Internment raised constitutional issues because people lost ______ without due ______.",
                "In Korematsu v. United States (1944), the Supreme Court ______ the removal as a wartime necessity.",
                "A lasting lesson is that fear must not override civil ______; in ______ the U.S. issued a formal apology.",
            ],
            "cloze": [
                "EO 9066 (1942) = ordered ______ of ~120,000 Japanese Americans to incarceration ______.",
                "Constitutional issues = loss of ______, property, and due ______ based on ancestry.",
                "Korematsu (1944) = Court ______ (upheld) the removal; widely condemned later.",
                "Lessons = protect civil ______; the Civil Liberties Act (______) gave an apology + redress.",
            ],
            "wordbank": "removal · camps · liberty · process · upheld · rights · 1988",
            "model": "Korematsu v. United States (name) was a 1944 Supreme Court case that upheld Japanese American internment (define) — a ruling later condemned as unjust (example).",
        },
    },
    "US.55": {
        "cues": [
            ("①  Rationing & Conservation", "▶ Deck · DI 1 of 4", "How did rationing reshape daily life?"),
            ("②  War Bonds & Propaganda", "▶ Deck · DI 2 of 4", "How did the government fund and sell the war?"),
            ("③  Migration, Factory Conversion, Bracero", "▶ Deck · DI 3 of 4", "How did the economy retool for war?"),
            ("④  Tennessee's Wartime Role", "▶ Deck · DI 4 of 4", "How did Tennessee contribute to the war effort?"),
        ],
        "supports": {
            "code": "US.55",
            "title_tail": "build your notes, your way · US.55",
            "frames": [
                "Rationing limited goods like ______ and sugar so the military had enough.",
                "The government funded the war by selling war ______ and used ______ to build support.",
                "The ______ Program brought Mexican ______ to fill wartime labor shortages.",
                "Tennessee contributed through sites like Oak Ridge and TVA ______.",
            ],
            "cloze": [
                "Rationing = limited ______, sugar, and rubber; families used ration ______.",
                "War bonds = citizens lent money by buying ______; ______ posters sold the effort.",
                "Economy = plants retooled for war; the ______ Program hired Mexican farm ______.",
                "Tennessee = Oak Ridge and war plants; TVA ______ powered production.",
            ],
            "wordbank": "gasoline · books · bonds · propaganda · Bracero · workers · electricity",
            "model": "The Bracero Program (name) was a wartime agreement bringing Mexican laborers to U.S. farms (define) — for example, braceros harvested crops while American men were at war (example).",
        },
    },
    "US.56": {
        "cues": [
            ("①  Oak Ridge, Tennessee Selection", "▶ Deck · DI 1 of 4", "Why was Oak Ridge, TN chosen?"),
            ("②  Manhattan Project Overview", "▶ Deck · DI 2 of 4", "What was the Manhattan Project?"),
            ("③  Rationale for Using Atomic Weapons", "▶ Deck · DI 3 of 4", "Why did the U.S. use the atomic bomb?"),
            ("④  The Ethical Debate", "▶ Deck · DI 4 of 4", "What ethical questions does the bomb raise?"),
        ],
        "supports": {
            "code": "US.56",
            "title_tail": "build your notes, your way · US.56",
            "frames": [
                "Oak Ridge, Tennessee was chosen for its space, secrecy, and access to TVA ______.",
                "The Manhattan Project was the secret U.S. effort to build the first atomic ______.",
                "The U.S. used the atomic bomb to force Japan's quick ______ and avoid a costly ______.",
                "The ethical debate weighs a fast end to the war against the ______ deaths at Hiroshima and ______.",
            ],
            "cloze": [
                "Oak Ridge = secret TN site chosen for space, secrecy, and ______ power to enrich ______.",
                "Manhattan Project = secret program (led by ______) that built the atomic ______.",
                "Rationale = force Japan's ______ and avoid a bloody ______ of the home islands.",
                "Ethics = a fast end vs. mass ______ deaths at Hiroshima & ______.",
            ],
            "wordbank": "electricity · uranium · Oppenheimer · bomb · surrender · invasion · civilian · Nagasaki",
            "model": "The Manhattan Project (name) was the secret U.S. program that developed the atomic bomb (define) — for example, work at Oak Ridge, TN enriched uranium for the weapon (example).",
        },
    },
    "US.57": {
        "cues": [
            ("①  Yalta Conference (Feb 1945)", "▶ Deck · DI 1 of 4", "What did the Big Three decide at Yalta?"),
            ("②  Potsdam Conference (Jul–Aug 1945)", "▶ Deck · DI 2 of 4", "What changed by Potsdam?"),
            ("③  Cold War Origins", "▶ Deck · DI 3 of 4", "How did wartime diplomacy seed the Cold War?"),
            ("④  Assessing Allied Diplomacy", "▶ Deck · DI 4 of 4", "How well did Allied diplomacy work?"),
        ],
        "supports": {
            "code": "US.57",
            "title_tail": "build your notes, your way · US.57",
            "frames": [
                "At the Yalta Conference (Feb 1945), the Big Three planned to divide ______ and hold free ______ in Eastern Europe.",
                "By the Potsdam Conference (1945), new leaders met and tensions rose over ______ Europe.",
                "The Cold War began as the U.S. and the ______ split over ideology and ______.",
                "Allied diplomacy succeeded in ______ the war but left a divided ______.",
            ],
            "cloze": [
                "Yalta (Feb 1945) = FDR, Churchill, Stalin agreed to divide ______ and hold free ______ (Stalin later broke this).",
                "Potsdam (1945) = new leaders (______); dispute over ______ Europe grew.",
                "Cold War origins = U.S. vs. ______ rivalry over ideology and ______.",
                "Assessment = diplomacy ______ the alliance to win, but left a divided ______.",
            ],
            "wordbank": "Germany · elections · Truman · Eastern · USSR · power · held · Europe",
            "model": "The Yalta Conference (name) was the Feb. 1945 meeting where the Big Three planned postwar Europe (define) — for example, they agreed to divide Germany into occupation zones (example).",
        },
    },
    "US.58": {
        "cues": [
            ("①  Lessons from the League's Failure", "▶ Deck · DI 1 of 4", "Why did the League fail, and what was learned?"),
            ("②  Cordell Hull's Role", "▶ Deck · DI 2 of 4", "Why is Tennessean Cordell Hull the 'Father of the UN'?"),
            ("③  UN Goals & Structure", "▶ Deck · DI 3 of 4", "What are the UN's goals and structure?"),
            ("④  UN Legacy & Limitations", "▶ Deck · DI 4 of 4", "What has the UN achieved, and where is it limited?"),
        ],
        "supports": {
            "code": "US.58",
            "title_tail": "build your notes, your way · US.58",
            "frames": [
                "The League of Nations failed partly because the U.S. never ______ and it could not ______ its decisions.",
                "Tennessean Cordell ______ helped plan the UN and is called its 'Father of the United ______.'",
                "The UN's main goal is to keep international ______ through bodies like the ______ Council.",
                "The UN has succeeded in peacekeeping but is limited by the ______ power of major nations.",
            ],
            "cloze": [
                "League's failure = the U.S. never ______; no power to ______ its decisions.",
                "Cordell Hull = U.S. ______ of State; 'Father of the United ______' (Nobel Peace Prize).",
                "UN structure = keep ______; key organs = General Assembly + ______ Council.",
                "Legacy/limits = peacekeeping & aid, but the ______ can block ______.",
            ],
            "wordbank": "joined · enforce · Secretary · Nations · peace · Security · veto · action",
            "model": "Cordell Hull (name) was the U.S. Secretary of State called the 'Father of the United Nations' (define) — for example, he helped design the UN and won the 1945 Nobel Peace Prize (example).",
        },
    },
}


SELF_CHECK = "☐  I named the idea      ☐  I defined it in my own words      ☐  I gave an example      ☐  A reader could follow it"


def _has_supports(doc, code):
    for ch in list(doc.element.body):
        if "NOTES SUPPORTS" in _ptext(ch) and code in _ptext(ch):
            return True
    return False


def apply_standard(doc, code, ref_supports_block):
    cfg = STANDARDS[code]
    # FRONT — expand rows to match the DI-segment count, then seed cues (idempotent:
    # ensure_cue_rows is a no-op once the rows exist; seed clears + re-writes the cue cells)
    tbl = find_cornell_table(doc, code)
    ensure_cue_rows(tbl, len(cfg["cues"]))
    seed_guided_cornell(tbl, cfg["cues"])
    # BACK — clone the reference NOTES SUPPORTS for any standard that doesn't already have one.
    # (US.45 is skipped only when its own block IS the reference living in this same doc.)
    if not _has_supports(doc, code):
        anchor = None
        for ch in list(doc.element.body):
            if ch.tag == qn("w:p") and _ptext(ch).startswith("Activity 4") and code in _ptext(ch):
                anchor = ch; break
        if anchor is None:
            raise ValueError(f"Activity 4 anchor for {code} not found")
        clone_notes_supports(ref_supports_block, cfg["supports"], anchor)


def main():
    # Usage:
    #   build_guided_notes.py IN.docx OUT.docx [US.xx] [--ref REF.docx]
    # --ref points at a workbook that already contains the LOCKED US.45 NOTES SUPPORTS block to
    # clone for formatting parity. Omit it when IN.docx itself already carries that block.
    argv = [a for a in sys.argv[1:]]
    ref_path = None
    if "--ref" in argv:
        i = argv.index("--ref"); ref_path = argv[i + 1]; del argv[i:i + 2]
    if len(argv) < 2:
        print(__doc__)
        sys.exit(1)
    src, out = argv[0], argv[1]
    only = argv[2] if len(argv) > 2 else None
    doc = Document(src)
    ref_doc = Document(ref_path) if ref_path else doc
    ref_block = find_notes_supports_block(ref_doc, "US.45")  # the locked reference to clone
    codes = [only] if only else list(STANDARDS.keys())
    for code in codes:
        apply_standard(doc, code, ref_block)
        print(f"applied guided notes → {code}")
    doc.save(out)
    print(f"saved {out}  (render + run the QC gate — zero blank pages, notebook lines visible)")


if __name__ == "__main__":
    main()
