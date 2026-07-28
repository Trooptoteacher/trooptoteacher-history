# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.90 The George H.W. Bush Administration (timeline).
Four milestones of the Cold War's end and post-Cold War power: fall of the Berlin
Wall -> Panama invasion -> Gulf War -> Soviet collapse. Dates left, events right,
as FADED cues. HAS a Tennessee Connection. Content approved for US.90.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .tl{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .tl-ends{ display:flex; align-items:center; gap:10px; flex:0 0 auto; margin-bottom:2px; }
  .tl-ends .sp{ width:44px; flex:0 0 44px; text-align:center; }
  .tl-ends .lbl{ font-size:8pt; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); }
  .tl-ends .lbl.d{ width:150px; flex:0 0 150px; text-align:center; }
  .tl-row{ flex:1 1 0; display:flex; align-items:stretch; gap:10px; min-height:0; }
  .tl-date{ width:150px; flex:0 0 150px; align-self:center; position:relative; }
  .tl-date .well{ height:60px; }
  .tl-date .df{ position:absolute; top:9px; left:9px; right:9px; font-size:8.6pt; font-weight:800;
       color:#8ea0c4; line-height:1.14; text-align:center; }
  .tl-spine{ width:44px; flex:0 0 44px; position:relative; }
  .tl-spine::before{ content:''; position:absolute; left:50%; top:0; bottom:0; width:5px;
    background:var(--navy); transform:translateX(-50%); }
  .tl-dot{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
    width:30px; height:30px; border-radius:50%; background:var(--gold); border:3px solid var(--navy);
    color:var(--navy); font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; z-index:2; }
  .tl-row:first-child .tl-spine::before{ top:50%; }
  .tl-row:last-child .tl-spine::before{ bottom:50%; }
  .tl-event{ flex:1 1 auto; align-self:center; position:relative; }
  .tl-event .well{ height:66px; }
  .tl-event .ef{ position:absolute; top:9px; left:12px; right:12px; font-size:8.4pt; font-style:italic;
       color:#9aa4b4; line-height:1.28; } .tl-event .ef b{ color:#7a8598; font-style:normal; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.4pt; line-height:1.28; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

_events = [
    ("1", "Nov 1989", "<b>The Berlin Wall falls</b> &mdash; communism collapses across Eastern Europe; Bush avoids triumphalism &amp; backs German reunification."),
    ("2", "Dec 1989", "<b>Panama invasion</b> (Operation Just Cause) removes dictator Manuel Noriega, indicted for drug trafficking."),
    ("3", "1990&ndash;91", "<b>The Gulf War</b> &mdash; Iraq invades Kuwait; Bush builds a UN&#8209;backed coalition; Desert Storm liberates Kuwait quickly."),
    ("4", "1991", "<b>The Soviet Union dissolves</b> &mdash; the Cold War ends and the U.S. stands as the world&rsquo;s sole superpower."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow these four turning points from top (earliest) to bottom (latest). On each line, write <b>what happened</b> and <b>why it mattered</b> &mdash; the faint notes are starters. Together they mark the end of the Cold War.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">The Cold War ends &middot; a new world order</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:150px;flex:0 0 150px;"></div>
          <div style="width:44px;flex:0 0 44px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; America as sole superpower</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee Senator <b>Al Gore</b> ran as the 1988 Democratic vice&#8209;presidential
        nominee before joining Clinton&rsquo;s ticket in 1992. And Tennessee&rsquo;s <b>Fort Campbell</b> deployed troops to the
        Gulf War as part of Operation Desert Storm.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="27_us90_timeline",
    title="The Cold War Ends: Bush and a New World",
    kicker="Unit 10 &middot; US.90 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline lines up the events that ended the Cold War &mdash; from the wall&rsquo;s fall to the Soviet collapse "
         "&mdash; so students see how quickly the world reordered. "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four events on cards; sequence them by date before writing why each mattered.",
        extend="Being the &ldquo;sole superpower&rdquo; brought new responsibilities. Name one and explain it.",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>map</b> where each event happened."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.90 (labeled)",
)]
