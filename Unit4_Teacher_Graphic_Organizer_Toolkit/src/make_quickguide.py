# -*- coding: utf-8 -*-
"""Front page: 'Which Organizer, When' Quick Guide (task -> organizer -> why).
Bespoke branded page (not an organizer, so no UDL strip). Writes pages/00_quickguide.html.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from toolkit_lib import SHARED_CSS, FOOTER_BRAND  # noqa

# (task, organizer label, color, why) — colors: navy/red/gold family
ROWS = [
    ("Compare <b>two</b> things", "Venn diagram &middot; T&#8209;chart", "navy",
     "The overlap makes shared traits visible and sharpens the differences. <i>Marzano&rsquo;s #1 strategy.</i>", "10&ndash;15"),
    ("Compare <b>three or more</b> on set criteria", "Comparison matrix", "navy",
     "Holds many cases against the same yardstick so patterns pop.", "15&ndash;20"),
    ("Trace <b>causes &amp; effects</b>", "Cause &amp; Effect", "red",
     "Makes the chain of &ldquo;why it happened&rdquo; visible. <i>Builds SSP.05.</i>", "15&ndash;20"),
    ("Put events <b>in order</b> / show change over time", "Timeline", "red",
     "Sequence exposes cause across time. <i>Builds SSP.05 chronology.</i>", "15&ndash;20"),
    ("<b>Brainstorm</b> &amp; connect ideas", "Concept web", "gold",
     "Surfaces prior knowledge and shows how ideas link to one hub.", "10&ndash;15"),
    ("<b>Summarize</b> &mdash; find the main point", "Main Idea &amp; Details", "navy",
     "Separates the big idea from the details that support it.", "10&ndash;15"),
    ("<b>Activate</b> prior knowledge &amp; <b>track</b> learning", "K&#8209;W&#8209;L chart", "gold",
     "Sets a purpose and makes thinking metacognitive. <i>UDL self-regulation.</i>", "10&ndash;15"),
    ("<b>Learn a key term</b>", "Frayer model", "navy",
     "Builds deep word knowledge &mdash; not a definition students forget by Friday.", "10&ndash;15"),
    ("<b>Analyze a source</b>", "HIPPO <span class='alt'>(or OPTIC)</span>", "red",
     "Gives students a historian&rsquo;s routine for interrogating a document.", "15&ndash;20"),
    ("Make an <b>evidence-based claim</b>", "C&#8209;E&#8209;R", "navy",
     "Turns an opinion into a defensible argument: claim, evidence, reasoning.", "20&ndash;25"),
    ("<b>Weigh two sides</b> or options", "T&#8209;chart &middot; Problem&ndash;Solution", "red",
     "Forces a decision that rests on evidence from both sides.", "15&ndash;20"),
    ("Get the <b>basics of an event</b>", "5 Ws", "gold",
     "Fast, complete factual capture &mdash; who, what, when, where, why.", "5&ndash;10"),
]
TN_ROW = ("Connect the <b>nation</b> to <b>Tennessee</b>", "&#9733; Tennessee Connection",
          "Local ties make national history stick &mdash; and it&rsquo;s what sets History Hack apart. <b>Our signature move.</b>", "10&ndash;15")

def dot(color):
    c = {"navy": "var(--navy)", "red": "var(--red)", "gold": "var(--gold)"}[color]
    return f'<span class="dot" style="background:{c}"></span>'

rows_html = []
for task, org, color, why, mins in ROWS:
    rows_html.append(f"""      <div class="qr">
        <div class="c-task">{task}</div>
        <div class="c-org">{dot(color)}<span>{org}</span></div>
        <div class="c-time">{mins}<small>min</small></div>
        <div class="c-why">{why}</div>
      </div>""")
tn_html = f"""      <div class="qr tn">
        <div class="c-task">{TN_ROW[0]}</div>
        <div class="c-org"><span class="star">&#9733;</span><span>Tennessee Connection</span></div>
        <div class="c-time">{TN_ROW[3]}<small>min</small></div>
        <div class="c-why">{TN_ROW[2]}</div>
      </div>"""

CSS = r"""
  .cover{ flex:0 0 auto; background:var(--navy); color:#fff; border-radius:9px; padding:15px 20px;
          display:flex; justify-content:space-between; align-items:center; }
  .cover .ttl{ font-family:Georgia,serif; font-size:25pt; font-weight:700; line-height:1.02; }
  .cover .ttl .thin{ display:block; font-family:"Helvetica Neue",Arial,sans-serif; font-size:10.5pt;
                     font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); margin-bottom:4px; }
  .cover .sub{ font-size:10pt; color:#cdd4e2; margin-top:5px; }
  .cover .r{ text-align:right; display:flex; flex-direction:column; align-items:flex-end; gap:7px; }
  .cover .repro2{ border:1.5px solid var(--gold); color:var(--gold); font-size:8pt; font-weight:800;
                  letter-spacing:.08em; text-transform:uppercase; padding:4px 10px; border-radius:4px; }
  .cover .seal{ font-family:Georgia,serif; font-style:italic; font-size:10pt; color:#e6d3a3; max-width:190px; text-align:right; line-height:1.25; }
  .lede{ flex:0 0 auto; margin:11px 2px 8px; font-size:10.5pt; color:#2c3446; line-height:1.35; }
  .lede b{ color:var(--navy); } .lede .big{ font-family:Georgia,serif; font-style:italic; color:var(--red); }
  .lede .pace{ display:block; margin-top:6px; background:var(--gold-tint); border-left:4px solid var(--gold);
               border-radius:0 5px 5px 0; padding:5px 11px; font-size:9.4pt; color:#3a2f12; }
  .lede .pace b{ color:#7a5c15; }
  .qtbl{ flex:1 1 auto; display:flex; flex-direction:column; border:2px solid var(--navy); border-radius:8px; overflow:hidden; min-height:0; }
  .qh{ flex:0 0 auto; display:grid; grid-template-columns:1.1fr 0.95fr 0.42fr 1.45fr; background:var(--navy); color:#fff; }
  .qh div{ padding:7px 12px; font-size:8.4pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase; }
  .qh div+div{ border-left:1px solid #3a4b68; }
  .qh .h-time{ text-align:center; padding:7px 4px; }
  .qr{ flex:1 1 0; display:grid; grid-template-columns:1.1fr 0.95fr 0.42fr 1.45fr; align-items:center; border-top:1px solid var(--rule); min-height:0; }
  .qr:nth-child(even){ background:#fafbfc; }
  .qr>div{ padding:5px 12px; } .qr>div+div{ border-left:1px solid var(--rule); }
  .c-task{ font-size:9.3pt; color:#2c3446; } .c-task b{ color:var(--navy); }
  .c-org{ display:flex; align-items:center; gap:8px; font-size:9.5pt; font-weight:800; color:var(--navy); }
  .c-org .alt{ font-weight:600; font-size:8pt; color:var(--muted); }
  .c-org .dot{ width:12px; height:12px; border-radius:50%; flex:0 0 auto; }
  .c-time{ text-align:center; font-family:Georgia,serif; font-weight:700; font-size:11pt; color:var(--navy); line-height:1; }
  .c-time small{ display:block; font-family:"Helvetica Neue",Arial,sans-serif; font-weight:700; font-size:6.6pt; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); margin-top:2px; }
  .c-why{ font-size:8.6pt; color:#3a4455; line-height:1.22; } .c-why i{ color:var(--muted); }
  .qr.tn{ background:var(--gold-tint); } .qr.tn .c-org{ color:#7a5c15; }
  .qr.tn .star{ color:#b8860b; font-size:13pt; } .qr.tn .c-why b{ color:#7a5c15; }
  .foot{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:center;
         margin-top:8px; padding-top:6px; border-top:1px solid var(--rule); font-size:7.7pt; color:var(--muted); }
  .foot .brand{ font-weight:700; color:var(--navy); }
"""

HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Which Organizer, When &mdash; Quick Guide</title>
<style>{SHARED_CSS}
{CSS}</style></head>
<body>
<div class="page">
  <div class="cover">
    <div class="l">
      <div class="ttl"><span class="thin">Teacher Graphic Organizer Toolkit</span>Which Organizer, When?</div>
      <div class="sub">Unit 4 &middot; The Roaring Twenties &nbsp;(1920&ndash;1929) &middot; US.28&ndash;US.38</div>
    </div>
    <div class="r">
      <div class="repro2">&#10003; Reproducible</div>
      <div class="seal">Match the task to the tool &mdash; then teach the <b>why</b>.</div>
    </div>
  </div>

  <div class="lede">Students don&rsquo;t need more worksheets &mdash; they need the <b>right thinking tool</b> for the task in front of them.
  Find the <span class="big">verb</span> in the assignment, then reach for the organizer built for that kind of thinking.
  <span class="pace"><b>45&#8209;minute class?</b> Plan <b>one</b> deep organizer (~20 min) <em>or</em> <b>two</b> quick ones (~10 min each), plus warm&#8209;up &amp; discussion. Every page prints its own time estimate.</span></div>

  <div class="qtbl">
    <div class="qh"><div>When the task asks students to&hellip;</div><div>Reach for</div><div class="h-time">&asymp; Time</div><div>Because it works</div></div>
{chr(10).join(rows_html)}
{tn_html}
  </div>

  <div class="foot">
    <span class="brand">{FOOTER_BRAND}</span>
    <span>Teacher Graphic Organizer Toolkit &middot; Front Guide</span>
  </div>
</div></body></html>
"""

out = os.path.join(os.path.dirname(HERE), "pages", "00_quickguide.html")
with open(out, "w") as f:
    f.write(HTML)
print("wrote", out)
