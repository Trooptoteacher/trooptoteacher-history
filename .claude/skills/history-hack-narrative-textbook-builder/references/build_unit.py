#!/usr/bin/env python3
"""
Generalized narrative-textbook UNIT builder (To Form a More Perfect Union).
Builds one unit section: divider + who-you'll-travel-with + per-standard stops
(photo OR verbatim-excerpt primary source) + writing pages + Arc-of-the-Union
coordinate plot. Content pulled from the canonical banks; page-fill QC gate.

Usage: python3 build_unit.py <unitNumber>
Layout governed entirely by style.css. Reference edition: U.S. History.
"""
import json as _json, html as _html, sys
from pathlib import Path
from weasyprint import HTML

BASE = Path(__file__).parent
ROOT = BASE.parents[1]
A = "assets"
def esc(s): return _html.escape(str(s or ""), quote=False)
def load(p): return _json.load(open(ROOT/p))

# ─────────────────────────────────────────────────────────────────────────────
# UNIT CONFIGS (per-stop presentation metadata; content merged from the banks).
# kind: 'photo' → asset image + image-bank/File citation;  'excerpt' → verbatim
# text primary source (sourceId in the text-source bank).  HVT/TN/title/who-when-
# why are builder synthesis or verified facts (TN flagged when not verified).
# ─────────────────────────────────────────────────────────────────────────────
UNITS = {
 2:{
  "title":"Turning the Light On","era":"The Progressive Era","years":"1890–1920",
  "eq":"When money and machines hold the real power, can ordinary people take democracy back — and for whom?",
  "extrapolate":"1929","next":3,
  "stops":[
   {"codes":["US.08","US.09"],"title":"Two Roads Out","kind":"excerpt","src":"ps-us09-1",
    "who":"Booker T. Washington — founder of Tuskegee Institute.","when":"1895 — the ‘Atlanta Compromise’ address.","why":"To urge Black economic self-help and accommodation with the white South.",
    "closer":"Washington counsels patience; Du Bois demands rights now. Whose road, and at what cost?",
    "hvt":"Two roadmaps for Black progress: Washington’s vocational self-help and accommodation (Atlanta Compromise) vs. Du Bois’s demand for immediate civil rights and the ‘Talented Tenth.’",
    "vocab":["Booker T. Washington","W.E.B. Du Bois","Social Darwinism","Social Gospel"],
    "tn":"<b>★ Tennessee Connection.</b> W.E.B. Du Bois earned his first degree at <b>Fisk University in Nashville</b> — where he first saw the Jim Crow South up close, and where Ada studies in this unit."},
   {"codes":["US.10","US.11"],"title":"The Freight Bill That Ate the Farm","kind":"photo","img":"u2/homestead.jpg",
    "cap":"The aftermath of the Homestead Steel Strike, 1892 — Carnegie’s mill, where the company brought in armed Pinkerton guards and the strike ended in blood.","cite":"Underwood &amp; Underwood, <i>The Homestead strike, 1892</i>. Stereograph. Library of Congress.",
    "who":"Underwood &amp; Underwood — a commercial stereograph publisher.","when":"1892 — the Homestead Strike at Carnegie Steel.","why":"To sell a mass audience a ‘you-are-there’ view of a national labor war.",
    "closer":"Farmers organized against the railroad; workers against the mill. What did each risk — and win?",
    "hvt":"Farmers (Grange, Farmers’ Alliance, Populists) and workers (labor unions) organized against railroads and trusts — and met force at Homestead (1892).",
    "vocab":["Populism","Granger Movement","Free Silver","Labor Union","Collective Bargaining"],
    "tn":"<b>★ Tennessee Connection.</b> Tennessee’s <b>Coal Creek War</b> (1891–92) — armed miners freeing convict laborers leased into the mines — was one of the era’s fiercest labor uprisings, and pushed the state to end convict leasing."},
   {"codes":["US.12","US.16","US.17"],"title":"Breaking the Trusts","kind":"excerpt","src":"ps-us16-1",
    "who":"President Theodore Roosevelt.","when":"1903 — the ‘Square Deal.’","why":"To promise fairness between capital and labor — a government that referees, not rigs, the game.",
    "closer":"TR’s Square Deal and Wilson’s New Freedom both fight the trusts. Same enemy — same cure?",
    "hvt":"Progressive presidents took on the trusts: TR’s Square Deal (trust-busting, regulation, conservation) and Wilson’s New Freedom (Clayton Act, FTC, Federal Reserve).",
    "vocab":["Trust","Monopoly","Sherman Antitrust Act","Square Deal","New Freedom","Federal Reserve System"],
    "tn":"<b>★ Tennessee Connection — investigate.</b> How did trusts and the railroads shape a Tennessee industry (start with coal or timber)? <i>[pending historian-verified fill]</i>"},
   {"codes":["US.13"],"title":"146 Never Came Home","kind":"photo","img":"u2/triangle.jpg",
    "cap":"Washington Place, New York, March 25, 1911 — the street outside the Triangle Shirtwaist Factory, where 146 garment workers, most of them young immigrant women, died behind locked doors.","cite":"Bain News Service. “Scene of Washington Place fire.” Photograph, March 1911. Library of Congress, Prints and Photographs Division.",
    "who":"Bain News Service — a news-photo agency.","when":"March 25, 1911 — the Triangle Shirtwaist fire.","why":"To put the disaster in front of a public that had looked away from the sweatshops for years.",
    "closer":"The doors were locked to stop breaks and theft. What does that one fact reveal about the era’s priorities?",
    "hvt":"Deadly conditions — child labor, sweatshops, and the Triangle fire (1911, 146 dead) — drove landmark workplace-safety and labor laws.",
    "vocab":["Sweatshop","Child Labor","Strike","Labor Union"],
    "tn":"<b>★ Tennessee Connection — investigate.</b> Where did Tennessee children work in this era (mills, mines, fields), and what did reformers do about it? <i>[pending historian-verified fill]</i>"},
   {"codes":["US.14"],"title":"The Notebook Beats the Tentacle","kind":"excerpt","src":"ps-us14-1",
    "who":"Upton Sinclair — novelist and muckraker.","when":"1906 — <i>The Jungle</i>.","why":"To expose the meatpacking industry and rally the public for reform.",
    "closer":"Sinclair aimed for workers’ hearts and hit the country’s stomach. Did the reform match his goal?",
    "hvt":"Muckrakers (Tarbell on Standard Oil, Sinclair’s <i>The Jungle</i>, Riis) exposed abuse and forced reform — the Pure Food & Drug and Meat Inspection Acts (1906).",
    "vocab":["Muckraker","Progressive Movement","Trust-Busting"],
    "tn":"<b>★ Tennessee Connection.</b> Muckraking had deep Tennessee roots: <b>Ida B. Wells</b> built her anti-lynching investigations from a Memphis newspaper before a mob destroyed her press."},
   {"codes":["US.15"],"title":"Power to the Voters","kind":"excerpt","src":"ps-us15-1",
    "who":"The United States Constitution.","when":"1913 — the 16th Amendment.","why":"To let Congress tax incomes directly — funding a more active, reforming government.",
    "closer":"Initiative, referendum, recall, direct primary: each one moves a decision. From whom, to whom?",
    "hvt":"Progressives expanded democracy — initiative, referendum, recall, the direct primary, and the 16th (income tax) and 17th (direct election of senators) Amendments.",
    "vocab":["Initiative","Referendum","Recall","Direct Primary","16th Amendment","17th Amendment"],
    "tn":"<b>★ Tennessee Connection — investigate.</b> How did direct-democracy reforms play out in Tennessee’s cities and state government? <i>[pending historian-verified fill]</i>"},
   {"codes":["US.18"],"title":"One Vote, in Tennessee","kind":"excerpt","src":"ps-us18-2",
    "who":"Carrie Chapman Catt — president of the National American Woman Suffrage Association.","when":"1917 — “The Crisis.”","why":"To warn politicians that stalling the suffrage amendment would carry a political price.",
    "closer":"Seventy years of work came down to one state — then one vote. What does that say about how change happens?",
    "hvt":"The women’s suffrage movement won the 19th Amendment (1920) — ratified by the deciding 36th state: Tennessee.",
    "vocab":["Women's Suffrage","19th Amendment","Alice Paul","Carrie Chapman Catt","Anne Dallas Dudley"],
    "tn":"<b>★ Tennessee Connection.</b> Tennessee cast the <b>deciding 36th vote</b> for the 19th Amendment in August 1920 — 24-year-old Rep. <b>Harry Burn</b> changed his vote after a letter from his mother. Nashville’s <b>Anne Dallas Dudley</b> helped lead the campaign."},
  ],
 },
}

