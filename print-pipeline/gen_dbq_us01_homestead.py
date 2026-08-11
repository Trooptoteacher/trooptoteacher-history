#!/usr/bin/env python3
"""U.S. History Hack — Unit 1 / US.01 standalone DBQ SKU (print-first, no docx).

Investigation: "The Homestead Act of 1862 — Who Gained a Homestead, and Who Lost a Homeland?"

Builds THREE PDFs via WeasyPrint:
  1. US01_Homestead_DBQ_Workbook_<ts>.pdf   — student DBQ: how-to-use (first-DBQ
     scaffold), US.01 + SSP crosswalk, investigation question, 6-document set
     (2 verbatim statute-text HIPPO docs + 4 visual-primary OPTIC docs), faded
     scaffolds, plain-language access sidebars, Tennessee Connection,
     evidence-planning organizer, essay prompt + AP-aligned rubric.
  2. US01_Homestead_DBQ_Scaffold_Supports_<ts>.pdf — scaffold / language-access
     companion for the three inclusion sections: worked HIPPO + OPTIC models,
     EN/ES word bank, sentence stems, bucketing organizer, thesis builder, a
     step-by-step "How to do a DBQ" checklist. Works ALONGSIDE (never in place
     of) a student's IEP/504 accommodations.
  3. US01_Homestead_DBQ_Teacher_Guide_<ts>.pdf — teacher implementation, source
     notes, model thesis + annotated exemplar, scoring guidance, the rubric,
     a differentiation plan (3 inclusion sections vs 2 honors sections), and an
     honest author-generated disclosure.

Every document is public-domain with honest provenance (real repository + verified
verbatim wording). Follows history-hack-dbq-workbook LOCKED gates: America 250
palette, TM not (R), ISBN "[to be assigned]", text=HIPPO / visual-primary=OPTIC,
scaffold fading preserved, version timestamp in filename + on-page.
"""
import base64
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
IMG = ROOT.parent / ".claude/skills/history-hack-tcap-deck-builder/assets/unit1-example/img"
OUT = ROOT.parent / "HistoryHack_Platinum/dbq_us01_homestead"
OUT.mkdir(parents=True, exist_ok=True)

TS = datetime.now(timezone.utc)
STAMP = TS.strftime("%Y%m%d_%H%M")
ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ")

# America 250 palette (BRAND_PALETTE.md — canonical)
NAVY, NAVY2, RED, GOLD, CARD, LIGHT, BORDER, INK = \
    "#1F3A5F", "#2C3E63", "#B22234", "#C9A227", "#F8F5EF", "#EEF2F8", "#C9C2B4", "#20262E"

STATUTE_CITE = ("Homestead Act of 1862, 12 Stat. 392 (37th Cong., Sess. II, ch. 75); approved "
                "May 20, 1862. General Records of the U.S. Government, RG 11, U.S. National "
                "Archives. Verbatim transcription: National Archives &amp; State Historical "
                "Society of North Dakota. Public domain (U.S. statute).")


def img_uri(name):
    b = base64.b64encode((IMG / name).read_bytes()).decode()
    return f"data:image/jpeg;base64,{b}"


# ---------------------------------------------------------------------------
# DOCUMENT SET — verified public-domain; text=HIPPO, visual-primary=OPTIC.
# Fields: (letter, title, kind, badge, level, citation, context, verbatim-or-img,
#          guiding_q, extension_q)
# ---------------------------------------------------------------------------
DOC_A_TEXT = (
    "<b>Sec. 1.</b> <i>Be it enacted &hellip;</i> That any person who is the head of a family, "
    "or who has arrived at the age of twenty-one years, and is a citizen of the United States, "
    "or who shall have filed his declaration of intention to become such &hellip; and who has "
    "never borne arms against the United States Government or given aid and comfort to its "
    "enemies, shall &hellip; be entitled to enter one quarter section [160 acres] or a less "
    "quantity of unappropriated public lands &hellip; subject to preemption at one dollar and "
    "twenty-five cents, or less, per acre.<br><br>"
    "<b>Sec. 2.</b> &hellip; That the person applying &hellip; shall make affidavit &hellip; that "
    "such application is made for his or her exclusive use and benefit, and that said entry is "
    "made for the purpose of actual settlement and cultivation, and not either directly or "
    "indirectly for the use or benefit of any other person &hellip; and on payment of ten "
    "dollars, he or she shall thereupon be permitted to enter the quantity of land specified.")

DOC_A_PLAIN = ("Any adult head of a family, or anyone 21 or older, who was a U.S. citizen (or "
               "was becoming one) and had not fought against the Union, could claim up to 160 "
               "acres of public land in the West. They paid a small filing fee and promised the "
               "land was for their own farm — not secretly for someone else.")

DOC_B_TEXT = (
    "&hellip; no certificate shall be given, or patent issued therefor, until the expiration of "
    "<b>five years</b> from the date of such entry; and if, at the expiration of such time &hellip; "
    "the person making such entry &hellip; shall prove by <b>two credible witnesses</b> that he, "
    "she, or they have resided upon or cultivated the same for the term of five years &hellip; and "
    "shall make affidavit that no part of said land has been alienated &hellip; then &hellip; if at "
    "that time a citizen of the United States, [they] shall be entitled to a patent.<br><br>"
    "&hellip; if &hellip; it shall be proven &hellip; that the person having filed such affidavit "
    "shall have actually changed his or her residence, or abandoned the said land for more than "
    "<b>six months</b> at any time, then &hellip; the land so entered shall <b>revert to the "
    "government</b>.")

DOC_B_PLAIN = ("You did not own the land right away. You had to live on it and farm it for five "
               "years, then bring two witnesses to prove it. Only then did you receive the "
               "'patent' — the legal title. If you left the land for more than six months, you "
               "lost your claim and it went back to the government.")

