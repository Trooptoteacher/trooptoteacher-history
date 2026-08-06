#!/usr/bin/env python3
"""
Flight Log builder — the write-in student companion to the narrative textbook
("To Form a More Perfect Union"). Generates, per unit: a brand cover, a SMART-
goals page, and one cross-referenced log entry per stop, then an Arc-of-the-
Union capture. The log entries and the textbook's per-stop writing cues are
generated from the SAME stop data, so the cross-reference is accurate by
construction (Textbook Stop N ⇄ Flight Log Entry N).

Course-parameterized. Usage: python3 build_flightlog.py <unitNumber>
Layout governed by style.css (+ flight-log styles).
"""
import json as _json, html as _html, sys
from pathlib import Path
from weasyprint import HTML

BASE = Path(__file__).parent
ROOT = BASE.parents[1]
def esc(s): return _html.escape(str(s or ""), quote=False)

# Per-unit stop index: (stop#, [standard codes], short title). Titles mirror the
# narrative build exactly so the cross-reference is identical.
STOPS = {
 1:{"title":"The Nation Turns West — and the Cities Rise","years":"1877–1900",
    "stops":[(1,["US.01"],"Free Land — and Whose Land?"),(2,["US.02"],"Made to Vanish"),
             (3,["US.03"],"The Refs Walk Off"),(4,["US.04"],"The Group Chat You’re Not In"),
             (5,["US.05"],"Gospel — and Its Price"),(6,["US.06"],"The City That Can’t House Its Workers"),
             (7,["US.07"],"‘Expat’ or ‘Immigrant’?")]},
 2:{"title":"Turning the Light On","years":"1890–1920",
    "stops":[(1,["US.08","US.09"],"Two Roads Out"),(2,["US.10","US.11"],"The Freight Bill That Ate the Farm"),
             (3,["US.12","US.16","US.17"],"Breaking the Trusts"),(4,["US.13"],"146 Never Came Home"),
             (5,["US.14"],"The Notebook Beats the Tentacle"),(6,["US.15"],"Power to the Voters"),
             (7,["US.18"],"One Vote, in Tennessee")]},
}
# The crew member whose narrative debrief the student writes from (the Debriefer).
DEBRIEFER = "MSgt “Muck”"

