#!/usr/bin/env python3
"""Homestead Act of 1862 — student-facing, print-first handouts (WeasyPrint, no docx):

  US01_Homestead_Reading_TwoColumn_<ts>.pdf
      Full excerpt as a TWO-COLUMN chart (left = the Act's own words, chunked;
      right = "In shorter words"). Section 1 on page 1, Section 2 on its own
      page, Section 3 starts a new page (Sections 3-5 together).

  US01_Homestead_FullText_Continuous_<ts>.pdf
      The same excerpt as ONE continuous reading — no columns, no chunking,
      no divisions — Sections 1-5 verbatim, flowing.

  US01_Homestead_HIPP_Chart_<ts>.pdf
      HIPP source-analysis graphic organizer (analysis only, not an essay).

Left-column / continuous text is the verbatim public-domain Homestead Act of
1862 (12 Stat. 392; approved May 20, 1862), verified against the U.S. National
Archives, NPS, Teaching American History, and the ND State Historical Society
transcript. The two-column right side is a plain short restatement, clearly
headed. All [square brackets] are editorial. America 250 palette; ™ not (R).
"""
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "HistoryHack_Platinum/homestead_reading_hipp"
OUT.mkdir(parents=True, exist_ok=True)
TS = datetime.now(timezone.utc)
STAMP = TS.strftime("%Y%m%d_%H%M")
ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ")

NAVY, RED, GOLD, CARD, BORDER, INK = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF", "#C9C2B4", "#20262E"

CITE = ("Homestead Act of 1862, 12 Stat. 392 (37th Cong., Sess. II, ch. 75); approved May 20, 1862. "
        "U.S. National Archives (RG 11). Public domain.")
COPYRIGHT = ("© 2026 TroopToTeacher Technologies LLC &middot; U.S. History Hack™. All rights reserved. "
             "Licensed for single-classroom reproduction.")

# Two-column data — per section: (number, [ (verbatim chunk, short restatement), ... ])
CHART = [
    ("1", [
        ("<b>Be it enacted</b> &hellip; That any person who is the head of a family, or who has arrived at the "
         "age of twenty-one years,", "Any adult 21 or older, or the head of a family,"),
        ("and is a citizen of the United States, or who shall have filed his declaration of intention to "
         "become such,", "who is a U.S. citizen (or is becoming one),"),
        ("and who has never borne arms against the United States Government or given aid and comfort to its "
         "enemies,", "and who never fought against the United States,"),
        ("shall &hellip; be entitled to enter one quarter section or a less quantity of unappropriated public "
         "lands,", "could claim up to 160 acres (a quarter section) of public land."),
        ("subject to preemption at one dollar and twenty-five cents, or less, per acre;",
         "Most of that land cost $1.25 an acre or less."),
        ("or eighty acres or less of such unappropriated lands, at two dollars and fifty cents per acre,",
         "Smaller 80-acre plots cost $2.50 an acre."),
        ("to be located in a body &hellip; and after the same shall have been surveyed.",
         "The land had to be in one block and already surveyed."),
    ]),
    ("2", [
        ("That the person applying &hellip; shall &hellip; make affidavit before the said register or receiver",
         "To apply, you went to the land office and signed a sworn statement (an affidavit)."),
        ("that he or she is the head of a family, or is twenty-one years or more of age, or shall have "
         "performed service in the army or navy of the United States,",
         "You swore you were 21+, a head of family, or a veteran,"),
        ("and that he has never borne arms against the Government of the United States or given aid and "
         "comfort to its enemies,", "that you never fought against the U.S.,"),
        ("and that said entry is made for the purpose of actual settlement and cultivation, and not &hellip; "
         "for the use or benefit of any other person &hellip;",
         "and that the land was for your own farm — not secretly for someone else."),
        ("and on payment of ten dollars, he or she shall thereupon be permitted to enter the quantity of land "
         "specified:", "You paid a $10 fee and could then claim the land."),
        ("Provided, however, That no certificate shall be given or patent issued therefor until the expiration "
         "of five years from the date of such entry;", "But you did not get the title (patent) for five years."),
        ("and &hellip; the person making such entry shall prove by two credible witnesses that he, she, or they "
         "have resided upon or cultivated the same for the term of five years &hellip;",
         "After five years, two witnesses had to prove you lived on and farmed the land."),
        ("and shall make affidavit that no part of said land has been alienated, and that he has borne true "
         "allegiance to the Government of the United States;",
         "You also swore you had not sold any of it and had stayed loyal to the U.S."),
        ("then &hellip; he, she, or they, if at that time a citizen of the United States, shall be entitled to "
         "a patent.", "Then, if a citizen, you finally got the title to the land."),
    ]),
    ("3", [
        ("And be it further enacted, That the register of the land office shall note all such applications "
         "&hellip; and keep a register of all such entries,", "The land officer recorded every claim in official books,"),
        ("and make return thereof to the General Land Office, together with the proof upon which they have been "
         "founded.", "and sent the records and proof to the main Land Office."),
    ]),
    ("4", [
        ("And be it further enacted, That no lands acquired under the provisions of this act shall in any event "
         "become liable to the satisfaction of any debt or debts contracted prior to the issuing of the patent "
         "therefor.", "Old debts could not be used to take your homestead before you earned the title."),
    ]),
    ("5", [
        ("And be it further enacted, That if &hellip; the person having filed such affidavit shall have actually "
         "changed his or her residence, or abandoned the said land for more than six months at any time,",
         "If you moved away or left the land for more than six months,"),
        ("then and in that event the land so entered shall revert to the government.",
         "you lost it — the land went back to the government."),
    ]),
]