DOCS = [
    ("A", "The Homestead Act of 1862 &mdash; Who Could Claim the Land", "text", "HIPPO &middot; TEXT", "full",
     STATUTE_CITE, "Signed during the Civil War, the Act opened federal &ldquo;public&rdquo; land in the "
     "West to ordinary settlers &mdash; including immigrants and, after 1866, freedpeople.",
     DOC_A_TEXT,
     "According to the law itself, <b>who could</b> claim a homestead &mdash; and what did the word "
     "&ldquo;unappropriated&rdquo; public land assume about who was already there?",
     "&#9650; Honors: The Act barred anyone who had &ldquo;borne arms against&rdquo; the U.S. Whose "
     "land claims did that clause reward, and how does it tie the Act to the Civil War?"),
    ("B", "The Homestead Act of 1862 &mdash; Prove It Up, or Lose It", "text", "HIPPO &middot; TEXT", "full",
     STATUTE_CITE, "The land was not a gift. Section-by-section, the Act set the terms a settler had to "
     "meet over five years before the government would grant legal title.",
     DOC_B_TEXT,
     "What did a settler have to <b>do</b> to turn a claim into ownership &mdash; and who would "
     "struggle most to meet a five-year residence rule?",
     "&#9650; Honors: A separate clause let a settler &ldquo;commute&rdquo; the claim by paying "
     "$1.25/acre. Who could afford to buy out early, and how might that advantage the wealthy?"),
    ("C", "Driving the Last Spike, Promontory Summit, 1869", "visual", "OPTIC &middot; PHOTO", "reduced",
     "Russell, Andrew J. <i>East and West Shaking Hands at the Laying of the Last Rail</i>, Promontory "
     "Summit, Utah Territory, May 10, 1869. Public domain. (Held: Yale Collection of Western Americana.)",
     "The Transcontinental Railroad &mdash; the other half of standard US.01 &mdash; met here in 1869, "
     "carrying settlers, mail, and goods to the lands the Homestead Act opened.",
     "transcontinental-railroad-ceremony.jpg",
     "The photograph stages a national triumph. <b>Who is pictured</b> celebrating &mdash; and which "
     "workers (Chinese, Irish) and which displaced nations are <i>not</i> in the frame?",
     "&#9650; Honors: This image was carefully posed for the press. How does that staging shape the "
     "story Americans told themselves about &ldquo;winning&rdquo; the West?"),
    ("D", "Railroad Systems of the United States, 1890", "visual", "OPTIC &middot; MAP", "reduced",
     "<i>Railroad Systems of the United States: 1890</i> (Plate 60). Henry Gannett / U.S. Census Office, "
     "<i>Statistical Atlas of the United States</i>. Library of Congress, Geography &amp; Map Division. "
     "Public domain.",
     "By 1890 rail lines webbed the continent &mdash; dense in the East, reaching across the very "
     "Plains and mountain West that had been home to Native nations.",
     "railroad-map-1890.jpg",
     "Read this <b>as geography</b> (SSP.06): where are the lines thickest, and whose homelands did the "
     "new western lines cross to reach open land?",
     "&#9650; Honors: Compare the western rail pattern to where the Homestead Act land lay. How did rail "
     "access decide <i>which</i> homesteads could actually succeed?"),
    ("E", "A Homestead Family &lsquo;Proved Up,&rsquo; Custer County, Nebraska, 1886", "visual",
     "OPTIC &middot; PHOTO", "reduced",
     "Butcher, Solomon D. <i>Sod house of the Sylvester Rawding family, north of Sargent, Custer "
     "County, Nebraska.</i> 1886. Nebraska State Historical Society, Solomon D. Butcher Collection. "
     "(Copy: Library of Congress, LC-USZ62-8276.) Public domain.",
     "On the treeless Plains, homesteaders built houses of cut sod. This family posed with their "
     "animals and possessions to record that they had made it &mdash; note the cow on the roof.",
     "rawding-sod-house.jpg",
     "For <b>this</b> family, what did the Homestead Act deliver? List two pieces of visual evidence "
     "that the promise of land was real for some settlers.",
     "&#9650; Honors: Butcher sold these photos to homesteaders as proof of success. How might that "
     "purpose make the image an <i>argument</i>, not just a record?"),
    ("F", "Tom Torlino, Navajo &mdash; Carlisle Indian School, 1882 &amp; 1885", "visual",
     "OPTIC &middot; PHOTO", "independent",
     "Choate, John N. <i>Tom Torlino, Navajo</i> &mdash; on arrival (1882) and after about three years "
     "(1885) at the Carlisle Indian Industrial School, Pennsylvania. Carlisle Indian School Digital "
     "Resource Center / Richard Henry Pratt Papers, Beinecke Library, Yale University. Public domain.",
     "The &ldquo;unappropriated&rdquo; land of the Act was Native homeland. As it was opened to "
     "settlers, the U.S. pressed Native children into boarding schools whose motto was &ldquo;Kill the "
     "Indian, save the man.&rdquo;",
     "tom-torlino-carlisle.jpg",
     "These two photographs of the <b>same young man</b> were paired on purpose. What transformation do "
     "they record &mdash; and what cost of westward settlement does that pairing make visible?",
     "&#9650; Honors: Who created this before/after pairing, and for what audience? How does that "
     "purpose change how you weigh it as evidence of &ldquo;progress&rdquo;?"),
]

PERSPECTIVES = [
    ("Who gained a homestead?", "Settlers, immigrants, and (after 1866) freedpeople; the railroads that sold and served the land", "A, B, E"),
    ("Who lost a homeland?", "American Indian nations whose land the Act called &ldquo;unappropriated&rdquo; and opened to settlement", "D, F"),
    ("Who decided?", "Congress, the federal land office, and the railroads granted millions of acres", "A, C, D"),
]

