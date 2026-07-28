# -*- coding: utf-8 -*-
"""Blank reproducible: Vertical Timeline (Order / Change Over Time).
Date well sits to the LEFT of each event; tick on the spine; wide event well right."""

CSS = r"""
  .tl{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .tl-ends{ display:flex; align-items:center; gap:10px; flex:0 0 auto; margin-bottom:2px; }
  .tl-ends .sp{ width:44px; flex:0 0 44px; text-align:center; }
  .tl-ends .lbl{ font-size:8pt; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); }
  .tl-ends .lbl.d{ width:150px; flex:0 0 150px; text-align:center; }
  .tl-row{ flex:1 1 0; display:flex; align-items:stretch; gap:10px; min-height:0; }
  /* left DATE well (small, light) */
  .tl-date{ width:150px; flex:0 0 150px; align-self:center; }
  .tl-date .well{ height:56px; }
  /* center spine + numbered tick */
  .tl-spine{ width:44px; flex:0 0 44px; position:relative; }
  .tl-spine::before{ content:''; position:absolute; left:50%; top:0; bottom:0; width:5px;
    background:var(--navy); transform:translateX(-50%); }
  .tl-dot{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
    width:30px; height:30px; border-radius:50%; background:var(--gold); border:3px solid var(--navy);
    color:var(--navy); font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; z-index:2; }
  /* first/last spine caps so the line starts/ends at the ticks */
  .tl-row:first-child .tl-spine::before{ top:50%; }
  .tl-row:last-child .tl-spine::before{ bottom:50%; }
  /* wide EVENT well (light) */
  .tl-event{ flex:1 1 auto; align-self:center; }
  .tl-event .well{ height:64px; }
  .cue{ z-index:1; }
  /* bottom arrowhead = flow direction */
  .tl-arrow{ display:flex; flex:0 0 auto; }
  .tl-arrow .sp{ width:44px; flex:0 0 44px; display:flex; justify-content:center; }
  .tl-arrow .sp .arr-d{ margin:0; }
  .tl-arrow .lbl{ width:150px; flex:0 0 150px; }
"""

def _row(n):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"><span class="cue">Date / When</span></div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"><span class="cue">What happened &middot; why it matters</span></div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Order the events from <b>earliest</b> (top) to <b>latest</b> (bottom). On each line, write the <b>date on the left</b>, then <b>what happened</b> on the right.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">Order &middot; change over time</div>
        </div>
""" + "".join(_row(n) for n in range(1, 6)) + r"""
        <div class="tl-arrow">
          <div class="lbl"></div>
          <div class="sp"><div class="arr-d"></div></div>
          <div class="lbl" style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest / most recent</div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="07_timeline_blank",
    title="Timeline &mdash; Order &amp; Change Over Time",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Order / sequence", "navy"), ("SSP.05 &middot; Chronology", "skill")],
    why=("Use to put events in <b>order</b> and see how things <b>change over time</b> &mdash; the vertical "
         "spine makes sequence and distance between events visible. "
         "<span class='cite'>Chronological reasoning &mdash; ordering events and tracking change &mdash; is a core "
         "practice (TN Social Studies Practices SSP.05).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the events on cards and have students <b>physically sequence</b> them before writing. Sentence starter: &ldquo;First ___, then ___, and finally ___.&rdquo;",
        extend="Mark the moment of biggest <b>change</b>. Explain in one sentence what caused it and what it changed.",
        show="Students may <b>write</b> dates, <b>say</b> the sequence aloud, <b>draw</b> an icon per event, or <b>build</b> the line with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
