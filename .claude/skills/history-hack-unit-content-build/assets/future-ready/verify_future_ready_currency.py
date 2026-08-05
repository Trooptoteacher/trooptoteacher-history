#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Future Ready CURRENCY guardrail — fails CI when time-sensitive figures go stale.

Enforces, against future_ready_data.json:
  1. PROVENANCE  — every figure carries source + source_url + last_verified.
  2. ANNUAL GATE — hard-fail once _meta.review_by has passed (forces yearly re-verify).
  3. FRESHNESS   — warn when the latest published loan-rate academic year is behind
                   the current academic year (a newer federal rate probably exists).
  4. SANITY      — chart_example_apr sits within the range of the known rate table;
                   dates parse; last_verified is not in the future.

Exit code 0 = pass (warnings allowed), 1 = fail (blocks the build/PR).
Run: python3 verify_future_ready_currency.py [path/to/future_ready_data.json]
CI runs it on every PR AND on a monthly schedule so an overdue review surfaces
within ~30 days even with no code change.
"""
import json, sys, os
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "future_ready_data.json")

fails, warns = [], []
def fail(m): fails.append(m)
def warn(m): warns.append(m)

def parse_d(s, where):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        fail(f"{where}: bad date '{s}' (want YYYY-MM-DD)"); return None

def current_academic_year(today):
    # Federal Direct Loan rates are effective for loans first disbursed July 1.
    y = today.year
    start = y if today.month >= 7 else y - 1
    return f"{start}-{str(start+1)[2:]}"

def check_provenance(name, obj):
    for f in ("source", "source_url", "last_verified"):
        if not obj.get(f):
            fail(f"{name}: missing required provenance field '{f}'")
    lv = obj.get("last_verified")
    if lv:
        d = parse_d(lv, f"{name}.last_verified")
        if d and d > TODAY:
            fail(f"{name}: last_verified '{lv}' is in the future")

def main():
    global TODAY
    TODAY = date.today()
    if not os.path.exists(PATH):
        print(f"FAIL: data file not found: {PATH}"); sys.exit(1)
    data = json.load(open(PATH))
    meta = data.get("_meta", {})

    # 2. ANNUAL GATE
    rb = meta.get("review_by")
    if not rb:
        fail("_meta.review_by is missing (annual gate cannot be enforced)")
    else:
        d = parse_d(rb, "_meta.review_by")
        if d:
            if TODAY > d:
                fail(f"ANNUAL REVIEW OVERDUE — review_by {rb} has passed. "
                     f"{meta.get('review_trigger','Re-verify every figure, bump dates, move review_by forward one year.')}")
            elif (d - TODAY).days <= 60:
                warn(f"Annual review due soon ({rb}, in {(d-TODAY).days} days).")

    # 1. PROVENANCE on every figure (time-sensitive + historical)
    ts = data.get("time_sensitive", {})
    hs = data.get("historical_stable", {})
    if not ts:
        fail("time_sensitive block is empty")
    for name, obj in list(ts.items()) + list(hs.items()):
        check_provenance(f"{name}", obj)

    # 3 + 4. Loan-rate freshness + example-APR sanity
    rates = ts.get("direct_loan_rates_undergrad", {}).get("by_year", {})
    if not rates:
        fail("direct_loan_rates_undergrad.by_year is empty")
    else:
        years = sorted(rates.keys())
        latest = years[-1]
        cay = current_academic_year(TODAY)
        if latest < cay:
            warn(f"Latest loan-rate year on file is {latest}, but the current academic year is {cay}. "
                 f"A newer federal rate likely published — verify at "
                 f"{ts['direct_loan_rates_undergrad'].get('source_url')} and add it.")
        vals = list(rates.values())
        ex = ts.get("chart_example_apr", {}).get("value")
        if ex is None:
            fail("chart_example_apr.value missing")
        elif not (min(vals) - 1.0 <= ex <= max(vals) + 1.0):
            fail(f"chart_example_apr {ex}% is outside the plausible range of the rate table "
                 f"[{min(vals)}–{max(vals)}] — is it still representative?")

    # Report
    print("=" * 64)
    print("FUTURE READY — CURRENCY GUARDRAIL")
    print(f"data: {os.path.relpath(PATH, HERE)}   today: {TODAY}   review_by: {meta.get('review_by')}")
    print("=" * 64)
    for w in warns: print(f"  ⚠ WARN  {w}")
    for f in fails: print(f"  ✗ FAIL  {f}")
    if not fails:
        print(f"  ✓ PASS  provenance complete on all figures; annual gate not yet overdue"
              + (f"; {len(warns)} warning(s)" if warns else ""))
    print("=" * 64)
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