# ---------------------------------------------------------------------------
# Shared CSS
# ---------------------------------------------------------------------------
def head_css(footer_label):
    return ("""
* { box-sizing:border-box; }
body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; font-size:10.6pt; line-height:1.42; }
h2,h3,.k,.doch,.brand,.iq,.type,.sec,.lens b,.frame .k,.pill { font-family:'DejaVu Sans', Arial, sans-serif; }
.page { page-break-after:always; }
.avoid { page-break-inside:avoid; }
.cover { height:9.1in; background:%(NAVY)s; color:#fff; padding:0.9in 0.8in; page-break-after:always; position:relative; border-left:16px solid %(RED)s; }
.cover .brand { color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:12pt; }
.cover h1 { font-size:29pt; margin:14px 0 4px; line-height:1.08; }
.cover .sub { font-size:13pt; color:#DCE6F1; }
.cover .dbqt { font-size:17pt; color:#fff; font-style:italic; margin-top:12px; border-top:2px solid %(GOLD)s; padding-top:12px; }
.cover .tn { margin-top:20px; background:%(GOLD)s; color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; padding:8px 12px; border-radius:5px; display:inline-block; font-size:10.5pt; }
.cover .foot { position:absolute; bottom:0.7in; left:0.8in; right:0.8in; font-family:'DejaVu Sans'; font-size:8.5pt; color:#AFC0D6; }
.copyr { padding:0.35in 0.15in; font-size:9.2pt; color:#3a4250; }
.copyr p { margin:7px 0; }
.sec { color:%(NAVY)s; border-bottom:2px solid %(GOLD)s; padding-bottom:3px; margin:2px 0 9px; font-size:15pt; page-break-after:avoid; }
.sub2 { color:%(NAVY)s; font-size:12pt; margin:12px 0 5px; font-family:'DejaVu Sans'; }
.iq { background:%(NAVY)s; color:#fff; padding:13px 16px; border-radius:6px; font-size:12.5pt; }
.iq .lab { color:%(GOLD)s; font-weight:bold; font-size:9pt; display:block; letter-spacing:1px; margin-bottom:3px; }
.lens { display:flex; gap:8px; margin:11px 0; }
.lens .c { flex:1; background:%(CARD)s; border:1pt solid %(BORDER)s; border-top:4px solid %(RED)s; border-radius:5px; padding:8px 10px; font-size:9pt; }
.lens .c b { color:%(NAVY)s; display:block; margin-bottom:3px; }
.doc { border:1pt solid %(BORDER)s; border-radius:6px; margin:0 0 13px; }
.dtop { page-break-inside:avoid; }
.doch { background:%(NAVY)s; color:#fff; padding:7px 11px; display:flex; justify-content:space-between; align-items:center; page-break-after:avoid; }
.doch .l { font-weight:bold; font-size:10.5pt; }
.type { background:%(GOLD)s; color:%(NAVY)s; font-size:8pt; font-weight:bold; padding:2px 9px; border-radius:9px; white-space:nowrap; }
.docb { padding:10px 13px; }
.docimg { text-align:center; margin:6px 0; page-break-inside:avoid; }
.docimg img { max-width:82%%; max-height:3.5in; border:1pt solid %(BORDER)s; }
.src { font-size:8pt; color:#5C6470; font-style:italic; margin:4px 0 7px; line-height:1.3; }
.excerpt { background:#FBFAF6; border-left:4px solid %(NAVY2)s; padding:8px 12px; font-size:10pt; line-height:1.5; margin:5px 0; }
.plain { background:%(LIGHT)s; border:1pt dashed %(NAVY2)s; border-radius:5px; padding:6px 10px; font-size:9.2pt; margin:6px 0; }
.plain .k { color:%(RED)s; font-weight:bold; font-size:8pt; letter-spacing:.4px; font-family:'DejaVu Sans'; }
.ctx { font-size:9.8pt; margin:5px 0; }
.gq { background:%(CARD)s; border-left:4px solid %(RED)s; padding:7px 11px; font-size:10pt; margin-top:7px; page-break-inside:avoid; }
.gq b { color:%(NAVY)s; }
.ext { font-size:9pt; color:%(NAVY)s; margin-top:5px; font-style:italic; }
.frame { border:1pt solid %(NAVY2)s; border-radius:5px; padding:7px 11px; margin-top:8px; background:#fff; }
.frame .k { color:%(RED)s; font-weight:bold; font-size:8.5pt; letter-spacing:.5px; }
.frame table { width:100%%; border-collapse:collapse; margin-top:4px; }
.frame table tr { page-break-inside:avoid; }
.frame td { border:0.5pt solid %(BORDER)s; padding:5px 7px; font-size:9pt; vertical-align:top; }
.frame td.q { width:27%%; background:%(CARD)s; font-family:'DejaVu Sans'; font-weight:bold; color:%(NAVY)s; }
.writeline { border-bottom:0.6pt solid #AEB6C2; height:0.32in; }
.fade { font-size:8pt; color:%(RED)s; font-family:'DejaVu Sans'; font-weight:bold; }
table.plan { width:100%%; border-collapse:collapse; }
table.plan th { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; padding:7px; font-size:9.5pt; text-align:left; }
table.plan tr { page-break-inside:avoid; }
table.plan td { border:1pt solid %(BORDER)s; padding:7px 9px; font-size:9.5pt; vertical-align:top; }
.rubric { width:100%%; border-collapse:collapse; }
.rubric th { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; padding:6px 8px; font-size:9pt; text-align:left; }
.rubric tr { page-break-inside:avoid; }
.rubric td { border:0.5pt solid %(BORDER)s; padding:6px 8px; font-size:9pt; vertical-align:top; }
.rubric td.cr { background:%(CARD)s; font-family:'DejaVu Sans'; font-weight:bold; color:%(NAVY)s; }
.tnbox { background:%(CARD)s; border:1.5pt solid %(GOLD)s; border-radius:6px; padding:11px 14px; margin:9px 0; }
.tnbox .k { color:%(RED)s; font-family:'DejaVu Sans'; font-weight:bold; display:block; margin-bottom:4px; }
.note { font-size:8.4pt; color:#5C6470; font-style:italic; }
.stem { background:%(CARD)s; border:1pt solid %(BORDER)s; border-radius:5px; padding:8px 12px; margin:6px 0; font-size:9.8pt; }
.stem b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
.step { display:flex; gap:10px; margin:9px 0; align-items:flex-start; }
.step .n { background:%(RED)s; color:#fff; font-family:'DejaVu Sans'; font-weight:bold; min-width:26px; height:26px; border-radius:50%%; text-align:center; line-height:26px; font-size:11pt; }
.step .t { flex:1; font-size:10pt; }
.step .t b { color:%(NAVY)s; }
.keybox { display:flex; gap:8px; margin:9px 0; }
.keybox .c { flex:1; border:1pt solid %(BORDER)s; border-radius:5px; padding:7px 9px; font-size:8.8pt; background:#fff; }
.keybox .c b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
.pill { display:inline-block; background:%(NAVY)s; color:#fff; font-size:8pt; padding:1px 8px; border-radius:9px; margin-right:4px; }
.callout { border:1pt solid %(BORDER)s; border-left:5px solid %(NAVY)s; background:%(LIGHT)s; border-radius:5px; padding:8px 12px; margin:8px 0; font-size:9.4pt; }
ul.tight { margin:5px 0 5px 18px; padding:0; }
ul.tight li { margin:3px 0; font-size:9.8pt; }
@page { size:Letter portrait; margin:0.7in 0.7in 0.85in 0.7in;
  @bottom-left { content:"%(FOOT)s"; font:8pt 'DejaVu Sans'; color:#5C6470; }
  @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:8pt 'DejaVu Sans'; color:#5C6470; } }
@page:first { margin:0; }
""" % dict(INK=INK, NAVY=NAVY, NAVY2=NAVY2, RED=RED, GOLD=GOLD, CARD=CARD, LIGHT=LIGHT, BORDER=BORDER, FOOT=footer_label))


def lines(n):
    return "".join('<div class="writeline"></div>' for _ in range(n))


# ---------------------------------------------------------------------------
# HIPPO / OPTIC frames (fade with level)
# ---------------------------------------------------------------------------
def hippo_frame(level):
    fade = {"full": "Full scaffold", "reduced": "Reduced cues", "independent": "Independent"}[level]
    if level == "independent":
        return ('<div class="frame"><span class="k">HIPPO &mdash; source it independently</span> '
                f'<span class="fade">({fade})</span>{lines(3)}</div>')
    rows = [("H — Historical context", "When/where was this written, and what was happening?"),
            ("I — Intended audience", "Who was meant to read or obey it?"),
            ("P — Point of view", "Whose interests does it serve — and who is left out?"),
            ("P — Purpose", "Why was it created?"),
            ("O — Outside evidence", "What do you already know that connects?")]
    if level == "reduced":
        rows = [("P — Point of view", ""), ("P — Purpose", ""), ("O — Outside evidence", "")]
    tr = "".join(f'<tr><td class="q">{q}{("<div class=note>"+h+"</div>") if h else ""}</td><td></td></tr>' for q, h in rows)
    return f'<div class="frame"><span class="k">HIPPO &mdash; analyze this text source</span> <span class="fade">({fade})</span><table>{tr}</table></div>'


def optic_frame(level):
    fade = {"full": "Full scaffold", "reduced": "Reduced cues", "independent": "Independent"}[level]
    if level == "independent":
        return ('<div class="frame"><span class="k">OPTIC &mdash; analyze this visual source independently</span> '
                f'<span class="fade">({fade})</span>{lines(3)}</div>')
    rows = [("O — Overview", "First impression — what is happening?"),
            ("P — Parts", "List the people, objects, and details you see."),
            ("T — Title / Text", "How do the caption and any words steer meaning?"),
            ("I — Interrelationships", "How do the parts connect to make a point?"),
            ("C — Conclusion", "What does this source show about who gained or lost?")]
    if level == "reduced":
        rows = [("P — Parts", "People, objects, details"), ("I — Interrelationships", "How they connect"),
                ("C — Conclusion", "What it shows about gain or loss")]
    tr = "".join(f'<tr><td class="q">{q}{("<div class=note>"+h+"</div>") if h else ""}</td><td></td></tr>' for q, h in rows)
    return f'<div class="frame"><span class="k">OPTIC &mdash; visual primary source (its own document)</span> <span class="fade">({fade})</span><table>{tr}</table></div>'


