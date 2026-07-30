# -*- coding: utf-8 -*-
"""Unit 1 labeled best-fit organizers, one per standard GC.01-GC.09.
Every topic, name, date, and statute is drawn VERBATIM from
05_STANDARDS_ALIGNMENT/government_standards_source.json (TN GC standards +
instructional-guide 'I can' targets). Nothing is invented. Writable areas stay
light; seeded prompts are questions, not asserted facts, so students supply the
content. GC.06 is a Venn because the 'I can' explicitly says to plot federal /
reserved / concurrent powers on a Venn; GC.08 carries the T.C.A. sec. 49-6-1028
star flag (this instruction is legally required in Tennessee).
"""
from common import (venn2, tchart, matrix, cause_effect_chain, concept_web,
                    main_idea)

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role)
    d.update(kw)
    return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; {std} (labeled)"
def KICK(std): return f"Unit 1 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.01 — Enlightenment roots -> concept web
  _o("20_gc01_conceptweb",
     "Roots of American Government",
     KICK("GC.01"),
     [("Concept Web &middot; Connect Ideas", "navy"), ("DOK 2&ndash;3 &middot; Synthesis", "skill")],
     "The Framers borrowed from Enlightenment thinkers and classical models. A concept web lets students gather those "
     "influences around one hub &mdash; the <b>social contract</b> and the purpose of government. "
     "<span class='cite'>Synthesizing multiple sources builds TN Practice SSP.03.</span>",
     concept_web("In each bubble, note the idea this influence gave American government; in the hub, state the social contract.",
                 "SOCIAL CONTRACT / &amp; the purpose of government",
                 ["John Locke", "Montesquieu", "Thomas Hobbes", "Rousseau",
                  "Magna Carta", "Greek democracy", "Roman Republic"]),
     dict(scaffold="Give a matching set (thinker &rarr; idea) to place first: e.g., Montesquieu &rarr; separation of powers.",
          extend="In the hub, explain Social Contract Theory and connect it to the overall purpose of the U.S. government.",
          show=_SHOW),
     ROLE("GC.01")),

  # GC.02 — Declaration & grievances -> cause & effect chain
  _o("21_gc02_causeeffect",
     "From English Rights to the Declaration",
     KICK("GC.02"),
     [("Cause &amp; Effect &middot; Chain", "red"), ("SSP.05 &middot; DOK 2&ndash;3", "skill")],
     "English rights documents set expectations the colonists believed Britain violated &mdash; a chain that ends in the "
     "Declaration of Independence. Tracing it makes the &ldquo;why&rdquo; of 1776 visible. "
     "<span class='cite'>Cause-and-effect reasoning is TN Practice SSP.05.</span>",
     cause_effect_chain(
       "Work down the chain: what each step established, and how it led to the next.",
       [("English rights traditions",
         "&mdash; what did the Magna Carta, Petition of Right &amp; English Bill of Rights guarantee?"),
        ("British actions in the colonies",
         "&mdash; which of those established rights did colonists claim were violated?"),
        ("Colonial grievances",
         "&mdash; how did colonists list and justify their complaints?"),
        ("Declaration of Independence (1776)",
         "&mdash; how does it use those grievances to justify separation?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>Cite it:</b> Name one grievance in the Declaration and the '
             'English document whose right it echoes. ____________________________________</div>')),
     dict(scaffold="Provide the three English documents as cards; students match each to the right it protects before building the chain.",
          extend="Choose the grievance you find most serious and defend the choice with evidence from an English document.",
          show=_SHOW),
     ROLE("GC.02")),

  # GC.03 — Articles of Confederation strengths/weaknesses -> T-chart
  _o("22_gc03_tchart",
     "The Articles of Confederation",
     KICK("GC.03"),
     [("T&#8209;Chart &middot; Two Sides", "navy"), ("DOK 2&ndash;3", "skill")],
     "The nation&rsquo;s first plan of government had real strengths and real weaknesses. A T&#8209;chart forces students to "
     "hold both before judging whether it needed replacing. "
     "<span class='cite'>Weighing evidence on both sides builds argument (SSP.04).</span>",
     tchart("Define <b>confederation</b>, then gather evidence of what worked and what did not.",
            "STRENGTHS", "what the Articles could do", "WEAKNESSES", "what the Articles could not do",
            [("Structure", "what government did the Articles set up?"),
             ("Powers held", "what was the national government allowed to do?")],
            [("Missing powers", "could Congress tax or regulate trade?"),
             ("Enforcement", "why was it hard to act as one nation?")],
            "<b>Weigh it:</b> Did the weaknesses require a new Constitution, or could the Articles have been fixed? ______________________"),
     dict(scaffold="Give a short word bank (tax, trade, army, amend, states) to sort into strengths vs. weaknesses.",
          extend="Write a one-paragraph judgment: keep, amend, or replace the Articles &mdash; and why.",
          show=_SHOW),
     ROLE("GC.03")),

  # GC.04 — Federalists vs Anti-Federalists -> T-chart
  _o("23_gc04_tchart",
     "Federalists <span style='font-family:Georgia;font-style:italic;font-size:15pt'>vs.</span> Anti-Federalists",
     KICK("GC.04"),
     [("T&#8209;Chart &middot; Two Positions", "navy"), ("DOK 3 &middot; Perspective", "skill")],
     "After the Great Compromise, ratification split the country. Laying the two positions side by side shows students that "
     "the Constitution was argued into existence, not simply announced. "
     "<span class='cite'>Comparing viewpoints with evidence is TN Practice SSP.04.</span>",
     tchart("Give each side equal weight: their view of government power, key figures, and economic interests.",
            "FEDERALISTS", "favored ratifying the Constitution", "ANTI-FEDERALISTS", "opposed ratification as written",
            [("Government power", "how strong should the national government be?"),
             ("Key figures", "who argued for this side?"),
             ("Economic interests", "whose interests lined up here?")],
            [("Government power", "why fear a strong central government?"),
             ("Key figures", "who argued for this side?"),
             ("Bill of Rights", "why demand one before ratifying?")],
            "<b>Ratification:</b> Which argument would have persuaded you in 1788 &mdash; and why? ______________________________"),
     dict(scaffold="Sort a set of quotations/claims into the correct column before writing.",
          extend="Honors: cite evidence from the Federalist and Anti-Federalist papers on the fight over ratification.",
          show=_SHOW),
     ROLE("GC.04")),

  # GC.05 — Preamble purposes -> Main Idea & Details
  _o("24_gc05_mainidea",
     "The Preamble &mdash; Why Government Exists",
     KICK("GC.05"),
     [("Main Idea &amp; Details", "navy"), ("DOK 2", "skill")],
     "The Preamble states the <b>purposes</b> of government in one sentence. Pulling out its goals turns a famous line into "
     "a checklist students can test against government today. "
     "<span class='cite'>Separating central idea from supporting detail is core disciplinary literacy (SSP.02).</span>",
     main_idea(
       "The main idea is the Preamble&rsquo;s purpose; the details are its six goals. Give a present-day example of each.",
       "&ldquo;We the People &hellip; in Order to&hellip;&rdquo; &mdash; the purposes of government",
       [("Union &amp; Justice", "&ldquo;a more perfect Union&rdquo; &middot; &ldquo;establish Justice&rdquo;"),
        ("Peace &amp; Defense", "&ldquo;domestic Tranquility&rdquo; &middot; &ldquo;common defence&rdquo;"),
        ("Welfare &amp; Liberty", "&ldquo;general Welfare&rdquo; &middot; &ldquo;Blessings of Liberty&rdquo;")],
       "<b>In one sentence:</b> Which purpose matters most today &mdash; and why? ______________________________________________"),
     dict(scaffold="Provide the Preamble text; students underline each goal, then match it to the right column.",
          extend="Connect one goal to a basic constitutional principle (e.g., limited government, popular sovereignty).",
          show=_SHOW),
     ROLE("GC.05")),

  # GC.06 — Federalism powers -> Venn (SOURCE-MANDATED)
  _o("25_gc06_venn",
     "Federalism &mdash; Who Holds Which Powers",
     KICK("GC.06"),
     [("Venn &middot; Federal / State", "navy"), ("DOK 2&ndash;3", "skill")],
     "Federalism divides power between the national and state governments, with some powers shared. The &lsquo;I can&rsquo; target "
     "asks students to <b>plot these powers on a Venn</b> &mdash; delegated, reserved, and concurrent. "
     "<span class='cite'>Sorting by shared vs. unique traits is Marzano&rsquo;s highest-yield strategy.</span>",
     venn2("Place each power where it belongs: only national, only state, or shared by <b>both</b>.",
           "FEDERAL &mdash; Delegated (Enumerated)", "powers the national government holds",
           "STATE &mdash; Reserved", "powers kept by the states",
           ["only national?", "e.g., coin money?", "declare war?"],
           ["only the states?", "e.g., schools?", "licenses?"],
           ["shared by both?", "tax? courts?", "borrow money?"],
           cap_a="FEDERAL", cap_b="STATE", cap_both="CONCURRENT"),
     dict(scaffold="Give a card set of powers to sort into the three regions before writing them in.",
          extend="Explain how the Supremacy Clause resolves a conflict between a federal and a state power.",
          show=_SHOW),
     ROLE("GC.06")),

  # GC.07 — Structure & amendment process -> sequence/flow
  _o("26_gc07_sequence",
     "Amending the Constitution (Article V)",
     KICK("GC.07"),
     [("Sequence &middot; Process Flow", "red"), ("SSP.05 &middot; DOK 2", "skill")],
     "Article V sets a deliberately hard, two-stage path to change the Constitution: propose, then ratify &mdash; each with two "
     "methods. Mapping the flow shows students why amendments are rare. "
     "<span class='cite'>Sequencing a process builds chronological reasoning (SSP.05).</span>",
     cause_effect_chain(
       "Work down the process. In each box, record <b>both</b> methods and the fraction each requires.",
       [("PROPOSE an amendment",
         "&mdash; 2/3 of both houses of Congress, <em>or</em> a national convention called by 2/3 of the states?"),
        ("RATIFY the amendment",
         "&mdash; 3/4 of state legislatures, <em>or</em> 3/4 of state ratifying conventions?"),
        ("Amendment added to the Constitution",
         "&mdash; how many amendments have succeeded, out of thousands proposed?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>Why so hard?</b> Name the two reasons the Framers built it this way '
             '(emphasis on federalism &middot; checks &amp; balances). ____________________________________</div>')),
     dict(scaffold="Provide the four methods on cards; students place each under Propose or Ratify first.",
          extend="Summarize the seven articles of the Constitution and say which article each branch is defined in.",
          show=_SHOW),
     ROLE("GC.07")),

  # GC.08 — Bill of Rights -> Matrix (TCA-required; TN flagged)
  _o("27_gc08_matrix",
     "The Bill of Rights &mdash; Limits on Government",
     KICK("GC.08"),
     [("Matrix &middot; Amendments 1&ndash;8", "navy"), ("DOK 2&ndash;3", "skill")],
     "The first eight Amendments each draw a boundary the government may not cross. A matrix holds all eight to the same two "
     "questions so the pattern &mdash; <b>limited government</b> &mdash; becomes unmistakable. "
     "<span class='cite'>Tennessee law (T.C.A. &sect; 49-6-1028) requires this instruction.</span>",
     matrix("For each Amendment, name the personal protection it guarantees and the limit it places on government.",
            [("What it protects", "the personal right", "navy"),
             ("How it limits government", "the boundary it draws", "red")],
            [("1st", ["", ""]), ("2nd", ["", ""]), ("3rd", ["", ""]), ("4th", ["", ""]),
             ("5th", ["", ""]), ("6th", ["", ""]), ("7th", ["", ""]), ("8th", ["", ""])],
            "<b>9th &amp; 10th Amendments:</b> How do they connect to federalism and rights not listed? ______________________"),
     dict(scaffold="Pre-fill the 1st and 4th rows together, then students complete the rest.",
          extend="Use an example to show how a national&ndash;state conflict over a right is resolved by the Supremacy Clause.",
          show=_SHOW),
     ROLE("GC.08"), tn=True),

  # GC.09 — Democracy vs Republic -> Venn
  _o("28_gc09_venn",
     "Democracy <span style='font-family:Georgia;font-style:italic;font-size:15pt'>&amp;</span> Republic",
     KICK("GC.09"),
     [("Venn &middot; Compare Two", "navy"), ("DOK 2&ndash;3", "skill")],
     "&ldquo;Democracy&rdquo; and &ldquo;republic&rdquo; overlap more than students expect. A Venn examines the <b>relationship</b> between the "
     "two &mdash; and where a constitution limits each. "
     "<span class='cite'>Comparing to find shared vs. distinct traits is Marzano&rsquo;s highest-yield move.</span>",
     venn2("Sort each trait: only a democracy, only a republic, or true of <b>both</b> under a constitution.",
           "DEMOCRACY", "constitutional democracy", "REPUBLIC", "constitutional republic",
           ["people decide directly?", "majority rules?"],
           ["elected representatives?", "law limits the majority?"],
           ["power from the people?", "constitution limits government?"],
           cap_a="DEMOCRACY", cap_b="REPUBLIC", cap_both="BOTH"),
     dict(scaffold="Give one clear example of each (a direct vote vs. an elected legislature) to anchor the &lsquo;only&rsquo; regions.",
          extend="Give a real example of each and explain how the U.S. is best described as a constitutional republic.",
          show=_SHOW),
     ROLE("GC.09")),
]
