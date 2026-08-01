# -*- coding: utf-8 -*-
"""Shared organizer-body builders for the Government Hack Unit 1 toolkit.
Every builder returns (body_html, extra_css). Bodies compose the SHARED_CSS
primitives from toolkit_lib (.row/.col/.fill/.band/.well/.arr-*), with only a
little component CSS each. Visual shapes (Venn, concept web, 5 Ws) are inline
SVG with all text kept INSIDE the viewBox so labels track the geometry.

Design rules honored here (see references/guardrails.md):
  * writable areas are LIGHT (.well); dark .band bars are LABELS only.
  * Venn region labels + hints live INSIDE the <svg>; topic keys go ABOVE.
  * neutral framing; two-sided organizers get equal weight + identical prompts.
"""

# ---------------------------------------------------------------- Venn (2)
_VENN_CSS = r"""
  .vhead{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:flex-end; padding:0 3%; margin-bottom:2px; }
  .vhead .oh{ display:flex; flex-direction:column; max-width:44%; }
  .vhead .oh.b{ align-items:flex-end; text-align:right; }
  .vhead .nm{ font-weight:800; font-size:12.5pt; line-height:1.05; }
  .vhead .yr{ font-size:8pt; font-weight:700; color:var(--muted); }
  .vhead .a .nm{ color:var(--navy); } .vhead .b .nm{ color:var(--red); }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
"""

def venn2(prompt, a_nm, a_yr, b_nm, b_yr, a_only, b_only, both, cap_a="", cap_b="", cap_both="BOTH"):
    """Two-circle Venn. a_only/b_only/both = list[str] faded hint prompts inside each lobe."""
    def _hints(items, x, y0, fill):
        out = []
        y = y0
        for t in items:
            out.append(f'<text x="{x}" y="{y}" fill="{fill}">{t}</text>')
            y += 19
        return "\n            ".join(out)
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="vhead">
      <span class="oh a"><span class="nm">{a_nm}</span><span class="yr">{a_yr}</span></span>
      <span class="oh b"><span class="nm">{b_nm}</span><span class="yr">{b_yr}</span></span>
    </div>
    <div class="canvas">
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet" font-family="Helvetica Neue, Arial, sans-serif">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,71.4 A 245,245 0 0,1 450,498.6 A 245,245 0 0,1 450,71.4 Z" fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <g stroke="#B9C2D0" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="150" y1="345" x2="300" y2="345"/><line x1="140" y1="383" x2="300" y2="383"/><line x1="150" y1="421" x2="300" y2="421"/></g>
          <g stroke="#D8B3B7" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="600" y1="345" x2="750" y2="345"/><line x1="600" y1="383" x2="760" y2="383"/><line x1="600" y1="421" x2="750" y2="421"/></g>
          <g stroke="#E0CB94" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="408" y1="370" x2="492" y2="370"/><line x1="404" y1="408" x2="496" y2="408"/></g>
          <g text-anchor="middle" font-weight="800">
            <text x="212" y="250" font-size="18" fill="#1B2A4A">{cap_a or "ONLY&nbsp;A"}</text>
            <text x="688" y="250" font-size="18" fill="#B22234">{cap_b or "ONLY&nbsp;B"}</text>
            <text x="450" y="205" font-size="18" fill="#8a6a1e">{cap_both}</text>
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="12.5" fill="#9aa2b2">
            {_hints(a_only, 212, 284, "#9aa2b2")}
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="12.5" fill="#caa8ad">
            {_hints(b_only, 688, 284, "#caa8ad")}
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="11.5" fill="#c1a860">
            {_hints(both, 450, 300, "#c1a860")}
          </g>
        </svg>
      </div>
    </div>
