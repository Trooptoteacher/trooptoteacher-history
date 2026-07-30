# -*- coding: utf-8 -*-
"""Unit 1 Teacher Deck — one continuous teacher deck for Foundations of
Constitutional Government (GC.01-GC.09), built to the platinum standard.

Reproducible: one JSON source (unit1_content.json) -> N 16:9 slides. Every fact
(targets, hooks, vocabulary, primary-source quotations + attributions, the CFU
answer key + rationale) is read verbatim from the authored content; nothing is
invented here. Brand = Government Hack (navy / red / gold / cream), matching the
U.S. History Hack teacher-deck house style. Rendered to a landscape PDF via
headless Chromium.
"""
import os, json, html, base64, mimetypes

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "..", "..", "unit6", "analysis", "unit6_content.json")
IMAGES = os.path.join(HERE, "unit6_images.json")
ASSETS = HERE  # image 'file' paths in the manifest are relative to this folder
AUDIENCE = os.environ.get("AUDIENCE", "teacher")
STUDENT = (AUDIENCE == "student")
DECK_KIND = "Student Deck" if STUDENT else "Teacher Deck"
if STUDENT:
    OUT = os.path.join(HERE, "..", "Unit6_Student_Deck", "pages", "unit6_student_deck.html")
else:
    OUT = os.path.join(HERE, "pages", "unit6_teacher_deck.html")

D = json.load(open(CONTENT))
U = D["unit"]
ORDER = D["order"]
S = D["standards"]
IMG = json.load(open(IMAGES)) if os.path.exists(IMAGES) else {}

def esc(x):
    return html.escape(str(x), quote=False)

TYPE_ICON = {"document": "&#128220;", "cartoon": "&#128499;", "portrait": "&#128100;", "emblem": "&#127894;"}

def source_frame(code, quote=None, qattr=None):
    """Render the primary-source visual for a standard: the real image if the
    binary is present, else a cited source frame (so the deck teaches with the
    source now and auto-fills when the scan is dropped in). Never fabricates."""
    rec = (IMG.get(code) or {}).get("anchor")
    if not rec:
        return ""
    quote_html = (f'<div class="imgquote">&ldquo;{esc(quote)}&rdquo; '
                  f'<span class="qa">&mdash; {esc(qattr)}</span></div>') if quote else ""
    cite = f"{esc(rec['title'])} &middot; {esc(rec['creator'])} ({esc(rec['year'])}) &middot; {esc(rec['repository'])}"
    fpath = os.path.join(ASSETS, rec["file"])
    if os.path.exists(fpath):
        mime = mimetypes.guess_type(fpath)[0] or "image/jpeg"
        b64 = base64.b64encode(open(fpath, "rb").read()).decode()
        inner = f'<div class="imgwrap"><img src="data:{mime};base64,{b64}" alt="{esc(rec.get("alt_en",""))}"></div>'
    else:
        icon = TYPE_ICON.get(rec.get("type", "document"), "&#128220;")
        inner = (f'<div class="imgph"><div class="ic">{icon}</div>'
                 f'<div class="phlbl">PRIMARY SOURCE &middot; {esc(rec.get("type","document")).upper()}</div>'
                 f'<div class="phttl">{esc(rec["title"])}</div>'
                 f'<div class="phsub">drop image: <code>{esc(os.path.basename(rec["file"]))}</code></div></div>')
    return (f'<div class="card srcimg" style="flex:1 1 auto;"><div class="ch navy">Primary Source</div>'
            f'<div class="cb">{inner}<div class="imgtext"><div class="imgcap">{esc(rec["caption"])}</div>'
            f'{quote_html}<div class="imgcite">{cite}</div></div></div></div>')

