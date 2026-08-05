#!/usr/bin/env python3
"""
WCS Technology Use Guidance — compliance guardrail.

This is the machine-checkable "no breach" proof. It reads the single source of
truth (`requirements.json`) and FAILS (exit 1) if any WCS requirement is not
backed by real, resolvable evidence — so "we meet or exceed the law" can never
drift into an unverified assertion.

Fails on any of:
  1. A requirement whose status is "gap" (an unmet WCS requirement).
  2. A requirement with NO resolvable evidence of any kind — nothing proves it.
  3. Any "doctrine"/"repo" evidence path that does not exist or is an empty file.
  4. Any "webapp" evidence path that is missing WHEN the web app is co-located
     (env WEBAPP_ROOT, or a sibling history-hack-web-app checkout). When the web
     app is absent, webapp evidence is reported as "declared" (cross-repo) and
     does not fail the run — UNLESS --require-webapp is set (CI mode), which makes
     an absent web app a hard error so declared evidence can never mask a gap.
  5. A malformed registry (bad posture/status/kind, missing fields, duplicate id).

The authoritative run (CI) co-locates the web app and passes --require-webapp, so
every requirement is verified against real product code. A content-repo-only run
still verifies all doctrine/repo anchors and prints which requirements remain
"declared" pending the web app.

Usage:
  python3 verify_wcs_compliance.py [--json] [--webapp-root PATH] [--require-webapp]

Exit codes: 0 = all requirements proven; 1 = one or more breaches/unresolved.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "requirements.json"
# content repo root = .../trooptoteacher-history (this file is at 06_.../wcs-technology-use/)
CONTENT_ROOT = HERE.parent.parent

VALID_POSTURE = {"meets", "exceeds"}
VALID_STATUS = {"verified", "declared", "gap"}
VALID_KINDS = {"doctrine", "repo", "webapp", "webapp_route", "external"}
CONTENT_KINDS = {"doctrine", "repo"}


def find_webapp_root(cli_value: str | None) -> Path | None:
    """Locate a co-located history-hack-web-app checkout, if any.

    Pass --webapp-root none (or WEBAPP_ROOT=none) to force content-only mode
    even when a web app is present on disk — used to test/run the exact
    behavior CI sees when the web app is not checked out.
    """
    env_val = os.environ.get("WEBAPP_ROOT")
    if (cli_value and cli_value.lower() == "none") or (env_val and env_val.lower() == "none"):
        return None
    candidates = []
    if cli_value:
        candidates.append(Path(cli_value))
    if env_val:
        candidates.append(Path(env_val))
    # common sibling locations
    candidates.append(CONTENT_ROOT.parent / "history-hack-web-app")
    candidates.append(Path("/workspace/history-hack-web-app"))
    for c in candidates:
        try:
            if c.is_dir() and (c / "package.json").exists():
                return c.resolve()
        except OSError:
            continue
    return None


def resolvable(root: Path, ref: str) -> bool:
    """A path evidence resolves if it exists and is a non-empty file or a dir."""
    p = (root / ref).resolve()
    # keep evidence inside the repo it claims to be in
    try:
        p.relative_to(root)
    except ValueError:
        return False
    if p.is_dir():
        return any(p.iterdir())
    if p.is_file():
        return p.stat().st_size > 0
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="WCS Technology Use Guidance compliance guardrail")
    ap.add_argument("--json", action="store_true", help="emit a JSON report")
    ap.add_argument("--webapp-root", default=None, help="path to a history-hack-web-app checkout")
    ap.add_argument("--require-webapp", action="store_true",
                    help="CI mode: fail if the web app is not co-located (no declared-only passes)")
    args = ap.parse_args()

    if not REGISTRY.exists():
        print(f"FATAL: registry not found at {REGISTRY}", file=sys.stderr)
        return 1
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FATAL: requirements.json is not valid JSON: {e}", file=sys.stderr)
        return 1

    reqs = data.get("requirements", [])
    if not reqs:
        print("FATAL: registry has no requirements", file=sys.stderr)
        return 1

    webapp_root = find_webapp_root(args.webapp_root)

    errors: list[str] = []
    warnings: list[str] = []
    declared: list[str] = []
    seen_ids: set[str] = set()
    counts = {"meets": 0, "exceeds": 0}
    webapp_checked = 0
    webapp_declared = 0

    if args.require_webapp and webapp_root is None:
        errors.append(
            "[require-webapp] CI mode: the history-hack-web-app checkout was not found "
            "(set --webapp-root or WEBAPP_ROOT). Cannot authoritatively verify webapp evidence."
        )

    for r in reqs:
        rid = r.get("id", "<no-id>")
        if rid in seen_ids:
            errors.append(f"[dup] duplicate requirement id '{rid}'")
        seen_ids.add(rid)

        for field in ("id", "group", "source", "requirement", "hh_response", "posture", "status", "evidence"):
            if not r.get(field):
                errors.append(f"[schema] {rid}: missing required field '{field}'")

        posture = r.get("posture")
        if posture not in VALID_POSTURE:
            errors.append(f"[schema] {rid}: invalid posture '{posture}'")
        else:
            counts[posture] += 1

        status = r.get("status")
        if status not in VALID_STATUS:
            errors.append(f"[schema] {rid}: invalid status '{status}'")

        # 1. an unmet requirement is a breach
        if status == "gap":
            errors.append(f"[gap] {rid}: WCS requirement is UNMET (status=gap) — {r.get('source','')}")

        evidence = r.get("evidence", []) or []
        resolved_count = 0        # evidence entries proven on disk right now
        declared_count = 0        # webapp entries pending a co-located web app
        for ev in evidence:
            kind = ev.get("kind")
            ref = ev.get("ref", "")
            if kind not in VALID_KINDS:
                errors.append(f"[schema] {rid}: invalid evidence kind '{kind}'")
                continue
            if kind in CONTENT_KINDS:
                if resolvable(CONTENT_ROOT, ref):
                    resolved_count += 1
                else:
                    errors.append(f"[missing] {rid}: content evidence '{ref}' (kind={kind}) does not resolve in content repo")
            elif kind == "webapp":
                if webapp_root is not None:
                    if resolvable(webapp_root, ref):
                        resolved_count += 1
                        webapp_checked += 1
                    else:
                        errors.append(f"[missing] {rid}: webapp evidence '{ref}' not found in {webapp_root.name}")
                else:
                    declared_count += 1
                    webapp_declared += 1
            # webapp_route and external are informational; the web app's own
            # product-edition registry test enforces route existence.

        # 2. every requirement must be proven by at least one resolvable evidence.
        if not evidence:
            errors.append(f"[anchor] {rid}: has no evidence at all")
        elif resolved_count == 0:
            if declared_count > 0 and not args.require_webapp:
                # webapp-only requirement, web app not co-located: report, do not fail.
                declared.append(f"{rid}: proven only by web-app evidence (co-locate the web app to verify)")
            else:
                errors.append(f"[anchor] {rid}: no resolvable evidence — nothing proves this requirement")

    total = len(reqs)
    report = {
        "total_requirements": total,
        "meets": counts["meets"],
        "exceeds": counts["exceeds"],
        "webapp_root": str(webapp_root) if webapp_root else None,
        "webapp_evidence_checked": webapp_checked,
        "webapp_evidence_declared_cross_repo": webapp_declared,
        "requirements_declared_pending_webapp": declared,
        "errors": errors,
        "warnings": warnings,
        "pass": not errors,
    }

    if args.json:
        print(json.dumps(report, indent=2))
        return 0 if not errors else 1

    print("=" * 72)
    print("WCS TECHNOLOGY USE GUIDANCE — COMPLIANCE GUARDRAIL")
    print("=" * 72)
    print(f"Requirements checked : {total}")
    print(f"  meets              : {counts['meets']}")
    print(f"  exceeds            : {counts['exceeds']}")
    if webapp_root:
        print(f"Web app co-located   : {webapp_root}")
        print(f"  webapp evidence OK : {webapp_checked}")
    else:
        print(f"Web app             : not co-located — {webapp_declared} webapp evidences declared (cross-repo)")
    if declared:
        print("-" * 72)
        print(f"Declared pending web app ({len(declared)}) — co-locate the web app for full proof:")
        for d in declared:
            print("  ~ " + d)
    print("-" * 72)
    if errors:
        print(f"FAILED — {len(errors)} breach(es)/unresolved evidence:\n")
        for e in errors:
            print("  " + e)
        print(f"\n{len(errors)} problem(s). No requirement may ship in breach.")
        return 1
    print("PASS — every WCS requirement is backed by resolvable evidence; no breach.")
    print("Where History Hack EXCEEDS the requirement is marked in the printable matrix.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
