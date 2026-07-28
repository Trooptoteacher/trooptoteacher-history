# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.62 The Korean War (timeline).
Five stages show the war's course: divided at the 38th parallel -> North invades ->
Inchon landing -> Chinese entry -> armistice near the 38th parallel. Dates left,
events right, as FADED cues students trace over. HAS a Tennessee Connection.
Content approved for US.62.
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
    ("1", "After WWII", "Korea is split at the <b>38th parallel</b> &mdash; USSR occupies the North, the U.S. the South."),
    ("2", "June 1950", "<b>North Korea invades</b> the South; UN forces are pushed back to the Pusan perimeter."),
    ("3", "Sept. 1950", "<b>Inchon landing</b> &mdash; MacArthur&rsquo;s surprise attack turns the tide and pushes North."),
    ("4", "Oct.&ndash;Nov. 1950", "<b>China enters</b> &mdash; 300,000 &ldquo;volunteers&rdquo; force a UN retreat; the war becomes a stalemate."),
    ("5", "1953", "<b>Armistice</b> &mdash; the line settles near the 38th parallel; 36,000+ U.S. deaths; Korea stays divided."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow the war&rsquo;s <b>course</b> from top (earliest) to bottom (latest). Write over the faint notes, then notice the ending: after three years, the border was almost exactly where it started.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">The course of the Korean War</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:150px;flex:0 0 150px;"></div>
          <div style="width:44px;flex:0 0 44px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; a divided Korea</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Thousands of Tennesseans served in Korea. <b>Fort Campbell&rsquo;s
        187th Airborne</b> made combat jumps at Sukchon and Munsan&#8209;ni, and Tennessee&rsquo;s Korean War veterans are
        memorialized at the <b>War Memorial Building in Nashville</b>.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="23_us62_timeline",
    title="The Korean War: Back Where It Started",
    kicker="Unit 7 &middot; US.62 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline makes the war&rsquo;s <b>course</b> visible &mdash; and drives home why it&rsquo;s called a stalemate: after "
         "three years and heavy losses, the border barely moved. "
         "<span class='cite'>Chronological reasoning is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the five stages on cards; have students <b>sequence</b> them before writing. Ask: where did the tide turn twice?",
        extend="Was Korea a win, a loss, or a draw for the U.S.? Use the ending to defend your answer.",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>map</b> the front line moving up and down Korea."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.62 (labeled)",
)]
