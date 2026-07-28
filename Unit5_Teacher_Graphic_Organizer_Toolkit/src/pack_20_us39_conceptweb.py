# -*- coding: utf-8 -*-
"""Unit 5 labeled -- US.39 Causes of the Great Depression (concept web).
Center hub = "THE GREAT DEPRESSION" as a faint watermark over writing lines. Four
spokes group the nine named causes into families (financial collapse, overproduction
& easy credit, policy failures, weak consumer base) -- each a LIGHT bubble with a
bold anchor label and a FADED italic hint students write over. A bottom LIGHT box
captures the cascade. HAS a Tennessee Connection. Content approved for US.39.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .web-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .web-wrap > svg{ position:absolute; inset:0; width:100%; height:100%; }
  .node{ position:absolute; transform:translate(-50%,-50%);
         display:flex; flex-direction:column; align-items:stretch; justify-content:flex-start;
         background:var(--paper); border:2px solid var(--navy); border-radius:16px; padding:6px 12px 8px; }
  .node .nlab{ font-family:Georgia,serif; font-weight:700; font-size:10pt; color:var(--navy);
         line-height:1.04; text-align:center; }
  .node .nsub{ font-size:7.3pt; font-style:italic; color:#9aa6bd; text-align:center; line-height:1.16; margin-top:3px; }
  .node .nline{ border-bottom:1.4px dashed #C4CCDA; height:0; margin-top:9px; }
  .hub{ background:var(--navy-tint); border:3px solid var(--navy); border-radius:50%;
        align-items:center; justify-content:center; padding:0; }
  .hub .hcue{ font-family:Georgia,serif; font-weight:700; font-size:11.5pt; color:#97a2ba;
              letter-spacing:.02em; text-align:center; line-height:1.04; text-transform:uppercase; }
  .hub .hguides{ position:absolute; left:14%; right:14%; bottom:19%; }
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
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""


def _node(x, y, w, h, lab, sub):
    return (f'<div class="node" style="left:{x}%; top:{y}%; width:{w}px; height:{h}px;">'
            f'<div class="nlab">{lab}</div><div class="nsub">{sub}</div>'
            f'<div class="nline"></div><div class="nline"></div></div>')


# four grouped-cause spokes: (x%, y%, anchor label, faded content hint)
_outer = [
    (21, 20, "Financial Collapse", "bank failures (9,000+, no FDIC); buying on margin; the Crash, Oct.&nbsp;1929"),
    (79, 20, "Overproduction &amp; Easy Credit", "factories &amp; farms made more than people could buy; heavy borrowing"),
    (21, 82, "Policy Failures", "Smoot&#8209;Hawley Tariff (1930) &rarr; trade fell 25%; laissez&#8209;faire"),
    (79, 82, "Weak Consumer Base", "income inequality; farm prices down 60%; rising unemployment"),
]
_outer_html = "\n        ".join(_node(x, y, 214, 96, lab, sub) for x, y, lab, sub in _outer)

BODY = f"""
    <div class="prompt">The hub is the Depression. On each bubble, write how that family of causes helped bring it on &mdash; the faint notes are starters. Then answer the box below: how did the causes <b>feed one another</b>?</div>
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
        <div class="node hub" style="left:50%; top:51%; width:212px; height:150px;">
          <div class="hcue">The Great<br/>Depression</div>
          <div class="hguides"><div class="nline"></div><div class="nline"></div></div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did these causes <b>cascade</b> &mdash; one failure triggering the next?</div>
        <div class="well lines" style="position:relative;">
          <span class="fh">a bank fails &rarr; savings vanish &rarr; loans stop &rarr; spending falls &rarr; more businesses &amp; banks fail &rarr; unemployment rises</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Caldwell and Company</b> empire &mdash; based in
        <b>Nashville</b> and once the largest investment bank in the South &mdash; collapsed in
        <b>November 1930</b>, wiping out thousands of Tennesseans&rsquo; savings and triggering a cascade of
        bank failures across the region.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="20_us39_conceptweb",
    title="What Caused the Great Depression?",
    kicker="Unit 5 &middot; US.39 &middot; Best&#8209;Fit Organizer",
    chips=[("Concept Web", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("No single cause brought on the Depression. A web groups the many causes into families around one hub &mdash; "
         "then shows how they fed each other into a cascade. "
         "<span class='cite'>Tracing multiple, interacting causes is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give the four family labels as a word bank; sort a list of causes into the right bubble together first.",
        extend="Which cause do you think mattered most? Draw arrows <b>between</b> bubbles to show the cascade.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>draw</b> the domino chain of causes."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; US.39 (labeled)",
)]
