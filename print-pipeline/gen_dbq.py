#!/usr/bin/env python3
"""Unit 1 standalone DBQ SKU (print-first, no docx) — two PDFs via WeasyPrint:
  1. Unit1_DBQ_Workbook_<ts>.pdf     — student DBQ: investigation question, 8-document
     set (HIPPO for text/photo, OPTIC for cartoons), faded scaffolds, TN Connection,
     evidence-planning, essay prompt + rubric.
  2. Unit1_DBQ_Scaffold_Supports_<ts>.pdf — the scaffold / language-access companion:
     worked HIPPO + OPTIC frames, EN/ES word bank, thesis + CER stems, bucketing
     organizer, thesis builder. Works ALONGSIDE (never in place of) IEP/504 supports.
Every document is public-domain with honest provenance (real repository + URL).
Follows history-hack-dbq-workbook guardrails: America 250, TM not (R), ISBN "[to be
assigned]", visual-primary sources get standalone OPTIC, scaffold fading preserved,
version timestamp in filename + on-page.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT.parent / ".claude/skills/history-hack-tcap-deck-builder/assets/unit1-example"
TS = datetime.now(timezone.utc)
STAMP = TS.strftime("%Y%m%d_%H%M")
ISO = TS.strftime("%Y-%m-%dT%H:%M:%SZ")

NAVY, NAVY2, RED, GOLD, CARD, LIGHT, BORDER, INK = \
    "#1F3A5F", "#2C3E63", "#B22234", "#C9A227", "#F8F5EF", "#EEF2F8", "#C9C2B4", "#20262E"

# Document set — all verified public-domain assets from _images.json (honest citations).
DOCS = [
    ("A", "Golden Spike Ceremony at Promontory, Utah", "img/transcontinental-railroad-ceremony.jpg", "HIPPO", "full",
     "Russell, Andrew J. <i>Golden Spike Ceremony at Promontory, Utah.</i> 1869. Photograph. National Archives (RG 16-G). catalog.archives.gov/id/594940",
     "The Union Pacific and Central Pacific met here on May 10, 1869, completing the first transcontinental railroad.",
     "Whose achievement does this photograph celebrate — and whose labor and land are <i>not</i> pictured?"),
    ("B", "Official Railroad Map of the United States", "img/railroad-map-1890.jpg", "MAP", "full",
     "Matthews, Northrup &amp; Co. <i>Official Railroad Map of the United States, Dominion of Canada and Mexico.</i> ca. 1890. Library of Congress, Geography &amp; Map Division. loc.gov/item/gm71000843/",
     "By 1890 rail lines webbed the continent, moving people, crops, cattle, ore, and manufactured goods.",
     "What does the density of rail lines reveal about who could now reach markets — and who was displaced to build them?"),
    ("C", "Tom Torlino, Navajo — Before and After", "img/tom-torlino-carlisle.jpg", "HIPPO", "full",
     "Choate, John N. <i>Tom Torlino, Navajo, Before and After.</i> 1882 &amp; 1885. Richard Henry Pratt Papers, Beinecke Library, Yale University.",
     "The Carlisle Indian Industrial School photographed students on arrival and after assimilation. Its motto: “Kill the Indian, save the man.”",
     "What was the documented <i>purpose</i> of pairing these two images — and what cost does the transformation record?"),
    ("D", "“The Union as It Was — Worse Than Slavery”", "img/nast-worse-than-slavery.jpg", "OPTIC", "reduced",
     "Nast, Thomas. <i>The Union as It Was — Worse Than Slavery.</i> Harper’s Weekly, Oct. 24, 1874. Library of Congress Prints &amp; Photographs. loc.gov/pictures/item/2001696840/",
     "Published as Reconstruction collapsed, this cartoon depicts White League and Klan violence against a Southern Black family.",
     "What argument is Nast making about the <i>consequences</i> of ending Reconstruction protections?"),
    ("E", "“The Bosses of the Senate”", "img/bosses-of-the-senate.jpg", "OPTIC", "reduced",
     "Keppler, Joseph. <i>The Bosses of the Senate.</i> Puck, Jan. 23, 1889. Library of Congress Prints &amp; Photographs. loc.gov/pictures/item/2002718861/",
     "Bloated “trust” moneybags loom over senators; the “people’s entrance” is bolted shut.",
     "According to Keppler, <i>who decided</i> in Gilded Age politics — voters or corporate wealth?"),
    ("F", "“Next!” — the Standard Oil octopus", "img/standard-oil-octopus.jpg", "OPTIC", "reduced",
     "Keppler, Udo J. <i>Next!</i> Puck, Sept. 7, 1904. Library of Congress Prints &amp; Photographs (LC-DIG-ppmsca-25884). loc.gov/pictures/item/2001695241/",
     "A Standard Oil octopus grips statehouses, Congress, and industries, reaching for the White House.",
     "What does the octopus claim about the <i>reach</i> of monopoly power over American life?"),
    ("G", "“Five Cents a Spot” — a Bayard St. tenement", "img/five-cents-a-spot-riis.jpg", "HIPPO", "independent",
     "Riis, Jacob A. <i>Five Cents a Spot — Unauthorized Immigrant Lodgings in a Bayard Street Tenement.</i> 1889. Library of Congress Prints &amp; Photographs. loc.gov/pictures/item/2002710259/",
     "Riis used flash photography to document immigrant lodging houses in New York’s Lower East Side.",
     "What cost of industrial-era immigration does Riis make visible — and how might his framing shape the viewer?"),
    ("H", "Foreign-Born Population, by State: 1890", "img/map-foreign-born-1890.jpg", "DATA", "independent",
     "Gannett, Henry, and U.S. Census Office. <i>Foreign Born Population, by States and Territories: 1890.</i> Statistical Atlas of the United States. Library of Congress, Geography &amp; Map Division.",
     "An 1890 Census diagram mapping where the era’s immigrants concentrated.",
     "Where did “new” immigrants settle, and how does that pattern connect to the industrial centers on Doc B?"),
]

PERSPECTIVES = [
    ("Who benefited?", "Industrialists, railroads, settlers, national markets", "A, B"),
    ("Who bore the cost?", "American Indians, freedpeople, immigrant workers, the urban poor", "C, D, G"),
    ("Who decided?", "Trusts, party machines, and monopoly power", "E, F"),
]

FRAME = """<div class="page"></div>"""


def img_uri(rel):
    p = ASSETS / rel
    import base64
    b = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/jpeg;base64,{b}"


HEAD_CSS = """
* { box-sizing:border-box; }
body { font-family:'DejaVu Serif', Georgia, serif; color:%(INK)s; margin:0; font-size:10.6pt; line-height:1.4; }
h2,h3,.k,.doclabel,.brand { font-family:'DejaVu Sans', Arial, sans-serif; }
.page { page-break-after:always; }
.cover { height:9.1in; background:%(NAVY)s; color:#fff; padding:0.9in 0.8in; page-break-after:always; position:relative; border-left:14px solid %(RED)s;}
.cover .brand { color:%(GOLD)s; font-weight:bold; letter-spacing:1px; font-size:12pt; }
.cover h1 { font-size:30pt; margin:14px 0 6px; line-height:1.1; }
.cover .dbqt { font-size:15pt; color:#DCE6F1; font-style:italic; }
.cover .tn { margin-top:22px; background:%(GOLD)s; color:%(NAVY)s; font-family:'DejaVu Sans'; font-weight:bold; padding:8px 12px; border-radius:5px; display:inline-block; }
.cover .foot { position:absolute; bottom:0.7in; left:0.8in; right:0.8in; font-family:'DejaVu Sans'; font-size:8.5pt; color:#AFC0D6; }
.copyr { padding:0.5in 0.2in; font-size:9pt; color:#3a4250; }
.sec { color:%(NAVY)s; border-bottom:2px solid %(GOLD)s; padding-bottom:3px; margin:0 0 8px; font-size:15pt; }
.iq { background:%(NAVY)s; color:#fff; padding:12px 16px; border-radius:6px; font-size:13pt; font-family:'DejaVu Sans'; }
.iq .lab { color:%(GOLD)s; font-weight:bold; font-size:9pt; display:block; letter-spacing:1px; }
.lens { display:flex; gap:8px; margin:10px 0; }
.lens .c { flex:1; background:%(CARD)s; border:1pt solid %(BORDER)s; border-top:4px solid %(RED)s; border-radius:5px; padding:7px 9px; font-size:9pt; }
.lens .c b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
.doc { border:1pt solid %(BORDER)s; border-radius:6px; margin:0 0 12px; page-break-inside:avoid; }
.doch { background:%(NAVY)s; color:#fff; padding:6px 10px; font-family:'DejaVu Sans'; display:flex; justify-content:space-between; }
.doch .l { font-weight:bold; }
.doch .type { background:%(GOLD)s; color:%(NAVY)s; font-size:8pt; font-weight:bold; padding:1px 8px; border-radius:9px; }
.docb { padding:9px 12px; }
.docimg { text-align:center; margin:6px 0; }
.docimg img { max-width:78%%; max-height:3.2in; border:1pt solid %(BORDER)s; }
.src { font-size:8pt; color:#5C6470; font-style:italic; margin:3px 0 6px; }
.ctx { font-size:9.6pt; margin:4px 0; }
.gq { background:%(LIGHT)s; border-left:4px solid %(NAVY)s; padding:6px 10px; font-size:10pt; margin-top:6px; }
.gq b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
.frame { border:1pt dashed %(NAVY2)s; border-radius:5px; padding:6px 10px; margin-top:7px; background:#fff; }
.frame .k { color:%(RED)s; font-weight:bold; font-size:8.5pt; letter-spacing:.5px; }
.frame table { width:100%%; border-collapse:collapse; margin-top:3px; }
.frame td { border:0.5pt solid %(BORDER)s; padding:4px 6px; font-size:9pt; vertical-align:top; }
.frame td.q { width:26%%; background:%(CARD)s; font-family:'DejaVu Sans'; font-weight:bold; color:%(NAVY)s; }
.writeline { border-bottom:0.5pt solid #B9C0CC; height:0.34in; }
.fade { font-size:8pt; color:%(RED)s; font-family:'DejaVu Sans'; font-weight:bold; }
table.plan { width:100%%; border-collapse:collapse; }
table.plan th { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; padding:6px; font-size:9.5pt; text-align:left; }
table.plan td { border:1pt solid %(BORDER)s; padding:6px 8px; font-size:9.5pt; vertical-align:top; }
.rubric th { background:%(NAVY)s; color:#fff; font-family:'DejaVu Sans'; padding:5px 7px; font-size:9pt; text-align:left; }
.rubric td { border:0.5pt solid %(BORDER)s; padding:5px 7px; font-size:9pt; vertical-align:top; }
.tnbox { background:%(CARD)s; border:1.5pt solid %(GOLD)s; border-radius:6px; padding:9px 13px; margin:8px 0; }
.tnbox .k { color:%(RED)s; font-family:'DejaVu Sans'; font-weight:bold; }
.note { font-size:8.4pt; color:#5C6470; font-style:italic; }
.stem { background:%(CARD)s; border:1pt solid %(BORDER)s; border-radius:5px; padding:7px 11px; margin:6px 0; font-size:9.6pt; }
.stem b { color:%(NAVY)s; font-family:'DejaVu Sans'; }
@page { size:Letter portrait; margin:0.7in 0.7in 0.8in 0.7in;
  @bottom-left { content:"U.S. History Hack™ · Unit 1 DBQ"; font:8pt 'DejaVu Sans'; color:#5C6470; }
  @bottom-right { content:"© 2026 TroopToTeacher Technologies LLC · p. " counter(page); font:8pt 'DejaVu Sans'; color:#5C6470; } }
@page:first { margin:0; }
""" % dict(INK=INK, NAVY=NAVY, NAVY2=NAVY2, RED=RED, GOLD=GOLD, CARD=CARD, LIGHT=LIGHT, BORDER=BORDER)


def hippo_frame(level):
    fade = {"full": "Full scaffold", "reduced": "Reduced cues", "independent": "Independent"}[level]
    if level == "independent":
        return ('<div class="frame"><span class="k">HIPPO — analyze independently</span> '
                '<span class="fade">(' + fade + ')</span>'
                '<div class="writeline"></div><div class="writeline"></div><div class="writeline"></div></div>')
    rows = [("Historical context", "When/where was this made, and what was happening?"),
            ("Intended audience", "Who was meant to see it?"),
            ("Point of view", "Whose perspective — and what is left out?"),
            ("Purpose", "Why was it created?"),
            ("Outside evidence", "What do you already know that connects?")]
    if level == "reduced":
        rows = [("Point of view", ""), ("Purpose", ""), ("Outside evidence", "")]
    tr = "".join(f'<tr><td class="q">{q}{("<div class=note>"+h+"</div>") if h else ""}</td><td></td></tr>' for q, h in rows)
    return f'<div class="frame"><span class="k">HIPPO — text/photograph source</span> <span class="fade">({fade})</span><table>{tr}</table></div>'


def optic_frame(level):
    fade = {"full": "Full scaffold", "reduced": "Reduced cues", "independent": "Independent"}[level]
    rows = [("Overview", "First impression — what is happening?"),
            ("Parts", "List people, objects, symbols, labels."),
            ("Title / Text", "How do words/caption steer meaning?"),
            ("Interrelationships", "How do the parts connect to make a point?"),
            ("Conclusion", "What argument is the artist making?")]
    if level == "reduced":
        rows = [("Parts", "People, objects, symbols, labels"), ("Interrelationships", "How parts connect"), ("Conclusion", "The artist’s argument")]
    tr = "".join(f'<tr><td class="q">{q}{("<div class=note>"+h+"</div>") if h else ""}</td><td></td></tr>' for q, h in rows)
    return f'<div class="frame"><span class="k">OPTIC — visual primary source (its own document)</span> <span class="fade">({fade})</span><table>{tr}</table></div>'


def workbook_html():
    docs = ""
    for L, title, img, typ, level, cite, ctx, gq in DOCS:
        badge = {"HIPPO": "HIPPO", "OPTIC": "OPTIC", "MAP": "MAP · DATA", "DATA": "DATA"}[typ]
        frame = optic_frame(level) if typ == "OPTIC" else hippo_frame(level)
        docs += (f'<div class="doc"><div class="doch"><span class="l">Document {L} — {title}</span>'
                 f'<span class="type">{badge}</span></div><div class="docb">'
                 f'<div class="docimg"><img src="{img_uri(img)}"></div>'
                 f'<div class="src">Source: {cite} · Public domain.</div>'
                 f'<div class="ctx">{ctx}</div>'
                 f'<div class="gq"><b>Guiding question:</b> {gq}</div>{frame}</div></div>')

    plan = "".join(f'<tr><td><b>{q}</b></td><td>{d}</td><td>{docs_}</td><td></td></tr>'
                   for q, d, docs_ in PERSPECTIVES)

    rubric = """<table class="rubric" style="width:100%;border-collapse:collapse">
    <tr><th>Criterion</th><th>4 — Exceeds</th><th>3 — Meets</th><th>2 — Approaching</th><th>1 — Beginning</th></tr>
    <tr><td><b>Thesis</b></td><td>Defensible, nuanced claim answering “for whom?”</td><td>Clear claim that takes a position</td><td>Claim restates the prompt</td><td>No clear claim</td></tr>
    <tr><td><b>Evidence (docs)</b></td><td>Uses ≥5 documents accurately as evidence</td><td>Uses 4 documents accurately</td><td>Uses 2–3 documents</td><td>0–1 documents</td></tr>
    <tr><td><b>Sourcing (HIPPO/OPTIC)</b></td><td>Sources ≥3 docs (POV/purpose/audience)</td><td>Sources 2 docs</td><td>Sources 1 doc</td><td>No sourcing</td></tr>
    <tr><td><b>Analysis / perspective</b></td><td>Weighs benefit vs. cost across groups</td><td>Notes benefit and cost</td><td>One-sided</td><td>Summary only</td></tr>
    <tr><td><b>Tennessee Connection</b></td><td>Integrates a TN example as evidence</td><td>Mentions a TN example</td><td>Vague TN reference</td><td>None</td></tr></table>"""

    lens = "".join(f'<div class="c"><b>{q}</b><br>{d}</div>' for q, d, _ in PERSPECTIVES)

    cover = f"""<div class="cover"><div class="brand">U.S. HISTORY HACK™ · AMERICA 250</div>
      <h1>Unit 1 · Document-Based Investigation</h1>
      <div class="dbqt">Industrialization &amp; Westward Expansion, 1877–1900 — <b>Progress for Whom?</b></div>
      <div class="tn">TENNESSEE CONNECTION: Pap Singleton &amp; the Exodusters · George Jordan, Buffalo Soldier (Williamson Co.)</div>
      <div class="foot">Standalone DBQ SKU · 8 verified public-domain documents · HIPPO + OPTIC ·
      ISBN [to be assigned] · TroopToTeacher Technologies LLC<br>Generated: {ISO}</div></div>"""

    copyr = f"""<div class="copyr"><p><b>U.S. History Hack™ — Unit 1 Document-Based Investigation.</b> © 2026 TroopToTeacher
      Technologies LLC. Author/producer: TroopToTeacher Technologies LLC. Single-classroom reproduction license.</p>
      <p>All documents are in the <b>public domain</b>, with honest provenance and a citable archive behind each asset
      (Library of Congress, National Archives, and the Beinecke Library, Yale). Nothing here is composed and presented
      as a primary source. Pearson / McGraw&nbsp;Hill / Savvas are category references only.</p>
      <p><i>Framework stack:</i> Tennessee Academic Standards (US.01–US.07) first → RH/WHST literacy practices
      (cross-subject proof only; not marketed as Common Core per T.C.A. §49-6-2202) → AP U.S. History → C3 → IDM.</p>
      <p class="note">Trademarks use ™. ISBN “[to be assigned].” Generated {ISO}. This is a district/school-board
      adoption artifact — provenance is honest and every claim is verifiable.</p></div>"""

    intro = f"""<h2 class="sec">The Investigation</h2>
      <div class="iq"><span class="lab">INVESTIGATION QUESTION</span>
      Between 1877 and 1900, American industry, railroads, and cities grew at breathtaking speed. Using the documents,
      answer: <b>Was industrial progress a benefit or a cost — and for whom?</b></div>
      <p style="margin:9px 2px">Read each document, source it (HIPPO for photographs and text; <b>OPTIC</b> for political
      cartoons — each cartoon is its own document), and sort your evidence by the three lenses below. Then write an
      evidence-based argument. Scaffolds fade as you go: Documents A–C give full frames, D–F reduced cues, G–H you analyze independently.</p>
      <div class="lens">{lens}</div>"""

    tnbox = """<div class="tnbox"><span class="k">TENNESSEE CONNECTION — reason with it as evidence.</span>
      As Reconstruction collapsed (Doc D), <b>Benjamin “Pap” Singleton of Nashville</b> organized the <b>Exodusters</b> —
      thousands of Black Tennesseans and Southerners who migrated to Kansas seeking land and safety. Meanwhile
      <b>George Jordan</b> of Williamson County served in the Buffalo Soldiers and earned the Medal of Honor on the
      frontier opened by Docs A–B. <i>How do these Tennesseans complicate a simple “progress” story?</i></div>"""

    planning = f"""<h2 class="sec">Plan Your Evidence</h2>
      <table class="plan"><tr><th style="width:20%">Lens</th><th style="width:34%">Group affected</th>
      <th style="width:14%">Best docs</th><th style="width:32%">Your evidence + reasoning</th></tr>{plan}</table>"""

    essay = f"""<h2 class="sec">Write Your Argument</h2>
      <p><b>Prompt.</b> Using at least <b>five</b> documents and one Tennessee example, argue whether industrialization
      and westward expansion (1877–1900) were, on balance, <b>progress</b> — and <b>for whom</b>. Source at least three
      documents (name the point of view or purpose). </p>
      <div class="stem"><b>Thesis frame:</b> “Although industrialization brought ______ for ______, it came at the cost
      of ______ for ______; therefore progress was ______.”</div>
      {''.join('<div class="writeline"></div>' for _ in range(9))}
      <h3 class="sec" style="font-size:12pt;margin-top:10px">Scoring Rubric</h3>{rubric}
      <p class="note" style="margin-top:6px">Sensitive documents (e.g., Doc C, Doc D) are analyzed historian-grade:
      students examine documented intent and consequences from the evidence — no conclusion is handed to them.</p>"""

    body = (cover + '<div class="page">' + copyr + '</div>'
            + '<div class="page">' + intro + tnbox + '</div>'
            + '<h2 class="sec">The Documents</h2>' + docs
            + '<div class="page">' + planning + '</div>'
            + essay)
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{HEAD_CSS}</style></head><body>{body}</body></html>'


def scaffold_html():
    wordbank = [("industrialization", "the shift to large-scale factory production", "industrialización"),
                ("monopoly / trust", "one company controlling an entire industry", "monopolio"),
                ("assimilation", "forcing a group to give up its culture", "asimilación"),
                ("tenement", "an overcrowded urban apartment building", "vivienda / conventillo"),
                ("disenfranchisement", "taking away the right to vote", "privación del voto"),
                ("political machine", "an organization that controls votes and favors", "maquinaria política"),
                ("nativism", "favoring native-born people over immigrants", "nativismo"),
                ("perspective / point of view", "whose side the source shows", "punto de vista")]
    wb = "".join(f'<tr><td><b>{t}</b></td><td>{d}</td><td>{es}</td></tr>' for t, d, es in wordbank)

    worked_hippo = """<table><tr><td class="q">Historical context</td><td>“This was made in <u>1889</u>, when trusts dominated the economy…”</td></tr>
      <tr><td class="q">Intended audience</td><td>“<i>Puck</i>’s readers were middle-class reformers…”</td></tr>
      <tr><td class="q">Point of view</td><td>“The artist opposes trust power, so he exaggerates…”</td></tr>
      <tr><td class="q">Purpose</td><td>“He wants to persuade readers that…”</td></tr>
      <tr><td class="q">Outside evidence</td><td>“I know the Sherman Antitrust Act (1890) tried to…”</td></tr></table>"""

    stems = [("Sourcing", "“Because this source was made by ___ for ___, its point of view is ___, which means ___.”"),
             ("Using a document", "“Document ___ shows ___. This is evidence that ___ because ___.”"),
             ("Weighing perspectives", "“While ___ benefited (Doc ___), ___ bore the cost (Doc ___).”"),
             ("Thesis", "“Although industrialization brought ___ for ___, it cost ___ for ___; therefore progress was ___.”"),
             ("Tennessee Connection", "“In Tennessee, ___ (e.g., Pap Singleton / George Jordan) shows that ___.”")]
    stem_html = "".join(f'<div class="stem"><b>{k}:</b> {v}</div>' for k, v in stems)

    css = HEAD_CSS.replace('content:"U.S. History Hack™ · Unit 1 DBQ"', 'content:"U.S. History Hack™ · Unit 1 DBQ — Scaffold Supports"')
    cover = f"""<div class="cover"><div class="brand">U.S. HISTORY HACK™ · SCAFFOLD SUPPORTS</div>
      <h1>Unit 1 DBQ · Scaffold &amp; Language-Access Companion</h1>
      <div class="dbqt">Use alongside the Unit 1 Document-Based Investigation</div>
      <div class="tn">Works ALONGSIDE — never in place of — a student’s IEP/504 accommodations.</div>
      <div class="foot">Faded HIPPO + OPTIC frames · EN/ES word bank · thesis &amp; CER stems · bucketing organizer ·
      TroopToTeacher Technologies LLC<br>Generated: {ISO}</div></div>"""

    body = cover + f"""
    <h2 class="sec">1 · Worked HIPPO frame (text &amp; photographs)</h2>
    <p class="note">Every text or photograph source: source it before you use it. Here is a completed model on Doc F (“Next!”).</p>
    <div class="frame"><span class="k">MODEL — HIPPO</span>{worked_hippo}</div>

    <h2 class="sec">2 · Worked OPTIC frame (political cartoons)</h2>
    <p>Each cartoon is <b>its own document</b>. OPTIC = <b>O</b>verview · <b>P</b>arts · <b>T</b>itle/Text ·
    <b>I</b>nterrelationships · <b>C</b>onclusion. Name the symbols first, then the argument.</p>
    <div class="frame"><span class="k">OPTIC — steps</span>
      <table><tr><td class="q">Overview</td><td>What is happening at first glance?</td></tr>
      <tr><td class="q">Parts</td><td>List every person, object, symbol, and label.</td></tr>
      <tr><td class="q">Title / Text</td><td>How do the words steer the meaning?</td></tr>
      <tr><td class="q">Interrelationships</td><td>How do the parts connect?</td></tr>
      <tr><td class="q">Conclusion</td><td>What argument is the artist making — and about whom?</td></tr></table></div>

    <h2 class="sec">3 · Word bank (EN / ES)</h2>
    <table class="plan"><tr><th style="width:24%">Term</th><th style="width:52%">Plain-language meaning</th><th style="width:24%">Español</th></tr>{wb}</table>

    <h2 class="sec">4 · Sentence stems &amp; frames</h2>{stem_html}

    <h2 class="sec">5 · Evidence-bucketing organizer</h2>
    <table class="plan"><tr><th>Who benefited? (docs)</th><th>Who bore the cost? (docs)</th><th>Who decided? (docs)</th></tr>
    <tr><td style="height:1.5in"></td><td></td><td></td></tr></table>

    <h2 class="sec">6 · Thesis builder</h2>
    <div class="stem"><b>Formula:</b> Concession (“Although ___”) + Claim (“progress ___”) + <b>for whom</b> (“for ___, but not ___”) + Reason (“because ___”).</div>
    <div class="writeline"></div><div class="writeline"></div>
    <p class="note" style="margin-top:8px">Scaffold fading: use full frames on Docs A–C, drop to reduced cues on D–F, and analyze G–H independently.
    These supports complement — they never replace — a student’s legally required accommodations.</p>
    """
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def main():
    (ROOT / "out").mkdir(exist_ok=True)
    wb = ROOT / f"out/Unit1_DBQ_Workbook_{STAMP}.pdf"
    sc = ROOT / f"out/Unit1_DBQ_Scaffold_Supports_{STAMP}.pdf"
    HTML(string=workbook_html(), base_url=str(ASSETS)).write_pdf(str(wb))
    HTML(string=scaffold_html(), base_url=str(ASSETS)).write_pdf(str(sc))
    print("wrote", wb.name, "+", sc.name, "| ts", ISO)


if __name__ == "__main__":
    main()
