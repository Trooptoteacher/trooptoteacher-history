#!/usr/bin/env python3
"""Homestead Act — interactive Word Wall for an emerging reader (~grade 3-4 Lexile).

Big, colorful vocabulary cards (2 per page) with a color-emoji picture cue, a
kid-friendly definition, a "clap the syllables" line, a Draw-it box, a use-it
line, and an "I know it!" star to color. Print-first via WeasyPrint.

US01_Homestead_WordWall_<ts>.pdf

America 250 brand + friendly card colors. Public-domain color emoji (Noto).
"""
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "HistoryHack_Platinum/homestead_wordwall"
OUT.mkdir(parents=True, exist_ok=True)
TS = datetime.now(timezone.utc)
STAMP = TS.strftime("%Y%m%d_%H%M")
ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ")

# word, emoji, kid-friendly definition (~grade 3-4), syllable break
WORDS = [
    ("HOMESTEAD", "🏡", "A home and the land around it where a family lives and works.", "home·stead"),
    ("SETTLER", "🧳", "A person who moves to live and work on new land.", "set·tler"),
    ("WEST", "🌅", "The land toward the sunset, in the western United States.", "West"),
    ("PRAIRIE", "🌾", "Flat land with lots of tall grass in the middle of the country.", "prai·rie"),
    ("CLAIM", "✋", "To say, “I want this land!” and ask to own it.", "claim"),
    ("FARM", "🚜", "To grow food and raise animals on the land.", "farm"),
    ("SOD HOUSE", "🏠", "A house built from blocks of dirt and grass.", "sod house"),
    ("CITIZEN", "🗽", "A person who belongs to a country, like the United States.", "cit·i·zen"),
    ("PATENT", "📜", "A special paper that says, “This land is yours.”", "pat·ent"),
    ("RAILROAD", "🚂", "A train track that carried people and goods across the country.", "rail·road"),
]

# friendly header colors: (background, text)
COLORS = [("#1F3A5F", "#FFFFFF"), ("#B22234", "#FFFFFF"), ("#2A7DA3", "#FFFFFF"),
          ("#2E7D5B", "#FFFFFF"), ("#C9A227", "#1F3A5F")]

CSS = """
* { box-sizing:border-box; }
body { font-family:'DejaVu Sans', 'Noto Color Emoji', Arial, sans-serif; color:#20262E; margin:0; }
.wallhdr { position:running(wh); width:7.5in; background:#1F3A5F; color:#fff;
  border-radius:0 0 16px 16px; padding:7px 18px; }
.wallhdr .t { font-size:19pt; font-weight:bold; text-align:center; }
.wallhdr .tag { font-size:11pt; color:#FFE08A; text-align:center; letter-spacing:.5px; }
.card { border:5px solid #1F3A5F; border-radius:18px; overflow:hidden; margin:0 0 0.18in;
  min-height:4.35in; page-break-inside:avoid; display:flex; flex-direction:column; }
.chead { display:flex; align-items:center; gap:16px; padding:8px 18px; }
.chead .em { font-family:'Noto Color Emoji'; font-size:40pt; line-height:1; }
.chead .w { font-size:33pt; font-weight:bold; letter-spacing:1px; }
.cbody { flex:1; display:flex; flex-direction:column; padding:12px 18px 14px; background:#FBFAF6; }
.def { font-size:15.5pt; line-height:1.4; color:#20262E; }
.syll { font-size:13pt; margin:9px 0 2px; color:#20262E; }
.syll b { color:#B22234; letter-spacing:1px; }
.crow { display:flex; gap:14px; flex:1; margin-top:9px; }
.draw { flex:1.3; border:2px dashed #8894A6; border-radius:12px; padding:6px 10px; }
.draw .dl { font-size:12pt; font-weight:bold; color:#1F3A5F; }
.rside { flex:1; display:flex; flex-direction:column; justify-content:space-between; }
.use { font-size:12.5pt; color:#1F3A5F; font-weight:bold; }
.uline { border-bottom:2px solid #AEB6C2; height:0.32in; margin-top:3px; }
.know { font-size:14pt; font-weight:bold; color:#1F3A5F; margin-top:8px; }
.know .star { font-size:20pt; color:#C9A227; }
.know .box { display:inline-block; width:20px; height:20px; border:2px solid #1F3A5F; border-radius:5px;
  vertical-align:-3px; margin-left:4px; }
.src { text-align:center; font-size:8pt; color:#5C6470; margin-top:4px; }
@page { size:Letter portrait; margin:1.0in 0.5in 0.55in 0.5in;
  @top-center { content: element(wh); vertical-align:top; }
  @bottom-center { content:"© 2026 TroopToTeacher Technologies LLC · U.S. History Hack™ · Homestead Word Wall";
    font:8pt 'DejaVu Sans'; color:#8894A6; } }
"""


def card(i, word, em, definition, syll):
    bg, tx = COLORS[i % len(COLORS)]
    return (f'<div class="card" style="border-color:{bg}">'
            f'<div class="chead" style="background:{bg};color:{tx}">'
            f'<span class="em">{em}</span><span class="w">{word}</span></div>'
            f'<div class="cbody">'
            f'<div class="def">{definition}</div>'
            f'<div class="syll">👏 Clap it: <b>{syll}</b></div>'
            f'<div class="crow">'
            f'<div class="draw"><span class="dl">✏ Draw it!</span></div>'
            f'<div class="rside">'
            f'<div><div class="use">✍ Use it in a sentence:</div><div class="uline"></div><div class="uline"></div></div>'
            f'<div class="know">I know this word! <span class="star">★</span><span class="box"></span></div>'
            f'</div></div></div></div>')


def build():
    banner = ('<div class="wallhdr"><div class="t">🏡 Homestead Word Wall 🚂</div>'
              '<div class="tag">Read it! · Say it! · Draw it!</div></div>')
    cards = "".join(card(i, *w) for i, w in enumerate(WORDS))
    body = banner + cards + f'<div class="src">Name: ______________________     ·     Generated {ISO}</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def main():
    name = f"US01_Homestead_WordWall_{STAMP}.pdf"
    HTML(string=build()).write_pdf(str(OUT / name))
    print("wrote", name, "| out:", OUT, "| ts", ISO)


if __name__ == "__main__":
    main()
