#!/usr/bin/env python3
"""Fail-closed validator for executable primary-source manifests.

This complements validate_primary_sources.py. The existing validator checks
Schedule F and repository policy; this validator checks whether a record is an
exact, rights-evidenced, tested item that a download pipeline can execute.
Uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

KINDS = {"candidate", "manual_review", "production"}
TIERS = {"candidate": "RED", "manual_review": "YELLOW", "production": "GREEN"}
STANDARD_RE = re.compile(r"^(US|GC|TN|W|6|7|8)\.\d{1,3}[A-Za-z]?$")
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")
ISO_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")
SEARCH_PATH_RE = re.compile(
    r"(^|/)(search|search-results?|results|catalog/search|collections?/search)(/|$)",
    re.IGNORECASE,
)
SEARCH_QUERY_KEYS = {
    "q", "query", "search", "searchterm", "search_term", "keywords", "keyword",
    "lookfor", "searchtext",
}
PLACEHOLDER_VALUES = {
    "", "unknown", "various", "multiple", "n/a", "na", "tbd", "to be determined",
}
ALLOWED_RIGHTS = {
    "explicit_public_domain", "pre_1929", "us_government_work",
    "official_document_text", "cc0", "cc_by", "permission",
}
IMAGE_TYPES = {"image", "map", "cartoon", "artifact"}
MIME_EXTENSIONS = {
    "image/jpeg": {".jpg", ".jpeg"},
    "image/png": {".png"},
    "image/tiff": {".tif", ".tiff"},
    "image/gif": {".gif"},
    "image/webp": {".webp"},
    "application/pdf": {".pdf"},
    "text/plain": {".txt"},
    "text/html": {".html", ".htm"},
    "audio/mpeg": {".mp3"},
    "audio/wav": {".wav"},
    "video/mp4": {".mp4"},
}

BASE_REQUIRED = (
    "asset_id", "course", "unit", "standard", "asset_type", "title",
    "source_page_url", "target_filename", "drive_subfolder",
    "readiness_tier", "review_reason",
)
PRODUCTION_REQUIRED = (
    "creator_or_institution", "date", "repository", "exact_item_id",
    "delivery_kind", "license", "rights_basis", "rights_url", "attribution",
    "commercial_use_ok", "compound_request", "asset_count",
    "expected_mime_type", "detected_mime_type", "retrieval_method",
    "retrieval_status", "retrieval_tested_at", "source_verified_at",
    "http_status", "downloaded_bytes", "content_sha256",
    "file_signature_valid", "verified",
)


def truthy(value) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def integer(value, default=-1) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def is_blank(value) -> bool:
    return value is None or str(value).strip().lower() in PLACEHOLDER_VALUES


def valid_http_url(value) -> bool:
    try:
        parsed = urlparse(str(value))
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except ValueError:
        return False


def is_search_url(value) -> bool:
    if not valid_http_url(value):
        return False
    parsed = urlparse(str(value))
    if SEARCH_PATH_RE.search(parsed.path):
        return True
    keys = {key.lower() for key in parse_qs(parsed.query, keep_blank_values=True)}
    return bool(keys & SEARCH_QUERY_KEYS)


def load_manifest(path: Path, kind_override: str | None):
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            records = list(csv.DictReader(handle))
        return kind_override or "candidate", "", "", records

    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, list):
        return kind_override or "candidate", "", "", data
    records = data.get("records")
    if records is None:
        records = data.get("sources") or data.get("items") or []
    return (
        kind_override or data.get("manifest_kind") or "candidate",
        data.get("course", ""),
        data.get("unit", ""),
        records,
    )


def validate_record(record: dict, index: int, kind: str, course: str, unit: str):
    errors, warnings = [], []
    label = record.get("asset_id") or f"row-{index}"

    for field in BASE_REQUIRED:
        if field not in record or is_blank(record.get(field)):
            errors.append(f"missing required field: {field}")

    standard = str(record.get("standard", "")).strip()
    if standard and not STANDARD_RE.fullmatch(standard):
        errors.append(f"invalid Tennessee standard code: {standard}")

    source_url = record.get("source_page_url", "")
    if source_url and not valid_http_url(source_url):
        errors.append("source_page_url is not an HTTP(S) URL")
    if source_url and is_search_url(source_url):
        errors.append("source_page_url is a search/results URL, not an exact item page")

    if course and record.get("course") != course:
        errors.append("record course does not match manifest course")
    if unit and record.get("unit") != unit:
        errors.append("record unit does not match manifest unit")

    expected_tier = TIERS[kind]
    if record.get("readiness_tier") != expected_tier:
        errors.append(
            f"{kind} records must use readiness_tier={expected_tier}"
        )

    if kind != "production":
        if not str(record.get("review_reason", "")).strip():
            errors.append("non-production record must explain review_reason")
        if truthy(record.get("verified")):
            warnings.append("non-production record is marked verified")
        return label, errors, warnings

    for field in PRODUCTION_REQUIRED:
        if field not in record or is_blank(record.get(field)):
            errors.append(f"production field missing or placeholder: {field}")

    if str(record.get("review_reason", "")).strip().lower() not in {
        "production-ready", "production ready", "none",
    }:
        errors.append("production review_reason must be 'production-ready'")

    if truthy(record.get("compound_request")):
        errors.append("compound_request must be false")
    if integer(record.get("asset_count")) != 1:
        errors.append("asset_count must equal 1")
    if not truthy(record.get("commercial_use_ok")):
        errors.append("commercial_use_ok must be true")
    if record.get("rights_basis") not in ALLOWED_RIGHTS:
        errors.append("rights_basis is unresolved or not production-approved")
    if not valid_http_url(record.get("rights_url")):
        errors.append("rights_url must be item-level HTTP(S) evidence")

    delivery = record.get("delivery_kind")
    direct_url = record.get("direct_download_url", "")
    if delivery == "file":
        if not valid_http_url(direct_url):
            errors.append("file delivery requires a direct_download_url")
        elif is_search_url(direct_url):
            errors.append("direct_download_url is a search/results URL")
    elif delivery == "canonical_html":
        if record.get("asset_type") != "canonical_html":
            errors.append("canonical_html delivery requires asset_type=canonical_html")
    else:
        errors.append("delivery_kind must be file or canonical_html")

    if record.get("retrieval_method") in {"browser", "none"}:
        errors.append("production retrieval must be deterministic, not browser/none")
    if record.get("retrieval_status") != "success":
        errors.append("retrieval_status must be success")
    if integer(record.get("http_status")) != 200:
        errors.append("http_status must equal 200")
    if integer(record.get("downloaded_bytes")) <= 0:
        errors.append("downloaded_bytes must be greater than zero")
    if not SHA256_RE.fullmatch(str(record.get("content_sha256", ""))):
        errors.append("content_sha256 must be 64 hexadecimal characters")
    if not truthy(record.get("file_signature_valid")):
        errors.append("file_signature_valid must be true")
    if not truthy(record.get("verified")):
        errors.append("verified must be true")

    for field in ("retrieval_tested_at", "source_verified_at"):
        if not ISO_UTC_RE.fullmatch(str(record.get(field, ""))):
            errors.append(f"{field} must be an ISO 8601 UTC timestamp ending in Z")

    expected_mime = str(record.get("expected_mime_type", "")).split(";", 1)[0].strip().lower()
    detected_mime = str(record.get("detected_mime_type", "")).split(";", 1)[0].strip().lower()
    if expected_mime != detected_mime:
        errors.append("detected_mime_type does not match expected_mime_type")

    extension = Path(str(record.get("target_filename", ""))).suffix.lower()
    allowed_extensions = MIME_EXTENSIONS.get(expected_mime)
    if allowed_extensions and extension not in allowed_extensions:
        errors.append(
            f"target_filename extension {extension or '(none)'} conflicts with {expected_mime}"
        )

    if record.get("asset_type") in IMAGE_TYPES:
        if integer(record.get("image_width")) <= 0:
            errors.append("image_width must be recorded for image-like assets")
        if integer(record.get("image_height")) <= 0:
            errors.append("image_height must be recorded for image-like assets")

    return label, errors, warnings


def validate_file(path: Path, kind_override: str | None):
    kind, course, unit, records = load_manifest(path, kind_override)
    file_errors, file_warnings = [], []
    if kind not in KINDS:
        return [(str(path), [f"invalid manifest_kind: {kind}"], [])]
    if not isinstance(records, list):
        return [(str(path), ["records must be an array"], [])]

    seen_ids, seen_items, results = set(), set(), []
    for index, record in enumerate(records, 1):
        if not isinstance(record, dict):
            results.append((f"row-{index}", ["record must be an object"], []))
            continue
        label, errors, warnings = validate_record(
            record, index, kind, course, unit
        )
        asset_id = str(record.get("asset_id", "")).strip()
        item_key = (
            str(record.get("repository", "")).strip().lower(),
            str(record.get("exact_item_id", "")).strip().lower(),
        )
        if asset_id:
            if asset_id in seen_ids:
                errors.append(f"duplicate asset_id: {asset_id}")
            seen_ids.add(asset_id)
        if kind == "production" and all(item_key):
            if item_key in seen_items:
                errors.append("duplicate repository + exact_item_id")
            seen_items.add(item_key)
        results.append((label, errors, warnings))
    if not records:
        file_warnings.append("manifest contains zero records")
    if file_errors or file_warnings:
        results.insert(0, (str(path), file_errors, file_warnings))
    return results


def iter_inputs(input_path: Path):
    if input_path.is_file():
        yield input_path
        return
    for path in sorted(input_path.rglob("*")):
        if path.suffix.lower() in {".json", ".csv"} and path.is_file():
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="manifest file or directory")
    parser.add_argument("--kind", choices=sorted(KINDS))
    args = parser.parse_args()

    paths = list(iter_inputs(args.input))
    if not paths:
        print(f"FAIL: no JSON or CSV manifests found at {args.input}")
        return 2

    blockers = warnings = records = 0
    for path in paths:
        print(f"\nValidating {path}")
        for label, errors, warns in validate_file(path, args.kind):
            if label != str(path):
                records += 1
            if errors or warns:
                print(f"[{label}]")
            for message in errors:
                print(f"  BLOCKER: {message}")
            for message in warns:
                print(f"  warn: {message}")
            blockers += len(errors)
            warnings += len(warns)

    print(
        f"\nRESULT: {blockers} blocker(s), {warnings} warning(s), "
        f"{records} record(s), {len(paths)} file(s)."
    )
    if blockers:
        print("FAIL — reclassify or correct blocked records.")
        return 1
    print("PASS — manifest readiness gate satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