# ─────────────────────────────────────────────────────────────────────────────
def build(unit):
    U = UNITS[unit]
    NARR = load(f"content-build/us-history/narrative/unit-0{unit}.json")
    VOCAB = {t["term"]: t["definition"] for t in load(f"public/data/us-history/vocabulary/unit-{unit}.json")}
    TEXTSRC = {(it.get("sourceId") or it.get("id")): it for it in load(f"public/data/us-history/primary-sources/unit-{unit}.json")}
    spreads = {sp["spreadNumber"]: sp for sp in NARR["spreads"]}
    standards = {s["code"]: (s.get("description") or s.get("text") or "") for s in NARR.get("standards",[])}
    codes_sorted = [s["code"] for s in NARR.get("standards",[])]
    arc = [(a.get("year"), a.get("label") or a.get("milestone")) for a in NARR.get("arcPoints",[])]

    def sec(eyebrow,title):
        return f'<div class="sec"><div class="eyebrow">{esc(eyebrow)}</div><h2>{esc(title)}</h2><div class="u"></div></div>'
    def wordwall(terms):
        return "".join(f'<div class="v"><span class="t">{esc(t)}</span> — {esc(VOCAB[t])}</div>' for t in terms if t in VOCAB)
    def excerpt_of(sid):
        it = TEXTSRC.get(sid, {})
        exc = (it.get("excerpt") or it.get("text") or "").strip()
        # keep to ~3 sentences so the block fits the column
        parts = exc.replace("…","… ").split(". ")
        short = ". ".join(parts[:3]).strip()
        if short and not short.endswith((".","!","?","”","…")): short += "…"
        cite = it.get("citation") or {}
        mla = cite.get("mlaCitation") if isinstance(cite,dict) else cite
        return short, (mla or "")

    # DIVIDER
    stds = "".join(f'<div class="std"><span class="chip">{c}</span><span class="txt">{esc(standards.get(c,""))[:90]}</span></div>' for c in codes_sorted)
    before = f'''<div class="value"><div class="vh"><span class="tag">Before You Fly</span><h4>Set your heading — predict, commit, self-check</h4></div>
<p><b>Anticipation guide.</b> Agree or disagree on instinct — revisit at <i>The Arc of the Union</i>.</p>
<div class="ag-row"><span class="st">1. Big business and big cities made life better for everyone who worked hard.</span><span class="boxes"><span class="cb"></span>Agree &nbsp;<span class="cb"></span>Disagree</span></div>
<div class="ag-row"><span class="st">2. Reform works best when ordinary people force it from below.</span><span class="boxes"><span class="cb"></span>Agree &nbsp;<span class="cb"></span>Disagree</span></div>
<div class="ag-row"><span class="st">3. Winning the vote settled the question of women’s equality.</span><span class="boxes"><span class="cb"></span>Agree &nbsp;<span class="cb"></span>Disagree</span></div>
<p style="margin-top:9px"><b>Set your goal (SMART).</b> One thing you’ll master this unit:</p><div class="write"><div class="ln"></div></div>
<div class="fr-tie"><b>Future-Ready · ACT-Ready.</b> Predict, then revise from evidence — the ACT-reading move. Rate your starting knowledge of {codes_sorted[0]}–{codes_sorted[-1]}: <span class="rate">1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;5</span></div></div>'''
    page_div = f'''<section class="page">
<div style="border-top:3px solid var(--rule);border-bottom:3px solid var(--rule);padding:14px 0;margin-bottom:6px">
  <div style="font:700 10pt 'DejaVu Sans';letter-spacing:.2em;color:var(--red)">UNIT {unit}</div>
  <h1 style="font-size:30pt;margin:4px 0 2px">{esc(U["title"])}</h1>
  <div class="toc-meta" style="font-size:11pt">{esc(U["era"])} · {esc(U["years"])}</div></div>
<div class="std-list">{stds}</div>
<div class="callout"><b>Essential Question.</b> {esc(U["eq"])}</div>
{before}</section>'''

    # FRIENDS (from perspectives)
    seen={}
    for sp in NARR["spreads"]:
        for p in (sp.get("perspectives") or []):
            fid=p.get("friendId") or ""; head=p.get("heading") or ""
            if head and fid and fid not in seen: seen[fid]=head
    fr = "".join(f'<div class="friend"><div><div class="fn">{esc(h.split("·")[0].strip())}</div><div class="fd">{esc(h.split("·",1)[1].strip() if "·" in h else "")}</div></div></div>' for h in seen.values())
    predict = f'''<div class="value"><div class="vh"><span class="tag">Make Your Call</span><h4>Predict before you land</h4></div>
<p><b>Predict:</b> in the Progressive Era, who finally gains real power — and who is still left out when the unit ends in {U["years"].split("–")[1]}? Commit now; test it at every stop.</p>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="fr-tie"><b>Why this matters.</b> Naming a claim before all the evidence is in — then revising honestly — is the core habit of a historian and a Ready Graduate.</div></div>'''
    page_friends = f'''<section class="page">{sec("Unit "+str(unit),"Who you’ll travel with")}
<p class="lead">These era-friends carry the unit — <b>composite characters</b> built from the documented record and marked as fiction. Real historical figures appear only in their own recorded words.</p>
{fr}<div class="tint" style="margin-top:8px"><b>🔦 Witness Lens — the ballot &amp; the paycheck.</b> Two things measure this era: who can <i>vote</i>, and who is paid a living <i>wage</i>. Track both at every stop — the Progressive promise is tested against them.</div>{predict}</section>'''

    # STOPS
    def stop_page(i, st):
        sp = next((spreads[n] for n in spreads if set(st["codes"]) & set(spreads[n].get("standardCodes") or [])), {})
        code = ", ".join(st["codes"])
        lo = esc(sp.get("learningObjective"))
        hook = esc(sp.get("engagementHook"))
        # deterministic fill: scale the left column (photo height / excerpt min-height)
        # inversely to the other content weight (hook + vocab) so each stop self-levels.
        terms = st["vocab"][:3] if len(",".join(VOCAB.get(t,"") for t in st["vocab"]))>620 else st["vocab"]
        weight = len(sp.get("engagementHook") or "") + sum(len(VOCAB.get(t,"")) for t in terms)
        h = 3.9 if weight<700 else 3.6 if weight<900 else 3.35 if weight<1050 else 3.1
        jot = ('<div class="wlabel" style="margin-top:8px">First glance — jot one thing you notice before you read on:</div>'
               '<div class="write"><div class="ln"></div></div>') if weight<900 else ''
        if st["kind"]=="photo":
            left = f'<figure class="stopfig"><img src="{A}/{st["img"]}" alt="{esc(st.get("cap",""))[:110]}" style="height:{h}in"><figcaption>{st.get("cap","")} <i>{st.get("cite","")}</i></figcaption></figure>'
        else:
            exc, mla = excerpt_of(st["src"])
            left = f'<div class="excerpt" style="min-height:{h}in"><div class="eq">“{esc(exc)}”</div><div class="ec">— {st["who"].replace("<i>","").replace("</i>","")}<br><span class="cite">{esc(mla)}</span></div></div>'
        return f'''<section class="page">
<div class="stop-hd"><span class="n">{i}</span><span class="t">{esc(st["title"])}</span></div>
<p class="small"><b>Standard {code} · Learning target:</b> {lo}</p>
<div class="callout"><b>Spark asks:</b> {hook} <b>What do you notice?</b></div>
{jot}
<div class="stop-media">
  {left}
  <div class="src-col">
    <div class="source-band"><h4>Source It First</h4>
      <dl><dt>WHO</dt><dd>{st["who"]}</dd><dt>WHEN</dt><dd>{st["when"]}</dd><dt>WHY</dt><dd>{st["why"]}</dd></dl>
      <div class="small"><b>Read it closer:</b> {st["closer"]}</div></div>
    <div class="hvt"><div class="hvt-hd"><span class="hvt-badge">◎ HVT</span> High-Value Target — lock this in</div><p>{st["hvt"]}</p></div>
  </div>
</div>
<div class="sec" style="border-left-color:var(--gold);margin:8px 0 6px"><div class="eyebrow">Word Wall · EN/ES</div></div>
<div class="vocab">{wordwall(terms)}</div>
<div class="tint cool" style="margin-top:10px">{st["tn"]}</div>
<div class="fl-cue">▶ Now make your call — log it as <b>Flight Log · Entry {i}</b> (then check it in the Writing Lab).</div>
</section>'''
    def writing_page(i, st):
        sp = next((spreads[n] for n in spreads if set(st["codes"]) & set(spreads[n].get("standardCodes") or [])), {})
        cc = sp.get("comprehensionCheck"); cc = cc if isinstance(cc,dict) else {}
        prompt = esc(cc.get("question")) or "Make the call on this stop, and defend it with evidence from the source."
        nxt = f"fly to Stop {i+1}." if i < len(U["stops"]) else "head to the Arc of the Union."
        L=lambda k:"".join('<div class="ln"></div>' for _ in range(k))
        return f'''<section class="page">{sec("MSgt “Muck” · Debrief", st["title"]+" — Make Your Call")}
<p class="lead">{prompt} <b>Claim first, then prove it — evidence from the source.</b></p>
<div class="wlabel">Your claim — one sentence:</div><div class="write">{L(8)}</div>
<div class="two-ev"><div><div class="wlabel">Evidence — first point:</div><div class="write">{L(4)}</div></div>
<div><div class="wlabel">Evidence — second point:</div><div class="write">{L(4)}</div></div></div>
<div class="sec" style="border-left-color:var(--gold);margin:12px 0 5px"><div class="eyebrow">Self-grade before you fly</div></div>
<table class="rubric"><thead><tr><th>4 — Cleared</th><th>3 — Airworthy</th><th>2 — Pre-flight</th><th>1 — Grounded</th></tr></thead>
<tbody><tr><td>Clear claim + evidence from <b>both</b> points; names the tension.</td><td>Claim + evidence from both; tension implied.</td><td>Claim with evidence from one point only.</td><td>An opinion, no evidence yet.</td></tr></tbody></table>
<div class="wlabel" style="margin-top:10px">Muck’s debrief — in ONE sentence: what did this stop cost, and what did it buy?</div><div class="write">{L(3)}</div>
<div class="app"><span class="badge">Web · Writing Lab</span> &nbsp;Now go to <b>History Hack online → Writing Lab</b>, type your response, and check it for <b>instant feedback</b>. Revise here, then {nxt}</div></section>'''
    stops_html = "".join(stop_page(i+1, st) + writing_page(i+1, st) for i, st in enumerate(U["stops"]))

    # ARC
    def X(i,nt): return 74 + (i-0.5)/nt*(662-74-12)
    GH=475 if len(arc)<9 else 332
    def Y(v): return 20 + (3-v)/6*(GH-20-44)
    def grid():
        nt=len(arc); s=[f'<svg viewBox="0 0 662 {GH}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans">']
        yl={3:"+3 Toward",2:"+2",1:"+1",0:"0  no change",-1:"−1",-2:"−2",-3:"−3 Away"}
        for v in range(-3,4):
            y=Y(v); b=v==0
            s.append(f'<line x1="74" y1="{y:.1f}" x2="650" y2="{y:.1f}" stroke="{"#1b3a6b" if b else "#d3d8e0"}" stroke-width="{1.4 if b else .8}"/>')
            s.append(f'<text x="68" y="{y+3:.1f}" text-anchor="end" font-size="9" fill="#41506a">{yl[v]}</text>')
        for i,(yr,_) in enumerate(arc,1):
            x=X(i,nt); s.append(f'<line x1="{x:.1f}" y1="20" x2="{x:.1f}" y2="{GH-44:.0f}" stroke="#eef1f6" stroke-width=".8"/>')
            s.append(f'<text x="{x:.1f}" y="{GH-30:.0f}" text-anchor="middle" font-size="9" font-weight="bold" fill="#1b3a6b">{i}</text>')
            s.append(f'<text x="{x:.1f}" y="{GH-17:.0f}" text-anchor="middle" font-size="7.5" fill="#7a828e">{yr}</text>')
        s.append('<line x1="74" y1="20" x2="74" y2="{GH-44:.0f}" stroke="#1b2a41" stroke-width="1"/></svg>'); return "".join(s)
    rows="".join(f'<tr><td class="c">{i}</td><td class="c">{yr}</td><td>{esc(lab)}</td><td class="call">−3 &nbsp;−2 &nbsp;−1 &nbsp;0 &nbsp;+1 &nbsp;+2 &nbsp;+3</td></tr>' for i,(yr,lab) in enumerate(arc,1))
    page_arc1 = f'''<section class="page">{sec("The Arc of the Union · its own section","Chart the Nation’s Climb")}
<p class="lead">You made a call at every stop. Now turn it into data. <b>1)</b> Score each milestone (−3 far from the promise … +3 toward it). <b>2)</b> Plot each on the grid. <b>3)</b> Connect the dots — that line is the Arc of the Union.</p>
<table class="arc"><thead><tr><th class="c">#</th><th class="c">Year</th><th>Milestone</th><th>My call — circle one</th></tr></thead><tbody>{rows}</tbody></table>
<div class="grid-wrap">{grid()}</div>
<p class="small" style="text-align:center;margin-top:2px">Milestone (1–{len(arc)}) →&nbsp;&nbsp;plot your call, then connect the points in order.</p></section>'''
    page_arc2 = f'''<section class="page">{sec("The Arc of the Union","Read the Arc — the cross-curricular part")}
<p class="lead">A graph turns {len(arc)} separate judgments into one picture you can defend. Read your own data like a mathematician and a scientist.</p>
<div class="xc"><div class="value tight"><div class="vh"><span class="tag">Math</span><h4>Trend &amp; average</h4></div>
<p>Each call is an ordered pair — <b>(milestone, score)</b> — and your connected points are a <b>line graph</b>. Does it mostly <b>climb</b> (positive slope) or <b>fall</b>?</p>
<p>Add your scores and divide by {len(arc)} — the <b>mean</b>. Positive = the nation moved toward the promise; negative = away.</p>
<p><b>My mean:</b> <span class="blank">&nbsp;</span> · Overall trend: <b>Climbing &nbsp; Falling &nbsp; Mixed</b></p></div>
<div class="value tight"><div class="vh"><span class="tag">Science</span><h4>Pattern in the data</h4></div>
<p>Scientists plot data to reveal patterns a table hides. Your graph exposes the <b>shape</b> of this era.</p>
<p>Where is the <b>steepest climb</b>? The <b>steepest drop</b>? Name a milestone where the line turns, and why.</p>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div></div>
<div class="callout" style="margin-top:12px"><b>Make the call — with your graph as evidence.</b> In these years, did America move <i>toward</i> a more perfect union, or away? Defend it with the shape of your arc — trend, mean, and the turning point that matters most.</div>
<div class="write"><div class="ln"></div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>
<div class="xc" style="margin-top:10px"><div class="value tight"><div class="vh"><span class="tag">Correlate</span><h4>Compare arcs</h4></div>
<p>Trade graphs with a partner. Where do your lines <b>agree</b>? Where do they <b>diverge</b> — and why can the same evidence plot differently?</p></div>
<div class="value tight"><div class="vh"><span class="tag">Extrapolate → Unit {U["next"]}</span><h4>Predict the next arc</h4></div>
<p>Your data stops in {arc[-1][0]}. <b>Extend the line:</b> where would <b>{U["extrapolate"]}</b> land? Draw a <b>dotted prediction</b> — you’ll test it next unit.</p></div></div>
<div class="fr-tie"><b>Cross-curricular · Future-Ready.</b> Plotting evidence, finding a trend, extrapolating, and defending a claim with data is one skill across history, math, science, and every career path.</div></section>'''

    html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>
{page_div}{page_friends}{stops_html}{page_arc1}{page_arc2}</body></html>'''
    out = BASE/"out"/f"ToFormAMorePerfectUnion_Unit{unit}.pdf"
    HTML(string=html, base_url=str(BASE)).write_pdf(str(out))
    print("WROTE", out)
    # QC gate
    import fitz
    d=fitz.open(str(out)); DPI=100; FOOT=int(0.55*DPI); fails=[]
    print(f"PAGE-FILL QC (target 90%):")
    for i in range(d.page_count):
        pm=d[i].get_pixmap(colorspace=fitz.csGRAY,dpi=DPI); W,H=pm.width,pm.height; px=pm.samples; lim=H-FOOT; end=0
        for y in range(lim):
            if min(px[y*W:(y+1)*W])<205: end=y
        f=100*end/lim
        if f<90: fails.append((i+1,f))
        print(f"  p{i+1:>2} {f:5.1f}% {'OK' if f>=90 else '*** BELOW ***'}")
    print("QC PASS" if not fails else "QC FAIL: "+", ".join(f"p{n}({f:.0f}%)" for n,f in fails))

if __name__=="__main__":
    build(int(sys.argv[1]) if len(sys.argv)>1 else 2)
