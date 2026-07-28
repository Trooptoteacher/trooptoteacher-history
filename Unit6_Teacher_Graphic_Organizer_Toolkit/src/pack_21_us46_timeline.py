# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.46 FDR's Response to World Crises (timeline).
Five dated steps show America moving from isolationism toward involvement:
Neutrality Acts -> Quarantine Speech -> Four Freedoms -> Lend-Lease -> Atlantic
Charter. Each row pre-loads the date (left) and the event (right) as FADED cues
students trace/write over. Neutral framing. No TN tie in source. Approved US.46.
"""

CSS = r"""
  .tl{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .tl-ends{ display:flex; align-items:center; gap:10px; flex:0 0 auto; margin-bottom:2px; }
  .tl-ends .sp{ width:44px; flex:0 0 44px; text-align:center; }
  .tl-ends .lbl{ font-size:8pt; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); }
  .tl-ends .lbl.d{ width:150px; flex:0 0 150px; text-align:center; }
  .tl-row{ flex:1 1 0; display:flex; align-items:stretch; gap:10px; min-height:0; }
  .tl-date{ width:150px; flex:0 0 150px; align-self:center; position:relative; }
  .tl-date .well{ height:60px; }
  .tl-date .df{ position:absolute; top:8px; left:9px; right:9px; font-size:8.4pt; font-weight:800;
       font-style:normal; color:#8ea0c4; line-height:1.14; text-align:center; }
  .tl-spine{ width:44px; flex:0 0 44px; position:relative; }
  .tl-spine::before{ content:''; position:absolute; left:50%; top:0; bottom:0; width:5px;
    background:var(--navy); transform:translateX(-50%); }
  .tl-dot{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%);
    width:30px; height:30px; border-radius:50%; background:var(--gold); border:3px solid var(--navy);
    color:var(--navy); font-weight:800; font-size:12pt; display:flex; align-items:center; justify-content:center; z-index:2; }
  .tl-row:first-child .tl-spine::before{ top:50%; }
  .tl-row:last-child .tl-spine::before{ bottom:50%; }
  .tl-event{ flex:1 1 auto; align-self:center; position:relative; }
  .tl-event .well{ height:68px; }
  .tl-event .ef{ position:absolute; top:8px; left:12px; right:12px; font-size:8.3pt; font-style:italic;
       color:#9aa4b4; line-height:1.26; } .tl-event .ef b{ color:#7a8598; font-style:normal; }
  .tl-arrow{ display:flex; flex:0 0 auto; }
  .tl-arrow .sp{ width:44px; flex:0 0 44px; display:flex; justify-content:center; }
  .tl-arrow .lbl{ width:150px; flex:0 0 150px; }
"""

# (n, date, event hint)
_events = [
    ("1", "Neutrality Acts<br>1935&ndash;1937", "<b>Isolationism.</b> Laws aim to keep the U.S. out of foreign wars &mdash; the mood FDR had to work against."),
    ("2", "Quarantine Speech<br>Oct.&nbsp;5, 1937", "FDR calls aggressor nations a <b>disease</b> peaceful nations should &ldquo;quarantine&rdquo; &mdash; his first break from isolationism."),
    ("3", "Four Freedoms<br>Jan.&nbsp;6, 1941", "Speech, worship, freedom from <b>want</b>, freedom from <b>fear</b> &mdash; the moral case for what America would fight for."),
    ("4", "Lend&#8209;Lease Act<br>March 1941", "The &ldquo;<b>arsenal of democracy</b>&rdquo; &mdash; the U.S. lends arms &amp; supplies to Britain and the Allies."),
    ("5", "Atlantic Charter<br>Aug.&nbsp;14, 1941", "FDR &amp; Churchill set <b>post&#8209;war aims</b> &mdash; no territorial gain, self&#8209;determination, a freer world."),
]

def _row(n, date, ev):
    return f"""
      <div class="tl-row">
        <div class="tl-date"><div class="well top navy"></div><div class="df">{date}</div></div>
        <div class="tl-spine"><div class="tl-dot">{n}</div></div>
        <div class="tl-event"><div class="well top lines"></div><div class="ef">{ev}</div></div>
      </div>"""

BODY = r"""
    <div class="prompt">Read the five steps from <b>earliest</b> (top) to <b>latest</b> (bottom). The date is on the <b>left</b>, the event on the <b>right</b> &mdash; write over the faint notes, then mark where America shifts from <b>staying out</b> to <b>helping the Allies</b>.</div>
    <div class="canvas">
      <div class="tl">
        <div class="tl-ends">
          <div class="lbl d">&#9650;&nbsp; Earliest &middot; isolationism</div>
          <div class="sp"></div>
          <div class="lbl">FDR moves the U.S. toward involvement</div>
        </div>
""" + "".join(_row(n, d, e) for n, d, e in _events) + r"""
        <div class="tl-arrow">
          <div class="lbl"></div>
          <div class="sp"><div class="arr-d"></div></div>
          <div class="lbl" style="font-size:8pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);align-self:center;">Latest &middot; on the brink of war</div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us46_timeline",
    title="From Neutral to the Arsenal of Democracy",
    kicker="Unit 6 &middot; US.46 &middot; Best&#8209;Fit Organizer",
    chips=[("Timeline &middot; Change Over Time", "navy"), ("DOK 2 &middot; Chronology", "skill")],
    why=("A timeline makes the <b>sequence</b> visible &mdash; each step moves the U.S. a little further from isolationism "
         "toward aiding the Allies, well before Pearl Harbor. "
         "<span class='cite'>Chronological reasoning &mdash; ordering events and tracking change &mdash; is TN Social "
         "Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the five events on cards; have students <b>sequence</b> them before writing. Ask: which one was the biggest step toward war?",
        extend="Between which two steps did America change the most? Explain what caused the shift.",
        show="Students may <b>write</b> the events, <b>say</b> the sequence aloud, or <b>build</b> the line with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.46 (labeled)",
)]
