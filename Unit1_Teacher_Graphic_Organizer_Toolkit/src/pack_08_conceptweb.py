# -*- coding: utf-8 -*-
"""Blank reproducible: Concept Web (central idea + spokes)."""

CSS = r"""
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:center; justify-content:center;
         background:var(--paper); border:2px solid var(--rule); border-radius:50%; }
  .node .ncue{ font-size:8pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase; color:var(--muted); }
  .node .nline{ width:74%; border-bottom:1.5px dashed #C4CCDA; height:0; margin-top:15px; }
  .node .nline+.nline{ margin-top:14px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:11pt; color:#8f9bb3;
              letter-spacing:.02em; text-align:center; line-height:1.0; }
  .hub .nline{ border-bottom-color:#9aa6bd; }
  .snode{ border-style:dashed; border-color:#C4CCDA; }
  .snode .ncue{ font-size:7.2pt; color:#8792a4; }
"""

def _node(x, y, w, h, cue, cls="node", lines=2):
    guides = "".join('<div class="nline"></div>' for _ in range(lines))
    return (f'<div class="{cls}" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="ncue">{cue}</div>{guides}</div>')

_outer = [(50, 12, "Idea 1"), (85, 31, "Idea 2"), (85, 69, "Idea 3"),
          (50, 88, "Idea 4"), (15, 69, "Idea 5"), (15, 31, "Idea 6")]
_small = [(8, 13, "detail"), (92, 13, "detail"), (8, 87, "detail"), (92, 87, "detail")]

_outer_html = "\n      ".join(_node(x, y, 172, 108, cue) for x, y, cue in _outer)
_small_html = "\n      ".join(_node(x, y, 104, 66, cue, cls="node snode", lines=1) for x, y, cue in _small)

BODY = f"""
    <div class="prompt">Write the big idea in the center. On each outer bubble, add an idea that <b>connects</b> to it &mdash; then use the small bubbles for a supporting detail.</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="50" y2="12"/>
            <line x1="50" y1="50" x2="85" y2="31"/>
            <line x1="50" y1="50" x2="85" y2="69"/>
            <line x1="50" y1="50" x2="50" y2="88"/>
            <line x1="50" y1="50" x2="15" y2="69"/>
            <line x1="50" y1="50" x2="15" y2="31"/>
          </g>
          <g stroke="#D4DAE4" stroke-width="0.6" stroke-dasharray="1.4 1.4">
            <line x1="15" y1="31" x2="8" y2="13"/>
            <line x1="85" y1="31" x2="92" y2="13"/>
            <line x1="15" y1="69" x2="8" y2="87"/>
            <line x1="85" y1="69" x2="92" y2="87"/>
          </g>
        </svg>
        {_outer_html}
      {_small_html}
        <div class="node hub" style="left:50%; top:50%; width:196px; height:150px;">
          <div class="hcue">Central Idea</div>
          <div class="nline"></div><div class="nline"></div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="08_conceptweb_blank",
    title="Concept Web",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Brainstorm / connect", "navy"), ("DOK 2 &middot; Relationships", "skill")],
    why=("Use to <b>brainstorm</b> around a central concept and show how ideas branch and <b>connect</b> to it. "
         "The hub-and-spoke shape makes relationships between ideas visible at a glance. "
         "<span class='cite'>Organizing ideas into a nonlinear web supports schema-building (UDL 3.0).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Seed two bubbles for students and give a linking stem: &ldquo;This connects to the center because ___.&rdquo;",
        extend="Draw new lines <b>between</b> outer bubbles that relate to each other and label what the link is.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> icons in bubbles, or <b>build</b> it with sticky notes."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
