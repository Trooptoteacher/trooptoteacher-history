# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.86 The Watergate Scandal (timeline).
Five stages: the break-in -> the cover-up -> the press & the hearings -> United
States v. Nixon -> resignation & pardon. Dates left, events right, as FADED cues.
Strong Tennessee tie (Howard Baker). Content approved for US.86.
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
  .tl-date .well{ height:52px; }
  .tl-date .df{ position:absolute; top:7px; left:9px; right:9px; font-size:8.5pt; font-weight:800;
       color:#8ea0c4; line-height:1.13; text-align:center; }
  .tl-spine{ width:44px; flex:0 0 44px; position:relative; }
  .tl-spine::before{ content:''; position:absolute; left:50%; top:0; bottom:0; width:5px;
    background:var(--navy); transform:translateX(-50%); }
  .tl-dot{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
    width:30px; height:30px; border-radius:50%; background:var(--gold); border:3px solid var(--navy);
    color:var(--navy); font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; z-index:2; }
  .tl-row:first-child .tl-spine::before{ top:50%; }
  .tl-row:last-child .tl-spine::before{ bottom:50%; }
  .tl-event{ flex:1 1 auto; align-self:center; position:relative; }
  .tl-event .well{ height:58px; }
  .tl-event .ef{ position:absolute; top:7px; left:12px; right:12px; font-size:8.2pt; font-style:italic;
       color:#9aa4b4; line-height:1.25; } .tl-event .ef b{ color:#7a8598; font-style:normal; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.4pt; line-height:1.28; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

_events = [
    ("1", "June 1972", "<b>The break&#8209;in</b> &mdash; five men are caught inside Democratic headquarters at the Watergate complex."),
    ("2", "1972&ndash;73", "<b>The cover&#8209;up</b> &mdash; the trail leads to Nixon&rsquo;s campaign (CREEP) &amp; the White House; the cover&#8209;up proves worse than the crime."),
    ("3", "1973", "<b>Press &amp; hearings</b> &mdash; Woodward &amp; Bernstein follow the money; televised Senate hearings hold power to account."),
    ("4", "1974", "<b>United States v. Nixon</b> &mdash; a unanimous Court: executive privilege can&rsquo;t hide evidence; <b>no one is above the law</b>."),
    ("5", "Aug 1974", "<b>Resignation</b> &mdash; Nixon resigns rather than face impeachment; President Ford later pardons him."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow the scandal from top (earliest) to bottom (latest). On each line, write <b>what happened</b> and <b>why it mattered</b> &mdash; the faint notes are starters. Watch how a small break&#8209;in became a constitutional crisis.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">From a burglary to a resignation</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:150px;flex:0 0 150px;"></div>
          <div style="width:44px;flex:0 0 44px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; a limit on presidential power</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee Senator <b>Howard Baker</b> served as <b>vice chairman of the
        Senate Watergate Committee</b>. His question in the televised hearings &mdash; <i>&ldquo;What did the President know, and
        when did he know it?&rdquo;</i> &mdash; made him a national figure.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="23_us86_timeline",
    title="Watergate: How a Break-In Toppled a President",
    kicker="Unit 10 &middot; US.86 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline shows the chain from burglary to cover&#8209;up to court ruling to resignation &mdash; and why the "
         "cover&#8209;up, not the crime, brought Nixon down. "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the five stages on cards; sequence them by date before writing why each mattered.",
        extend="<i>United States v. Nixon</i> said no one is above the law. Explain why that ruling still matters today.",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>diagram</b> how the cover&#8209;up unraveled."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.86 (labeled)",
)]
