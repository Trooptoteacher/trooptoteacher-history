---
name: history-hack-primary-source-manifest
description: "Fail-closed executability gate + operating prompt for producing DOWNLOAD-READY, rights-cleared, retrieval-tested primary-source manifests for the History Hack Social Studies suite (Grades 6–8, Tennessee History, World History, U.S. History, Government). This is the sourcing-pipeline contract that turns a standard→source sourcing list into machine-readable records a download agent can execute WITHOUT new research. Owns the three-tier manifest workflow (candidate=RED lead / manual_review=YELLOW / production=GREEN), the versioned v2 schema (exact item identity, item-level rights evidence, retrieval-test results), and the standard-library validator that rejects search/collection URLs, compound multi-asset rows, unresolved or non-commercial rights, missing item IDs, untested downloads, MIME/extension mismatches, and bad image metadata. Use when the user wants to source, verify, or vet primary sources for download; build or validate a primary-source manifest; stand up the manifest-readiness CI gate; or produce candidate / manual-review / production manifests per course-unit. Distinct lane from history-hack-dbq-workbook (which CONSUMES cleared sources into a DBQ product), copyright-integrity-accreditation (IP/FERPA-COPPA policy review), and historian-factcheck-agent (claim-by-claim factual verification). It reports and gates; it does not author lessons."
license: Proprietary
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "2.0"
  schema: "primary-source-manifest-v2 (schema_version 2.0)"
  reference_repository: "-2026-27-Social-Studies-Primary-Sources"
  origin: "Codified to stop search-page/compound/untested rows reaching the download pipeline."
---

# History Hack — Primary-Source Manifest (download-ready, rights-cleared, tested)

## Why this exists

A primary source is only *usable* when a machine can fetch the exact item, we can prove its rights
at the item level, and the fetch has actually been tested. A sourcing list full of repository search
pages, "see the LOC collection" leads, or two-books-in-one rows looks complete but is **not
executable** — feed it to a downloader and it fails, or worse, pulls the wrong asset or a rights-
encumbered one. This skill is the fail-closed gate that makes that class of defect impossible to ship
silently. It complements the Schedule F / policy screen (which asks "is this a good source for the
standard?") by answering the orthogonal question: **"can we actually download this exact item, are we
allowed to, and did we prove it?"**

Accuracy and rights are foundational (Policy 2.600 · Rule 7 zero-copyright-risk). An unresolved right
or an untested link is a blocker, not a footnote.

## The three-tier contract (one exact asset per row)

Every record carries a `readiness_tier`, and the tier is the whole point — never inflate it.

| Tier | `manifest_kind` | What it means | May feed the downloader? |
|---|---|---|---|
| **GREEN** | `production` | Exact item + item-level rights evidence + commercial use affirmed + a **successful** deterministic retrieval test (MIME, bytes, signature, SHA-256, dimensions for images). | **Yes — only GREEN.** |
| **YELLOW** | `manual_review` | An exact candidate exists but needs browser/session access, human rights interpretation, or ambiguity resolution. | No — routes to a human. |
| **RED** | `candidate` | Unresolved request, a repository search result, a missing exact item, a broken link, or thin metadata. A lead only. | No. |

Use three files per course/unit:

```text
manifests-v2/<course>/<unit>/
  candidate_manifest.json      # RED leads
  manual_review_manifest.json  # YELLOW, browser/rights-gated
  production_manifest.json     # GREEN, the ONLY downloader input
```

## Non-negotiable rules (the guardrail)

1. **One exact asset per row.** Never combine books, images, creators, editions, or documents.
2. **No search / results / collection landing / menu / bibliography / catalog page** in a production
   manifest — the validator rejects `search`, `results`, `catalog/search`, and `?q=`/`?query=` URLs.
3. **Do not guess** item IDs, direct-download URLs, metadata, or rights.
4. Use **exact item-level** catalog URLs and repository identifiers.
5. **Confirm rights at the item level.** Repository reputation is not rights evidence.
6. **Production rights must support commercial educational reuse.** If unclear → manual review; never
   infer or substitute. Allowed bases: `explicit_public_domain`, `pre_1929`, `us_government_work`,
   `official_document_text`, `cc0`, `cc_by`, `permission`.
7. **Retrieve every production candidate once before approval** — HTTP 200, nonzero bytes, file
   signature, MIME, extension, image dimensions when applicable, and SHA-256.
8. Preserve original bytes and original authorized format during the test.
9. **Do not silently substitute** a different item. If the requested item can't be verified, keep the
   candidate/manual-review record and say why.
10. No browser automation for bulk sourcing — route browser/session/JS-only items to manual review.
11. Repository APIs and deterministic HTTP **before** open-web search.
12. Stop testing a repository after the pilot if it isn't operationally suitable; don't scale a
    failing access pattern.

## How to run

### Validate a manifest (the gate)

```bash
# GREEN downloader input — must pass at zero blockers
python3 tools/validate_manifest_readiness.py \
  manifests-v2/<course>/<unit>/production_manifest.json --kind production

# The lead / review tiers (structure + tier discipline)
python3 tools/validate_manifest_readiness.py \
  manifests-v2/<course>/<unit>/candidate_manifest.json    --kind candidate
python3 tools/validate_manifest_readiness.py \
  manifests-v2/<course>/<unit>/manual_review_manifest.json --kind manual_review
```

Exit `0` **only** at zero blockers. Point the validator at a directory to sweep every `*.json`/`*.csv`
under it. Standard-library only — no dependencies to install. **Do not weaken the validator or edit the
allowed-rights set to make a record pass — correct or reclassify the record.**

### Regression-test the validator

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### Build a manifest (the operating prompt)

`prompts/CLAUDE_CODE_SOURCE_MANIFEST.md` is the ready-to-paste Claude Code operating prompt for a
deterministic manifest build: preflight → pilot-before-scale → candidate resolution → retrieval test →
classification → validation → checkpoint. Fill in the angle-bracket values (course, unit, standards
input) and run it from the primary-sources repository root.

## Bundled assets

| Path | Role |
|---|---|
| `schema/primary-source-manifest-v2.schema.json` | The versioned v2 contract (`schema_version: "2.0"`): exact item identity, item-level rights evidence, retrieval-test fields. |
| `tools/validate_manifest_readiness.py` | The fail-closed validator. Stdlib-only; JSON **and** CSV manifests. |
| `tests/test_validate_manifest_readiness.py` | Regression tests (valid GREEN passes; search page / compound / untested / tier discipline all blocked). |
| `templates/production-manifest-v2.example.json` | A complete, passing GREEN record to copy from (Magna Carta canonical-html example). |
| `prompts/CLAUDE_CODE_SOURCE_MANIFEST.md` | The deterministic manifest-builder operating prompt. |
| `assets/ci/manifest-readiness.yml` | Reference GitHub Actions workflow — runs the regression tests and validates every file under `manifests-v2/**` on PRs/pushes. Copy into a manifests repo's `.github/workflows/` to activate the gate there; it is bundled here (not wired into this repo's CI) because this repo has no `manifests-v2/` tree. |