# ===========================================================================
# FILE 1 — STUDENT WORKBOOK
# ===========================================================================
def workbook_html():
    css = head_css("U.S. History Hack™ · US.01 DBQ · Homestead Act of 1862")

    cover = f"""<div class="cover"><div class="brand">U.S. HISTORY HACK™ · AMERICA 250</div>
      <h1>Document-Based Investigation</h1>
      <div class="sub">Unit 1 &middot; Standard <b>US.01</b> &mdash; The Homestead Act &amp; the Transcontinental Railroad</div>
      <div class="dbqt">The Homestead Act of 1862:<br>Who Gained a Homestead &mdash; and Who Lost a Homeland?</div>
      <div class="tn">TENNESSEE CONNECTION INSIDE &mdash; reason from your own state's land history</div>
      <div class="foot">Standalone DBQ SKU &middot; 6 verified public-domain documents &middot; HIPPO (text) + OPTIC (visual)
      &middot; Your first Document-Based Investigation &middot; ISBN [to be assigned] &middot; TroopToTeacher Technologies LLC<br>
      Generated: {ISO}</div></div>"""

    copyr = f"""<div class="copyr"><p><b>U.S. History Hack™ &mdash; Unit 1 (US.01) Document-Based Investigation:
      The Homestead Act of 1862.</b> © 2026 TroopToTeacher Technologies LLC. Author / producer: TroopToTeacher
      Technologies LLC. Single-classroom reproduction license — reproduce for your own students only.</p>
      <p>All six documents are in the <b>public domain</b>, with honest provenance and a citable archive behind each
      asset (U.S. National Archives; Library of Congress; Nebraska State Historical Society, Solomon D. Butcher
      Collection; Beinecke Library, Yale University). The statute text is a <b>verbatim excerpt</b> of the Homestead
      Act of 1862 (12&nbsp;Stat.&nbsp;392); nothing here is composed and presented as a primary source. Pearson /
      McGraw&nbsp;Hill / Savvas are category references only.</p>
      <p><i>Framework stack:</i> Tennessee Academic Standards (US.01) first &rarr; RH/WHST literacy practices
      (cross-subject proof only; not marketed as Common Core per T.C.A. §49-6-2202) &rarr; AP U.S. History &rarr;
      C3 Framework &rarr; Inquiry Design Model (IDM).</p>
      <p class="note">Trademarks use ™. ISBN &ldquo;[to be assigned].&rdquo; Generated {ISO}. This is a
      district / school-board adoption artifact — provenance is honest and every claim is verifiable against the
      cited archive.</p></div>"""

    # Standards crosswalk
    crosswalk = f"""<h2 class="sec">Tennessee Standards Alignment</h2>
      <table class="plan"><tr><th style="width:15%">Standard</th><th style="width:52%">Verbatim TDOE standard</th>
      <th style="width:15%">Where</th><th style="width:18%">Depth</th></tr>
      <tr><td><b>US.01</b></td><td><i>Explain how the Homestead Act and the Transcontinental Railroad impacted the
      settlement of the West</i> — including their effects on American Indians, immigrants, and settlers.</td>
      <td>This entire investigation</td><td><b>Full</b> &mdash; the Act is the anchor source</td></tr></table>
      <h3 class="sub2">Social Studies Practices exercised (SSP.01–06) — all <b>Full</b></h3>
      <table class="plan"><tr><th style="width:24%">Practice</th><th style="width:44%">How this DBQ exercises it</th>
      <th style="width:32%">Where</th></tr>
      <tr><td><b>SSP.01</b> Collect from sources</td><td>Gather evidence from a 6-document set</td><td>Docs A–F</td></tr>
      <tr><td><b>SSP.02</b> Examine a source</td><td>HIPPO (text) &amp; OPTIC (visual) sourcing on every document</td><td>Every frame</td></tr>
      <tr><td><b>SSP.03</b> Synthesize / compare</td><td>Weigh promise vs. cost across documents</td><td>Plan Your Evidence</td></tr>
      <tr><td><b>SSP.04</b> Construct arguments</td><td>Write an evidence-based CER argument with a rubric</td><td>Write Your Argument</td></tr>
      <tr><td><b>SSP.05</b> Historical awareness</td><td>Place the Act in its Civil-War-era context</td><td>Docs A–C</td></tr>
      <tr><td><b>SSP.06</b> Geographic awareness</td><td>Read the 1890 rail map as spatial evidence</td><td>Doc D</td></tr></table>
      <p class="note">Depth labeled honestly: <b>Full</b> = the standard is directly taught and assessed here.</p>"""

    # How to use — first-DBQ scaffold
    howto = f"""<h2 class="sec">What Is a DBQ? &mdash; How to Use This Investigation</h2>
      <div class="callout"><b>This is your first Document-Based Investigation (DBQ).</b> A DBQ asks you to be a
      historian: read a set of real primary sources, figure out what each one shows, and then use them as
      <b>evidence</b> to answer one big question. You are not looking for a single &ldquo;right answer&rdquo; in the
      back of the book — you are <b>building an argument</b> and backing it up.</div>

      <h3 class="sub2">Follow these five steps &mdash; in order</h3>
      <div class="step"><div class="n">1</div><div class="t"><b>READ</b> each document and the short context note above it.
      For the two law excerpts, use the <b>Plain-Language</b> box if the old wording is hard.</div></div>
      <div class="step"><div class="n">2</div><div class="t"><b>SOURCE IT</b> — before you trust a source, ask who made it, when,
      and why. Fill in the <b>HIPPO</b> box (for text) or <b>OPTIC</b> box (for pictures) under each document.</div></div>
      <div class="step"><div class="n">3</div><div class="t"><b>SORT</b> your evidence using the three lenses:
      <i>Who gained a homestead? &middot; Who lost a homeland? &middot; Who decided?</i></div></div>
      <div class="step"><div class="n">4</div><div class="t"><b>PLAN</b> — put your best documents into the &ldquo;Plan Your
      Evidence&rdquo; organizer so every part of your answer has proof.</div></div>
      <div class="step"><div class="n">5</div><div class="t"><b>WRITE</b> your argument using the thesis frame and the CER
      pattern (Claim &middot; Evidence &middot; Reasoning). Then check it against the rubric.</div></div>

      <div class="keybox">
        <div class="c"><b>HIPPO</b> (text sources) = <b>H</b>istorical context · <b>I</b>ntended audience ·
        <b>P</b>oint of view · <b>P</b>urpose · <b>O</b>utside evidence.</div>
        <div class="c"><b>OPTIC</b> (pictures &amp; maps) = <b>O</b>verview · <b>P</b>arts · <b>T</b>itle/Text ·
        <b>I</b>nterrelationships · <b>C</b>onclusion.</div>
      </div>

      <div class="callout"><b>The scaffolds fade on purpose.</b> Documents <b>A–B</b> give you the full sourcing frames,
      <b>C–E</b> give reduced cues, and <b>F</b> asks you to source it on your own — because by then you can.
      <br><br><b>Difficulty key you'll see on questions:</b>
      <span class="pill">★ Entry</span> start here if this is new ·
      <span class="pill">● On-Level</span> the target for everyone ·
      <span class="pill">▲ Extension</span> push your thinking further.
      Need extra support? Use the <b>Scaffold &amp; Language-Access Companion</b> alongside this book.</div>"""

    # Investigation
    lens = "".join(f'<div class="c"><b>{q}</b>{d}</div>' for q, d, _ in PERSPECTIVES)
    intro = f"""<h2 class="sec">The Investigation</h2>
      <div class="iq"><span class="lab">YOUR INVESTIGATION QUESTION</span>
      The Homestead Act of 1862 offered up to <b>160 acres</b> of Western land to anyone who would live on it and
      farm it for five years. Using the documents, answer: <b>Who gained a homestead — and who lost a homeland?</b></div>
      <p style="margin:10px 2px">As you read, sort every piece of evidence into one of these three lenses. You will
      use them again when you plan and write.</p>
      <div class="lens">{lens}</div>
      <div class="callout"><b>A note on hard history.</b> Document F shows a Native child changed by a government
      boarding school, and the law in Documents A–B calls Native homeland &ldquo;unappropriated.&rdquo; We study these
      honestly — as a historian would — to understand both what settlers gained and what Native nations lost. No
      conclusion is handed to you; you weigh the evidence.</div>"""

    # Pre-reading activity (activate prior knowledge + word preview + prediction) — fills the page and primes a first DBQ
    predict = f"""<h3 class="sub2">Before You Investigate &mdash; Activate &amp; Predict</h3>
      <div class="callout">You have not read the documents yet. Historians predict first, then test the prediction
      against the evidence — and change their minds when the evidence says so. Warm up your thinking, then make your
      best guess. You will come back to this page after Document&nbsp;F.</div>
      <div class="sub2" style="font-size:11pt;margin-top:10px">1 &middot; What do you already know?</div>
      <div class="frame"><span class="k">PRIOR KNOWLEDGE</span>
      <div style="font-size:9.6pt;margin:4px 0 2px">List two things you have heard, seen, or learned about Americans
      moving West in the 1800s (movies, family stories, and earlier grades all count).</div>{lines(2)}</div>
      <div class="sub2" style="font-size:11pt;margin-top:10px">2 &middot; Preview four key words &mdash; guess first</div>
      <table class="plan"><tr><th style="width:22%">Word</th><th style="width:40%">My best guess at the meaning</th>
      <th style="width:38%">What it really meant (fill in after you read)</th></tr>
      <tr><td><b>homestead</b></td><td></td><td></td></tr>
      <tr><td><b>public land</b></td><td></td><td></td></tr>
      <tr><td><b>patent</b></td><td></td><td></td></tr>
      <tr><td><b>unappropriated</b></td><td></td><td></td></tr></table>
      <div class="sub2" style="font-size:11pt;margin-top:10px">3 &middot; Make your prediction</div>
      <div class="frame"><span class="k">MY PREDICTION (we will test it)</span>
      <div style="font-size:9.6pt;margin:4px 0 2px"><b>a.</b> Who do you think <b>gained</b> the most from the
      Homestead Act, and why?</div>{lines(2)}
      <div style="font-size:9.6pt;margin:7px 0 2px"><b>b.</b> Who might have <b>lost</b> something, and why?</div>{lines(2)}</div>"""

    # Documents
    docs_html = ""
    for L, title, kind, badge, level, cite, ctx, payload, gq, ext in DOCS:
        if kind == "text":
            body = (f'<div class="excerpt">{payload}</div>'
                    f'<div class="plain"><span class="k">PLAIN-LANGUAGE MEANING</span><br>{[d for d in [DOC_A_PLAIN if L=="A" else DOC_B_PLAIN]][0]}</div>')
            frame = hippo_frame(level)
        else:
            body = f'<div class="docimg"><img src="{img_uri(payload)}"></div>'
            frame = optic_frame(level)
        docs_html += (f'<div class="doc"><div class="doch"><span class="l">Document {L} &mdash; {title}</span>'
                      f'<span class="type">{badge}</span></div><div class="docb">'
                      f'{body}'
                      f'<div class="src">Source: {cite}</div>'
                      f'<div class="ctx">{ctx}</div>'
                      f'<div class="gq"><b>● Guiding question:</b> {gq}</div>'
                      f'<div class="ext">{ext}</div>{frame}</div></div>')

    # Tennessee Connection
    tnbox = """<h2 class="sec">Tennessee Connection</h2>
      <div class="tnbox"><span class="k">REASON FROM YOUR OWN STATE'S LAND HISTORY.</span>
      Tennessee sits on <b>both</b> sides of this question. Thousands of Tennesseans joined the westward migration the
      Homestead Act encouraged, leaving worn-out farms for a fresh 160 acres. But Tennessee also knew the other side
      first-hand: a generation earlier, the same federal power that opened western land had forced the <b>Cherokee</b>
      from East Tennessee on the <b>Trail of Tears (1838)</b> — the land many Tennesseans farmed had itself once been
      Native homeland. <br><br><i>How does Tennessee's own story — settlers heading west, and Native nations pushed
      off their land — help you answer &ldquo;who gained a homestead and who lost a homeland&rdquo;?</i></div>
      <div class="frame"><span class="k">TENNESSEE REASONING — write two sentences</span>%s</div>""" % lines(3)

    # Plan your evidence
    plan_rows = "".join(f'<tr><td><b>{q}</b></td><td>{d}</td><td>{docs_}</td><td></td></tr>' for q, d, docs_ in PERSPECTIVES)
    planning = f"""<h2 class="sec">Plan Your Evidence</h2>
      <p>Before you write, load your best proof into this organizer. Every row of your argument needs a document.</p>
      <table class="plan"><tr><th style="width:20%">Lens</th><th style="width:34%">Who / what to look for</th>
      <th style="width:13%">Best docs</th><th style="width:33%">Your evidence + why it matters</th></tr>{plan_rows}</table>"""

    # Essay + rubric
    rubric = """<table class="rubric">
      <tr><th style="width:18%">Criterion</th><th>4 — Exceeds</th><th>3 — Meets (target)</th><th>2 — Approaching</th><th>1 — Beginning</th></tr>
      <tr><td class="cr">Thesis (Claim)</td><td>Defensible claim that answers &ldquo;for whom?&rdquo; with nuance</td><td>Clear claim that takes a position</td><td>Claim mostly restates the prompt</td><td>No clear claim</td></tr>
      <tr><td class="cr">Evidence — documents</td><td>Uses ≥4 documents accurately as evidence</td><td>Uses 3 documents accurately</td><td>Uses 2 documents</td><td>0–1 documents</td></tr>
      <tr><td class="cr">Sourcing (HIPPO/OPTIC)</td><td>Sources ≥2 docs (names POV or purpose)</td><td>Sources 1 doc</td><td>Attempts sourcing</td><td>No sourcing</td></tr>
      <tr><td class="cr">Analysis — gain &amp; cost</td><td>Weighs who gained <i>and</i> who lost, with reasoning</td><td>Names both a gain and a cost</td><td>One-sided</td><td>Summary only</td></tr>
      <tr><td class="cr">Tennessee Connection</td><td>Uses a Tennessee example as evidence</td><td>Mentions a Tennessee example</td><td>Vague TN reference</td><td>None</td></tr></table>"""

    essay = f"""<h2 class="sec">Write Your Argument</h2>
      <p><b>Prompt.</b> Using at least <b>three</b> documents and your Tennessee Connection, answer the investigation
      question: <b>Who gained a homestead — and who lost a homeland?</b> Source at least <b>one</b> document (name its
      point of view or purpose). Aim for one strong paragraph (or more for <span class="pill">▲ Extension</span>).</p>
      <div class="stem"><b>Thesis frame (fill in):</b> &ldquo;The Homestead Act gave ______ to ______, but it came at
      the cost of ______ for ______; therefore ______.&rdquo;</div>
      <div class="stem"><b>CER pattern:</b> <b>Claim</b> (your answer) → <b>Evidence</b> (&ldquo;Document ___ shows
      ___&rdquo;) → <b>Reasoning</b> (&ldquo;This matters because ___&rdquo;). Repeat for each lens.</div>
      {lines(9)}
      <h3 class="sub2">Score Yourself — Rubric</h3>{rubric}
      <p class="note" style="margin-top:7px">Self-grade on the rubric, then (if your class uses the app) enter your
      thesis for real-time feedback and revise. Sensitive documents (D, F) are analyzed historian-grade: you examine
      documented intent and consequences from the evidence — no conclusion is handed to you.</p>"""

    body = (cover
            + '<div class="page">' + copyr + '</div>'
            + '<div class="page">' + crosswalk + howto + intro + predict + '</div>'
            + '<h2 class="sec">The Documents</h2>' + docs_html
            + tnbox + planning + essay)
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