"""
    return body, _VENN_CSS


def venn3(prompt, a_nm, b_nm, c_nm):
    """Three-circle Venn with a legend row above (topic keys + write-lines) and
    faded region captions inside the SVG."""
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="vhead" style="justify-content:flex-start;gap:22px">
      <span class="oh a"><span class="nm">&#9679; {a_nm}</span><span class="yr">write examples in the circle</span></span>
      <span class="oh" style="max-width:33%"><span class="nm" style="color:#8a6a1e">&#9679; {b_nm}</span><span class="yr">write examples in the circle</span></span>
      <span class="oh b"><span class="nm">&#9679; {c_nm}</span><span class="yr">write examples in the circle</span></span>
    </div>
    <div class="canvas"><div class="venn-wrap">
      <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet" font-family="Helvetica Neue, Arial, sans-serif">
        <circle cx="330" cy="230" r="205" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.2" opacity="0.92"/>
        <circle cx="570" cy="230" r="205" fill="#FAF3E2" stroke="#C89B3C" stroke-width="3.2" opacity="0.85"/>
        <circle cx="450" cy="380" r="205" fill="#FBEEEF" stroke="#B22234" stroke-width="3.2" opacity="0.8"/>
        <g text-anchor="middle" font-weight="800" font-size="15">
          <text x="225" y="170" fill="#1B2A4A">ONLY 1</text>
          <text x="675" y="170" fill="#8a6a1e">ONLY 2</text>
          <text x="450" y="470" fill="#B22234">ONLY 3</text>
          <text x="450" y="300" fill="#5A6579" font-size="13">ALL THREE</text>
        </g>
      </svg>
    </div></div>
"""
    return body, _VENN_CSS


# ---------------------------------------------------------------- T-chart
_TC_CSS = r"""
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .tc-cols{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc-col .band small{ display:block; font-weight:600; font-size:8pt; opacity:.9; letter-spacing:0; text-transform:none; }
  .rowlbl{ display:flex; align-items:flex-start; gap:7px; padding:6px 10px 0; }
  .rowlbl .tagn{ background:var(--navy); color:#fff; font-size:7.5pt; font-weight:800; padding:2px 7px; border-radius:9px; white-space:nowrap; flex:0 0 auto; margin-top:1px; }
  .rowlbl .tagr{ background:var(--red); }
  .rowlbl .q{ font-size:8.6pt; color:#3a4455; }
  .midbar{ flex:0 0 auto; background:var(--navy-tint); border:1.5px solid var(--navy); border-radius:6px; padding:6px 11px; font-size:9pt; }
  .midbar b{ color:var(--navy); }
  .tnbox{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.9pt; line-height:1.32; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
  .subj{ flex:0 0 auto; background:var(--cream); border:1.4px dashed var(--gold); border-radius:6px; padding:6px 10px; font-size:9pt; text-align:center; color:var(--navy); }
"""

def _rows(rows, red=False):
    cls = "tagn tagr" if red else "tagn"
    return "\n          ".join(
        f'<div class="rowlbl"><span class="{cls}">{tag}</span><span class="q">{q}</span></div>'
        for tag, q in rows)

