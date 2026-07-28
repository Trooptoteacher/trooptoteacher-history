# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.66 The Vietnam War (timeline).
Five stages show the war's course: Geneva Accords -> Gulf of Tonkin -> Tet
Offensive -> Paris Peace Accords -> Fall of Saigon. Dates left, events right, as
FADED cues. HAS a Tennessee Connection. Content approved for US.66.
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
    ("1", "1954", "<b>Geneva Accords</b> split Vietnam at the 17th parallel after France&rsquo;s defeat; the South (U.S.&#8209;backed) later refuses reunification elections."),
    ("2", "Aug. 1964", "<b>Gulf of Tonkin Resolution</b> &mdash; after alleged attacks, Congress hands LBJ a &ldquo;blank check&rdquo; to escalate."),
    ("3", "1968", "The <b>Tet Offensive</b> &mdash; a coordinated North Vietnamese assault shakes U.S. confidence, even though it fails militarily."),
    ("4", "1973", "The <b>Paris Peace Accords</b> let the U.S. withdraw &mdash; Nixon&rsquo;s &ldquo;peace with honor.&rdquo;"),
    ("5", "1975", "<b>Fall of Saigon</b> &mdash; North Vietnam wins; the country is reunified under communism."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow the war&rsquo;s <b>course</b> from top (earliest) to bottom (latest). Write over the faint notes, then mark the moment American public opinion turned against the war.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">The course of the Vietnam War</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:150px;flex:0 0 150px;"></div>
          <div style="width:44px;flex:0 0 44px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; a reunified Vietnam</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee was deeply affected: <b>Fort Campbell&rsquo;s 101st Airborne</b>
        served multiple tours and took heavy casualties, and the 101st&rsquo;s assault on <b>Hamburger Hill (1969)</b>
        became one of the war&rsquo;s most controversial battles.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="27_us66_timeline",
    title="The Vietnam War: A Long Road to 1975",
    kicker="Unit 7 &middot; US.66 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline makes the war&rsquo;s long <b>course</b> visible &mdash; from a divided country to a &ldquo;blank check,&rdquo; a "
         "turning point, and finally withdrawal. "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the five stages on cards; have students <b>sequence</b> them before writing. Ask: which stage was the turning point?",
        extend="The Tet Offensive was a U.S. military win but a political loss. Explain that paradox using the timeline.",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>map</b> Vietnam&rsquo;s division at the 17th parallel."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.66 (labeled)",
)]