def build(unit):
    U = STOPS[unit]
    codes = sorted({c for _,cs,_ in U["stops"] for c in cs})
    span = f'{codes[0]}–{codes[-1]}'

    # ---- BRAND COVER (hero art + Flight Log band) ----
    cover = f'''<section class="fl-cover">
  <img src="assets/cover.png" alt="To Form a More Perfect Union">
  <div class="fl-band">
    <div class="fl-kick">✈ Student Flight Log</div>
    <div class="fl-title">Unit {unit} · {esc(U["title"])}</div>
    <div class="fl-sub">To Form a More Perfect Union · {esc(U["years"])} · {span}</div>
    <div class="fl-name">NAME <span class="fl-line"></span> &nbsp; PERIOD <span class="fl-line short"></span></div>
  </div>
</section>'''

    # ---- SMART GOALS + HOW THE LOG WORKS ----
    goals = f'''<section class="page">
<div class="sec"><div class="eyebrow">Before the flight</div><h2>My SMART Goals</h2><div class="u"></div></div>
<p class="lead">This log is your co-pilot’s seat in the textbook. Every stop, the crew hands you a source and asks for your call — you capture it <b>here</b>, then type it into <b>History Hack online · Writing Lab</b> for instant feedback.</p>
<div class="tint" style="margin:6px 0 12px"><b>How the cross-check works.</b> Each entry below is tied to one <b>Stop</b> in the textbook. When {DEBRIEFER} says <i>“capture this in your Flight Log,”</i> come here to the matching entry number — and the entry tells you exactly where in the narrative to write from.</div>
<div class="wlabel">Short-term goal (this unit)</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:8px">Mid-term goal (this quarter)</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:8px">Long-term goal (Ready Graduate — ACT ≥ 21 or an EPSO/credential)</div><div class="write"><div class="ln"></div></div>
<div class="fr-tie" style="margin-top:12px"><b>Reflect &amp; commit.</b> How does today’s work ladder toward the long-term goal? Name one habit you’ll hold all unit.</div>
<div class="write"><div class="ln"></div><div class="ln"></div></div></section>'''

    # ---- LOG ENTRIES (cross-referenced) ----
    def entry(n, cs, title):
        codestr = ", ".join(cs)
        return f'''<div class="fl-entry">
  <div class="fl-eh"><span class="fl-num">{n}</span><span class="fl-et">{esc(title)}</span><span class="fl-ec">{codestr}</span></div>
  <div class="fl-xref">↳ <b>In the textbook:</b> write from {DEBRIEFER}’s debrief on the <b>Stop {n}</b> page (Unit {unit}, {codestr}) — the “Make Your Call” prompt.</div>
  <div class="fl-cap"><b>My claim (one sentence):</b><div class="write"><div class="ln"></div></div>
  <b>My evidence (from the source):</b><div class="write"><div class="ln"></div><div class="ln"></div></div>
  <div class="fl-grade">Self-grade before you fly: <b>4</b> claim + evidence, names the tension &nbsp; <b>3</b> both, tension implied &nbsp; <b>2</b> one side &nbsp; <b>1</b> opinion only &nbsp; → <span class="fl-box"></span></div></div>
</div>'''
    # group entries onto pages (3 per page)
    ent = U["stops"]
    pages = []
    for i in range(0, len(ent), 3):
        chunk = ent[i:i+3]
        body = "".join(entry(n, cs, t) for n, cs, t in chunk)
        head = f'<div class="sec"><div class="eyebrow">Flight Log · every stop</div><h2>Log your calls — Stops {chunk[0][0]}–{chunk[-1][0]}</h2><div class="u"></div></div>' if i==0 else f'<div class="sec" style="margin-bottom:8px"><div class="eyebrow">Flight Log · continued</div><h2 style="font-size:15pt">Stops {chunk[0][0]}–{chunk[-1][0]}</h2></div>'
        pages.append(f'<section class="page">{head}{body}<div class="app"><span class="badge">Web · Writing Lab</span> &nbsp;Type each call into <b>History Hack online → Writing Lab</b> and check it against the rubric for <b>instant feedback</b>.</div></section>')
    entries_html = "".join(pages)

    # ---- ARC CAPTURE (points back to the textbook Arc section) ----
    arc = f'''<section class="page">
<div class="sec"><div class="eyebrow">End of the flight</div><h2>The Arc of the Union — my call</h2><div class="u"></div></div>
<p class="lead">Turn to <b>The Arc of the Union</b> at the end of Unit {unit} in the textbook. Plot each milestone there, then bring your overall verdict home to this page.</p>
<div class="wlabel">My mean score (−3 … +3):</div><div class="write"><div class="ln"></div></div>
<div class="wlabel" style="margin-top:8px">Overall trend (circle): &nbsp; Climbing &nbsp; Falling &nbsp; Mixed</div>
<div class="wlabel" style="margin-top:10px">Make the call — did the country move <b>toward</b> a more perfect union in these years, or away? Defend it with your graph.</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="fr-tie" style="margin-top:12px"><b>Debrief for {DEBRIEFER}.</b> In one sentence: what did this unit cost, and what did it buy?</div>
<div class="write"><div class="ln"></div><div class="ln"></div></div></section>'''

    html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>
{cover}{goals}{entries_html}{arc}</body></html>'''
    out = BASE/"out"/f"ToFormAMorePerfectUnion_Unit{unit}_FlightLog.pdf"
    HTML(string=html, base_url=str(BASE)).write_pdf(str(out))
    print("WROTE", out)

if __name__=="__main__":
    build(int(sys.argv[1]) if len(sys.argv)>1 else 1)
