#!/usr/bin/env python3
"""
History Hack — Unit 6 (WWII, TN US.45-US.58) Visual Asset Builder
====================================================================
Generates all fresh-built data-graphic PNGs and fresh-built schematic
maps required by the Unit 6 sourcing manifest. Verified downloaded
maps (US.47, US.48, US.50 x2, US.57, US.58) are handled separately by
shell `curl` commands documented in QA_REPORT.md / README.md — this
script only builds NEW assets from verified numeric/geographic data.

Run: python3 build_assets.py

Design system: History Hack dark navy/red/gold palette, WCAG AA
contrast, no 3D, no pie charts, color-independent patterns, source
footers on every chart/map.
"""
import json
import os
import csv
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
from matplotlib.lines import Line2D
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# History Hack brand palette (dark navy / red / gold), WCAG AA on dark bg
# ----------------------------------------------------------------------
NAVY_BG      = "#0B1B2B"   # primary dark navy background
NAVY_PANEL   = "#122A40"   # panel / plot background
NAVY_LIGHT   = "#1D3A54"   # gridlines / secondary panel
GOLD         = "#E8B84B"   # primary accent (contrast ~9:1 on navy bg)
RED          = "#C24A4A"   # secondary accent / alert (contrast ~5.4:1 on navy bg)
CREAM        = "#F2ECDD"   # primary text (contrast ~14:1 on navy bg)
CREAM_MUTED  = "#B9C4CE"   # secondary text / muted labels (contrast ~7.8:1)
TEAL         = "#4FA9A2"   # tertiary categorical
STEEL        = "#7C93A8"   # neutral categorical / grid
WHITE        = "#FFFFFF"

CATEGORICAL = [GOLD, RED, TEAL, STEEL, "#D98E3E", "#8C6FB0", "#5E7C9A", "#B75C5C"]

plt.rcParams.update({
    "figure.facecolor": NAVY_BG,
    "axes.facecolor": NAVY_PANEL,
    "savefig.facecolor": NAVY_BG,
    "text.color": CREAM,
    "axes.labelcolor": CREAM,
    "axes.edgecolor": NAVY_LIGHT,
    "xtick.color": CREAM_MUTED,
    "ytick.color": CREAM_MUTED,
    "axes.titlecolor": CREAM,
    "grid.color": NAVY_LIGHT,
    "grid.alpha": 0.6,
    "font.family": "DejaVu Sans",
    "font.size": 15,
    "axes.titlesize": 24,
    "axes.titleweight": "bold",
    "axes.labelsize": 16,
})

FIG_W, FIG_H, DPI = 16, 9, 150  # 2400 x 1350 @ 150 dpi (16:9)


def new_fig():
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, layout="constrained")
    return fig


def source_footer(fig, text, y=-0.02):
    wrapped = textwrap.fill(text, 150)
    fig.text(0.01, y, wrapped, ha="left", va="top", fontsize=11, color=CREAM_MUTED, wrap=False)


def save(fig, path, note=""):
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor=NAVY_BG)
    plt.close(fig)
    from PIL import Image
    im = Image.open(path)
    print(f"  saved {os.path.relpath(path, ROOT)}  {im.size}  {os.path.getsize(path):,} bytes  {note}")


def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print(f"  saved {os.path.relpath(path, ROOT)}")


