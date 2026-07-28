# -*- coding: utf-8 -*-
"""Blank reproducible: 5 Ws (Who/What/When/Where/Why + How) hub-and-spoke."""

CSS = r"""
  .ws-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .ws-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .wnode{ position:absolute; transform:translate(-50%,-50%); width:206px;
          border:2px solid var(--rule); border-radius:8px; overflow:hidden; background:var(--paper); }
  .wband{ color:#fff; font-weight:800; font-size:10pt; letter-spacing:.05em; text-transform:uppercase;
          text-align:center; padding:4px 6px; }
  .wsub{ font-weight:600; font-size:7pt; letter-spacing:.03em; opacity:.85; }
  .wwell{ background:var(--paper); height:66px;
          background-image:repeating-linear-gradient(to bottom, transparent 0 22px, #C4CCDA 22px 23px);
          background-position:0 12px; }
  .wn-navy{ border-color:var(--navy);} .wn-navy .wband{ background:var(--navy);}
  .wn-red{ border-color:var(--red);}  .wn-red .wband{ background:var(--red);}
  .wn-gold{ border-color:var(--gold);} .wn-gold .wband{ background:var(--gold); color:var(--navy);}
  .hub5{ position:absolute; transform:translate(-50%,-50%); width:214px;
         border:3px solid var(--navy); border-radius:10px; overflow:hidden; background:var(--paper); }
  .hub5 .wband{ font-size:11.5pt; padding:6px; }
  .hub5 .hwell{ background:var(--paper); height:64px;
                background-image:repeating-linear-gradient(to bottom, transparent 0 21px, #C4CCDA 21px 22px);
                background-position:0 12px; }
"""

def _wnode(x, y, color, label, sub):
    return (f'<div class="wnode wn-{color}" style="left:{x}%; top:{y}%;">'
            f'<div class="wband">{label} <span class="wsub">{sub}</span></div>'
            f'<div class="wwell"></div></div>')

_nodes = [
    (50, 12, "navy", "Who", "&middot; people"),
    (85, 31, "red",  "What", "&middot; happened"),
    (85, 69, "gold", "When", "&middot; time"),
    (50, 88, "navy", "Where", "&middot; place"),
    (15, 69, "red",  "Why", "&middot; reason"),
    (15, 31, "gold", "How", "&middot; the way"),
]
_nodes_html = "\n      ".join(_wnode(*n) for n in _nodes)

BODY = f"""
    <div class="prompt">Name the event in the center, then answer each spoke to capture the <b>essential facts</b>. (Use <b>How</b> to stretch to six.)</div>
    <div class="canvas">
      <div class="ws-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.8">
            <line x1="50" y1="50" x2="50" y2="12"/>
            <line x1="50" y1="50" x2="85" y2="31"/>
            <line x1="50" y1="50" x2="85" y2="69"/>
            <line x1="50" y1="50" x2="50" y2="88"/>
            <line x1="50" y1="50" x2="15" y2="69"/>
            <line x1="50" y1="50" x2="15" y2="31"/>
          </g>
        </svg>
        {_nodes_html}
        <div class="hub5" style="left:50%; top:50%;">
          <div class="wband" style="background:var(--navy);">EVENT / TOPIC <span class="wsub">&middot; name it here</span></div>
          <div class="hwell"></div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="11_5ws_blank",
    title="5 Ws &mdash; Who &middot; What &middot; When &middot; Where &middot; Why",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Basics of an event", "navy"), ("DOK 1&ndash;2 &middot; Comprehension", "skill")],
    why=("Use to quickly capture the <b>essential facts</b> of an event &mdash; who, what, when, where, and why "
         "(plus how). The hub-and-spoke keeps every key question in view at once. "
         "<span class='cite'>Establishing the who/what/when/where anchors chronological reasoning "
         "(TN Social Studies Practices).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Provide sentence stems for each spoke: &ldquo;This happened because ___,&rdquo; &ldquo;It took place in ___.&rdquo;",
        extend="Turn the six facts into a one-sentence summary, or rank which W matters most for understanding the event.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> the spokes with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
