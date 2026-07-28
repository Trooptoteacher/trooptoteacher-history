# -*- coding: utf-8 -*-
"""Unit 3 labeled best-fit organizer -- Comparison Matrix.
US.26: WWI home front. Three columns (Political | Economic | Social) held against
       three questions (What changed | A key example | Who was most affected).
       Required items seeded as faint hints in each cell.
TN tie: Nashville / Memphis / Chattanooga hubs; Red Cross & bond drives.
Neutral framing: wartime laws and dissent limits described factually; students
judge which change mattered most.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.82fr 1fr 1fr 1fr; grid-template-rows:auto 1fr 1fr 1fr; }
  .mx .corner{ background:transparent; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10.5pt; text-align:center; padding:7px 6px;
              border-radius:6px; display:flex; flex-direction:column; justify-content:center; background:var(--navy); }
  .mx .chead small{ font-weight:600; font-size:7.3pt; opacity:.9; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.4pt; padding:6px 9px;
              border-radius:6px; display:flex; flex-direction:column; justify-content:center; line-height:1.15; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule); border-radius:6px;
             background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
             background-position:0 30px; }
  .mx .cell .sh{ position:absolute; top:6px; left:9px; right:9px; font-size:7.6pt; font-style:italic;
                 color:#9aa4b4; line-height:1.28; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:8px 12px;
         font-size:9.2pt; color:var(--navy); } .cbar b{ color:var(--navy); }
"""

COLS = [
    ("Political", "government &amp; law"),
    ("Economic", "money &amp; mobilization"),
    ("Social", "people &amp; roles"),
]
# rows: (criterion label + subline, [political hint, economic hint, social hint])
ROWS = [
    ("What changed", "the big shift",
     ["Federal power expands; new limits on dissent.",
      "The economy mobilizes for total war.",
      "Roles at home begin to shift."]),
    ("A key example", "name the evidence",
     ["Committee on Public Information (George Creel); Espionage &amp; Sedition Acts; Schenck v. U.S. &mdash; a &ldquo;clear and present danger.&rdquo;",
      "Voluntary rationing (&ldquo;meatless / wheatless days&rdquo;); Liberty / war bonds; booming war industries.",
      "Women enter the workforce (fueling suffrage momentum); the Great Migration north."]),
    ("Who was most affected", "the people",
     ["War critics &amp; conscientious objectors.",
      "Households, farmers, and war workers.",
      "Women, African Americans, and other minorities."]),
]

def _grid():
    cells = ['<div class="corner"></div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for label, sub, hints in ROWS:
        cells.append(f'<div class="rhead">{label}<small style="font-weight:600;font-size:7.2pt;opacity:.9;font-style:italic;">{sub}</small></div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="sh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'

BODY = f"""
    <div class="prompt">Track how the war changed life at home across three fronts. Fill the <b>&ldquo;What changed&rdquo;</b> row across all three columns first, then work down &mdash; the faint hints are anchors, not the whole answer.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee&rsquo;s home front expanded military training facilities and war industries;
      <b>Nashville, Memphis, and Chattanooga</b> served as training and supply hubs, and Tennessee women organized Red Cross chapters and Liberty Bond drives statewide.</span>
    </div>
    <div class="cbar"><b>Synthesize:</b> Across all three fronts, how did World War I change life at home? ___________________________________________</div>
"""

_UDL = dict(
    scaffold="Fill the &ldquo;What changed&rdquo; row across all three columns first, then work down. Frame: &ldquo;On the ___ front, the war ___.&rdquo;",
    extend="Which change had the longest&#8209;lasting effect on American life? Defend it with evidence from the matrix.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, <b>draw</b> a symbol per cell, or <b>chart</b> it on the board.")

ORGANIZERS = [
    dict(
        slug="27_us26_matrix",
        title="The War Comes Home",
        kicker="Unit 3 &middot; US.26 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 3 &middot; Analyze", "skill")],
        why=("A three&#8209;column matrix holds the war&rsquo;s political, economic, and social ramifications against one set "
             "of questions, so students analyze change on the home front across every dimension at once. "
             "<span class='cite'>Structured comparison across criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.26 (labeled)",
    ),
]