def write_svg_note(path, title, note):
    """Write a minimal, editable SVG source placeholder that documents the
    chart's data-driven construction where a full vector re-implementation
    is not practical inside this script; used only as a supplementary
    editable source pointer alongside the primary PNG + data.csv."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
<rect width="800" height="200" fill="{NAVY_BG}"/>
<text x="20" y="40" fill="{GOLD}" font-size="20" font-family="DejaVu Sans" font-weight="bold">{title}</text>
<text x="20" y="80" fill="{CREAM}" font-size="14" font-family="DejaVu Sans">{note}</text>
<text x="20" y="110" fill="{CREAM_MUTED}" font-size="12" font-family="DejaVu Sans">Editable source: regenerate from the paired .data.csv using build_assets.py (matplotlib).</text>
</svg>'''
    with open(path, "w") as f:
        f.write(svg)


# =========================================================================
# US.45 — U.S. Unemployment, Great Depression 1929-1940 (Census/NICB D65)
# =========================================================================
def build_us45():
    print("US.45 unemployment chart")
    years = list(range(1929, 1941))
    unemployed_thousands = [429, 2896, 7037, 11385, 11842, 9761, 9092, 7386, 6403, 9796, 8786, 6995]
    millions = [v / 1000.0 for v in unemployed_thousands]

    fig = new_fig()
    ax = fig.add_subplot(111)
    colors = [RED if y == 1933 else GOLD for y in years]
    bars = ax.bar(years, millions, color=colors, width=0.68, zorder=3,
                   edgecolor=NAVY_BG, linewidth=0.5)
    for x, v in zip(years, millions):
        ax.text(x, v + 0.22, f"{v:.1f}M", ha="center", va="bottom", fontsize=11,
                 color=CREAM, fontweight="bold" if x == 1933 else "normal")
    ax.set_title("U.S. unemployment rose sharply after 1929, peaking in 1933",
                  loc="left", fontsize=23)
    ax.set_ylabel("Unemployed persons (millions)")
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], rotation=0)
    ax.set_ylim(0, 13.5)
    ax.grid(axis="y", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    legend_patch = mpatches.Patch(color=RED, label="1933 = peak year in this series (11.84M)")
    ax.legend(handles=[legend_patch], loc="upper right", frameon=False, fontsize=12,
              labelcolor=CREAM)
    note = ("Source: U.S. Bureau of the Census, Historical Statistics of the United States, "
            "1789-1945 (1949), Series D62-76 (NICB), column D65 \"Unemployed,\" in thousands of "
            "persons. census.gov | SERIES CAVEAT: figures are the National Industrial Conference "
            "Board (NICB) series as published by the Census Bureau, not the modern BLS/Lebergott "
            "estimates (e.g. 1929 NICB=429K vs. ~1.55M modern estimate) - do not mix series. "
            "Estimates from 1930 on are midyear, not annual average. 1940 uses the new Census "
            "labor-force concept and is NOT comparable to 1929-1939 gainful-worker-concept figures "
            "(1940 on the old concept = 54,808,000 gainful workers). Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.45", "US.45_us_unemployment_great_depression.png"))

    write_csv(os.path.join(ROOT, "US.45", "US.45_us_unemployment_great_depression.data.csv"),
               ["year", "unemployed_thousands", "unemployed_millions", "gainful_workers_thousands", "employed_thousands"],
               [[1929,429,0.429,48354,47925],[1930,2896,2.896,49006,46081],[1931,7037,7.037,49597,42530],
                [1932,11385,11.385,50132,38727],[1933,11842,11.842,50691,38827],[1934,9761,9.761,51267,41474],
                [1935,9092,9.092,51769,42653],[1936,7386,7.386,52237,44830],[1937,6403,6.403,52692,46279],
                [1938,9796,9.796,53229,48416],[1939,8786,8.786,53811,44993],[1940,6995,6.995,53466,46683]])
    write_svg_note(os.path.join(ROOT, "US.45", "US.45_us_unemployment_great_depression.svg"),
                    "US.45 Unemployment 1929-1940", "Census/NICB Series D65, thousands of persons")


# =========================================================================
# US.46 — Lend-Lease aid by recipient (Twenty-First Report, Table 2)
# =========================================================================
def build_us46():
    print("US.46 lend-lease chart")
    rows = [
        ("British Empire", 30269210000),
        ("U.S.S.R.", 10801131000),
        ("France", 1406600000),
        ("China", 631509000),
        ("American Republics", 421467000),
        ("Netherlands", 162157000),
        ("Other recipients + non-charged aid", 43284000 + 2088249000 + 75416000 + 52443000 + 34640000 + 28063000 + 25885000),
    ]
    # "Other recipients + non-charged aid" = Greece+Belgium+Norway+Turkey+Yugoslavia+"Other countries"+"Aid not charged to foreign governments"
    labels = [r[0] for r in rows]
    values = [r[1] / 1e9 for r in rows]
    total = 46.040054

    fig = new_fig()
    ax = fig.add_subplot(111)
    y_pos = np.arange(len(labels))[::-1]
    colors = CATEGORICAL[:len(labels)]
    bars = ax.barh(y_pos, values, color=colors, height=0.62, zorder=3, edgecolor=NAVY_BG)
    for y, v, lbl in zip(y_pos, values, labels):
        ax.text(v + 0.35, y, f"${v:.2f}B", va="center", ha="left", fontsize=13, color=CREAM, fontweight="bold")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=13)
    ax.set_xlabel("Lend-Lease aid, current US$ billions (period: March 1941 - 1 Oct 1945)")
    ax.set_title(f"British Empire and U.S.S.R. received 89% of ${total:.2f}B total Lend-Lease aid",
                  loc="left", fontsize=22)
    ax.set_xlim(0, 33)
    ax.grid(axis="x", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.98, 0.06, f"Verified total (Table 2): ${total:.2f}B",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=13,
            color=GOLD, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc=NAVY_LIGHT, ec=GOLD, lw=1))
    note = ("Source: Twenty-First Report to Congress on Lend-Lease Operations, For the Period Ended "
            "September 30, 1945 (transmitted 31 Jan 1946), Table 2 \"Lend-Lease Aid, by Country, "
            "March 1941 to October 1, 1945.\" fraser.stlouisfed.org | \"Other recipients + non-charged "
            "aid\" = Greece + Belgium + Norway + Turkey + Yugoslavia + Other countries + Aid not "
            "charged to foreign governments (clearly-defined remainder, not a single reported line). "
            "Exact verified total = $46,040,054,000. Do not print later cumulative-to-1946/1951 "
            "totals ($31.4B/$11.3B/etc.) against this table - unverified in this session. "
            "Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.46", "US.46_lend_lease_by_country.png"))

    write_csv(os.path.join(ROOT, "US.46", "US.46_lend_lease_by_country.data.csv"),
               ["recipient", "amount_usd", "amount_usd_billions", "definition"],
               [["British Empire", 30269210000, 30.27, "Table 2 line item"],
                ["U.S.S.R.", 10801131000, 10.80, "Table 2 line item"],
                ["France", 1406600000, 1.41, "Table 2 line item"],
                ["China", 631509000, 0.63, "Table 2 line item"],
                ["American Republics", 421467000, 0.42, "Table 2 line item"],
                ["Netherlands", 162157000, 0.16, "Table 2 line item"],
                ["Other recipients + non-charged aid", rows[-1][1], round(rows[-1][1]/1e9,2),
                 "Sum of Greece+Belgium+Norway+Turkey+Yugoslavia+Other countries+Aid not charged to foreign governments"],
                ["TOTAL", 46040054000, 46.04, "Table 2 grand total, verified"]])
    write_svg_note(os.path.join(ROOT, "US.46", "US.46_lend_lease_by_country.svg"),
                    "US.46 Lend-Lease by Country", "Twenty-First Report to Congress, Table 2")


# =========================================================================
# US.47 — Holocaust deaths by country (USHMM largest non-overlapping)
# =========================================================================
def build_us47():
    print("US.47 holocaust deaths chart")
    # Largest NON-OVERLAPPING country-level entries (avoid double counting
    # sub-entries like Czechoslovakia parts, Hungary 1937 vs 1941 borders,
    # Romania + Bessarabia/Bukovina which are sub-components).
    # low, high (for ranges); single point where source gives one figure
    data = [
        ("Poland", 2770000, 3000000),
        ("Soviet Union", 1340000, 1340000),
        ("Hungary (1941 borders)", 564507, 564507),
        ("Romania", 211214, 260000),
        ("Germany", 165200, 165200),
        ("Netherlands", 102000, 102000),
        ("Lithuania", 130000, 130000),
        ("Czechoslovakia", 260000, 260000),
        ("France", 72900, 74000),
        ("Latvia", 70000, 70000),
        ("Yugoslavia", 67228, 67228),
        ("Austria", 65459, 65459),
        ("Greece", 58800, 65000),
    ]
    data.sort(key=lambda r: r[2])
    labels = [d[0] for d in data]
    lows = np.array([d[1] for d in data]) / 1000.0
    highs = np.array([d[2] for d in data]) / 1000.0
    mids = (lows + highs) / 2
    errs = (highs - lows) / 2

    fig = new_fig()
    ax = fig.add_subplot(111)
    y_pos = np.arange(len(labels))
    ax.barh(y_pos, mids, xerr=errs, color=GOLD, height=0.6, zorder=3,
            edgecolor=NAVY_BG, error_kw=dict(ecolor=CREAM, capsize=4, lw=1.5))
    for y, lo, hi in zip(y_pos, lows, highs):
        lbl = f"{lo:,.0f}K" if lo == hi else f"{lo:,.0f}-{hi:,.0f}K"
        ax.text(hi + 60, y, lbl, va="center", ha="left", fontsize=11.5, color=CREAM)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=12.5)
    ax.set_xlabel("Estimated Jewish deaths (thousands)")
    ax.set_title("Largest country-level Holocaust death estimates (non-overlapping totals)",
                  loc="left", fontsize=21)
    ax.set_xlim(0, 3400)
    ax.grid(axis="x", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.98, 0.05,
            "ESTIMATES SUBJECT TO CHANGE",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=13, color=RED, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc=NAVY_LIGHT, ec=RED, lw=1.4))
    note = ("Source: United States Holocaust Memorial Museum, \"Jewish Losses during the Holocaust: "
            "By Country,\" Holocaust Encyclopedia, last edited 27 Mar 2018. encyclopedia.ushmm.org | "
            "USHMM verbatim caveat: \"No one master list of those who perished exists anywhere in the "
            "world... All figures are estimates and subject to change with the discovery of new "
            "documentation.\" Rows shown are the largest NON-overlapping country totals; sub-entries "
            "(e.g. Czechoslovak regions, Hungary under 1937 vs. 1941 borders, Romania's Bessarabia/"
            "Bukovina) are excluded here to avoid double-counting. Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.47", "US.47_holocaust_deaths_by_country.png"))

    write_csv(os.path.join(ROOT, "US.47", "US.47_holocaust_deaths_by_country.data.csv"),
               ["country", "deaths_low", "deaths_high", "note"],
               [[d[0], d[1], d[2], "USHMM estimate; range shown where source gives a range"] for d in data])
    write_svg_note(os.path.join(ROOT, "US.47", "US.47_holocaust_deaths_by_country.svg"),
                    "US.47 Holocaust Deaths by Country", "USHMM Holocaust Encyclopedia, non-overlapping totals")


# =========================================================================
# US.48 — Pearl Harbor losses (NHHC)
# =========================================================================
def build_us48():
    print("US.48 pearl harbor losses chart")
    services = ["Navy", "Marine Corps", "Army", "Civilian"]
    killed = [2008, 109, 218, 68]
    wounded = [710, 69, 364, 35]

    fig = new_fig()
    ax = fig.add_subplot(111)
    x = np.arange(len(services))
    w = 0.35
    b1 = ax.bar(x - w/2, killed, width=w, label="Killed / missing", color=RED, zorder=3, edgecolor=NAVY_BG)
    b2 = ax.bar(x + w/2, wounded, width=w, label="Wounded", color=GOLD, zorder=3, edgecolor=NAVY_BG,
                hatch="//")
    for rects in (b1, b2):
        for r in rects:
            h = r.get_height()
            ax.text(r.get_x() + r.get_width()/2, h + 25, f"{int(h):,}", ha="center", va="bottom",
                     fontsize=12, color=CREAM)
    ax.set_xticks(x)
    ax.set_xticklabels(services, fontsize=14)
    ax.set_ylabel("Personnel / civilians")
    ax.set_title("Pearl Harbor, 7 Dec 1941: 2,403 killed or missing; 1,178 wounded",
                  loc="left", fontsize=22)
    ax.legend(loc="upper right", frameon=False, fontsize=13, labelcolor=CREAM)
    ax.set_ylim(0, 2300)
    ax.grid(axis="y", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    callout = ("Also per NHHC: 188 aircraft destroyed  |  5 battleships sunk, 3 damaged")
    ax.text(0.5, 0.94, callout, transform=ax.transAxes, ha="center", va="top", fontsize=14,
            color=NAVY_BG, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=GOLD, ec=GOLD))
    note = ("Source: Naval History and Heritage Command, \"Pearl Harbor Attack.\" history.navy.mil | "
            "Totals: killed/missing 2,403 (Navy 2,008 + Marine Corps 109 + Army 218 + civilian 68); "
            "wounded 1,178 (Navy 710 + Marine Corps 69 + Army 364 + civilian 35) - sums of NHHC "
            "service-level figures, not separately published totals on the source page. NHHC wording: "
            "\"the enemy sank five battleships and damaged three\"; \"188 Navy, Marine Corps, and "
            "U.S. Army Air Force planes were destroyed.\" Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.48", "US.48_pearl_harbor_losses.png"))

    write_csv(os.path.join(ROOT, "US.48", "US.48_pearl_harbor_losses.data.csv"),
               ["service", "killed_or_missing", "wounded"],
               [["Navy",2008,710],["Marine Corps",109,69],["Army",218,364],["Civilian",68,35],
                ["TOTAL",2403,1178]])
    write_svg_note(os.path.join(ROOT, "US.48", "US.48_pearl_harbor_losses.svg"),
                    "US.48 Pearl Harbor Losses", "NHHC Pearl Harbor Attack page")


# =========================================================================
# US.50 — WWII battle casualties (Midway/D-Day/Iwo Jima/Okinawa)
# =========================================================================
def build_us50():
    print("US.50 battle casualties chart")
    battles = ["Midway", "D-Day", "Iwo Jima", "Okinawa"]
    dates = ["4-7 Jun 1942", "6 Jun 1944", "19 Feb-26 Mar 1945", "1945"]
    values = [307, 2499, 6800, 12520]
    defs = ["U.S. personnel lost\n(single battle)", "American dead, 6 June\n(single day)",
            "American dead, all services\n(36-day campaign)", "U.S. killed or missing\n(multi-month campaign)"]
    colors = [TEAL, GOLD, RED, STEEL]

    fig = plt.figure(figsize=(FIG_W, 9.6), dpi=DPI, layout="constrained")
    ax = fig.add_subplot(111)
    x = np.arange(len(battles))
    bars = ax.bar(x, values, color=colors, width=0.55, zorder=3, edgecolor=NAVY_BG)
    for xi, v, d in zip(x, values, defs):
        ax.text(xi, v + 280, f"{v:,}", ha="center", va="bottom", fontsize=16, color=CREAM, fontweight="bold")
        ax.text(xi, -1900, d, ha="center", va="top", fontsize=10.5, color=CREAM_MUTED)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{b}\n{d}" for b, d in zip(battles, dates)], fontsize=13)
    ax.tick_params(axis="x", pad=12)
    ax.set_ylabel("U.S. dead / killed-missing")
    ax.set_title("U.S. dead varied widely by engagement type and duration",
                  loc="left", fontsize=22)
    ax.set_ylim(0, 15200)
    ax.grid(axis="y", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.99, 0.94, "CAVEAT: figures use different official\ndefinitions - not directly comparable",
            transform=ax.transAxes, ha="right", va="top", fontsize=11.5, color=RED, style="italic")
    note = ("Sources: Midway 307 - NHHC/govinfo summary of losses (GOVPUB-D221, govinfo.gov); D-Day "
            "2,499 - NPS \"D-Day 75th Anniversary\" (nps.gov); Iwo Jima 6,800 dead - NHHC Navy "
            "Department Library (history.navy.mil); Okinawa 12,520 killed or missing - U.S. Army CMH, "
            "Ryukyus, CMH Pub 72-35 (history.army.mil). CORRECTED figures: do not use previously "
            "circulated 317 (Midway) or 2,501 (D-Day) - unverified in this session. "
            "Verified 2026-08-01.")
    source_footer(fig, note, y=-0.10)
    save(fig, os.path.join(ROOT, "US.50", "US.50_wwii_battle_casualties.png"))

    write_csv(os.path.join(ROOT, "US.50", "US.50_wwii_battle_casualties.data.csv"),
               ["battle", "value", "definition", "duration"],
               [["Midway", 307, "U.S. personnel lost", "4-7 Jun 1942 (single battle)"],
                ["D-Day", 2499, "American dead, 6 June", "6 Jun 1944 (single day)"],
                ["Iwo Jima", 6800, "American dead, all services", "19 Feb-26 Mar 1945 (36-day campaign)"],
                ["Okinawa", 12520, "U.S. killed or missing", "1945 (multi-month campaign)"]])
    write_svg_note(os.path.join(ROOT, "US.50", "US.50_wwii_battle_casualties.svg"),
                    "US.50 WWII Battle Casualties", "NHHC / NPS / U.S. Army CMH")


# =========================================================================
# US.52 — Women workforce 1940-45 (two aligned panels, no dual axis)
# =========================================================================
def build_us52():
    print("US.52 women workforce chart")
    years = [1940, 1941, 1942, 1943, 1944, 1945]
    civ_labor_force_millions = [14.16, 14.64, 16.12, 18.81, 19.37, 19.03]  # col 16 (civilian) except 1945 uses civilian 19.03? -> use col16 all years
    # Use civilian labor force col.16 consistently: 1940=14160,1941=14640,1942=16110,1943=18700,1944=19170,1945=19030
    civ_labor_force_millions = [14.16, 14.64, 16.11, 18.70, 19.17, 19.03]
    employed_millions = [11.97, 13.00, 15.17, 18.20, 18.85, 18.61]
    female_share_pct = [25.4, 26.2, 28.6, 33.7, 35.1, 35.3]

    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, layout="constrained")
    gs = fig.add_gridspec(1, 2, wspace=0.12)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])

    x = np.arange(len(years))
    w = 0.38
    ax1.bar(x - w/2, civ_labor_force_millions, width=w, color=GOLD, label="Civilian labor force", zorder=3, edgecolor=NAVY_BG)
    ax1.bar(x + w/2, employed_millions, width=w, color=TEAL, label="Employed (civilian)", zorder=3, edgecolor=NAVY_BG, hatch="//")
    for xi, v in zip(x, civ_labor_force_millions):
        ax1.text(xi - w/2, v + 0.3, f"{v:.2f}M", ha="center", fontsize=10.5, color=CREAM)
    for xi, v in zip(x, employed_millions):
        ax1.text(xi + w/2, v + 0.3, f"{v:.2f}M", ha="center", fontsize=10.5, color=CREAM)
    ax1.set_xticks(x); ax1.set_xticklabels(years)
    ax1.set_ylabel("Women, millions (age 14+)")
    ax1.set_title("Women's civilian labor force: 14.16M -> 19.03M\nEmployed women: 11.97M -> 18.61M", loc="left", fontsize=18)
    ax1.set_ylim(0, 21.5)
    ax1.legend(loc="upper left", frameon=False, fontsize=11.5, labelcolor=CREAM)
    ax1.grid(axis="y", zorder=0)
    ax1.spines[["top", "right"]].set_visible(False)

    bars2 = ax2.bar(x, female_share_pct, width=0.55, color=RED, zorder=3, edgecolor=NAVY_BG)
    for xi, v in zip(x, female_share_pct):
        ax2.text(xi, v + 0.8, f"{v:.1f}%", ha="center", fontsize=12, color=CREAM, fontweight="bold")
    ax2.set_xticks(x); ax2.set_xticklabels(years)
    ax2.set_ylabel("Female share of civilian labor force (%)")
    ax2.set_title("Female share of the civilian labor force\nrose from 25.4% to 35.3%", loc="left", fontsize=18)
    ax2.set_ylim(0, 42)
    ax2.grid(axis="y", zorder=0)
    ax2.spines[["top", "right"]].set_visible(False)

    fig.suptitle("Women's role in the wartime labor force grew steadily, 1940-1945", fontsize=23, fontweight="bold", color=CREAM, x=0.01, ha="left")
    note = ("Source: U.S. Bureau of the Census, Historical Statistics of the United States, 1789-1945 "
            "(1949), Series D11-31 \"Labor Force - Total in Labor Force and Employment Status: 1940 to "
            "1945,\" persons 14 years old and over, non-institutional. census.gov | Two aligned panels "
            "used instead of a dual-axis chart. Left panel distinguishes civilian LABOR FORCE "
            "(14.16M->19.03M) from EMPLOYED women (11.97M->18.61M) - these are different measures, not "
            "interchangeable. Right panel: female share of civilian labor force = female civilian labor "
            "force / total civilian labor force (both sexes), calculated from the same table. "
            "Verified 2026-08-01.")
    source_footer(fig, note, y=-0.05)
    save(fig, os.path.join(ROOT, "US.52", "US.52_women_workforce_1940_45.png"))

    write_csv(os.path.join(ROOT, "US.52", "US.52_women_workforce_1940_45.data.csv"),
               ["year", "female_civilian_labor_force_millions", "female_employed_millions",
                "female_share_of_civilian_labor_force_pct"],
               list(zip(years, civ_labor_force_millions, employed_millions, female_share_pct)))
    write_svg_note(os.path.join(ROOT, "US.52", "US.52_women_workforce_1940_45.svg"),
                    "US.52 Women Workforce 1940-45", "Census Historical Statistics 1789-1945, Series D11-31")


# =========================================================================
# US.53 — Black migration employment (FEPC nonwhite share)
# =========================================================================
def build_us53():
    print("US.53 black migration employment chart")
    # early 1942 is "<3%" -> rendered as open marker at 3.0 with annotation, not a filled point
    labels = ["Early 1942", "Sep 1942", "Jan 1943", "Jan 1944", "Nov 1944"]
    values = [3.0, 4.6, 6.4, 7.2, 8.3]
    is_open = [True, False, False, False, False]

    fig = plt.figure(figsize=(FIG_W, 8.0), dpi=DPI, layout="constrained")
    ax = fig.add_subplot(111)
    x = np.arange(len(labels))
    ax.plot(x, values, color=GOLD, lw=2.5, zorder=3)
    for xi, v, open_marker in zip(x, values, is_open):
        if open_marker:
            ax.scatter([xi], [v], s=260, facecolors="none", edgecolors=GOLD, linewidths=2.5, zorder=4)
            ax.annotate("<3% (early 1942)\nopen marker = upper bound, not exact", (xi, v),
                        xytext=(xi + 0.15, v - 1.6), fontsize=11, color=CREAM,
                        arrowprops=dict(arrowstyle="->", color=CREAM_MUTED))
        else:
            ax.scatter([xi], [v], s=140, facecolors=GOLD, edgecolors=NAVY_BG, linewidths=1.5, zorder=4)
            ax.text(xi, v + 0.35, f"{v:.1f}%", ha="center", fontsize=13, color=CREAM, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=13)
    ax.set_ylabel("Nonwhite share of workers, WMC-reporting firms (%)")
    ax.set_title("Nonwhite share of workers in war-industry firms reporting to the\nWar Manpower Commission rose from under 3% to 8.3%",
                  loc="left", fontsize=20)
    ax.set_ylim(0, 10)
    ax.grid(axis="y", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)

    # NARA migration callout box (not an annual series - separate framing)
    callout = ("NARA context (not an annual series): approx. 6,000,000 Black Americans migrated from\n"
               "the South to Northern/Midwestern/Western states, roughly 1910s-1970s")
    ax.text(0.5, -0.16, callout, transform=ax.transAxes, ha="center", va="top", fontsize=12.5,
            color=NAVY_BG, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=TEAL, ec=TEAL), clip_on=False)
    note = ("Source: Committee on Fair Employment Practice, First Report, Fair Employment Practice "
            "Committee, July 1943-December 1944 (Washington, 1 May 1945), govinfo.gov "
            "(GOVPUB-PR32_400). Series = nonwhite workers (~96% Negro) in firms reporting to the War "
            "Manpower Commission, not all U.S. employment. Migration callout: National Archives, "
            "\"The Great Migration (1910-1970)\" (archives.gov) - a separate multi-decade population "
            "movement figure, not an annual employment series; the two data series must not be "
            "implied as directly linked year-by-year. Verified 2026-08-01.")
    source_footer(fig, note, y=-0.26)
    save(fig, os.path.join(ROOT, "US.53", "US.53_black_migration_employment.png"))

    write_csv(os.path.join(ROOT, "US.53", "US.53_black_migration_employment.data.csv"),
               ["period", "nonwhite_share_pct", "note"],
               [["Early 1942", "<3 (rendered as open marker at 3.0, conservative upper bound)", "FEPC First Report"],
                ["Sep 1942", 4.6, "FEPC First Report"],
                ["Jan 1943", 6.4, "FEPC First Report"],
                ["Jan 1944", 7.2, "FEPC First Report"],
                ["Nov 1944", 8.3, "FEPC First Report"],
                ["NARA context", "~6,000,000 total Black migrants 1910s-1970s", "National Archives; not an annual series, not linked to FEPC series"]])
    write_svg_note(os.path.join(ROOT, "US.53", "US.53_black_migration_employment.svg"),
                    "US.53 Nonwhite Workforce Share", "FEPC First Report 1943-1944 / NARA Great Migration")


# =========================================================================
# US.54 — Incarceration by camp (WRA Table 5 peak populations)
# =========================================================================
def build_us54():
    print("US.54 incarceration by camp chart")
    camps = [
        ("Tule Lake", 18789, "12-25-44"),
        ("Colorado River (Poston)", 17814, "9-2-42"),
        ("Gila River", 13348, "12-30-42"),
        ("Heart Mountain", 10767, "1-1-43"),
        ("Manzanar", 10046, "9-22-42"),
        ("Minidoka", 9397, "3-1-43"),
        ("Jerome", 8497, "2-11-43"),
        ("Rohwer", 8475, "3-11-43"),
        ("Central Utah (Topaz)", 8130, "3-17-43"),
        ("Granada", 7318, "2-1-43"),
    ]
    labels = [c[0] for c in camps]
    vals = [c[1] for c in camps]
    dates = [c[2] for c in camps]
    bars_sum = sum(vals)

    fig = new_fig()
    ax = fig.add_subplot(111)
    y_pos = np.arange(len(labels))[::-1]
    ax.barh(y_pos, vals, color=GOLD, height=0.6, zorder=3, edgecolor=NAVY_BG)
    for y, v, d in zip(y_pos, vals, dates):
        ax.text(v + 250, y, f"{v:,}  (peak {d})", va="center", fontsize=11.5, color=CREAM)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=13)
    ax.set_xlabel("Peak resident population")
    ax.set_title("WRA camp peak populations occurred on different dates, 1942-1944",
                  loc="left", fontsize=21)
    ax.set_xlim(0, 22000)
    ax.grid(axis="x", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    callout = (f"Bars sum to {bars_sum:,} (peak dates differ) - NOT the same as\n"
               f"120,313 cumulative WRA custody over the program's full history")
    ax.text(0.98, 0.06, callout, transform=ax.transAxes, ha="right", va="bottom", fontsize=12.5,
            color=NAVY_BG, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc=RED, ec=RED))
    note = ("Source: U.S. Department of the Interior, War Relocation Authority, The Evacuated People: "
            "A Quantitative Description (1946), Table 5, PDF p.33 / printed p.17. fraser.stlouisfed.org "
            "| \"Resident population refers to population excluding evacuees on short-term and seasonal "
            "leave.\" 120,313 = total persons who came under WRA custody over the program's entire "
            "history (Figure 1); it is explicitly NOT a sum of the ten peak populations shown here "
            "(which sum to 112,581) because peaks occurred on different dates and because 120,313 "
            "includes institutionalized cases and seasonal workers never assigned to a center. "
            "Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.54", "US.54_incarceration_by_camp.png"))

    write_csv(os.path.join(ROOT, "US.54", "US.54_incarceration_by_camp.data.csv"),
               ["camp", "peak_resident_population", "peak_date", "state", "county", "post_office"],
               [["Central Utah (Topaz)", 8130, "3-17-43", "Utah", "Millard", "Topaz"],
                ["Colorado River (Poston)", 17814, "9-2-42", "Arizona", "Yuma", "Poston"],
                ["Gila River", 13348, "12-30-42", "Arizona", "Pinal", "Rivers"],
                ["Granada", 7318, "2-1-43", "Colorado", "Prowers", "Amache"],
                ["Heart Mountain", 10767, "1-1-43", "Wyoming", "Park", "Heart Mountain"],
                ["Jerome", 8497, "2-11-43", "Arkansas", "Drew & Chicot", "Denson"],
                ["Manzanar", 10046, "9-22-42", "California", "Inyo", "Manzanar"],
                ["Minidoka", 9397, "3-1-43", "Idaho", "Jerome", "Hunt"],
                ["Rohwer", 8475, "3-11-43", "Arkansas", "Desha", "Relocation"],
                ["Tule Lake", 18789, "12-25-44", "California", "Modoc", "Newell"],
                ["CUMULATIVE WRA CUSTODY (not sum of bars)", 120313, "program total 1942-1946", "", "", ""]])
    write_svg_note(os.path.join(ROOT, "US.54", "US.54_incarceration_by_camp.svg"),
                    "US.54 Incarceration by Camp", "WRA, The Evacuated People (1946), Table 5")


# =========================================================================
# US.55 — U.S. war production 1941-1945 (WPB Table B-6 munitions $, stacked)
# =========================================================================
def build_us55():
    print("US.55 war production chart")
    periods = ["1940 H2", "1941", "1942", "1943", "1944", "1945\n(Jan-Aug)"]
    categories = [
        ("Aircraft", [370, 1804, 5817, 12514, 16047, 8279]),
        ("Ships", [391, 1852, 6957, 12498, 13429, 6011]),
        ("Combat & motor vehicles", [238, 1285, 4778, 5926, 4951, 3138]),
        ("Ammunition", [87, 427, 2743, 4908, 5768, 4173]),
        ("Guns & fire control", [78, 355, 1794, 3180, 2926, 1471]),
        ("Communication & electronic equip.", [27, 226, 1512, 3043, 3739, 2212]),
        ("Other equipment & supplies", [856, 2493, 6567, 9676, 10734, 7869]),
    ]
    x = np.arange(len(periods))
    fig = new_fig()
    ax = fig.add_subplot(111)
    bottom = np.zeros(len(periods))
    for i, (name, vals) in enumerate(categories):
        vals = np.array(vals) / 1000.0  # -> billions of 1945 munitions dollars
        # visually distinguish partial periods 1940H2 and 1945 Jan-Aug with lighter alpha + hatch
        colors_bar = []
        alphas = []
        ax.bar(x, vals, bottom=bottom, color=CATEGORICAL[i % len(CATEGORICAL)], width=0.6,
               edgecolor=NAVY_BG, zorder=3, label=name)
        bottom += vals
    # overlay hatch on partial-period bars (index 0 and 5) to visually flag them
    for container in ax.containers:
        pass
    # Add hatch overlay boxes for partial periods
    for idx in [0, 5]:
        ax.add_patch(mpatches.Rectangle((idx - 0.3, 0), 0.6, bottom[idx], fill=False,
                                          hatch="....", edgecolor=NAVY_BG, lw=0, zorder=4, alpha=0.35))
    for xi, v in zip(x, bottom):
        ax.text(xi, v + 0.6, f"${v:.1f}B", ha="center", fontsize=12.5, color=CREAM, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(periods, fontsize=12.5)
    ax.set_ylabel("Munitions production (billions of constant 1945 munitions $)")
    ax.set_title("U.S. munitions production nearly tripled from 1942 to 1943, then peaked in 1944",
                  loc="left", fontsize=20)
    ax.set_ylim(0, 65)
    ax.legend(loc="upper left", frameon=False, fontsize=10.5, labelcolor=CREAM, ncol=2)
    ax.grid(axis="y", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.99, 0.97, "Dotted overlay = partial-period totals\n(1940 H2 and 1945 Jan-Aug only)",
            transform=ax.transAxes, ha="right", va="top", fontsize=10.5, color=CREAM_MUTED, style="italic")
    note = ("Source: War Production Board, Program and Statistics Bureau, Table B-6 \"Munitions "
            "Production by Type (July 1940 to August 1945),\" reprinted in Office of Technology "
            "Assessment (OTA), Appendix B - Conservation in World War II: 1933-45. "
            "princeton.edu/~ota | Values are in millions of constant 1945 munitions dollars, converted "
            "here to billions. 1940 and 1945 bars are PARTIAL PERIODS (Jul-Dec 1940; Jan-Aug 1945) - "
            "visually flagged with a dotted overlay; only 1941-1944 are full-year totals. Excludes GDP "
            "percentage, tank unit counts, and unverified aircraft Table 74 figures per verified "
            "sourcing manifest. Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.55", "US.55_us_war_production_1941_1945.png"))

    write_csv(os.path.join(ROOT, "US.55", "US.55_us_war_production_1941_1945.data.csv"),
               ["category", "1940_H2_millions", "1941_millions", "1942_millions", "1943_millions",
                "1944_millions", "1945_JanAug_millions"],
               [[name] + vals for name, vals in categories])
    write_svg_note(os.path.join(ROOT, "US.55", "US.55_us_war_production_1941_1945.svg"),
                    "US.55 War Production by Type", "WPB Table B-6 via OTA Appendix B")


# =========================================================================
# US.56 — Hiroshima and Nagasaki casualties (1946 MED estimates)
# =========================================================================
def build_us56():
    print("US.56 hiroshima nagasaki casualties chart")
    cities = ["Hiroshima", "Nagasaki"]
    dead = [66000, 39000]
    injured = [69000, 25000]

    fig = new_fig()
    ax = fig.add_subplot(111)
    x = np.arange(len(cities))
    w = 0.32
    b1 = ax.bar(x - w/2, dead, width=w, color=RED, label="Dead (1946 MED estimate)", zorder=3, edgecolor=NAVY_BG)
    b2 = ax.bar(x + w/2, injured, width=w, color=GOLD, label="Injured (1946 MED estimate)", zorder=3, edgecolor=NAVY_BG, hatch="//")
    for rects in (b1, b2):
        for r in rects:
            h = r.get_height()
            ax.text(r.get_x() + r.get_width()/2, h + 1500, f"{int(h):,}", ha="center", fontsize=14, color=CREAM, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(cities, fontsize=16)
    ax.set_ylabel("Persons (1946 estimate)")
    ax.set_title("1946 Manhattan Engineer District estimates - not exact counts",
                  loc="left", fontsize=22)
    ax.legend(loc="upper right", frameon=False, fontsize=13, labelcolor=CREAM)
    ax.set_ylim(0, 82000)
    ax.grid(axis="y", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    note = ("Source: \"The Atomic Bombings of Hiroshima and Nagasaki,\" Manhattan Engineer District, "
            "United States Army, 29 June 1946, Table A \"Estimates of Casualties\" (public domain). "
            "gutenberg.org/ebooks/685 | Report's own uncertainty statement (verbatim): \"There has "
            "been great difficulty in estimating the total casualties in the Japanese cities as a "
            "result of the atomic bombing... the state of utter confusion immediately following the "
            "explosion, as well as the uncertainty regarding the actual population before the "
            "bombing, contribute to the difficulty.\" These are the 1946 MED figures ONLY; later "
            "estimates diverge widely and are not shown here. Verified 2026-08-01.")
    source_footer(fig, note)
    save(fig, os.path.join(ROOT, "US.56", "US.56_hiroshima_nagasaki_casualties.png"))

    write_csv(os.path.join(ROOT, "US.56", "US.56_hiroshima_nagasaki_casualties.data.csv"),
               ["city", "dead_1946_med_estimate", "injured_1946_med_estimate", "pre_raid_population"],
               [["Hiroshima", 66000, 69000, 255000], ["Nagasaki", 39000, 25000, 195000]])
    write_svg_note(os.path.join(ROOT, "US.56", "US.56_hiroshima_nagasaki_casualties.svg"),
                    "US.56 Hiroshima/Nagasaki Casualties", "Manhattan Engineer District report, 1946, Table A")


# =========================================================================
# US.58 — UN founding members timeline
# =========================================================================
def build_us58():
    print("US.58 UN founding timeline chart")
    events = [
        ("25 Jun 1945", "Charter adopted", "delegates of fifty nations adopt\nthe UN Charter at San Francisco"),
        ("26 Jun 1945", "Charter signed", "Charter signed at the\nSan Francisco Conference"),
        ("15 Oct 1945", "Poland signs", "Poland signs the Charter,\nbecoming an original member"),
        ("24 Oct 1945", "Entry into force", "Charter enters into force\n(UN Charter, Article 110 para. 3)"),
    ]
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, layout="constrained")
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-2.3, 2.3)
    ax.axhline(0, color=STEEL, lw=2.5, zorder=1)
    xs = list(range(4))
    colors_pts = [GOLD, GOLD, RED, TEAL]
    for i, (date, title, desc) in enumerate(events):
        ax.scatter([i], [0], s=420, color=colors_pts[i], edgecolor=NAVY_BG, linewidth=2.5, zorder=3)
        y_text = 0.55 if i % 2 == 0 else -0.55
        va = "bottom" if i % 2 == 0 else "top"
        ax.plot([i, i], [0, y_text], color=STEEL, lw=1.2, zorder=2)
        ax.text(i, y_text + (0.08 if i % 2 == 0 else -0.08), f"{date}\n{title}", ha="center", va=va,
                 fontsize=14, color=CREAM, fontweight="bold")
        y_desc = y_text + (0.62 if i % 2 == 0 else -0.62)
        ax.text(i, y_desc, desc, ha="center", va=va, fontsize=10.5, color=CREAM_MUTED)
    ax.axis("off")
    ax.set_title("From adoption to entry into force: the UN Charter, 1945", loc="left", fontsize=23, x=0.0, y=0.94)
    ax.text(0.5, 0.03, "51 ORIGINAL MEMBER STATES", transform=ax.transAxes, ha="center", va="center",
            fontsize=20, color=NAVY_BG, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.6", fc=GOLD, ec=GOLD))
    note = ("Source: United Nations, \"The San Francisco Conference,\" un.org/en/about-us/history-of-"
            "the-un/san-francisco-conference | UN page states \"delegates of fifty nations in all, "
            "gathered at the San Francisco Conference in April 1945\" - phrased here as \"delegates of "
            "fifty nations,\" NOT as an unverified exact \"50 signatories,\" per verified sourcing "
            "manifest. Poland signed later (15 Oct 1945), bringing original membership to 51. Charter "
            "adopted 25 Jun 1945, signed 26 Jun 1945, entered into force 24 Oct 1945 (Article 110, "
            "para. 3). Verified 2026-08-01.")
    source_footer(fig, note, y=-0.02)
    save(fig, os.path.join(ROOT, "US.58", "US.58_un_founding_members_timeline.png"))

    write_csv(os.path.join(ROOT, "US.58", "US.58_un_founding_members_timeline.data.csv"),
               ["date", "event"],
               [["1945-06-25", "UN Charter adopted (delegates of fifty nations)"],
                ["1945-06-26", "UN Charter signed at San Francisco Conference"],
                ["1945-10-15", "Poland signs the Charter"],
                ["1945-10-24", "Charter enters into force (Article 110, para. 3); 51 original members"]])
    write_svg_note(os.path.join(ROOT, "US.58", "US.58_un_founding_members_timeline.svg"),
                    "US.58 UN Founding Timeline", "United Nations, The San Francisco Conference")


# =========================================================================
# FRESH MAPS using US states GeoJSON basemap (schematic, PD-derived
# boundary data; US Census-style state outlines are not protected
# expression)
# =========================================================================
def load_states():
    with open(os.path.join(ROOT, "_basemap_data", "us-states.json")) as f:
        return json.load(f)


def draw_us_basemap(ax, states_geo, fc=NAVY_PANEL, ec=STEEL, lw=0.6, exclude=("Alaska", "Hawaii", "Puerto Rico")):
    for feat in states_geo["features"]:
        name = feat["properties"]["name"]
        if name in exclude:
            continue
        geom = feat["geometry"]
        polys = geom["coordinates"] if geom["type"] == "Polygon" else [p for multi in geom["coordinates"] for p in [multi]]
        if geom["type"] == "Polygon":
            polys = [geom["coordinates"]]
        else:
            polys = geom["coordinates"]
        for poly in polys:
            ring = poly[0]
            xs = [p[0] for p in ring]
            ys = [p[1] for p in ring]
            ax.fill(xs, ys, fc=fc, ec=ec, lw=lw, zorder=1)


# City / state approximate lon/lat for label placement (well-known, factual
# public coordinates; used only for point placement on a schematic map)
US_CITY_COORDS = {
    "Chicago, IL": (-87.63, 41.88),
    "Detroit, MI": (-83.05, 42.33),
    "New York, NY": (-74.01, 40.71),
    "Philadelphia, PA": (-75.16, 39.95),
}
SOUTH_LABEL_POS = (-89.5, 32.5)  # approx central Deep South for arrow origin


def build_us53_map():
    print("US.53 Great Migration schematic map")
    states_geo = load_states()
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, layout="constrained")
    ax = fig.add_subplot(111)
    draw_us_basemap(ax, states_geo)
    ax.set_xlim(-125, -66)
    ax.set_ylim(24, 50)
    ax.set_aspect(1.3)
    ax.axis("off")

    origin = SOUTH_LABEL_POS
    ax.scatter([origin[0]], [origin[1]], s=260, color=RED, edgecolor=NAVY_BG, linewidth=2, zorder=5)
    ax.text(origin[0], origin[1] - 1.6, "The American South\n(region of origin)", ha="center", va="top",
            fontsize=13, color=CREAM, fontweight="bold", zorder=6)

    for city, (lon, lat) in US_CITY_COORDS.items():
        ax.scatter([lon], [lat], s=200, color=GOLD, edgecolor=NAVY_BG, linewidth=2, zorder=5, marker="^")
        ax.annotate("", xy=(lon, lat), xytext=origin,
                    arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=2.2, alpha=0.85,
                                     connectionstyle="arc3,rad=0.12"), zorder=4)
        offset_y = 1.1 if city != "Philadelphia, PA" else -1.6
        va = "bottom" if offset_y > 0 else "top"
        ax.text(lon, lat + offset_y, city.split(",")[0], ha="center", va=va, fontsize=13,
                 color=CREAM, fontweight="bold", zorder=6)

    ax.set_title("Schematic migration flows, not person-by-person routes", loc="left", fontsize=22, color=GOLD)
    ax.text(0.01, 0.99, "The Great Migration, approx. 1910s-1970s", transform=ax.transAxes,
            ha="left", va="top", fontsize=16, color=CREAM, fontweight="bold")
    stat_box = ("Approx. 6,000,000 total, 1910s-1970s\n"
                "About 2,000,000 by WWII (through ~1940)\n"
                "A further ~3,000,000 within 20 years after WWII")
    ax.text(0.99, 0.02, stat_box, transform=ax.transAxes, ha="right", va="bottom", fontsize=13,
            color=NAVY_BG, bbox=dict(boxstyle="round,pad=0.5", fc=GOLD, ec=GOLD), zorder=7)
    note = ("Basemap: U.S. state boundaries (public geographic data, PublicaMundi MappingAPI "
            "us-states.json, derived from U.S. Census TIGER boundaries - factual geographic boundary "
            "data, not protected expression). Migration figures: National Archives, \"The Great "
            "Migration (1910-1970)\" (archives.gov/research/african-americans/migrations/"
            "great-migration): \"Approximately six million Black people moved from the American South "
            "to Northern, Midwestern, and Western states roughly from the 1910s until the 1970s\"; "
            "\"about two million\" by WWII; \"within twenty years of World War II, a further three "
            "million.\" Destination cities per U.S. Census Bureau framing (Chicago, Detroit, New York, "
            "Philadelphia). Arrows are schematic directional flows ONLY - they do not represent actual "
            "travel routes, rail lines, or individual migrant paths. Verified 2026-08-01.")
    source_footer(fig, note, y=-0.03)
    save(fig, os.path.join(ROOT, "US.53", "US.53_great_migration_map.jpg"))


def build_us54_map():
    print("US.54 WRA camps schematic map")
    states_geo = load_states()
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, layout="constrained")
    ax = fig.add_subplot(111)
    draw_us_basemap(ax, states_geo)
    ax.set_xlim(-125, -85)
    ax.set_ylim(30, 49)
    ax.set_aspect(1.3)
    ax.axis("off")

    # Approximate lon/lat for each center's county/post-office location
    # (public/factual geographic locations; approximate placement only)
    camps = [
        ("Central Utah\n(Topaz)", "UT", -112.78, 39.32),
        ("Colorado River\n(Poston)", "AZ", -114.39, 33.98),
        ("Gila River", "AZ", -111.68, 33.13),
        ("Granada\n(Amache)", "CO", -102.35, 38.05),
        ("Heart Mountain", "WY", -109.20, 44.51),
        ("Jerome\n(Denson)", "AR", -91.43, 33.43),
        ("Manzanar", "CA", -118.15, 36.73),
        ("Minidoka\n(Hunt)", "ID", -114.24, 42.67),
        ("Rohwer", "AR", -91.28, 33.78),
        ("Tule Lake\n(Newell)", "CA", -121.48, 41.93),
    ]
    # label offset overrides for closely-spaced camps (Jerome & Rohwer, AR are
    # only ~0.35 deg apart) to avoid text collision
    label_offsets = {
        "Jerome\n(Denson)": (-1.7, -0.1, "right"),
        "Rohwer": (1.6, 0.55, "left"),
    }
    for name, st, lon, lat in camps:
        ax.scatter([lon], [lat], s=230, color=GOLD, edgecolor=NAVY_BG, linewidth=2, marker="s", zorder=5)
        if name in label_offsets:
            dx, dy, ha = label_offsets[name]
            ax.text(lon + dx, lat + dy, f"{name} ({st})", ha=ha, va="bottom", fontsize=10.5,
                     color=CREAM, fontweight="bold", zorder=6)
        else:
            ax.text(lon, lat + 0.55, f"{name} ({st})", ha="center", va="bottom", fontsize=10.5,
                     color=CREAM, fontweight="bold", zorder=6)

    ax.set_title("10 War Relocation Authority centers, 1942-1946", loc="left", fontsize=22, color=GOLD)
    ax.text(0.01, 0.02,
            "Symbols mark approximate post-office/county locations from WRA Table 5,\nnot camp boundaries or exact site footprints.",
            transform=ax.transAxes, ha="left", va="bottom", fontsize=12.5, color=CREAM_MUTED)
    note = ("Basemap: U.S. state boundaries (public geographic data, PublicaMundi MappingAPI "
            "us-states.json - factual boundary data). Locations: U.S. Department of the Interior, "
            "War Relocation Authority, The Evacuated People: A Quantitative Description (1946), "
            "Table 5, state/county/post office for each center (fraser.stlouisfed.org). Marker "
            "positions are approximate placements for the named post office/county and are for "
            "orientation only - not authoritative site boundaries or camp perimeters. "
            "Verified 2026-08-01.")
    source_footer(fig, note, y=-0.10)
    save(fig, os.path.join(ROOT, "US.54", "US.54_wra_camps_map.jpg"))


def build_us56_map():
    print("US.56 Manhattan Project sites map (PNG)")
    states_geo = load_states()
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, layout="constrained")
    ax = fig.add_subplot(111)
    draw_us_basemap(ax, states_geo)
    ax.set_xlim(-125, -66)
    ax.set_ylim(24, 50)
    ax.set_aspect(1.3)
    ax.axis("off")

    sites = [
        ("Oak Ridge, Tennessee", -84.27, 36.01, GOLD, True),
        ("Los Alamos, New Mexico", -106.30, 35.89, TEAL, False),
        ("Hanford, Washington", -119.60, 46.55, RED, False),
    ]
    for name, lon, lat, color, prominent in sites:
        size = 420 if prominent else 260
        ax.scatter([lon], [lat], s=size, color=color, edgecolor=NAVY_BG, linewidth=2.5, zorder=5)
        fs = 17 if prominent else 14
        fw = "bold"
        ax.text(lon, lat + 1.3, name, ha="center", va="bottom", fontsize=fs, color=CREAM,
                 fontweight=fw, zorder=6)

    ax.set_title("The three NPS-confirmed Manhattan Project National Historical Park sites",
                  loc="left", fontsize=21, color=GOLD)
    ax.text(0.01, 0.02, "Oak Ridge, Tennessee is highlighted as the largest of the three park units.",
            transform=ax.transAxes, ha="left", va="bottom", fontsize=13, color=CREAM_MUTED)
    note = ("Basemap: U.S. state boundaries (public geographic data, PublicaMundi MappingAPI "
            "us-states.json - factual boundary data). Sites per National Park Service, Manhattan "
            "Project National Historical Park official page: Oak Ridge, Tennessee; Los Alamos, New "
            "Mexico; Hanford, Washington (nps.gov/mapr/learn/manhattan-project.htm). Only these three "
            "NPS-confirmed park units are shown; other wartime Manhattan Project facilities "
            "(e.g. Chicago Met Lab, Trinity Site, Dayton) are not NPS park units and are intentionally "
            "excluded from this map. Verified 2026-08-01.")
    source_footer(fig, note, y=-0.03)
    save(fig, os.path.join(ROOT, "US.56", "US.56_manhattan_project_sites_map.png"))


# =========================================================================
# Main
# =========================================================================
def main():
    print("=" * 70)
    print("History Hack Unit 6 — building fresh data graphics + schematic maps")
    print("=" * 70)
    build_us45()
    build_us46()
    build_us47()
    build_us48()
    build_us50()
    build_us52()
    build_us53()
    build_us54()
    build_us55()
    build_us56()
    build_us58()
    print("-" * 70)
    print("Schematic maps (US states basemap)")
    build_us53_map()
    build_us54_map()
    build_us56_map()
    print("=" * 70)
    print("Build complete.")


if __name__ == "__main__":
    main()