FOOT = "Government Hack&trade; &middot; Foundations of Constitutional Government &middot; Unit 1 Teacher Deck"

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0;}
:root{ --navy:#1B2A4A; --red:#B22234; --gold:#C89B3C; --cream:#F7F5EF; --paper:#fff;
  --navy-tint:#EEF1F7; --red-tint:#FBEEEF; --gold-tint:#FAF3E2; --green-tint:#EAF2EC;
  --rule:#CBD2DE; --muted:#5A6579; --ink:#1B2A4A; }
@page{ size:13.333in 7.5in; margin:0; }
html,body{ background:#8a8f99; font-family:"Helvetica Neue",Arial,sans-serif; color:var(--ink); }
.slide{ position:relative; width:13.333in; height:7.5in; background:var(--paper); overflow:hidden;
  page-break-after:always; display:flex; flex-direction:column; }
.slide:last-child{ page-break-after:auto; }

/* ---- shared header band ---- */
.shead{ flex:0 0 auto; background:var(--navy); color:#fff; display:flex; align-items:center;
  justify-content:space-between; padding:16px 34px; border-bottom:5px solid var(--red); }
.shead .l{ display:flex; flex-direction:column; gap:3px; }
.shead .kick{ font-size:11pt; letter-spacing:.14em; font-weight:800; color:var(--gold); text-transform:uppercase; }
.shead h2{ font-family:Georgia,serif; font-size:27pt; font-weight:700; line-height:1.02; }
.shead .r{ display:flex; flex-direction:column; align-items:flex-end; gap:6px; }
.chip{ background:rgba(255,255,255,.12); border:1.5px solid var(--gold); color:#fff; font-size:9.5pt;
  font-weight:700; padding:5px 12px; border-radius:14px; white-space:nowrap; }
.chip.ssp{ background:var(--red); border-color:var(--red); }

/* ---- body grid ---- */
.body{ flex:1 1 auto; display:flex; gap:22px; padding:22px 34px; min-height:0; }
.col{ display:flex; flex-direction:column; gap:14px; min-height:0; }
.col.main{ flex:1.35 1 0; } .col.side{ flex:1 1 0; }

.card{ border:1.8px solid var(--rule); border-radius:10px; overflow:hidden; display:flex; flex-direction:column; }
.card .ch{ font-size:10.5pt; font-weight:800; letter-spacing:.03em; text-transform:uppercase; color:#fff;
  padding:6px 14px; }
.card .cb{ padding:11px 15px; font-size:13.5pt; line-height:1.4; color:#22303f; }
.ch.navy{ background:var(--navy); } .ch.red{ background:var(--red); } .ch.gold{ background:var(--gold); color:var(--navy); }
.ch.green{ background:#1e6b40; }

.target{ background:var(--navy-tint); border-left:6px solid var(--navy); border-radius:0 8px 8px 0;
  padding:12px 16px; font-size:14pt; line-height:1.34; color:#22303f; }
.target b{ color:var(--navy); }
.hook{ background:var(--gold-tint); border-left:6px solid var(--gold); border-radius:0 8px 8px 0;
  padding:12px 16px; font-size:15pt; line-height:1.34; font-style:italic; color:#3a2f12; }
.hook .lbl{ font-style:normal; font-weight:800; font-size:9.5pt; letter-spacing:.08em; text-transform:uppercase; color:#7a5c15; display:block; margin-bottom:3px; }

/* vocab */
.vterm{ font-size:15pt; font-weight:800; color:var(--navy); }
.vterm .say{ font-size:10pt; font-weight:600; color:var(--muted); font-style:italic; }
.ves{ font-size:11pt; color:var(--red); font-weight:700; margin:2px 0 5px; }
.vdef{ font-size:12.5pt; line-height:1.36; color:#22303f; }

/* source image frame */
.srcimg .cb{ display:flex; gap:14px; align-items:stretch; padding:12px 15px; }
.imgwrap{ flex:0 0 auto; width:2.5in; display:flex; align-items:center; justify-content:center; }
.imgwrap img{ max-width:100%; max-height:2.9in; border:2px solid var(--navy); border-radius:4px; object-fit:contain; }
.imgph{ flex:0 0 auto; width:2.5in; min-height:2.6in; border:2.5px dashed var(--gold); border-radius:8px; background:var(--gold-tint);
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:14px; gap:6px; }
.imgph .ic{ font-size:42pt; line-height:1; }
.imgph .phlbl{ font-size:8.5pt; font-weight:800; letter-spacing:.08em; color:#7a5c15; }
.imgph .phttl{ font-size:12pt; font-weight:800; color:var(--navy); line-height:1.2; }
.imgph .phsub{ font-size:8.5pt; color:var(--muted); } .imgph code{ font-size:8pt; background:#fff; padding:1px 5px; border-radius:3px; border:1px solid var(--rule); }
.imgtext{ flex:1 1 0; display:flex; flex-direction:column; gap:7px; min-width:0; }
.imgcap{ font-size:12pt; line-height:1.36; color:#22303f; }
.imgquote{ font-family:Georgia,serif; font-style:italic; font-size:12pt; line-height:1.38; color:#3a4455;
  border-left:4px solid var(--gold); padding:2px 0 2px 11px; }
.imgquote .qa{ font-style:normal; font-size:9.5pt; font-weight:700; color:var(--muted); }
.imgcite{ margin-top:auto; font-size:8.5pt; color:var(--muted); font-weight:700; }

/* CFU */
.cfu .opt{ display:flex; gap:9px; align-items:flex-start; font-size:12.5pt; line-height:1.32; padding:3px 0; }
.cfu .k{ font-weight:800; color:var(--navy); flex:0 0 auto; }
.cfu .opt.key{ background:var(--green-tint); border-radius:6px; padding:5px 8px; }
.cfu .opt.key .k{ color:#1e6b40; }
.ans{ margin-top:9px; background:var(--green-tint); border:1.6px solid #1e6b40; border-radius:8px;
  padding:9px 13px; font-size:11.5pt; line-height:1.34; color:#173d27; }
.ans b{ color:#1e6b40; }

/* teacher notes strip */
.tnotes{ flex:0 0 auto; background:var(--cream); border-top:2px solid var(--gold); padding:9px 34px;
  font-size:10.5pt; line-height:1.3; color:#3a2f12; display:flex; gap:12px; align-items:baseline; }
.tnotes b{ color:#7a5c15; text-transform:uppercase; letter-spacing:.05em; font-size:9pt; flex:0 0 auto; }

/* per-standard UDL 3.0 + MTSS strip (visible to students AND teachers) */
.udlmtss{ flex:0 0 auto; background:var(--navy-tint); border-top:2px solid var(--navy); padding:7px 34px;
  font-size:9pt; line-height:1.32; color:#22303f; display:flex; flex-direction:column; gap:2px; }
.udlmtss .ln b{ color:var(--navy); text-transform:uppercase; letter-spacing:.04em; font-size:8.5pt; }
.access .r .t{ font-size:12pt; }

/* footer */
.sfoot{ position:absolute; bottom:8px; right:20px; font-size:8pt; color:#9aa2b2; }
.sfoot .brand{ color:var(--navy); font-weight:700; }
.pgno{ position:absolute; bottom:8px; left:20px; font-size:8pt; color:#9aa2b2; }

/* ---- title slide ---- */
.title{ background:var(--navy); color:#fff; justify-content:center; align-items:center; text-align:center; padding:0 90px; }
.title .eye{ font-size:12pt; letter-spacing:.22em; font-weight:800; text-transform:uppercase; color:var(--gold); }
.title h1{ font-family:Georgia,serif; font-size:52pt; font-weight:700; line-height:1.04; margin:16px 0 6px; }
.title .course{ font-size:16pt; color:#B5D4F4; font-weight:600; }
.title .rule{ width:120px; height:4px; background:var(--red); margin:22px auto; border-radius:2px; }
.title .eq{ font-family:Georgia,serif; font-style:italic; font-size:19pt; color:#e6d3a3; max-width:9in; line-height:1.4; }
.title .meta{ margin-top:20px; font-size:11pt; color:#8ea3c4; letter-spacing:.03em; }
.title .badge{ position:absolute; top:34px; right:44px; border:2px solid var(--gold); color:var(--gold);
  font-size:10pt; font-weight:800; letter-spacing:.1em; text-transform:uppercase; padding:6px 14px; border-radius:5px; }

/* ---- section/list slide ---- */
.big-eq{ flex:1 1 auto; display:flex; flex-direction:column; justify-content:center; padding:34px 60px; gap:20px; }
.big-eq .q{ font-family:Georgia,serif; font-size:30pt; font-weight:700; color:var(--navy); line-height:1.18; }
.big-eq .q .u{ color:var(--red); }
.road{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; }
.road .r{ background:var(--navy-tint); border-left:5px solid var(--navy); border-radius:0 8px 8px 0; padding:9px 13px; }
.road .r .c{ font-weight:800; color:var(--red); font-size:11pt; }
.road .r .t{ font-size:12pt; color:#22303f; line-height:1.25; margin-top:2px; }

/* perspectives */
.persp{ flex:1 1 auto; display:grid; grid-template-columns:1fr 1fr; gap:16px; padding:22px 34px; }
.persp .p{ background:var(--paper); border:1.8px solid var(--rule); border-top:5px solid var(--red); border-radius:8px; padding:13px 16px; }
.persp .p h3{ font-size:15pt; color:var(--navy); margin-bottom:5px; }
.persp .p p{ font-size:12pt; line-height:1.36; color:#22303f; }

/* tn slide */
.tnbig{ flex:1 1 auto; display:flex; gap:24px; padding:26px 44px; align-items:center; }
.tnbig .star{ font-size:80pt; color:var(--gold); flex:0 0 auto; }
.tnbig .t{ font-size:17pt; line-height:1.5; color:#22303f; } .tnbig .t b{ color:var(--navy); }

/* closing */
.close{ background:var(--navy); color:#fff; justify-content:center; align-items:center; text-align:center; padding:0 90px; }
.close h1{ font-family:Georgia,serif; font-size:34pt; margin-bottom:14px; }
.close .rule{ width:120px; height:4px; background:var(--red); margin:16px auto; border-radius:2px; }
.close p{ font-size:15pt; color:#cdd4e2; line-height:1.5; max-width:9in; }
.close .stds{ margin-top:18px; font-size:12pt; color:var(--gold); letter-spacing:.05em; }
"""

UDLMTSS = ('<div class="udlmtss">'
  '<div class="ln"><b>UDL 3.0 (CAST):</b> read-aloud on request &middot; key terms glossed EN/ES &middot; respond in writing, speech, or a labeled diagram &middot; large-print &amp; screen-reader friendly.</div>'
  '<div class="ln"><b>MTSS:</b> Tier 1 core lesson for all &middot; Tier 2 small-group reteach of this standard (Cornell cues + graphic organizer), then re-check &middot; Tier 3 intensive 1:1 with concrete&rarr;representational&rarr;abstract scaffolding, progress-monitored to the same standard.</div>'
  '</div>')
def tstrip(inner):
    # teacher-only note strip; dropped entirely in the student deck
    return "" if STUDENT else f'<div class="tnotes">{inner}</div>'
STD_NOTE = "<b>Teacher move</b><span>Open with the hook, read the source aloud, then run the CFU as a quick cold-call or mini-whiteboard check before the organizer. Vocabulary is bilingual (EN/ES) &mdash; project the Spanish gloss for ELL access.</span>"
PERSP_NOTE = f"<b>Why it matters</b><span>{esc(U['perspectives_intro'][:210])}</span>"
TN_NOTE = f"<b>Task</b><span>{esc(U.get('tn_connection_task',''))}</span>"
MIS_NOTE = "<b>Why it's here</b><span>These are the built-in UDL 3.0 moves — a belief-check (9.1), on-standard play (7.3), cross-unit spiral (3.4), and conversation norms (9.4). Use them; they make the unit stick.</span>"

slides = []
def slide(html_inner, cls="", pageno=None):
    foot = f'<div class="sfoot"><span class="brand">Government Hack&trade;</span> &middot; Unit 1</div>'
    pg = f'<div class="pgno">{pageno}</div>' if pageno else ""
    slides.append(f'<div class="slide {cls}">{html_inner}{foot}{pg}</div>')

# ---- 1. Title ----
slide(f"""
  <div class="badge">{DECK_KIND}</div>
  <div class="eye">Government Hack &middot; TroopToTeacher Technologies</div>
  <h1>Foundations of<br>Constitutional Government</h1>
  <div class="course">United States Government &amp; Civics (GC) &middot; Unit 1 &middot; GC.01&ndash;GC.09</div>
  <div class="rule"></div>
  <div class="eq">&ldquo;{esc(U['essential_question'])}&rdquo;</div>
  <div class="meta">Grades 9&ndash;12 &middot; Suggested {esc(U.get('suggested_days','15-17'))} days &middot; Supplemental under TCA &sect; 49-6-2202(a)(3)</div>
""", cls="title")

# ---- Student access slide (student deck only) ----
if STUDENT:
    slide(f"""
  <div class="shead"><div class="l"><div class="kick">Supports &middot; Universal Design for Learning</div><h2>Supports Available to Everyone</h2></div>
    <div class="r"><span class="chip">UDL 3.0</span><span class="chip ssp">Same target for all</span></div></div>
  <div class="big-eq access">
    <div class="q">Same learning target for all &mdash; <span class="u">supports available to everyone.</span></div>
    <div class="road">
      <div class="r"><div class="c">Read &amp; understand</div><div class="t">Ask for any text to be read aloud. Key terms are glossed in English and Spanish.</div></div>
      <div class="r"><div class="c">Show what you know</div><div class="t">Respond in writing, in speech, or with a labeled diagram &mdash; your choice.</div></div>
      <div class="r"><div class="c">Access for all</div><div class="t">Large-print and screen-reader friendly. Need another pass? Small-group and 1:1 support are built in.</div></div>
    </div>
  </div>
  {UDLMTSS}
""")

# ---- 2. Essential question + roadmap ----
road = ""
for c in ORDER:
    road += f'<div class="r"><div class="c">{esc(c)}</div><div class="t">{esc(S[c]["title"])}</div></div>'
slide(f"""
  <div class="shead"><div class="l"><div class="kick">Unit 1 &middot; Roadmap</div><h2>Where We Are Going</h2></div>
    <div class="r"><span class="chip">9 standards</span><span class="chip ssp">SSP.01&ndash;06</span></div></div>
  <div class="big-eq">
    <div class="q">Essential Question: <span class="u">{esc(U['essential_question'])}</span></div>
    <div class="road">{road}</div>
  </div>
""", pageno="2")

# ---- 3..N per-standard ----
pg = 3
for c in ORDER:
    s = S[c]
    v = s["vocab"][0]
    src = s["sources"][0]
    cfu = s["cfu"]
    opts = ""
    for k in ["A", "B", "C", "D"]:
        keycls = "" if STUDENT else (" key" if k == cfu["key"] else "")
        mark = "" if STUDENT else (" &check;" if k == cfu["key"] else "")
        opts += f'<div class="opt{keycls}"><span class="k">{k}{mark}</span><span>{esc(cfu["options"][k])}</span></div>'
    ans_html = "" if STUDENT else f'<div class="ans"><b>Answer: {esc(cfu["key"])}.</b> {esc(cfu["why"])}</div>'
    repo = src.get("repo", "")
    tn = s.get("tn_connection")
    tn_chip = '<span class="chip" style="background:var(--gold);color:var(--navy)">&#9733; Tennessee</span>' if tn else ""
    tnotes = (f'<b>&#9733; Tennessee</b><span>{esc(tn)}</span>' if tn else
              '<b>Teacher move</b><span>Open with the hook, read the source aloud, then run the CFU as a quick cold-call or mini-whiteboard check before the organizer. Vocabulary is bilingual (EN/ES) &mdash; project the Spanish gloss for ELL access.</span>')
    slide(f"""
  <div class="shead"><div class="l"><div class="kick">{esc(c)} &middot; {esc(s['civic_label'])}</div><h2>{esc(s['title'])}</h2></div>
    <div class="r"><span class="chip">{esc(c)}</span><span class="chip ssp">{esc(s['ssp_focus'])}</span>{tn_chip}</div></div>
  <div class="body">
    <div class="col main">
      <div class="target"><b>Learning target:</b> {esc(s['target'])}</div>
      {source_frame(c, src['quote'], f"{src['who']}, {src['title']} ({src['date']})")}
      <div class="hook"><span class="lbl">Hook</span>{esc(s['hook'])}</div>
    </div>
    <div class="col side">
      <div class="card"><div class="ch gold">Key Vocabulary</div>
        <div class="cb"><div class="vterm">{esc(v['term'])} <span class="say">/{esc(v.get('say',''))}/</span></div>
          <div class="ves">{esc(v.get('es',''))}</div>
          <div class="vdef">{esc(v['def'])}</div></div></div>
      <div class="card cfu" style="flex:1 1 auto;"><div class="ch red">Check for Understanding &middot; DOK {esc(cfu['dok'])}</div>
        <div class="cb"><div style="font-weight:700;margin-bottom:6px">{esc(cfu['stem'])}</div>
          {opts}
          {ans_html}</div></div>
    </div>
  </div>
  {tstrip(tnotes)}
  {UDLMTSS}
""", pageno=str(pg))
    pg += 1

# ---- Perspectives ----
pcards = ""
for name, desc in U["perspectives"]:
    pcards += f'<div class="p"><h3>{esc(name)}</h3><p>{esc(desc)}</p></div>'
slide(f"""
  <div class="shead"><div class="l"><div class="kick">Unit 1 &middot; Multiple Perspectives</div><h2>{esc(U['perspectives_title'])}</h2></div>
    <div class="r"><span class="chip ssp">SSP.03</span></div></div>
  <div class="persp">{pcards}</div>
  {tstrip(PERSP_NOTE)}
""", pageno=str(pg)); pg += 1

# ---- Tennessee Connection ----
slide(f"""
  <div class="shead"><div class="l"><div class="kick">Unit 1 &middot; {esc(U['tn_connection_label'])}</div><h2>Our Signature Move</h2></div>
    <div class="r"><span class="chip">&#9733; Tennessee</span></div></div>
  <div class="tnbig"><div class="star">&#9733;</div><div class="t">{esc(U['tn_connection'])}</div></div>
  {tstrip(TN_NOTE)}
""", pageno=str(pg)); pg += 1

# ---- Make It Stick (UDL 3.0 elements embedded: 9.1 belief-check, 7.3 play, 3.4 spiral, 9.4 norms) ----
if U.get("belief_check") or U.get("spiral"):
    play = U.get("play", {})
    spiral = U.get("spiral", [])
    norms = U.get("discussion_norms", {})
    spiral_html = "".join(
        f'<div style="margin-bottom:5px"><b style="color:var(--navy)">{esc(x["from"])} &rarr; {esc(x["to"])}</b><br>{esc(x["link"])}</div>'
        for x in spiral)
    norms_html = "".join(f"<li>{esc(n)}</li>" for n in norms.get("norms", []))
    slide(f"""
  <div class="shead"><div class="l"><div class="kick">{esc(U['code'])} &middot; Make It Stick</div><h2>Predict &middot; Play &middot; Spiral</h2></div>
    <div class="r"><span class="chip">UDL &middot; MTSS</span></div></div>
  <div class="persp">
    <div class="p" style="border-top-color:var(--gold)"><h3>Predict First &mdash; open the unit</h3><p>{esc(U.get('belief_check',''))}</p></div>
    <div class="p"><h3>Warm-Up Play &mdash; {esc(play.get('name',''))}</h3><p>{esc(play.get('how',''))}</p></div>
    <div class="p" style="border-top-color:var(--navy)"><h3>Spiral &mdash; retrieve &amp; connect</h3><p style="font-size:10.5pt">{spiral_html}</p></div>
    <div class="p" style="border-top-color:var(--gold)"><h3>{esc(norms.get('name','Discussion Norms'))}</h3><p><ul style="margin-left:15px">{norms_html}</ul></p></div>
  </div>
  {tstrip(MIS_NOTE)}
""", pageno=str(pg)); pg += 1

# ---- Closing ----
stds = " &middot; ".join(ORDER)
slide(f"""
  <div class="close-inner" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;height:100%;padding:0 90px">
  <h1>Revisit the Essential Question</h1>
  <div class="rule"></div>
  <p>&ldquo;{esc(U['essential_question'])}&rdquo;</p>
  <p style="margin-top:14px;font-size:13pt">Students now have the sources, vocabulary, and reasoning to answer it &mdash; in a CER paragraph or the unit DBQ.</p>
  <div class="stds">{stds}</div></div>
""", cls="close", pageno=str(pg))

doc = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Unit 1 {DECK_KIND} &mdash; Foundations of Constitutional Government</title>
<style>{CSS}</style></head><body>
{''.join(slides)}
</body></html>"""

# leakage guard
import re as _re
_scan = _re.sub(r"data:[^\"')]+", "", doc)  # exclude embedded base64 payloads from the leak scan
assert "W"+"CS" not in _scan and "History Hack" not in _scan, "leak detected"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write(doc)
print(f"wrote {OUT}: {len(slides)} slides, {len(doc)//1024} KB")
