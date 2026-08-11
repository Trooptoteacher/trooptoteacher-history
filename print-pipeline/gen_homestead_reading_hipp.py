#!/usr/bin/env python3
"""Homestead Act of 1862 — two separate, student-facing, print-first handouts (WeasyPrint, no docx):

  US01_Homestead_Reading_LargePrint_<ts>.pdf
      Just the authentic verbatim excerpt, LARGE print, plain. No UDL labels,
      no questions, no boxes — just the text, numbered for reference.

  US01_Homestead_HIPP_Chart_<ts>.pdf
      A HIPP source-analysis graphic organizer (Historical context · Intended
      audience · Point of view · Purpose) with a guiding question + sentence
      starter + write-space for each. Analysis only — not an essay.

Nothing labeled "UDL" appears on either student page. Statute text is a verbatim
public-domain excerpt of the Homestead Act of 1862 (12 Stat. 392; approved
May 20, 1862). America 250 palette; ™ not (R); version timestamp in filename + footer.
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

# Authentic verbatim excerpt, light inline [clarifications] only. Numbered for reference.
SEGMENTS = [
    "That any person who is the head of a family, or who has arrived at the age of twenty-one years, "
    "and is a citizen of the United States, or who shall have filed his declaration of intention to "
    "become such &hellip; shall &hellip; be entitled to enter one quarter section [160 acres] &hellip; "
    "of unappropriated public lands &hellip;",
    "&hellip; and who has never borne arms against the United States Government or given aid and comfort "
    "to its enemies &hellip;",
    "&hellip; subject to preemption at one dollar and twenty-five cents [$1.25], or less, per acre.",
    "[Sec. 2.] &hellip; the person applying &hellip; shall make affidavit [a sworn promise] &hellip; that "
    "said entry is made for the purpose of actual settlement and cultivation, and not &hellip; for the use "
    "or benefit of any other person &hellip;",
    "&hellip; and on payment of ten dollars [$10], he or she shall thereupon be permitted to enter the "
    "quantity of land specified.",
    "[Sec. 3.] &hellip; no certificate shall be given, or patent [legal title] issued &hellip; until the "
    "expiration of five years from the date of such entry &hellip;",
    "&hellip; [the settler] shall prove by two credible witnesses that he, she, or they have resided upon "
    "or cultivated the same for the term of five years &hellip;",
    "&hellip; [but] if &hellip; [the settler] shall have &hellip; abandoned the said land for more than "
    "six months at any time, then &hellip; the land so entered shall revert to [go back to] the government.",
]

# HIPP: (letter, name, guiding question, sentence starter)
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


# ---------------------------------------------------------------------------
def reading_html():
    css = """
    * { box-sizing:border-box; }
    body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; }
    .title { border-left:14px solid %(RED)s; background:%(NAVY)s; color:#fff; padding:16px 20px; }
    .title .kick { font-family:'DejaVu Sans'; color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:12pt; }
    .title h1 { font-size:26pt; margin:6px 0 2px; }
    .title .sub { font-size:13pt; color:#DCE6F1; font-style:italic; }
    .wrap { padding:22px 6px 0; }
    .dir { font-family:'DejaVu Sans'; font-size:14pt; color:%(NAVY)s; font-weight:bold; margin:0 0 16px; }
    .seg { display:flex; gap:14px; margin:0 0 16px; page-break-inside:avoid; }
    .seg .n { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; font-weight:bold; min-width:34px; height:34px;
      border-radius:50%%; text-align:center; line-height:34px; font-size:15pt; }
    .seg .t { flex:1; font-size:15.5pt; line-height:1.7; }
    .src { font-family:'DejaVu Sans'; font-size:9.5pt; color:#5C6470; font-style:italic; margin-top:20px;
      border-top:1pt solid %(BORDER)s; padding-top:8px; }
    @page { size:Letter portrait; margin:0.7in 0.75in 0.8in 0.75in;
      @bottom-left { content:"The Homestead Act of 1862 — Reading"; font:9pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"U.S. History Hack™ · p. " counter(page); font:9pt 'DejaVu Sans'; color:#5C6470; } }
    @page:first { margin-top:0; }
    """ % dict(INK=INK, NAVY=NAVY, RED=RED, GOLD=GOLD, BORDER=BORDER)
    segs = "".join(f'<div class="seg"><div class="n">{i+1}</div><div class="t">{t}</div></div>'
                   for i, t in enumerate(SEGMENTS))
    body = (f'<div class="title"><div class="kick">U.S. HISTORY HACK™ · STANDARD US.01</div>'
            f'<h1>The Homestead Act of 1862</h1>'
            f'<div class="sub">An Act to secure Homesteads to actual Settlers on the Public Domain — excerpt</div></div>'
            f'<div class="wrap"><div class="dir">Directions: Read the excerpt below. Each part is numbered.</div>'
            f'{segs}<div class="src">Source: {CITE}  ·  © 2026 TroopToTeacher Technologies LLC  ·  Generated {ISO}</div></div>')
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
    .box { border:1.2pt solid %(BORDER)s; border-radius:7px; margin:0 0 6px; page-break-inside:avoid; }
    .box .hd { background:%(NAVY)s; color:#fff; display:flex; align-items:center; gap:12px; padding:5px 12px; }
    .box .hd .L { background:%(GOLD)s; color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; font-size:15pt;
      width:28px; height:28px; border-radius:6px; text-align:center; line-height:28px; }
    .box .hd .nm { font-family:'DejaVu Sans'; font-weight:bold; font-size:13pt; }
    .box .bd { padding:7px 13px; }
    .q { font-size:10.8pt; margin:0 0 4px; }
    .q b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
    .stem { font-family:'DejaVu Sans'; font-size:10pt; color:%(NAVY)s; background:%(CARD)s; border:1pt solid %(BORDER)s;
      border-radius:5px; padding:5px 9px; margin:0 0 6px; }
    .stem b { color:%(RED)s; }
    .wl { border-bottom:0.7pt solid #AEB6C2; height:0.31in; }
    .foot { font-family:'DejaVu Sans'; font-size:9.5pt; color:%(NAVY)s; background:%(CARD)s; border:1pt solid %(GOLD)s;
      border-radius:6px; padding:7px 12px; margin-top:2px; }
    @page { size:Letter portrait; margin:0.6in 0.7in 0.75in 0.7in;
      @bottom-left { content:"HIPP Source Analysis — The Homestead Act of 1862"; font:8.5pt 'DejaVu Sans'; color:#5C6470; }
      @bottom-right { content:"U.S. History Hack™ · p. " counter(page); font:8.5pt 'DejaVu Sans'; color:#5C6470; } }
    @page:first { margin-top:0; }
    """ % dict(INK=INK, NAVY=NAVY, RED=RED, GOLD=GOLD, CARD=CARD, BORDER=BORDER)

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
            f'<div class="foot">Tip: use the numbered parts of the reading as your evidence — point to a part '
            f'number (for example, &ldquo;Part&nbsp;8 shows &hellip;&rdquo;) instead of copying long sentences.</div>'
            f'</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    r = f"US01_Homestead_Reading_LargePrint_{STAMP}.pdf"
    h = f"US01_Homestead_HIPP_Chart_{STAMP}.pdf"
    HTML(string=reading_html()).write_pdf(str(OUT / r))
    HTML(string=hipp_html()).write_pdf(str(OUT / h))
    print("wrote", r)
    print("wrote", h)
    print("out:", OUT, "| ts", ISO)


if __name__ == "__main__":
    main()
