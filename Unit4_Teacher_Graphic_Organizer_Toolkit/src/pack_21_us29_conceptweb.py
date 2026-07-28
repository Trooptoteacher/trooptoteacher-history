# -*- coding: utf-8 -*-
"""Unit 4 labeled -- US.29 Radio, Movies & Popular Culture (concept web).
Center hub = "1920s POP CULTURE" as a faint watermark over writing lines. Four
spokes = radio, movies, celebrities, advertising & news -- each a LIGHT bubble
with a bold anchor label and a FADED italic content hint students write over. A
bottom LIGHT box captures how these built one national culture.
HAS a Tennessee Connection (gold chip + gold callout). Content approved for US.29.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10.2pt; color:var(--navy);
         line-height:1.04; text-align:center; }
  .node .nlab b{ color:var(--red); }
  .node .nsub{ font-size:7.3pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.16; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:12.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.02; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:20%; }
  .hub .hguides .nline{ border-bottom-color:#9aa6bd; margin-top:12px; }
  .synthbox{ flex:0 0 auto; margin-top:7px; display:flex; flex-direction:column; }
  .synthbox .band{ border-radius:6px 6px 0 0; }
  .synthbox .well{ min-height:64px; }
  .synthbox .fh{ position:absolute; top:7px; left:12px; right:12px; font-size:8pt; font-style:italic;
             color:#9aa6bd; line-height:1.4; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


# four spokes: (x%, y%, anchor label, faded content hint)
_outer = [
    (21, 20, "Radio", "60,000 sets (1922) &rarr; 10 million (1929); music, news, sports, drama"),
    (79, 20, "Movies", "silent films &rarr; &ldquo;talkies&rdquo; (<i>The Jazz Singer</i>, 1927); 50M weekly by 1929"),
    (21, 82, "Celebrities", "Chaplin&rsquo;s &ldquo;Tramp,&rdquo; Mary Pickford, Valentino; Lindbergh, 1927"),
    (79, 82, "Advertising &amp; News", "national brands &amp; ads; shared news reaching the whole country"),
]
_outer_html = "\n        ".join(_node(x, y, 206, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the new mass culture. On each bubble, write how that force grew popular culture &mdash; the faint notes are starters. Then answer the box below: how did these build <b>one</b> national culture?</div>
    <div class="canvas">
      <div class="web-wrap">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none">
          <g stroke="#C4CCDA" stroke-width="0.7">
            <line x1="50" y1="50" x2="21" y2="20"/>
            <line x1="50" y1="50" x2="79" y2="20"/>
            <line x1="50" y1="50" x2="21" y2="82"/>
            <line x1="50" y1="50" x2="79" y2="82"/>
          </g>
        </svg>
        {_outer_html}
        <div class="node hub" style="left:50%; top:51%; width:210px; height:150px;">
          <div class="hcue">1920s<br/>Pop&nbsp;Culture</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did radio &amp; film create <b>one</b> shared national culture?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">the same songs, stars, ads &amp; news reached millions at once &nbsp;&middot;&nbsp; people far apart now shared references &nbsp;&middot;&nbsp; advertising tied it to buying</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee sat at the center of the radio revolution:
        <b>WSM Radio</b> launched in <b>Nashville in 1925</b>, and its <b>Grand Ole Opry</b> became the
        longest&#8209;running radio program in American history.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us29_conceptweb",
    title="How Radio &amp; Movies Made a National Culture",
    kicker="Unit 4 &middot; US.29 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2 &middot; Describe", "skill")],
    why=("A web shows radio, film, celebrity, and advertising as one system feeding a brand&#8209;new mass culture &mdash; "
         "and how ideas link back to a single hub. "
         "<span class='cite'>Surfacing prior knowledge and connecting ideas builds SSP.01 (collect information).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four bubble labels as a word bank and fill one together. Ask: which reached the <b>most</b> people?",
        extend="Draw links <b>between</b> bubbles &mdash; e.g., how did advertising connect to radio and to movies?",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> an icon for each part of pop culture."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.29 (labeled)",
)]