# ===========================================================================
# FILE 2 — SCAFFOLD & LANGUAGE-ACCESS COMPANION (inclusion sections)
# ===========================================================================
WORDBANK = [
    ("homestead", "a home and piece of land where a family lives and works", "granja familiar"),
    ("public land", "land owned by the government", "tierra pública"),
    ("claim", "a formal request to own or use land", "reclamo / solicitud"),
    ("affidavit", "a written promise a person swears is true", "declaración jurada"),
    ("citizen", "a legal member of a country", "ciudadano/a"),
    ("naturalization", "the legal process of becoming a citizen", "naturalización"),
    ("cultivate", "to prepare and grow crops on land", "cultivar"),
    ("patent", "the official paper that proves you own the land", "título de propiedad"),
    ("revert", "to go back to an earlier owner", "revertir / volver"),
    ("allegiance", "loyalty to a country or government", "lealtad"),
    ("reservation", "land set aside by the government for a Native nation", "reserva"),
    ("dispossession", "the forced loss of land or property", "despojo"),
    ("transcontinental", "crossing the whole continent", "transcontinental"),
    ("unappropriated", "not yet claimed by the government for a use (but often Native homeland)", "no asignado"),
]


def scaffold_html():
    css = head_css("U.S. History Hack™ · US.01 DBQ — Scaffold & Language-Access Companion")

    cover = f"""<div class="cover"><div class="brand">U.S. HISTORY HACK™ · SCAFFOLD SUPPORTS</div>
      <h1>Scaffold &amp; Language-Access Companion</h1>
      <div class="sub">Use alongside the US.01 Homestead Act Document-Based Investigation</div>
      <div class="dbqt">Everything you need to do your first DBQ with confidence.</div>
      <div class="tn">Works ALONGSIDE — never in place of — a student's IEP / 504 accommodations.</div>
      <div class="foot">Worked HIPPO + OPTIC models · EN/ES word bank · sentence stems · bucketing organizer ·
      thesis builder · step-by-step checklist · TroopToTeacher Technologies LLC<br>Generated: {ISO}</div></div>"""

    checklist = """<h2 class="sec">1 · Your DBQ Checklist — do these in order</h2>
      <div class="step"><div class="n">1</div><div class="t"><b>READ</b> the document and its context note. Use the
      Plain-Language box for the two law excerpts.</div></div>
      <div class="step"><div class="n">2</div><div class="t"><b>SOURCE IT.</b> Fill the HIPPO box (text) or OPTIC box
      (picture). Ask: who made it, when, and <i>why</i>?</div></div>
      <div class="step"><div class="n">3</div><div class="t"><b>SORT.</b> Which lens does it fit — gained a homestead,
      lost a homeland, or who decided?</div></div>
      <div class="step"><div class="n">4</div><div class="t"><b>PLAN.</b> Put your best documents in the bucketing
      organizer (section 5).</div></div>
      <div class="step"><div class="n">5</div><div class="t"><b>WRITE.</b> Use the thesis builder (section 6) and the
      sentence stems (section 4), then check the rubric in your workbook.</div></div>"""

    worked_hippo = """<table><tr><td class="q">H — Historical context</td><td>&ldquo;This law was passed in <u>1862</u>,
      during the Civil War, when the government wanted people to settle the West.&rdquo;</td></tr>
      <tr><td class="q">I — Intended audience</td><td>&ldquo;It speaks to ordinary people who wanted land — including
      immigrants becoming citizens.&rdquo;</td></tr>
      <tr><td class="q">P — Point of view</td><td>&ldquo;It is written by the U.S. government, which wanted the West
      settled — so it treats the land as free to give away.&rdquo;</td></tr>
      <tr><td class="q">P — Purpose</td><td>&ldquo;To get citizens to move west, farm the land, and build the
      nation.&rdquo;</td></tr>
      <tr><td class="q">O — Outside evidence</td><td>&ldquo;I know this land was already home to Native nations, which
      the law ignores.&rdquo;</td></tr></table>"""

    worked_optic = """<table><tr><td class="q">O — Overview</td><td>&ldquo;Two photos of the same young man — before and
      after a boarding school.&rdquo;</td></tr>
      <tr><td class="q">P — Parts</td><td>&ldquo;Left: long hair, traditional clothing. Right: short hair, a suit and
      tie.&rdquo;</td></tr>
      <tr><td class="q">T — Title / Text</td><td>&ldquo;The pairing is labeled &lsquo;before and after&rsquo; — it wants
      us to see a change.&rdquo;</td></tr>
      <tr><td class="q">I — Interrelationships</td><td>&ldquo;The school changed his hair, clothes, and name on
      purpose.&rdquo;</td></tr>
      <tr><td class="q">C — Conclusion</td><td>&ldquo;This shows a real cost of settling the West: Native children were
      forced to give up their culture.&rdquo;</td></tr></table>"""

    wb = "".join(f'<tr><td><b>{t}</b></td><td>{d}</td><td>{es}</td></tr>' for t, d, es in WORDBANK)

    stems = [("Sourcing", "&ldquo;Because Document ___ was made by ___ for ___, its purpose is ___, which means ___.&rdquo;"),
             ("Using a document", "&ldquo;Document ___ shows ___. This is evidence that ___ because ___.&rdquo;"),
             ("Weighing gain vs. cost", "&ldquo;While ___ gained ___ (Doc ___), ___ lost ___ (Doc ___).&rdquo;"),
             ("Thesis", "&ldquo;The Homestead Act gave ___ to ___, but it cost ___ for ___; therefore ___.&rdquo;"),
             ("Tennessee Connection", "&ldquo;In Tennessee, ___ (settlers heading west / the Cherokee removal) shows that ___.&rdquo;")]
    stem_html = "".join(f'<div class="stem"><b>{k}:</b> {v}</div>' for k, v in stems)

    body = cover + f"""
    {checklist}

    <h2 class="sec">2 · Worked HIPPO model (for text sources — Documents A &amp; B)</h2>
    <p class="note">Every text source: source it before you use it. Here is a completed model on Document A (the law).</p>
    <div class="frame"><span class="k">MODEL — HIPPO on Document A</span>{worked_hippo}</div>

    <h2 class="sec">3 · Worked OPTIC model (for pictures &amp; maps — Documents C–F)</h2>
    <p>Each picture is <b>its own document</b>. OPTIC = <b>O</b>verview · <b>P</b>arts · <b>T</b>itle/Text ·
    <b>I</b>nterrelationships · <b>C</b>onclusion. Name what you see first, then say what it means.</p>
    <div class="frame"><span class="k">MODEL — OPTIC on Document F (Tom Torlino)</span>{worked_optic}</div>

    <h2 class="sec">4 · Sentence stems &amp; frames</h2>{stem_html}

    <h2 class="sec">5 · Word bank (English / Español)</h2>
    <table class="plan"><tr><th style="width:26%">Term</th><th style="width:50%">Plain-language meaning</th>
    <th style="width:24%">Español</th></tr>{wb}</table>

    <h2 class="sec">6 · Evidence-bucketing organizer</h2>
    <p>Write each document letter under the lens it supports. A document can appear under more than one.</p>
    <table class="plan"><tr><th>Who gained a homestead? (docs)</th><th>Who lost a homeland? (docs)</th><th>Who decided? (docs)</th></tr>
    <tr><td style="height:1.4in"></td><td></td><td></td></tr></table>

    <h2 class="sec">7 · Thesis builder</h2>
    <div class="stem"><b>Formula:</b> a gain (&ldquo;gave ___ to ___&rdquo;) + a cost (&ldquo;but cost ___ for ___&rdquo;)
    + your judgment (&ldquo;therefore ___&rdquo;).</div>
    <div class="frame"><span class="k">WRITE YOUR THESIS HERE</span>{lines(3)}</div>

    <div class="callout" style="margin-top:12px"><b>These supports add to — they never replace — a student's legally
    required IEP or 504 accommodations.</b> Scaffold fading: use the full frames on Documents A–B, drop to reduced cues
    on C–E, and try Document F on your own.</div>
    """
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


