# -*- coding: utf-8 -*-
"""Unit 7 labeled best-fit organizers (GC.28-GC.30 — Tennessee State & Local Government).
Best-fit: GC.28 a three-branch matrix (Legislative / Executive / Judicial functions,
agencies, and the courts); GC.29 a local-government types chart (County / City / Metro,
applied to YOUR OWN county — genericized, no district named); GC.30 a current-officials
LOOKUP organizer (blank record form — students look up and record the governor and their
own legislators from official sources; no names are asserted).
"""
from common import matrix

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role); d.update(kw); return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; {std} (labeled)"
def KICK(std): return f"Unit 7 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.28 — Tennessee's three branches -> Matrix (branch x function)
  _o("20_gc28_matrix", "Tennessee's Three Branches",
     KICK("GC.28"),
     [("Matrix &middot; Branch &times; Function", "navy"), ("SSP.01 &middot; DOK 2", "skill")],
     "Tennessee divides power into three departments, just like the nation. A matrix holds each branch to the "
     "same questions, so students see who leads it, what it does, and the Tennessee feature that makes it distinct. "
     "<span class='cite'>Identifying the structure and functions of government builds TN Practice SSP.01.</span>",
     matrix("For each branch, name who leads it, an agency/chamber/court within it, and one distinctly Tennessee feature.",
            [("LEGISLATIVE", "General Assembly", "navy"),
             ("EXECUTIVE", "Governor &amp; agencies", "red"),
             ("JUDICIAL", "the courts", "gold")],
            [("Who leads it &amp; its main job", ["", "", ""]),
             ("A chamber, agency, or court inside it", ["", "", ""]),
             ("One Tennessee feature (citizen legislature &middot; Grand Divisions &middot; Tennessee Plan &middot; Chancery/Circuit/Criminal)", ["", "", ""])],
            "<b>Pattern:</b> How do Tennessee&rsquo;s three branches check and balance one another? ____________________________________"),
     dict(scaffold="Give a card set — Governor, General Assembly, Supreme Court, a Chancery/Circuit/Criminal court, a state department — to sort into the three columns before writing.",
          extend="Explain the &lsquo;Tennessee Plan&rsquo; for choosing appellate judges, and how Chancery, Circuit, and Criminal courts divide the work. Then look up the current Chief Justice from an official source.", show=_SHOW),
     ROLE("GC.28")),

  # GC.29 — Types of local government -> Matrix (type x trait), applied to YOUR county
  _o("21_gc29_matrix", "Local Government in Tennessee",
     KICK("GC.29"),
     [("Matrix &middot; Type &times; Trait", "navy"), ("SSP.02 &middot; DOK 2", "skill")],
     "Tennessee is a unitary state: it creates the local governments beneath it. A matrix compares the three "
     "types side by side, then asks students to apply them to their own county and city. "
     "<span class='cite'>Comparing structures against one yardstick builds TN Practice SSP.02.</span>",
     matrix("Compare the three types, then apply them to your own community in the last row.",
            [("COUNTY", "covers all TN", "navy"),
             ("CITY", "municipality", "red"),
             ("METRO", "consolidated city-county", "gold")],
            [("How it is structured (who leads it)", ["", "", ""]),
             ("Services it typically provides", ["", "", ""]),
             ("How it depends on the state (legal &middot; fiscal &middot; operational)", ["", "", ""]),
             ("Which type(s) govern YOUR home? Name your own county / city and its model", ["", "", ""])],
            "<b>Pattern:</b> Why can no Tennessee county, city, or metro act beyond what the state allows (unitary government &middot; Dillon&rsquo;s Rule)? ______________"),
     dict(scaffold="Sort service cards — sheriff, city police, schools, water, zoning, property tax — into County / City / Metro first.",
          extend="Write the opinion piece: how can an individual best serve their community and take part in the political process at the local, state, and national levels? Defend a claim with examples.", show=_SHOW),
     ROLE("GC.29")),

  # GC.30 — Identify your current officials -> LOOKUP organizer (blank record form)
  _o("22_gc30_lookup", "Identify Your Current Officials",
     KICK("GC.30"),
     [("Lookup &middot; Record from an Official Source", "gold"), ("SSP.06 &middot; DOK 1", "skill")],
     "Officials change with every election, so this standard is a look-it-up task. This organizer is a blank record "
     "form: using official Tennessee sources, students find and write down who governs them right now &mdash; and where "
     "they found it. <span class='cite'>Locating and verifying current officials builds civic practice SSP.06.</span>",
     matrix("Use an OFFICIAL source (tn.gov &middot; capitol.tn.gov &lsquo;Find My Legislator&rsquo;). Record each office below; confirm — never guess.",
            [("WHO HOLDS IT NOW", "current name", "navy"),
             ("MY DISTRICT #", "from address lookup", "red"),
             ("OFFICIAL SOURCE I USED", "where I confirmed it", "gold")],
            [("Governor of Tennessee (statewide)", ["", "(statewide)", ""]),
             ("My State Senator", ["", "", ""]),
             ("My State Representative", ["", "", ""])],
            "<b>Governor&rsquo;s top stated priority</b> (from an official source, e.g. the State of the State): ____________________________________"),
     dict(scaffold="Model one lookup together on the board: enter a sample Tennessee address into the official &lsquo;Find My Legislator&rsquo; tool, then read off the Senate and House districts.",
          extend="Draft a short, respectful message to one of your legislators about an issue you care about — and explain why naming your specific district helps you be heard.", show=_SHOW),
     ROLE("GC.30")),
]