# Which sections share a page in the two-column doc: Sec 1 | Sec 2 | Sec 3-5.
PAGE_GROUPS = [["1"], ["2"], ["3", "4", "5"]]

# Full continuous verbatim text (for the undivided document). [brackets] = editorial.
FULL_SECTIONS = [
    ("1",
     "<b>Be it enacted</b> by the Senate and House of Representatives of the United States of America in "
     "Congress assembled, That any person who is the head of a family, or who has arrived at the age of "
     "twenty-one years, and is a citizen of the United States, or who shall have filed his declaration of "
     "intention to become such, as required by the naturalization laws of the United States, and who has "
     "never borne arms against the United States Government or given aid and comfort to its enemies, shall, "
     "from and after the first January, eighteen hundred and sixty-three, be entitled to enter one quarter "
     "section [160 acres] or a less quantity of unappropriated public lands, upon which said person may have "
     "filed a preemption claim, or which may, at the time the application is made, be subject to preemption "
     "at one dollar and twenty-five cents, or less, per acre; or eighty acres or less of such unappropriated "
     "lands, at two dollars and fifty cents per acre, to be located in a body, in conformity to the legal "
     "subdivisions of the public lands, and after the same shall have been surveyed."),
    ("2",
     "And be it further enacted, That the person applying for the benefit of this act shall, upon application "
     "to the register of the land office in which he or she is about to make such entry, make affidavit before "
     "the said register or receiver that he or she is the head of a family, or is twenty-one years or more of "
     "age, or shall have performed service in the army or navy of the United States, and that he has never "
     "borne arms against the Government of the United States or given aid and comfort to its enemies, and that "
     "such application is made for his or her exclusive use and benefit, and that said entry is made for the "
     "purpose of actual settlement and cultivation, and not either directly or indirectly for the use or "
     "benefit of any other person or persons whomsoever; and upon filing the said affidavit with the register "
     "or receiver, and on payment of ten dollars, he or she shall thereupon be permitted to enter the quantity "
     "of land specified: Provided, however, That no certificate shall be given or patent [legal title] issued "
     "therefor until the expiration of five years from the date of such entry; and if, at the expiration of "
     "such time, or at any time within two years thereafter, the person making such entry [or, if that person "
     "has died, the widow, heirs, or devisee] shall prove by two credible witnesses that he, she, or they have "
     "resided upon or cultivated the same for the term of five years immediately succeeding the time of filing "
     "the affidavit aforesaid, and shall make affidavit that no part of said land has been alienated, and that "
     "he has borne true allegiance to the Government of the United States; then, in such case, he, she, or "
     "they, if at that time a citizen of the United States, shall be entitled to a patent, as in other cases "
     "provided for by law. [Section 2 also includes a provision for the orphaned children of a settler who "
     "dies.]"),
    ("3",
     "And be it further enacted, That the register of the land office shall note all such applications on the "
     "tract books and plats of his office, and keep a register of all such entries, and make return thereof to "
     "the General Land Office, together with the proof upon which they have been founded."),
    ("4",
     "And be it further enacted, That no lands acquired under the provisions of this act shall in any event "
     "become liable to the satisfaction of any debt or debts contracted prior to the issuing of the patent "
     "therefor."),
    ("5",
     "And be it further enacted, That if, at any time after the filing of the affidavit, as required in the "
     "second section of this act, and before the expiration of the five years aforesaid, it shall be proven, "
     "after due notice to the settler, to the satisfaction of the register of the land office, that the person "
     "having filed such affidavit shall have actually changed his or her residence, or abandoned the said land "
     "for more than six months at any time, then and in that event the land so entered shall revert to the "
     "government."),
]

