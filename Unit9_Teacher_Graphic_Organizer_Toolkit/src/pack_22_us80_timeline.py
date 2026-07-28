# -*- coding: utf-8 -*-
"""Unit 9 labeled -- US.80 Significant Civil Rights Events (timeline).
Six milestones in order: Montgomery Bus Boycott -> Clinton HS -> Little Rock Nine
-> Nashville Sit-ins & Tent City -> Freedom Riders -> Birmingham & March on
Washington. Tennessee events (Clinton, Nashville, Fayette County) are central.
Dates left, events right, as FADED cues. Strong Tennessee tie. Approved for US.80.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .tl{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .tl-ends{ display:flex; align-items:center; gap:10px; flex:0 0 auto; margin-bottom:1px; }
  .tl-ends .sp{ width:40px; flex:0 0 40px; text-align:center; }
  .tl-ends .lbl{ font-size:7.6pt; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); }
  .tl-ends .lbl.d{ width:132px; flex:0 0 132px; text-align:center; }
  .tl-row{ flex:1 1 0; display:flex; align-items:stretch; gap:10px; min-height:0; }
  .tl-date{ width:132px; flex:0 0 132px; align-self:center; position:relative; }
  .tl-date .well{ height:44px; }
  .tl-date .df{ position:absolute; top:6px; left:8px; right:8px; font-size:8.1pt; font-weight:800;
       color:#8ea0c4; line-height:1.1; text-align:center; }
  .tl-spine{ width:40px; flex:0 0 40px; position:relative; }
  .tl-spine::before{ content:''; position:absolute; left:50%; top:0; bottom:0; width:5px;
    background:var(--navy); transform:translateX(-50%); }
  .tl-dot{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
    width:27px; height:27px; border-radius:50%; background:var(--gold); border:3px solid var(--navy);
    color:var(--navy); font-weight:800; font-size:11pt; display:flex; align-items:center; justify-content:center; z-index:2; }
  .tl-row:first-child .tl-spine::before{ top:50%; }
  .tl-row:last-child .tl-spine::before{ bottom:50%; }
  .tl-event{ flex:1 1 auto; align-self:center; position:relative; }
  .tl-event .well{ height:50px; }
  .tl-event .ef{ position:absolute; top:6px; left:11px; right:11px; font-size:8pt; font-style:italic;
       color:#9aa4b4; line-height:1.22; } .tl-event .ef b{ color:#7a8598; font-style:normal; }
  .tl-event .ef .tn{ color:#b8860b; font-style:normal; font-weight:800; }
  .tnbox{ flex:0 0 auto; margin-top:5px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.3pt; line-height:1.26; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

_events = [
    ("1", "1955&ndash;56", "<b>Montgomery Bus Boycott</b> &mdash; sparked by Rosa Parks; 381 days; elevates Dr. King."),
    ("2", "1956", "<span class=\"tn\">&#9733; TN &mdash;</span> <b>Clinton High School</b> is the first Southern high school to integrate; the Clinton 12 need Guard protection."),
    ("3", "1957", "<b>Little Rock Nine</b> &mdash; Gov. Faubus defies the court until President Eisenhower sends federal troops."),
    ("4", "1960", "<span class=\"tn\">&#9733; TN &mdash;</span> <b>Nashville sit&#8209;ins</b> (Diane Nash, John Lewis) desegregate lunch counters; <b>Tent City</b>, Fayette County shelters evicted would&#8209;be voters."),
    ("5", "1961", "<b>Freedom Riders</b> test desegregation rulings on interstate buses &mdash; and face firebombings &amp; beatings."),
    ("6", "1963", "<b>Birmingham Campaign</b> &amp; the <b>March on Washington</b> &mdash; 250,000 hear &ldquo;I Have a Dream.&rdquo;"),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow the movement from top (earliest) to bottom (latest). On each line, write <b>what happened</b> and <b>why it mattered</b> &mdash; the faint notes are starters. Three of these six events happened right here in Tennessee.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">The struggle to secure civil rights</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:132px;flex:0 0 132px;"></div>
          <div style="width:40px;flex:0 0 40px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:7.6pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; toward landmark legislation</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Nashville sit&#8209;ins</b> of 1960 &mdash; led by students including
        <b>Diane Nash</b> and <b>John Lewis</b> of Fisk University &mdash; were among the most organized of the whole movement.
        They desegregated Nashville&rsquo;s lunch counters and became a model copied nationwide.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="22_us80_timeline",
    title="The Movement, Step by Step",
    kicker="Unit 9 &middot; US.80 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline shows how one victory built on the last &mdash; boycott to sit&#8209;in to march &mdash; and puts "
         "Tennessee&rsquo;s Clinton, Nashville, and Fayette County events in the national story. "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the six events on cards; sequence them by date before writing why each mattered.",
        extend="Pick the event you think mattered most and defend it &mdash; did it change law, minds, or momentum?",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>map</b> where each event happened."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 9 &middot; US.80 (labeled)",
)]
