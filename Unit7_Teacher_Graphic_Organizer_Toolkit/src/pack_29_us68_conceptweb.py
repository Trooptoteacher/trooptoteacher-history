# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.68 Vietnam War Home Front Impact (concept web).
Center hub = "THE WAR AT HOME" as a faint watermark. Three spokes = the anti-war
movement, the draft lottery, and TV & the media -- each a LIGHT bubble with a bold
label and a FADED italic hint. A bottom LIGHT box asks how the home front changed
the war. HAS a Tennessee Connection. Content approved for US.68.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10.2pt; color:var(--navy);
         line-height:1.04; text-align:center; }
  .node .nsub{ font-size:7.4pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.2; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:8px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.04; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:15%; right:15%; bottom:22%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .synthbox{ flex:0 0 auto; margin-top:6px; display:flex; flex-direction:column; }
  .synthbox .band{ border-radius:6px 6px 0 0; }
  .synthbox .well{ min-height:56px; }
  .synthbox .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#9aa6bd; line-height:1.4; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.4pt; line-height:1.28; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


_outer = [
    (50, 16, "The Anti&#8209;War Movement", "small protests &rarr; millions; students (SDS), clergy, veterans &mdash; deep divisions"),
    (21, 79, "Draft by Lottery", "1969 lottery by birthdate; class bias remained &rarr; 26th Amendment (vote at 18)"),
    (79, 79, "TV &amp; the Media", "the first &ldquo;living room war&rdquo;; Cronkite&rsquo;s 1968 &ldquo;stalemate&rdquo; shifts opinion"),
]
_outer_html = "\n        ".join(_node(x, y, 234, 104, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the war&rsquo;s effect at home. On each bubble, write how it turned Americans against the war &mdash; the faint notes are starters. Then answer the box below.</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="50" y2="16"/>
            <line x1="50" y1="50" x2="21" y2="79"/>
            <line x1="50" y1="50" x2="79" y2="79"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:49%; width:196px; height:138px;">
          <div class="hcue">The War<br/>at Home</div>
          <div class="hguides"><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did the <b>home front</b> help change the course of the war?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">public opinion turned against the war &nbsp;&middot;&nbsp; TV brought the war home nightly &nbsp;&middot;&nbsp; protest pressured leaders to withdraw</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee campuses saw real anti&#8209;war activism &mdash; <b>Vanderbilt</b>
        in Nashville and <b>UT Knoxville</b> both had student protests &mdash; and <b>Senator Albert Gore Sr.</b> was one of
        the Senate&rsquo;s earliest critics of the war.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="29_us68_conceptweb",
    title="The First &ldquo;Living Room War&rdquo;",
    kicker="Unit 7 &middot; US.68 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 3 &middot; Evaluate", "skill")],
    why=("A web shows the anti&#8209;war movement, the draft, and television as one home&#8209;front system that turned "
         "public opinion &mdash; and, in turn, the war itself. "
         "<span class='cite'>Evaluating impact and connecting causes builds SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the three bubble labels; fill one together. Ask: which reached the most Americans &mdash; and how?",
        extend="Rank the three by impact on ending the war, and defend your order with evidence.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>design</b> a protest sign or a TV&#8209;news chyron."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.68 (labeled)",
)]
