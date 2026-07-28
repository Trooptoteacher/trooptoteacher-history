# -*- coding: utf-8 -*-
"""Blank reproducible: Cause & Effect (causes -> event -> effects)."""

CSS = r"""
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:6px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.7pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:11px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; }
  .cebox .well{ flex:1 1 0; }
  .ce-arrs{ flex:0 0 30px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:26px 0; }
  .ce-arrs .arr-r{ border-left-width:18px; border-top-width:13px; border-bottom-width:13px; }
  .ce-center{ flex:1.22 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band{ font-size:12pt; padding:8px; border-radius:7px 7px 0 0; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#8792a4; }
"""

def _boxes(kind, band):
    # three titled light wells for a side (kind = navy|red band)
    out = []
    for i in (1, 2, 3):
        out.append(
            f'<div class="cebox"><div class="band {kind} sm">{band}&nbsp;{i}</div>'
            f'<div class="well lines"></div></div>')
    return "\n        ".join(out)

BODY = f"""
    <div class="prompt">List what <b>led to</b> the event on the left, then what <b>followed from</b> it on the right. Arrows show the flow: <b>causes &rarr; event &rarr; effects</b>.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; what led to it</div>
          <div class="ce-stack">
        {_boxes("navy", "Cause")}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">EVENT / TOPIC</div>
            <div class="well lines cream"><span class="cue">Name the event or decision</span></div>
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; what followed</div>
          <div class="ce-stack">
        {_boxes("red", "Effect")}
          </div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="06_causeeffect_blank",
    title="Cause &amp; Effect",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Causes / Effects", "navy"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
    why=("Use when a task asks <b>what led to</b> an event and <b>what followed</b> from it &mdash; separating "
         "causes from effects builds reasoning about change over time. "
         "<span class='cite'>Analyzing cause &amp; effect is a core TN Social Studies Practice (SSP.05).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Offer sentence frames: &ldquo;Because ___, the event happened,&rdquo; and &ldquo;As a result, ___.&rdquo; Fill the event box first.",
        extend="Rank the causes from most to least important, or trace one effect into a new cause (a chain).",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> arrows/icons, or <b>build</b> it with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
