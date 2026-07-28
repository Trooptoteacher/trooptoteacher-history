# -*- coding: utf-8 -*-
"""Unit 8 labeled -- US.76 Youth Culture & Tennessee Music (timeline).
Five stages show the progression of popular music: swing -> rhythm & blues ->
Sun Studio -> rock 'n' roll -> music breaking racial barriers. Beatnik youth
culture framed as context. Dates/eras left, events right, as FADED cues. Strong
Tennessee tie (Sun Records, Memphis). Content approved for US.76.
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
    ("1", "1930s&ndash;40s", "<b>Swing</b> &mdash; big&#8209;band dance music is the mainstream sound the boomers&rsquo; parents grew up on."),
    ("2", "Late 1940s&ndash;50s", "<b>Rhythm &amp; blues</b> &mdash; African American music from Memphis&rsquo;s <b>Beale Street</b>; <b>Stax Records</b> &amp; B.B. King."),
    ("3", "Memphis, 1950s", "<b>Sun Studio</b> &mdash; Sam Phillips blends country &amp; blues into a bold new sound."),
    ("4", "Mid&#8209;1950s", "<b>Rock &rsquo;n&rsquo; roll</b> &mdash; Elvis (recorded at Sun) carries Black musical styles to white audiences."),
    ("5", "1950s&ndash;60s", "<b>Music breaks racial barriers</b> &mdash; shared songs integrate naturally, challenging segregation."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Follow the <b>progression</b> of popular music from top (earliest) to bottom (latest). Write over the faint notes. <i>Context:</i> a rebellious youth culture &mdash; the <b>beatniks</b> (Kerouac, Ginsberg) &mdash; rejected 1950s conformity right alongside this musical revolution.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest</div>
          <div class="sp"></div>
          <div class="lbl">From swing to rock &rsquo;n&rsquo; roll</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow" style="display:flex;">
          <div style="width:150px;flex:0 0 150px;"></div>
          <div style="width:44px;flex:0 0 44px;display:flex;justify-content:center;"><div class="arr-d"></div></div>
          <div style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; a new American sound</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Memphis&rsquo;s <b>Sun Records</b> and producer <b>Sam Phillips</b> launched
        <b>Elvis Presley, Johnny Cash, Carl Perkins, and Jerry Lee Lewis</b> &mdash; the artists who defined the leap from
        country and blues to rock &rsquo;n&rsquo; roll &mdash; while Nashville&rsquo;s Grand Ole Opry kept shaping country music nationwide.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="25_us76_timeline",
    title="How Tennessee Invented a New Sound",
    kicker="Unit 8 &middot; US.76 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline makes the <b>progression</b> visible &mdash; how swing gave way to rhythm &amp; blues and then rock "
         "&rsquo;n&rsquo; roll, much of it recorded in Tennessee. "
         "<span class='cite'>Chronological reasoning &mdash; tracking change over time &mdash; is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the five stages on cards; sequence them by listening to a short clip of each style before writing.",
        extend="How did music break racial barriers before the law did? Use stages 2&ndash;5 to defend your answer.",
        show="Students may <b>write</b>, <b>say</b> the sequence aloud, or <b>play</b> a sample of each style along the line."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 8 &middot; US.76 (labeled)",
)]
