# -*- coding: utf-8 -*-
"""Unit 3 labeled best-fit organizers, one per standard (GC.35, GC.10-GC.15).
Topics verbatim from the TN GC standards + instructional targets. Writable areas
light; seeded prompts are questions. Best-fit: GC.35 Venn, GC.10 Matrix,
GC.11 Cause&Effect, GC.12 T-chart, GC.13 Sequence, GC.14 Concept web,
GC.15 Main Idea & Details.
"""
from common import venn2, matrix, cause_effect_chain, tchart, concept_web, main_idea

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role); d.update(kw); return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; {std} (labeled)"
def KICK(std): return f"Unit 3 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.35 — Citizenship -> Venn
  _o("20_gc35_venn", "Natural-Born <span style='font-family:Georgia;font-style:italic;font-size:15pt'>vs.</span> Naturalized Citizens",
     KICK("GC.35"),
     [("Venn &middot; Compare Two", "navy"), ("DOK 2 &middot; Compare", "skill")],
     "Both are full U.S. citizens &mdash; but they arrive by different paths, and only one may become President. A Venn "
     "makes the shared rights and the key differences visible at once. "
     "<span class='cite'>Comparing to find shared vs. distinct traits is Marzano&rsquo;s highest-yield move.</span>",
     venn2("Sort each trait: only a natural-born citizen, only a naturalized citizen, or true of <b>both</b>.",
           "NATURAL-BORN", "citizen at birth", "NATURALIZED", "citizen by legal process",
           ["citizen at birth?", "may be President?"],
           ["took the Oath?", "passed the civics test?"],
           ["full rights?", "can vote &amp; serve on a jury?"],
           cap_a="NATURAL-BORN", cap_b="NATURALIZED", cap_both="BOTH"),
     dict(scaffold="Give a card set of traits to sort into the three regions before writing.",
          extend="Explain why the Framers required the President to be a natural-born citizen.", show=_SHOW),
     ROLE("GC.35")),

  # GC.10 — Article I & 17th -> Matrix
  _o("21_gc10_matrix", "House <span style='font-family:Georgia;font-style:italic;font-size:15pt'>vs.</span> Senate",
     KICK("GC.10"),
     [("Matrix &middot; Compare Two Chambers", "navy"), ("DOK 2 &middot; Analyze", "skill")],
     "Congress is bicameral by design. Holding the two chambers to the same questions makes the Framers&rsquo; choices &mdash; "
     "and the 17th Amendment&rsquo;s change &mdash; pop. "
     "<span class='cite'>Structured comparison against one yardstick is Marzano&rsquo;s highest-yield strategy.</span>",
     matrix("Fill each cell from Article I and the 17th Amendment; then read down each column for the pattern.",
            [("HOUSE", "chosen every 2 years", "navy"), ("SENATE", "6-year terms", "red")],
            [("Term length", ["", ""]), ("Minimum age", ["", ""]),
             ("Citizenship req.", ["", ""]), ("How elected (incl. 17th Am.)", ["", ""])],
            "<b>Pattern:</b> What does the design of the two chambers tell you about the Framers&rsquo; goals? ______________________"),
     dict(scaffold="Pre-fill the House column together; students complete the Senate column.",
          extend="Explain the significance of the 17th Amendment for how senators answer to voters.", show=_SHOW),
     ROLE("GC.10")),

  # GC.11 — Census/redistricting/Baker v Carr -> Cause & Effect chain
  _o("22_gc11_causeeffect", "From Census to &ldquo;One Person, One Vote&rdquo;",
     KICK("GC.11"),
     [("Cause &amp; Effect &middot; Chain", "red"), ("SSP.05 &middot; DOK 3", "skill")],
     "The census sets off a chain that ends in how much your vote is worth. Tracing it &mdash; through Tennessee&rsquo;s own "
     "Baker v. Carr &mdash; shows why redistricting is a fight worth having. "
     "<span class='cite'>Cause-and-effect reasoning is TN Practice SSP.05.</span>",
     cause_effect_chain(
       "Work down the chain: what each step sets in motion.",
       [("The Census (every 10 years)", "&mdash; what does the constitutional count measure?"),
        ("Apportionment", "&mdash; how are the 435 House seats split among the states?"),
        ("Redistricting", "&mdash; who redraws the lines within a state, and how can gerrymandering tilt them?"),
        ("Baker v. Carr (1962)", "&mdash; how did a Tennessee lawsuit lead to &lsquo;one person, one vote&rsquo;?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>So what?</b> How can drawing lines change who wins '
             'without changing a single vote? ____________________________________</div>')),
     dict(scaffold="Provide the four steps on cards; students order them, then add one effect each.",
          extend="Explain how population shifts to cities changed Tennessee&rsquo;s representation before Baker v. Carr.", show=_SHOW),
     ROLE("GC.11")),

  # GC.12 — Leadership -> T-chart
  _o("23_gc12_tchart", "Leadership of the Two Houses",
     KICK("GC.12"),
     [("T&#8209;Chart &middot; Two Chambers", "navy"), ("DOK 2 &middot; Organize", "skill")],
     "Party leadership decides which bills move. Laying the House and Senate side by side shows students who holds the "
     "gavel &mdash; and who chose them. "
     "<span class='cite'>Organizing information to reveal structure builds TN Practice SSP.01.</span>",
     tchart("List each chamber&rsquo;s leaders and how each is chosen.",
            "HOUSE LEADERSHIP", "majority party leads", "SENATE LEADERSHIP", "VP presides; party leaders steer",
            [("Speaker of the House", "who chooses the Speaker, and what do they control?"),
             ("Majority / Minority Leaders", "how do the party floor leaders differ?")],
            [("President of the Senate (VP)", "when does the VP actually vote?"),
             ("President pro tempore", "who traditionally holds this post?")],
            "<b>Judge it:</b> Which leadership position holds the most power over what becomes law &mdash; and why? ______________________"),
     dict(scaffold="Give the position names on cards; students place each under the correct chamber first.",
          extend="Explain why the Speaker is second in line to the presidency.", show=_SHOW),
     ROLE("GC.12")),

  # GC.13 — Bill to law -> Sequence
  _o("24_gc13_sequence", "How a Bill Becomes a Law",
     KICK("GC.13"),
     [("Sequence &middot; Process Flow", "red"), ("SSP.05 &middot; DOK 2", "skill")],
     "A bill&rsquo;s path is a gauntlet of checks. Mapping the flow &mdash; and where the House and Senate differ &mdash; shows "
     "students why most bills never make it. "
     "<span class='cite'>Sequencing a process builds chronological reasoning (SSP.05).</span>",
     cause_effect_chain(
       "Work down the process. Note where the House and Senate rules differ.",
       [("Introduction &amp; Committee", "&mdash; who introduces a bill, and why do most bills die here?"),
        ("Floor debate", "&mdash; House Rules Committee limits debate; the Senate allows the filibuster (ended by cloture) &mdash; how do they differ?"),
        ("Both chambers pass identical text", "&mdash; how does a conference committee reconcile differences?"),
        ("Presented to the President", "&mdash; sign, or veto? How can Congress override a veto?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>Weigh it:</b> Is it too hard for a bill to become law, '
             'or is the difficulty the point? ____________________________________</div>')),
     dict(scaffold="Provide the stages on cards; students order them, then mark the House/Senate difference.",
          extend="Explain how the filibuster and cloture change a bill&rsquo;s odds in the Senate.", show=_SHOW),
     ROLE("GC.13")),

  # GC.14 — TN delegation -> Concept web
  _o("25_gc14_conceptweb", "My Voice in Congress",
     KICK("GC.14"),
     [("Concept Web &middot; Locate &amp; Connect", "navy"), ("SSP.06 &middot; DOK 2", "skill")],
     "Representation is only real if you can name and reach the people who hold it. This organizer turns an abstract "
     "delegation into <em>your</em> senators, <em>your</em> representative, and <em>your</em> district. "
     "<span class='cite'>Locating oneself in place and scale builds TN geographic Practice SSP.06.</span>",
     concept_web("Fill each bubble with a real name, number, or fact about who represents you.",
                 "MY VOICE / IN CONGRESS",
                 ["U.S. Senator (TN) #1", "U.S. Senator (TN) #2", "My U.S. Representative",
                  "My congressional district #", "How to contact them", "A current issue I care about"]),
     dict(scaffold="Model finding one senator together using an official directory before students research the rest.",
          extend="Write a one-paragraph message to a representative about the current issue you named.", show=_SHOW),
     ROLE("GC.14")),

  # GC.15 — Powers of Congress -> Main Idea & Details
  _o("26_gc15_mainidea", "The Powers of Congress",
     KICK("GC.15"),
     [("Main Idea &amp; Details", "navy"), ("SSP.02 &middot; DOK 3", "skill")],
     "Congress&rsquo;s power comes in two kinds &mdash; the listed and the implied. Separating them, then anchoring the implied "
     "in McCulloch v. Maryland, shows students where federal power actually comes from. "
     "<span class='cite'>Distinguishing central idea from supporting detail builds disciplinary literacy (SSP.02).</span>",
     main_idea(
       "Main idea: where Congress&rsquo;s power comes from. Fill each column with examples.",
       "CONGRESS&rsquo;S POWER &mdash; Article I, Section 8",
       [("Enumerated (listed)", "tax? borrow? commerce? war?"),
        ("Implied (Necessary &amp; Proper)", "what&rsquo;s the &lsquo;Elastic Clause&rsquo; for?"),
        ("McCulloch v. Maryland (1819)", "how did Marshall expand implied power?")],
       "<b>In one sentence:</b> Do implied powers make Congress too strong, or are they necessary to govern? ______________________"),
     dict(scaffold="Give three enumerated powers to place first; then students add implied powers and the case.",
          extend="Explain how &lsquo;the power to tax involves the power to destroy&rsquo; shaped the McCulloch ruling.", show=_SHOW),
     ROLE("GC.15")),
]