## What the validator enforces (production tier)

- All base + production fields present and non-placeholder (rejects `""`, `unknown`, `various`, `tbd`…).
- Valid Tennessee standard code (`US`/`GC`/`TN`/`W`/`6`/`7`/`8` `. NN[a]`).
- `source_page_url` (and any `direct_download_url`) is an HTTP(S) **item** page, not a search/results URL.
- `readiness_tier == GREEN`, `review_reason == production-ready`, `compound_request == false`,
  `asset_count == 1`, `commercial_use_ok == true`.
- `rights_basis` in the allowed set; `rights_url` is item-level HTTP(S) evidence.
- `delivery_kind == file` requires a real `direct_download_url`; `canonical_html` requires
  `asset_type == canonical_html`.
- Retrieval proof: `retrieval_status == success`, `http_status == 200`, `downloaded_bytes > 0`,
  64-hex `content_sha256`, `file_signature_valid == true`, `verified == true`, ISO-8601-UTC timestamps.
- `detected_mime_type == expected_mime_type`, and `target_filename` extension matches the MIME.
- Image-like assets (`image`/`map`/`cartoon`/`artifact`) carry positive `image_width`/`image_height`.
- Duplicate `asset_id`, and duplicate `repository + exact_item_id`, are blockers.

For candidate/manual-review records the gate is lighter but still enforces tier discipline: the correct
tier, a written `review_reason`, and a warning if a non-production row is prematurely marked `verified`.

## Definition of done

A unit is complete only when **every** requested asset is either (1) a production record that passes
the gate at zero blockers, or (2) an explicit candidate/manual-review record with a concrete reason.
Never describe candidate or manual-review rows as cleared, verified, downloadable, or complete.

## Lane boundaries (one job, one owner)

- **This skill** produces and gates the *sourcing manifest* — the vetted, retrievable, rights-cleared
  records the pipeline downloads.
- `history-hack-dbq-workbook` **consumes** cleared sources into a DBQ/primary-source product.
- `copyright-integrity-accreditation` owns IP / licensing / FERPA-COPPA **policy** review.
- `historian-factcheck-agent` owns claim-by-claim **factual** verification of content.
- `tn-textbook-adoption-agent` owns the Schedule F **adoption** panel review.