def tchart(prompt, l_band, l_sub, r_band, r_sub, l_rows, r_rows, midbar, subj=None, tnbox=None):
    subj_html = f'<div class="subj">{subj}</div>' if subj else ""
    tn_html = ""
    if tnbox:
        tn_html = (f'<div class="tnbox"><span class="star">&#9733;</span>'
                   f'<span class="t">{tnbox}</span></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="tc">
      {subj_html}
      <div class="tc-cols">
        <div class="tc-col">
          <div class="band navy">{l_band}<small>{l_sub}</small></div>
          {_rows(l_rows)}
          <div class="well navy lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
        <div class="tc-col">
          <div class="band red">{r_band}<small>{r_sub}</small></div>
          {_rows(r_rows, red=True)}
          <div class="well red lines" style="margin:6px 8px 8px; flex:1 1 0;"></div>
        </div>
      </div>
      {tn_html}
      <div class="midbar">{midbar}</div>
    </div>
"""
    return body, _TC_CSS


# ---------------------------------------------------------------- Matrix
_MX_CSS = r"""
  .mx{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; border:2px solid var(--navy); border-radius:8px; overflow:hidden; }
  .mx-row{ flex:1 1 0; display:grid; min-height:0; border-top:1px solid var(--rule); }
  .mx-row:first-child{ border-top:none; }
  .mx-row.head{ flex:0 0 auto; }
  .mx-cell{ padding:5px 9px; border-left:1px solid var(--rule); min-width:0; display:flex; flex-direction:column; }
  .mx-cell:first-child{ border-left:none; }
  .mx-rowlbl{ background:var(--navy); color:#fff; font-size:8.4pt; font-weight:800; display:flex; align-items:center; }
  .mx-colhead{ color:#fff; font-size:9pt; font-weight:800; text-align:center; justify-content:center; align-items:center; letter-spacing:.02em; }
  .mx-colhead small{ display:block; font-weight:600; font-size:7pt; opacity:.9; }
  .mx-cell .cue{ position:static; font-size:7.4pt; color:#9aa2b2; font-style:italic; text-transform:none; letter-spacing:0; font-weight:600; margin-bottom:2px; }
  .mx-write{ flex:1 1 0; }
  .mx-concl{ flex:0 0 auto; background:var(--gold-tint); }
  .mx-concl .mx-cell{ font-size:8.6pt; color:#3a2f12; }
"""

def matrix(prompt, cols, rows, concl):
    """cols=list[(name, sub, color)] ; rows=list[(label, list_of_col_cues)] ; concl=str."""
    ncol = len(cols) + 1
    tmpl = "grid-template-columns:0.9fr " + " ".join("1fr" for _ in cols) + ";"
    head = f'<div class="mx-row head" style="{tmpl}">'
    head += '<div class="mx-cell mx-rowlbl" style="background:#0f1a30;"></div>'
    for nm, sub, color in cols:
        bg = {"navy": "var(--navy)", "red": "var(--red)", "gold": "var(--gold)"}[color]
        tc = "var(--navy)" if color == "gold" else "#fff"
        head += f'<div class="mx-cell mx-colhead" style="background:{bg};color:{tc}">{nm}<small>{sub}</small></div>'
    head += "</div>"
    body_rows = ""
    for label, cues in rows:
        body_rows += f'<div class="mx-row" style="{tmpl}"><div class="mx-cell mx-rowlbl">{label}</div>'
        for cue in cues:
            body_rows += f'<div class="mx-cell"><span class="cue">{cue}</span><div class="well lines mx-write"></div></div>'
        body_rows += "</div>"
    concl_row = (f'<div class="mx-row mx-concl" style="grid-template-columns:0.9fr 1fr;">'
                 f'<div class="mx-cell mx-rowlbl" style="background:var(--gold);color:var(--navy)">PATTERN</div>'
                 f'<div class="mx-cell" style="border-left:1px solid var(--gold)">{concl}</div></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="mx">
      {head}
      {body_rows}
      {concl_row}
    </div>
"""
    return body, _MX_CSS


# ---------------------------------------------------------------- Cause & Effect
_CE_CSS = r"""
  .ce{ flex:1 1 auto; display:flex; align-items:stretch; gap:6px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .ce-col.mid{ flex:0 0 27%; justify-content:center; }
  .ce-arrows{ flex:0 0 auto; display:flex; flex-direction:column; justify-content:center; }
  .ce-event{ background:var(--red); color:#fff; border-radius:8px; padding:9px 8px; text-align:center;
             font-weight:800; font-size:11pt; box-shadow:0 2px 0 rgba(0,0,0,.12); }
  .ce-event small{ display:block; font-weight:600; font-size:8pt; opacity:.92; margin-top:2px; }
  .ce-box{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-box .cue{ position:static; font-size:7.6pt; color:var(--muted); font-weight:800; text-transform:uppercase; letter-spacing:.03em; padding:2px 2px 3px; }
  .ce-chain{ flex:1 1 auto; display:flex; flex-direction:column; gap:0; min-height:0; }
  .ce-step{ flex:1 1 0; display:flex; align-items:stretch; gap:9px; min-height:0; }
  .ce-num{ flex:0 0 30px; background:var(--navy); color:#fff; border-radius:7px; display:flex; align-items:center; justify-content:center; font-family:Georgia,serif; font-size:14pt; font-weight:700; }
  .ce-scard{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .ce-scard .nm{ font-size:9.6pt; font-weight:800; color:var(--navy); }
  .ce-scard .nm .q{ font-weight:600; font-size:8.4pt; color:#5a6579; font-style:italic; }
  .ce-down{ flex:0 0 auto; }
"""

def cause_effect_chain(prompt, steps, tail=""):
    """Numbered vertical chain. steps=list[(name, question)]; tail optional reflection HTML."""
    rows = []
    n = len(steps)
    for i, (nm, q) in enumerate(steps):
        rows.append(
            f'<div class="ce-step"><div class="ce-num">{i+1}</div>'
            f'<div class="ce-scard"><div class="nm">{nm} <span class="q">{q}</span></div>'
            f'<div class="well navy lines fill" style="margin-top:3px"></div></div></div>')
        if i < n - 1:
            rows.append('<div class="arr-d" style="margin:1px 0 1px 8px"></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="ce-chain">
      {''.join(rows)}
    </div>
    {tail}
"""
    return body, _CE_CSS

def cause_effect_split(prompt, event_nm, event_sub, cause_cue, effect_cue, midbar=""):
    """Causes (left) -> EVENT -> Effects (right)."""
    mid = f'<div class="midbar" style="margin-top:8px">{midbar}</div>' if midbar else ""
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="ce">
      <div class="ce-col"><div class="band navy sm">CAUSES</div>
        <div class="ce-box"><span class="cue">{cause_cue}</span><div class="well navy lines" style="flex:1 1 0"></div></div></div>
      <div class="ce-arrows"><div class="arr-r"></div></div>
      <div class="ce-col mid"><div class="ce-event">{event_nm}<small>{event_sub}</small></div></div>
      <div class="ce-arrows"><div class="arr-r"></div></div>
      <div class="ce-col"><div class="band red sm">EFFECTS</div>
        <div class="ce-box"><span class="cue">{effect_cue}</span><div class="well red lines" style="flex:1 1 0"></div></div></div>
    </div>
    {mid}
"""
    return body, _CE_CSS


# ---------------------------------------------------------------- Timeline
_TL_CSS = r"""
  .tl{ flex:1 1 auto; position:relative; display:flex; flex-direction:column; min-height:0; padding-left:150px; }
  .tl::before{ content:""; position:absolute; left:132px; top:6px; bottom:6px; width:4px; background:var(--navy); border-radius:2px; }
  .ev{ flex:1 1 0; display:flex; align-items:stretch; position:relative; min-height:0; padding:5px 0; }
  .ev .date{ position:absolute; left:-150px; top:5px; width:120px; text-align:right; }
  .ev .date .d{ font-family:Georgia,serif; font-size:14pt; font-weight:700; color:var(--red); line-height:1; }
  .ev .date .w{ display:block; border-bottom:1.6px solid var(--rule); height:15px; margin-top:6px; }
  .ev .date .wl{ font-size:7pt; color:#8792a4; font-style:italic; }
  .ev .node{ position:absolute; left:-24px; top:6px; width:20px; height:20px; border-radius:50%; background:#fff; border:4px solid var(--gold); }
  .ev .card{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .ev .nm{ font-size:11.5pt; font-weight:800; color:var(--navy); }
  .ev .nm .q{ font-weight:600; font-size:8.4pt; color:#5a6579; font-style:italic; }
  .ev .well{ margin-top:3px; }
"""

def timeline(prompt, events, blank_dates=False):
    """events=list[(date, name, question, is_red)]. blank_dates=True hides dates for a blank reproducible."""
    rows = []
    for i, (d, nm, q, red) in enumerate(events):
        node = ' style="border-color:var(--red);"' if red else ""
        nmc = ' style="color:var(--red)"' if red else ""
        wc = "red" if red else "navy"
        wl = '<span class="wl">write the date</span>' if (i == 0 and blank_dates) else ""
        dd = "" if blank_dates else d
        rows.append(
            f'<div class="ev"><div class="date"><div class="d">{dd}</div><span class="w"></span>{wl}</div>'
            f'<div class="node"{node}></div>'
            f'<div class="card"><div class="nm"{nmc}>{nm} <span class="q">{q}</span></div>'
            f'<div class="well {wc} lines fill"></div></div></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="tl">
      {''.join(rows)}
    </div>
"""
    return body, _TL_CSS


# ---------------------------------------------------------------- Concept web
_CW_CSS = r"""
  .cw-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .cw-wrap svg{ width:100%; height:100%; display:block; }
"""

def _hub_text(hub, cx, cy):
    """Render the hub label on up to two lines (split on ' / ' if present)."""
    parts = [p.strip() for p in hub.split(" / ")]
    if len(parts) == 1:
        return (f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-size="12.5" '
                f'font-weight="800" fill="#7a5c15">{parts[0]}</text>')
    return (f'<text x="{cx}" y="{cy-10}" text-anchor="middle" font-size="12.5" font-weight="800" fill="#7a5c15">{parts[0]}</text>'
            f'<text x="{cx}" y="{cy+9}" text-anchor="middle" font-size="10.5" font-weight="700" fill="#8a6a1e">{parts[1]}</text>')

def concept_web(prompt, hub, spokes):
    """Hub-and-spoke. hub=str (use ' / ' to split across two lines). spokes=list[str] (up to 7)."""
    import math
    cx, cy, R = 450, 290, 205
    pts = []
    n = len(spokes)
    # place spokes around an ellipse
    for i in range(n):
        ang = -math.pi/2 + i * (2*math.pi/n)
        x = cx + int(R*1.55*math.cos(ang))
        y = cy + int(R*math.sin(ang))
        pts.append((x, y))
    lines = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="#C89B3C" stroke-width="2.4"/>'
        for x, y in pts)
    bubbles = ""
    for i, ((x, y), lbl) in enumerate(zip(pts, spokes)):
        bubbles += (f'<g><rect x="{x-92}" y="{y-30}" width="184" height="60" rx="10" '
                    f'fill="#EEF1F7" stroke="#1B2A4A" stroke-width="2"/>'
                    f'<text x="{x}" y="{y-14}" text-anchor="middle" font-size="11" font-weight="800" fill="#1B2A4A">{lbl}</text>'
                    f'<line x1="{x-78}" y1="{y+4}" x2="{x+78}" y2="{y+4}" stroke="#B9C2D0" stroke-width="1" stroke-dasharray="2 5"/>'
                    f'<line x1="{x-78}" y1="{y+20}" x2="{x+78}" y2="{y+20}" stroke="#B9C2D0" stroke-width="1" stroke-dasharray="2 5"/></g>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="canvas"><div class="cw-wrap">
      <svg viewBox="0 0 900 580" preserveAspectRatio="xMidYMid meet" font-family="Helvetica Neue, Arial, sans-serif">
        {lines}
        <circle cx="{cx}" cy="{cy}" r="100" fill="#FAF3E2" stroke="#C89B3C" stroke-width="3.5"/>
        {_hub_text(hub, cx, cy)}
        <text x="{cx}" y="{cy+34}" text-anchor="middle" font-size="9" font-style="italic" fill="#b9a25e">write the link</text>
        {bubbles}
      </svg>
    </div></div>
"""
    return body, _CW_CSS


# ---------------------------------------------------------------- Main Idea & Details
_MI_CSS = r"""
  .mi{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .mi-main{ flex:0 0 auto; }
  .mi-main .well{ height:58px; }
  .mi-details{ flex:1 1 auto; display:flex; gap:10px; min-height:0; }
  .mi-d{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .mi-up{ align-self:center; }
  .mi-d .band{ font-size:8.6pt; }
  .mi-sum{ flex:0 0 auto; background:var(--navy-tint); border:1.5px solid var(--navy); border-radius:6px; padding:6px 11px; font-size:9pt; }
  .mi-sum b{ color:var(--navy); }
"""

def main_idea(prompt, main_label, details, summary):
    """details=list[(band_label, cue)]."""
    dcols = ""
    for lbl, cue in details:
        dcols += (f'<div class="mi-d"><div class="arr-d mi-up"></div>'
                  f'<div class="band navy sm">{lbl}</div>'
                  f'<div class="well lines" style="flex:1 1 0"><span class="cue">{cue}</span></div></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="mi">
      <div class="mi-main"><div class="band gold">{main_label}</div>
        <div class="well lines cream" style="border-radius:0 0 6px 6px"></div></div>
      <div class="mi-details">
        {dcols}
      </div>
      <div class="mi-sum">{summary}</div>
    </div>
"""
    return body, _MI_CSS


# ---------------------------------------------------------------- KWL
_KWL_CSS = r"""
  .kwl{ flex:1 1 auto; display:flex; gap:10px; min-height:0; }
  .kwl-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .kwl-col .band small{ display:block; font-weight:600; font-size:7.6pt; opacity:.9; text-transform:none; letter-spacing:0; }
"""

def kwl(prompt):
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="kwl">
      <div class="kwl-col"><div class="band navy">K<small>what I already KNOW</small></div>
        <div class="well navy lines" style="flex:1 1 0;border-radius:0 0 6px 6px"></div></div>
      <div class="kwl-col"><div class="band red">W<small>what I WANT to know</small></div>
        <div class="well red lines" style="flex:1 1 0;border-radius:0 0 6px 6px"></div></div>
      <div class="kwl-col"><div class="band gold">L<small>what I LEARNED</small></div>
        <div class="well gold lines" style="flex:1 1 0;border-radius:0 0 6px 6px"></div></div>
    </div>
"""
    return body, _KWL_CSS


# ---------------------------------------------------------------- 5 Ws
_5W_CSS = r"""
  .fw-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .fw-wrap svg{ width:100%; height:100%; display:block; }
"""

def five_ws(prompt):
    cx, cy = 450, 285
    spokes = [("WHO", 150, 120), ("WHAT", 750, 120), ("WHEN", 90, 300),
              ("WHERE", 810, 300), ("WHY", 250, 470), ("HOW", 650, 470)]
    lines = "".join(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="#C89B3C" stroke-width="2.2"/>'
                    for _, x, y in spokes)
    bub = ""
    for lbl, x, y in spokes:
        bub += (f'<g><rect x="{x-95}" y="{y-34}" width="190" height="68" rx="10" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="2"/>'
                f'<text x="{x-83}" y="{y-16}" font-size="11" font-weight="800" fill="#B22234">{lbl}</text>'
                f'<line x1="{x-83}" y1="{y+2}" x2="{x+83}" y2="{y+2}" stroke="#B9C2D0" stroke-width="1" stroke-dasharray="2 5"/>'
                f'<line x1="{x-83}" y1="{y+20}" x2="{x+83}" y2="{y+20}" stroke="#B9C2D0" stroke-width="1" stroke-dasharray="2 5"/></g>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="canvas"><div class="fw-wrap">
      <svg viewBox="0 0 900 570" preserveAspectRatio="xMidYMid meet" font-family="Helvetica Neue, Arial, sans-serif">
        {lines}
        {bub}
        <rect x="{cx-105}" y="{cy-40}" width="210" height="80" rx="12" fill="#B22234"/>
        <text x="{cx}" y="{cy-8}" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">THE EVENT / ISSUE</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-size="9" font-style="italic" fill="#f3c9cd">name it here</text>
      </svg>
    </div></div>
"""
    return body, _5W_CSS


# ---------------------------------------------------------------- Problem–Solution
_PS_CSS = r"""
  .ps{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .ps-prob .well{ height:52px; }
  .ps-opts{ flex:1 1 auto; display:flex; gap:10px; min-height:0; }
  .ps-opt{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; border:1.6px solid var(--rule); border-radius:7px; overflow:hidden; }
  .ps-opt .oh{ background:var(--navy-tint); color:var(--navy); font-weight:800; font-size:8.6pt; padding:4px 9px; border-bottom:1px solid var(--rule); }
  .ps-opt .sec{ padding:4px 8px; } .ps-opt .sec .cue{ position:static; font-size:7.4pt; color:var(--muted); font-weight:800; text-transform:uppercase; }
  .ps-decide{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold); border-radius:6px; padding:6px 11px; font-size:9pt; color:#3a2f12; }
  .ps-decide b{ color:#7a5c15; }
"""

def problem_solution(prompt, problem_cue, options, decide):
    opt_html = ""
    for i, name in enumerate(options):
        opt_html += (f'<div class="ps-opt"><div class="oh">Option {chr(65+i)}: {name}</div>'
                     f'<div class="sec" style="flex:1 1 0;display:flex;flex-direction:column"><span class="cue">The idea</span>'
                     f'<div class="well lines" style="flex:1 1 0"></div></div>'
                     f'<div class="sec" style="flex:0 0 34%;display:flex;flex-direction:column;border-top:1px solid var(--rule)">'
                     f'<span class="cue">Trade-off / result</span><div class="well lines tint-red" style="flex:1 1 0"></div></div></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="ps">
      <div class="ps-prob"><div class="band red sm">THE PROBLEM</div>
        <div class="well red lines"><span class="cue">{problem_cue}</span></div></div>
      <div class="ps-opts">{opt_html}</div>
      <div class="ps-decide">{decide}</div>
    </div>
"""
    return body, _PS_CSS


# ---------------------------------------------------------------- Frayer
_FR_CSS = r"""
  .fr{ flex:1 1 auto; position:relative; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:10px; min-height:0; }
  .fr-q{ display:flex; flex-direction:column; min-height:0; border:1.6px solid var(--rule); border-radius:7px; overflow:hidden; }
  .fr-q .qh{ font-size:8.6pt; font-weight:800; padding:4px 9px; color:#fff; }
  .fr-q .well{ flex:1 1 0; }
  .fr-oval{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:150px; height:84px;
            background:#fff; border:2.5px solid var(--gold); border-radius:50%; display:flex; flex-direction:column;
            align-items:center; justify-content:flex-start; padding-top:12px; z-index:2; box-shadow:0 0 0 5px #fff; }
  .fr-oval .lbl{ font-size:7pt; font-weight:800; color:#b9a25e; letter-spacing:.08em; text-transform:uppercase; }
  .fr-oval .term{ font-size:8pt; color:var(--muted); font-style:italic; margin-top:2px; }
"""

def frayer(prompt, term_line="the term"):
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="fr">
      <div class="fr-q"><div class="qh" style="background:var(--navy)">DEFINITION <span style="font-weight:600;opacity:.85">(in your words)</span></div>
        <div class="well navy lines"></div></div>
      <div class="fr-q"><div class="qh" style="background:var(--red)">CHARACTERISTICS <span style="font-weight:600;opacity:.85">(must-have traits)</span></div>
        <div class="well red lines"></div></div>
      <div class="fr-q"><div class="qh" style="background:#1e6b40">EXAMPLES</div>
        <div class="well lines tint-green"></div></div>
      <div class="fr-q"><div class="qh" style="background:#8a6a1e">NON-EXAMPLES</div>
        <div class="well lines tint-gold"></div></div>
      <div class="fr-oval"><span class="lbl">Term</span><span class="term">{term_line}</span></div>
    </div>
"""
    return body, _FR_CSS


# ---------------------------------------------------------------- CER
_CER_CSS = r"""
  .cer{ flex:1 1 auto; display:flex; flex-direction:column; gap:0; min-height:0; }
  .cer-b{ display:flex; flex-direction:column; min-height:0; }
  .cer-claim{ flex:0 0 auto; } .cer-claim .well{ height:52px; }
  .cer-ev{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .cer-ev .well{ flex:1 1 0; }
  .cer-rz{ flex:0 0 auto; } .cer-rz .well{ height:70px; }
  .cer .arr-d{ margin:3px auto; }
"""

def cer(prompt, claim_cue, ev_cue, rz_cue):
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="cer">
      <div class="cer-b cer-claim"><div class="band navy sm">CLAIM &mdash; answer the question in one sentence</div>
        <div class="well navy lines"><span class="cue">{claim_cue}</span></div></div>
      <div class="arr-d"></div>
      <div class="cer-b cer-ev"><div class="band red sm">EVIDENCE &mdash; specific facts / quotations that support the claim</div>
        <div class="well red lines"><span class="cue">{ev_cue}</span></div></div>
      <div class="arr-d"></div>
      <div class="cer-b cer-rz"><div class="band gold sm">REASONING &mdash; why the evidence proves the claim</div>
        <div class="well gold lines"><span class="cue">{rz_cue}</span></div></div>
    </div>
"""
    return body, _CER_CSS


# ---------------------------------------------------------------- HIPPO (source analysis)
_HP_CSS = r"""
  .hp{ flex:1 1 auto; display:flex; flex-direction:column; gap:7px; min-height:0; }
  .hp-src{ flex:0 0 auto; background:var(--cream); border:1.4px dashed var(--gold); border-radius:6px; padding:6px 10px; font-size:8.8pt; color:var(--navy); }
  .hp-rows{ flex:1 1 auto; display:flex; flex-direction:column; gap:6px; min-height:0; }
  .hp-row{ flex:1 1 0; display:flex; gap:9px; min-height:0; align-items:stretch; }
  .hp-tile{ flex:0 0 168px; background:var(--gold); color:var(--navy); border-radius:6px; padding:5px 9px; display:flex; flex-direction:column; justify-content:center; }
  .hp-tile .L{ font-family:Georgia,serif; font-size:15pt; font-weight:700; line-height:1; }
  .hp-tile .n{ font-size:8pt; font-weight:800; text-transform:uppercase; letter-spacing:.03em; }
  .hp-tile .q{ font-size:7.4pt; font-weight:600; color:#5c4a17; margin-top:2px; line-height:1.2; }
  .hp-row .well{ flex:1 1 auto; }
"""

def hippo(prompt):
    rows = [
        ("H", "Historical context", "What was happening when this was made?"),
        ("I", "Intended audience", "Who was meant to see or read it?"),
        ("P", "Point of view", "Who made it &mdash; and how does that shape it?"),
        ("P", "Purpose", "Why was it made? What did it want to do?"),
        ("O", "Outside information", "What do you know that connects to it?"),
    ]
    rh = ""
    for L, n, q in rows:
        rh += (f'<div class="hp-row"><div class="hp-tile"><span class="L">{L}</span>'
               f'<span class="n">{n}</span><span class="q">{q}</span></div>'
               f'<div class="well gold lines"></div></div>')
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="hp">
      <div class="hp-src"><b>Source:</b> ________________________________________________&nbsp;&nbsp;
        <span class="hint">title &middot; author / creator &middot; date &middot; type</span></div>
      <div class="hp-rows">{rh}</div>
    </div>
"""
    return body, _HP_CSS


# ---------------------------------------------------------------- Tennessee Connection
_TNC_CSS = r"""
  .tnc{ flex:1 1 auto; display:flex; flex-direction:column; gap:9px; min-height:0; }
  .tnc-top{ flex:1 1 auto; display:flex; gap:10px; align-items:stretch; min-height:0; }
  .tnc-panel{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tnc-hub{ flex:0 0 96px; display:flex; flex-direction:column; align-items:center; justify-content:center; }
  .tnc-hub .ring{ width:80px; height:80px; border-radius:50%; background:var(--gold-tint); border:3px solid var(--gold);
                  display:flex; align-items:center; justify-content:center; text-align:center; font-size:7.6pt; font-weight:800; color:#7a5c15; padding:6px; }
  .tnc-hub .cn{ font-size:7.4pt; font-weight:800; color:var(--muted); text-transform:uppercase; letter-spacing:.04em; margin-top:5px; }
  .tnc-link{ flex:0 0 auto; background:var(--navy-tint); border:1.5px solid var(--navy); border-radius:6px; padding:6px 11px; font-size:9pt; }
  .tnc-link b{ color:var(--navy); }
  .tnc-why{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 11px; font-size:8.9pt; color:#3a2f12; }
  .tnc-why b{ color:#7a5c15; }
"""

def tn_connection(prompt, nat_label, tn_label):
    body = f"""
    <div class="prompt">{prompt}</div>
    <div class="tnc">
      <div class="tnc-top">
        <div class="tnc-panel"><div class="band navy sm">{nat_label}</div>
          <div class="well navy lines" style="flex:1 1 0;border-radius:0 0 6px 6px"></div></div>
        <div class="tnc-hub"><div class="ring">how are they connected?</div><div class="cn">&#9733; connects to</div></div>
        <div class="tnc-panel"><div class="band gold sm">{tn_label}</div>
          <div class="well gold lines" style="flex:1 1 0;border-radius:0 0 6px 6px"></div></div>
      </div>
      <div class="tnc-link"><b>How are they linked?</b> ___________________________________________________________</div>
      <div class="tnc-why"><b>Why the local story matters:</b> ______________________________________________________</div>
    </div>
"""
    return body, _TNC_CSS
