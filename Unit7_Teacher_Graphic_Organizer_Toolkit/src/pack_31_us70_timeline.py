# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.70 Detente & the Fall of the Berlin Wall (timeline).
Five steps show tensions easing: Nixon's detente -> SALT I -> SALT II ->
Reagan-Gorbachev INF Treaty -> fall of the Berlin Wall. Dates left, events right,
as FADED cues. HAS a Tennessee Connection. A strong closer for the Cold War unit.
Content approved for US.70.
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
  .tl-date .well{ height:56px; }
  .tl-date .df{ position:absolute; top:8px; left:9px; right:9px; font-size:8.6pt; font-weight:800;
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
  .tl-event .well{ height:62px; }
  .tl-event .ef{ position:absolute; top:8px; left:12px; right:12px; font-size:8.3pt; font-style:italic;
       color:#9aa4b4; line-height:1.26; } .tl-event .ef b{ color:#7a8598; font-style:normal; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.4pt; line-height:1.28; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

_events = [
    ("1", "Early 1970s", "<b>Nixon&rsquo;s d&eacute;tente</b> &mdash; relaxed tensions through diplomacy; he also opens relations with <b>China</b> to pressure the USSR."),
    ("2", "1972", "<b>SALT I</b> &mdash; the first nuclear arms&#8209;control treaty; it caps missile deployments and adds verification."),
    ("3", "1979", "<b>SALT II</b> extends the limits &mdash; though Cold War tensions rise again late in the decade."),
    ("4", "1987", "<b>Reagan &amp; Gorbachev</b> sign the <b>INF Treaty</b>, eliminating an entire class of nuclear missiles."),
    ("5", "1989", "The <b>Berlin Wall falls</b> &mdash; the clearest sign the Cold War is ending."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow how tensions <b>eased</b> from top (earliest) to bottom (latest). Write over the faint notes, then mark the step where the Cold War&rsquo;s end became unmistakable.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">Tensions ease &rarr; the Cold War winds down</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:150px;flex:0 0 150px;"></div>
          <div style="width:44px;flex:0 0 44px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; the Cold War ends</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee&rsquo;s <b>Senator Howard Baker</b> shaped Cold War diplomacy:
        as <b>Senate Majority Leader</b> in the Reagan era he backed <b>arms&#8209;reduction treaties</b> and helped navigate
        d&eacute;tente&rsquo;s politics; he later served as U.S. Ambassador to Japan.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="31_us70_timeline",
    title="How the Cold War Wound Down",
    kicker="Unit 7 &middot; US.70 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline makes the thaw visible &mdash; a string of treaties and openings that lowered tensions step by step, "
         "until the Berlin Wall fell in 1989. "
         "<span class='cite'>Chronological reasoning &mdash; tracking change over time &mdash; is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the five steps on cards; have students <b>sequence</b> them. Ask: which was a treaty, and which was a symbol?",
        extend="Détente wasn&rsquo;t a straight line &mdash; tensions rose again in the late 1970s. Explain what still moved the Cold War toward its end.",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>draw</b> the Wall coming down."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.70 (labeled)",
)]