CLOSING_NOTE = ("[The Act&rsquo;s remaining sections (6&ndash;8) cover the land-office fees, penalties for "
                "making a false affidavit, and protection for settlers&rsquo; existing pre-emption rights.]")

HIPP = [
    ("H", "Historical Context",
     "When and where was this law written, and what was happening in the country at that time?",
     "This law was written in ______, during ______, when the country was ______."),
    ("I", "Intended Audience",
     "Who was this law written for? Who was supposed to read it or obey it?",
     "This law was meant for ______, because ______."),
    ("P", "Point of View",
     "Whose side does the law show? Whose point of view is left out?",
     "The law shows the point of view of ______. It leaves out ______."),
    ("P", "Purpose",
     "Why did the government create this law? What did it want to happen?",
     "The government made this law in order to ______."),
]

COPYR_CSS = (".copyr { margin-top:9px; border-top:2px solid %(GOLD)s; padding-top:5px; text-align:center; "
             "font-family:'DejaVu Sans'; font-size:8.6pt; color:%(NAVY)s; }" % dict(GOLD=GOLD, NAVY=NAVY))


def copyr_block():
    return f'<div class="copyr">{COPYRIGHT}</div>'


# ---------------------------------------------------------------------------
def reading_html():
    css = ("""
    * { box-sizing:border-box; }
    body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; }
    .title { border-left:14px solid %(RED)s; background:%(NAVY)s; color:#fff; padding:14px 20px; }
    .title .kick { font-family:'DejaVu Sans'; color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:11.5pt; }
    .title h1 { font-size:23pt; margin:5px 0 2px; }
    .title .sub { font-size:12pt; color:#DCE6F1; font-style:italic; }
    .wrap { padding:14px 4px 0; }
    .dir { font-family:'DejaVu Sans'; font-size:11.5pt; color:%(NAVY)s; font-weight:bold; margin:0 0 12px; }
    .grp { page-break-before:always; }
    table.chart { width:100%%; border-collapse:collapse; margin-bottom:2px; }
    table.chart th { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; font-size:10.5pt; text-align:left;
      padding:5px 11px; }
    .secrow td { background:%(GOLD)s; color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; font-size:11.5pt;
      padding:4px 11px; }
    tr { page-break-inside:avoid; }
    td.l { width:52%%; border:1pt solid %(BORDER)s; padding:6px 10px; font-size:10.5pt; line-height:1.36; }
    td.r { width:48%%; border:1pt solid %(BORDER)s; padding:6px 10px; font-size:11pt; line-height:1.36;
      background:#FBFAF6; font-family:'DejaVu Sans'; color:#24303F; }
    .note { font-size:10.5pt; line-height:1.5; color:#43506A; font-style:italic; margin:12px 0 0;
      border-left:4px solid %(BORDER)s; padding-left:12px; }
    .src { font-family:'DejaVu Sans'; font-size:9pt; color:#5C6470; font-style:italic; margin-top:12px; }
    %(COPYR)s
    @page { size:Letter portrait; margin:0.6in 0.7in 0.8in 0.7in;
      @bottom-left { content:"The Homestead Act of 1862 — Reading (two-column)"; font:9pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:9pt 'DejaVu Sans'; color:#5C6470; } }
    @page:first { margin-top:0; }
    """ % dict(INK=INK, NAVY=NAVY, RED=RED, GOLD=GOLD, CARD=CARD, BORDER=BORDER, COPYR=COPYR_CSS))

    hdr = ('<tr><th style="width:52%">The law&rsquo;s own words (Homestead Act, 1862)</th>'
           '<th style="width:48%">In shorter words</th></tr>')
    chart_map = dict(CHART)
    groups_html = ""
    for gi, group in enumerate(PAGE_GROUPS):
        rows = hdr
        for num in group:
            rows += f'<tr class="secrow"><td colspan="2">Section {num}</td></tr>'
            for left, right in chart_map[num]:
                rows += f'<tr><td class="l">{left}</td><td class="r">{right}</td></tr>'
        cls = "grp" if gi > 0 else ""
        tail = ""
        if gi == len(PAGE_GROUPS) - 1:
            tail = (f'<div class="note">{CLOSING_NOTE}</div>'
                    f'<div class="src">Source: {CITE}  ·  Generated {ISO}</div>{copyr_block()}')
        groups_html += f'<div class="{cls}"><table class="chart">{rows}</table>{tail}</div>'

    body = (f'<div class="title"><div class="kick">U.S. HISTORY HACK™ · STANDARD US.01</div>'
            f'<h1>The Homestead Act of 1862</h1>'
            f'<div class="sub">An Act to secure Homesteads to actual Settlers on the Public Domain — excerpt</div></div>'
            f'<div class="wrap"><div class="dir">Directions: Read the law&rsquo;s own words on the left. '
            f'The right column says the same thing in a shorter sentence.</div>'
            f'{groups_html}</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


# ---------------------------------------------------------------------------
def continuous_html():
    css = ("""
    * { box-sizing:border-box; }
    body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; }
    .title { border-left:14px solid %(RED)s; background:%(NAVY)s; color:#fff; padding:15px 20px; }
    .title .kick { font-family:'DejaVu Sans'; color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:12pt; }
    .title h1 { font-size:25pt; margin:6px 0 2px; }
    .title .sub { font-size:13pt; color:#DCE6F1; font-style:italic; }
    .wrap { padding:20px 6px 0; }
    p.sec { font-size:13.5pt; line-height:1.6; margin:0 0 15px; text-align:justify; }
    p.sec .lab { font-family:'DejaVu Sans'; font-weight:bold; color:%(NAVY)s; }
    .grp { page-break-before:always; }
    .note { font-size:11.5pt; line-height:1.55; color:#43506A; font-style:italic; margin:6px 0 0;
      border-left:4px solid %(BORDER)s; padding-left:12px; }
    .src { font-family:'DejaVu Sans'; font-size:9.5pt; color:#5C6470; font-style:italic; margin-top:16px; }
    %(COPYR)s
    @page { size:Letter portrait; margin:0.75in 0.8in 0.85in 0.8in;
      @bottom-left { content:"The Homestead Act of 1862 — full text (excerpt)"; font:9pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:9pt 'DejaVu Sans'; color:#5C6470; } }
    @page:first { margin-top:0; }
    """ % dict(INK=INK, NAVY=NAVY, RED=RED, GOLD=GOLD, BORDER=BORDER, COPYR=COPYR_CSS))
    full_map = dict(FULL_SECTIONS)
    groups_html = ""
    for gi, group in enumerate(PAGE_GROUPS):
        inner = "".join(f'<p class="sec"><span class="lab">Section {num}.</span> {full_map[num]}</p>' for num in group)
        tail = ""
        if gi == len(PAGE_GROUPS) - 1:
            tail = (f'<div class="note">{CLOSING_NOTE}</div>'
                    f'<div class="src">Source: {CITE}  ·  Generated {ISO}</div>{copyr_block()}')
        groups_html += f'<div class="{"grp" if gi > 0 else ""}">{inner}{tail}</div>'
    body = (f'<div class="title"><div class="kick">U.S. HISTORY HACK™ · STANDARD US.01</div>'
            f'<h1>The Homestead Act of 1862</h1>'
            f'<div class="sub">An Act to secure Homesteads to actual Settlers on the Public Domain — excerpt</div></div>'
            f'<div class="wrap">{groups_html}</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


# ---------------------------------------------------------------------------
def hipp_html():
    css = """
    * { box-sizing:border-box; }
    body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; }
    .title { border-left:14px solid %(RED)s; background:%(NAVY)s; color:#fff; padding:14px 20px; }
    .title .kick { font-family:'DejaVu Sans'; color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:11pt; }
    .title h1 { font-size:22pt; margin:5px 0 2px; }
    .title .sub { font-size:12pt; color:#DCE6F1; }
    .wrap { padding:11px 4px 0; }
    .lead { font-family:'DejaVu Sans'; font-size:11pt; color:%(NAVY)s; margin:0 0 5px; }
    .lead b { color:%(RED)s; }
    .namebar { display:flex; gap:14px; font-family:'DejaVu Sans'; font-size:9.5pt; color:#43506A; margin:0 0 8px; }
    .namebar .f { flex:1; border-bottom:1pt solid %(BORDER)s; padding-bottom:2px; }
    .box { border:1.2pt solid %(BORDER)s; border-radius:7px; margin:0 0 4px; page-break-inside:avoid; }
    .box .hd { background:%(NAVY)s; color:#fff; display:flex; align-items:center; gap:12px; padding:4px 12px; }
    .box .hd .L { background:%(GOLD)s; color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; font-size:15pt;
      width:27px; height:27px; border-radius:6px; text-align:center; line-height:27px; }
    .box .hd .nm { font-family:'DejaVu Sans'; font-weight:bold; font-size:13pt; }
    .box .bd { padding:6px 13px; }
    .q { font-size:10.8pt; margin:0 0 3px; }
    .q b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
    .stem { font-family:'DejaVu Sans'; font-size:10pt; color:%(NAVY)s; background:%(CARD)s; border:1pt solid %(BORDER)s;
      border-radius:5px; padding:5px 9px; margin:0 0 5px; }
    .stem b { color:%(RED)s; }
    .wl { border-bottom:0.7pt solid #AEB6C2; height:0.27in; }
    .foot { font-family:'DejaVu Sans'; font-size:9.5pt; color:%(NAVY)s; background:%(CARD)s; border:1pt solid %(GOLD)s;
      border-radius:6px; padding:7px 12px; margin-top:2px; }
    %(COPYR)s
    @page { size:Letter portrait; margin:0.6in 0.7in 0.75in 0.7in;
      @bottom-left { content:"HIPP Source Analysis — The Homestead Act of 1862"; font:8.5pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:8.5pt 'DejaVu Sans'; color:#5C6470; } }
    @page:first { margin-top:0; }
    """ % dict(INK=INK, NAVY=NAVY, RED=RED, GOLD=GOLD, CARD=CARD, BORDER=BORDER, COPYR=COPYR_CSS)

    def wl(n):
        return "".join('<div class="wl"></div>' for _ in range(n))

    boxes = ""
    for L, name, q, stem in HIPP:
        boxes += (f'<div class="box"><div class="hd"><div class="L">{L}</div><div class="nm">{name}</div></div>'
                  f'<div class="bd"><div class="q"><b>Think about:</b> {q}</div>'
                  f'<div class="stem"><b>Sentence starter:</b> {stem}</div>{wl(2)}</div></div>')
    body = (f'<div class="title"><div class="kick">U.S. HISTORY HACK™ · STANDARD US.01</div>'
            f'<h1>HIPP Source Analysis</h1><div class="sub">The Homestead Act of 1862</div></div>'
            f'<div class="wrap">'
            f'<div class="lead"><b>HIPP</b> helps you analyze a primary source. Look back at the reading and, for each '
            f'part, write what you notice. <b>We are analyzing the source — not writing an essay yet.</b></div>'
            f'<div class="namebar"><div class="f">Name: </div><div class="f">Class / Period: </div><div class="f">Date: </div></div>'
            f'{boxes}'
            f'<div class="foot">Tip: use the Act&rsquo;s numbered Sections as your evidence — point to a Section '
            f'(for example, &ldquo;Section&nbsp;5 shows &hellip;&rdquo;) instead of copying long sentences.</div>'
            f'{copyr_block()}</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


# ---------------------------------------------------------------------------
def teacher_html():
    """Plain-language (~grade 3-4) version of the full excerpt, chunked by section.
    TEACHER REFERENCE ONLY — clearly marked not for student distribution."""
    css = ("""
    * { box-sizing:border-box; }
    body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; }
    .title { border-left:14px solid %(RED)s; background:%(NAVY)s; color:#fff; padding:14px 20px; }
    .title .kick { font-family:'DejaVu Sans'; color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:11.5pt; }
    .title h1 { font-size:22pt; margin:5px 0 2px; }
    .title .sub { font-size:12pt; color:#DCE6F1; font-style:italic; }
    .warn { background:%(RED)s; color:#fff; font-family:'DejaVu Sans'; font-weight:bold; font-size:11pt;
      text-align:center; padding:7px 12px; letter-spacing:.3px; }
    .wrap { padding:14px 6px 0; }
    .lead { font-family:'DejaVu Sans'; font-size:10.5pt; color:%(NAVY)s; margin:0 0 12px; }
    .sec { margin:0 0 13px; page-break-inside:avoid; }
    .sec .h { font-family:'DejaVu Sans'; font-weight:bold; color:#fff; background:%(NAVY)s; font-size:12pt;
      display:inline-block; padding:3px 14px; border-radius:5px; margin:0 0 7px; }
    .sec ul { margin:2px 0 0 20px; padding:0; }
    .sec li { font-size:12.5pt; line-height:1.5; margin:4px 0; }
    .src { font-family:'DejaVu Sans'; font-size:9pt; color:#5C6470; font-style:italic; margin-top:14px; }
    %(COPYR)s
    @page { size:Letter portrait; margin:0.6in 0.7in 0.8in 0.7in;
      @bottom-left { content:"TEACHER REFERENCE — plain-language Homestead Act (not for students)"; font:8.5pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:8.5pt 'DejaVu Sans'; color:#5C6470; } }
    @page:first { margin-top:0; }
    """ % dict(INK=INK, NAVY=NAVY, RED=RED, GOLD=GOLD, BORDER=BORDER, COPYR=COPYR_CSS))
    secs = ""
    for num, chunks in CHART:
        items = "".join(f'<li>{right}</li>' for _left, right in chunks)
        secs += f'<div class="sec"><div class="h">Section {num}</div><ul>{items}</ul></div>'
    body = (f'<div class="title"><div class="kick">U.S. HISTORY HACK™ · STANDARD US.01 · TEACHER REFERENCE</div>'
            f'<h1>The Homestead Act — in Plain Words</h1>'
            f'<div class="sub">Chunked plain-language version (≈ reading grade 3–4)</div></div>'
            f'<div class="warn">TEACHER PLANNING REFERENCE — NOT FOR STUDENT DISTRIBUTION</div>'
            f'<div class="wrap">'
            f'<div class="lead">Use this to plan your questions and check understanding. Students read the primary '
            f'source (the reading and/or the two-column chart) — this simplified version stays with you.</div>'
            f'{secs}'
            f'<div class="tnote" style="font-size:10pt;color:#43506A;font-style:italic;border-left:4px solid '
            f'{BORDER};padding-left:12px;margin-top:6px">This is a plain-language paraphrase for teacher planning — it '
            f'is not the primary source. The verbatim law is on the student reading.</div>'
            f'<div class="src">Paraphrase of the Homestead Act of 1862 (12 Stat. 392, public domain), by '
            f'TroopToTeacher Technologies LLC · Generated {ISO}</div>{copyr_block()}</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    scratch = OUT / "_html"
    scratch.mkdir(exist_ok=True)
    jobs = [
        (f"US01_Homestead_Reading_TwoColumn_{STAMP}", reading_html()),
        (f"US01_Homestead_FullText_{STAMP}", continuous_html()),
        (f"US01_Homestead_TEACHER_PlainWords_{STAMP}", teacher_html()),
        (f"US01_Homestead_HIPP_Chart_{STAMP}", hipp_html()),
    ]
    for base, html in jobs:
        HTML(string=html).write_pdf(str(OUT / f"{base}.pdf"))
        (scratch / f"{base}.html").write_text(html, encoding="utf-8")
        print("wrote", base + ".pdf")
    print("html sidecars:", scratch)
    print("out:", OUT, "| ts", ISO)


if __name__ == "__main__":
    main()
