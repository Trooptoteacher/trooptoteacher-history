# WCS Technology Use Guidance — Compliance (embedding + no-breach proof)

**Purpose.** Prove — with evidence a skeptic can check — that every requirement of the
**WCS Technology Use Guidance (2026)** and the laws, board policies, SOPs, and research frameworks it
cites is embedded in U.S. History Hack, that **nothing is in breach**, and to make **where we meet or
exceed the law visible** to any board member, parent, principal, or reviewer.

Owned by the `wcs-technology-use-compliance` skill (`.claude/skills/`).

## The three files

| File | What it is |
|---|---|
| `requirements.json` | **Single source of truth.** Every WCS requirement as a cited row with its posture (meets/exceeds) and resolvable evidence. If a claim isn't here, it isn't proven. |
| `verify_wcs_compliance.py` | **The guardrail.** Fails (exit 1) on any unmet requirement, unresolvable evidence, evidence-less requirement, or malformed registry. This is the machine "no breach" proof. |
| `build_wcs_matrix.py` | **The skeptic-facing artifact.** Generates `wcs-technology-use-matrix.html` — a print-first, America 250 matrix (law → requirement → how we meet it → MEETS/EXCEEDS → evidence). |
| `requirements.schema.json` | JSON Schema for `requirements.json`. |
| `wcs-technology-use-matrix.html` | Generated. Print or Save-as-PDF; hand to any skeptic. Do not hand-edit — regenerate. |

## Run it

```bash
# Guardrail — content-only (verifies all doctrine/repo anchors, schema, no gaps):
python3 verify_wcs_compliance.py

# Authoritative — also verifies web-app evidence (co-locate the web app):
WEBAPP_ROOT=/path/to/history-hack-web-app python3 verify_wcs_compliance.py --require-webapp

# (Re)build the skeptic-facing matrix:
python3 build_wcs_matrix.py
```

## Evidence kinds

- **doctrine / repo** — files in this curriculum repo (always checked).
- **webapp / webapp_route** — the History Hack web application (checked when co-located; the app's own
  product-edition registry test independently enforces route existence).
- **external** — the cited statute, policy, or framework (citation only).

## Contract (why this is trustworthy)

1. Posture `meets`/`exceeds` requires **resolvable evidence** — never an assertion.
2. **No fabrication** — no invented routes, policy numbers, citations, or effect sizes. An honest gap is a `gap`, and a `gap` fails the guardrail.
3. The matrix is **generated from the registry**, so it cannot drift from the verified truth.
4. Reviewed quarterly (Aug/Nov/Feb/May) alongside `../ADMINISTRATIVE_REVIEW.md`.

Content accuracy follows **TDOE Policy 2.600**.