# ===========================================================================
# FILE 3 — TEACHER GUIDE + ANSWER KEY + RUBRIC
# ===========================================================================
def teacher_html():
    css = head_css("U.S. History Hack™ · US.01 DBQ — Teacher Guide & Answer Key")

    cover = f"""<div class="cover"><div class="brand">U.S. HISTORY HACK™ · TEACHER GUIDE</div>
      <h1>Teacher Guide &amp; Answer Key</h1>
      <div class="sub">US.01 Homestead Act Document-Based Investigation</div>
      <div class="dbqt">Implementation · source notes · model response · scoring · differentiation for 3 inclusion &amp; 2 honors sections</div>
      <div class="tn">First-DBQ ready — everything you need to run it tomorrow.</div>
      <div class="foot">Author-generated teacher materials (not externally graded) · public-domain sources ·
      TroopToTeacher Technologies LLC<br>Generated: {ISO}</div></div>"""

    overview = """<h2 class="sec">1 · At a Glance</h2>
      <table class="plan"><tr><th style="width:26%">Field</th><th>Detail</th></tr>
      <tr><td><b>Standard</b></td><td>US.01 — Homestead Act &amp; Transcontinental Railroad → settlement of the West</td></tr>
      <tr><td><b>Investigation question</b></td><td>Who gained a homestead — and who lost a homeland?</td></tr>
      <tr><td><b>Documents</b></td><td>6 total: 2 verbatim statute-text (HIPPO) + 4 visual-primary (OPTIC)</td></tr>
      <tr><td><b>Time</b></td><td>1–2 class periods (first DBQ — plan for 2). Day 1: docs A–F + sourcing. Day 2: plan + write.</td></tr>
      <tr><td><b>Files</b></td><td>Student Workbook · Scaffold &amp; Language-Access Companion · this Teacher Guide</td></tr></table>
      <div class="callout"><b>Because this is students' first DBQ,</b> teach the process explicitly. Model HIPPO on
      Document A and OPTIC on Document C with the whole class before releasing them to work. The scaffolds in the
      workbook fade by design (A–B full → C–E reduced → F independent); do not restore earlier scaffolds on later
      documents — the fade is the skill.</div>"""

    pacing = """<h2 class="sec">2 · Suggested Pacing</h2>
      <table class="plan"><tr><th style="width:14%">Time</th><th style="width:22%">Phase</th><th>What students do</th></tr>
      <tr><td>10 min</td><td>Hook + frame</td><td>Read the investigation question; unpack &ldquo;What is a DBQ?&rdquo; page together.</td></tr>
      <tr><td>15 min</td><td>Model</td><td>Teacher thinks aloud: HIPPO on Doc A, OPTIC on Doc C. Students fill along.</td></tr>
      <tr><td>30 min</td><td>Guided → independent</td><td>Students work Docs B, D, E with reduced cues; Doc F independently.</td></tr>
      <tr><td>15 min</td><td>Tennessee Connection</td><td>Discuss, then students write two reasoning sentences.</td></tr>
      <tr><td>20 min</td><td>Plan + write</td><td>Complete the organizer, then draft the CER argument.</td></tr>
      <tr><td>10 min</td><td>Self-score</td><td>Students score their draft on the rubric (and enter the thesis in the app if used).</td></tr></table>"""

    # Source notes
    src_rows = ""
    for L, title, kind, badge, level, cite, ctx, payload, gq, ext in DOCS:
        teach = {
            "A": "Establishes the promise in law. Point students to &lsquo;unappropriated&rsquo; — the loaded assumption that Western land was free to give.",
            "B": "The five-year residence + &lsquo;prove up&rsquo; terms. Ask who could <i>afford</i> five years before a harvest; connect to commutation ($1.25/acre) as a wealth advantage.",
            "C": "Sourcing lens: a posed press photo of a national triumph. Ask who is <i>absent</i> — Chinese and Irish labor, and displaced nations.",
            "D": "Geographic reasoning (SSP.06). Have students trace how western lines cut through Native homelands to reach homestead country.",
            "E": "The promise realized for one family. Butcher sold these images as proof of success — a purpose that makes the photo a mild argument.",
            "F": "The cost. Handle with care and dignity; this is documented history of forced assimilation. Students reason from the pairing's intent, not a handed-down verdict.",
        }[L]
        src_rows += (f'<tr><td><b>Doc {L}</b></td><td>{title}<div class="note">{cite}</div></td>'
                     f'<td>{teach}</td></tr>')
    sources = f"""<h2 class="sec">3 · Source Notes (provenance + what to draw out)</h2>
      <table class="plan"><tr><th style="width:9%">Doc</th><th style="width:45%">Title &amp; citation</th>
      <th style="width:46%">Teaching move</th></tr>{src_rows}</table>
      <p class="note">All sources public domain with citable archives. Statute text is a verbatim excerpt of the
      Homestead Act of 1862 (12 Stat. 392); the workbook's Plain-Language boxes are paraphrase aids clearly labeled as
      such, never presented as the primary source.</p>"""

    model = """<h2 class="sec">4 · Model Thesis &amp; Annotated Exemplar</h2>
      <div class="callout"><b>Model thesis (target, level 3–4):</b> &ldquo;The Homestead Act gave 160 acres and a real
      chance at ownership to settlers and immigrants who could survive five years on the land (Docs A, B, E), but it
      treated Native homeland as &lsquo;unappropriated&rsquo; and helped push nations off their land (Docs D, F);
      therefore the Act was progress for some Americans and dispossession for others.&rdquo;</div>
      <p><b>Annotated exemplar paragraph</b> (teacher reference — how the parts earn rubric points):</p>
      <div class="stem"><b>[Claim]</b> The Homestead Act's benefits and costs fell on different people.
      <b>[Evidence + sourcing]</b> The law itself promised any adult citizen 160 acres for a $10 filing fee and five
      years' work (Doc A) — and the Rawding family photo (Doc E), <i>which a photographer sold as proof of success</i>,
      shows a family who made it. <b>[Reasoning]</b> For them the promise was real.
      <b>[Counter-evidence]</b> But the same law called the land &ldquo;unappropriated,&rdquo; and the before-and-after
      photos of Tom Torlino (Doc F) record Native children forced to shed their culture as their homelands were opened.
      <b>[Reasoning]</b> So &ldquo;free land&rdquo; for settlers was lost land for Native nations.</div>
      <p class="note">Use this to calibrate scoring — do not distribute it before students draft.</p>"""

    rubric = """<table class="rubric">
      <tr><th style="width:18%">Criterion</th><th>4 — Exceeds</th><th>3 — Meets</th><th>2 — Approaching</th><th>1 — Beginning</th></tr>
      <tr><td class="cr">Thesis (Claim)</td><td>Defensible claim answering &ldquo;for whom?&rdquo; with nuance</td><td>Clear claim that takes a position</td><td>Claim restates the prompt</td><td>No clear claim</td></tr>
      <tr><td class="cr">Evidence — documents</td><td>≥4 documents used accurately</td><td>3 documents used accurately</td><td>2 documents</td><td>0–1 documents</td></tr>
      <tr><td class="cr">Sourcing (HIPPO/OPTIC)</td><td>Sources ≥2 docs (POV/purpose)</td><td>Sources 1 doc</td><td>Attempts sourcing</td><td>No sourcing</td></tr>
      <tr><td class="cr">Analysis — gain &amp; cost</td><td>Weighs gain and cost with reasoning</td><td>Names a gain and a cost</td><td>One-sided</td><td>Summary only</td></tr>
      <tr><td class="cr">Tennessee Connection</td><td>Uses a TN example as evidence</td><td>Mentions a TN example</td><td>Vague TN reference</td><td>None</td></tr></table>
      <p class="note">20 points total (5 criteria × 4). Meets = 15/20. Convert to your gradebook as needed.</p>"""
    rubricsec = f"""<h2 class="sec">5 · Scoring Rubric (AP-aligned, 20 pts)</h2>{rubric}"""

    diff = """<h2 class="sec">6 · Differentiation Plan — 3 Inclusion Sections &amp; 2 Honors Sections</h2>
      <table class="plan"><tr><th style="width:22%">Group</th><th style="width:40%">What to hand them</th>
      <th style="width:38%">What success looks like</th></tr>
      <tr><td><b>3 Inclusion sections</b><br><span class="pill">★ Entry</span></td>
      <td>Workbook <b>+ the Scaffold &amp; Language-Access Companion</b>. Read the Plain-Language boxes aloud (or use the
      app read-aloud). Pre-teach the word bank. Do Docs A &amp; C together; allow partners for D–E; Doc F optional.
      Sentence stems available for the whole write.</td>
      <td>A claim + at least <b>2</b> documents + one sourced document, using the stems. Full HIPPO/OPTIC frames may
      stay in use throughout.</td></tr>
      <tr><td><b>2 Honors sections</b><br><span class="pill">▲ Extension</span></td>
      <td>Workbook only (no companion). Assign the <b>▲ Honors extension</b> question under each document and the
      historiography prompt below. Push independent sourcing from Doc B onward.</td>
      <td>A nuanced &ldquo;for whom&rdquo; thesis + <b>≥4</b> documents + <b>≥2</b> sourced + a weighed counterargument
      + the Tennessee Connection as real evidence.</td></tr></table>
      <div class="callout"><b>▲ Honors historiography prompt:</b> &ldquo;Historians disagree about whether the Homestead
      Act is best understood as a democratic land reform that built the American middle class, or as an engine of Native
      dispossession. Stake a position and defend it using at least four documents plus one piece of outside
      evidence.&rdquo;</div>
      <div class="callout"><b>Accommodations note.</b> These supports work <b>alongside — never in place of</b> — a
      student's legally required IEP/504 accommodations. Common built-ins available here: read-aloud (app), EN/ES word
      bank, sentence stems, chunked documents, partner work, extended time, and reduced document load (minimum 2 docs
      to meet the standard).</div>"""

    disclosure = f"""<h2 class="sec">7 · Honest Disclosure</h2>
      <div class="copyr" style="padding:0">
      <p>These teacher materials — model thesis, annotated exemplar, and rubric — are <b>author-generated by
      TroopToTeacher Technologies LLC</b> and have not been externally graded or normed. They are provided to calibrate
      scoring, not as an official answer key. The five documents are public domain; the statute text is verbatim from
      the Homestead Act of 1862 (12 Stat. 392, approved May 20, 1862).</p>
      <p><i>Framework stack:</i> TN US.01 first → RH/WHST literacy (cross-subject proof only; not marketed as Common
      Core per T.C.A. §49-6-2202) → AP U.S. History → C3 → IDM. History Hack is a <b>supplemental</b> resource under
      T.C.A. §49-6-2202(a)(3).</p>
      <p class="note">Trademarks use ™. ISBN [to be assigned]. Generated {ISO}.</p></div>"""

    body = (cover
            + '<div class="page">' + overview + pacing + sources + model + rubricsec + diff + disclosure + '</div>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    jobs = [
        (f"US01_Homestead_DBQ_Workbook_{STAMP}.pdf", workbook_html()),
        (f"US01_Homestead_DBQ_Scaffold_Supports_{STAMP}.pdf", scaffold_html()),
        (f"US01_Homestead_DBQ_Teacher_Guide_{STAMP}.pdf", teacher_html()),
    ]
    for name, html in jobs:
        HTML(string=html, base_url=str(IMG)).write_pdf(str(OUT / name))
        print("wrote", name)
    print("out dir:", OUT)
    print("ts", ISO)


if __name__ == "__main__":
    main()
