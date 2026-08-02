import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate_manifest_readiness.py"
SPEC = importlib.util.spec_from_file_location("readiness", MODULE_PATH)
readiness = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(readiness)


def valid_record():
    return {
        "asset_id": "world-u1-w02-magna",
        "course": "hs-world-history",
        "unit": "unit-01",
        "standard": "W.02",
        "asset_type": "canonical_html",
        "title": "Magna Carta (1215)",
        "creator_or_institution": "King John and the barons of England",
        "date": "1215",
        "repository": "Avalon Project, Yale Law School",
        "exact_item_id": "medieval/magna",
        "source_page_url": "https://avalon.law.yale.edu/medieval/magna.asp",
        "direct_download_url": "",
        "delivery_kind": "canonical_html",
        "target_filename": "W.02_magna-carta.html",
        "drive_subfolder": "HS World History/Unit 01/W.02",
        "license": "Public domain official document text",
        "rights_basis": "official_document_text",
        "rights_url": "https://avalon.law.yale.edu/medieval/magna.asp",
        "attribution": "Magna Carta, 1215. Avalon Project, Yale Law School.",
        "commercial_use_ok": True,
        "compound_request": False,
        "asset_count": 1,
        "expected_mime_type": "text/html",
        "detected_mime_type": "text/html",
        "retrieval_method": "canonical_html",
        "retrieval_status": "success",
        "retrieval_tested_at": "2026-08-02T21:00:00Z",
        "source_verified_at": "2026-08-02T21:00:00Z",
        "http_status": 200,
        "downloaded_bytes": 1000,
        "content_sha256": "a" * 64,
        "file_signature_valid": True,
        "image_width": None,
        "image_height": None,
        "verified": True,
        "readiness_tier": "GREEN",
        "review_reason": "production-ready",
        "source_warning": "",
    }


class ReadinessValidatorTests(unittest.TestCase):
    def validate(self, record, kind="production"):
        return readiness.validate_record(
            record, 1, kind, "hs-world-history", "unit-01"
        )[1]

    def test_valid_production_record_passes(self):
        self.assertEqual(self.validate(valid_record()), [])

    def test_search_page_is_blocked(self):
        record = valid_record()
        record["source_page_url"] = "https://www.loc.gov/search/?q=Magna+Carta"
        self.assertTrue(any("search/results" in e for e in self.validate(record)))

    def test_compound_asset_is_blocked(self):
        record = valid_record()
        record["compound_request"] = True
        record["asset_count"] = 2
        errors = self.validate(record)
        self.assertTrue(any("compound_request" in e for e in errors))
        self.assertTrue(any("asset_count" in e for e in errors))

    def test_untested_download_is_blocked(self):
        record = valid_record()
        record["retrieval_status"] = "not_tested"
        record["verified"] = False
        errors = self.validate(record)
        self.assertTrue(any("retrieval_status" in e for e in errors))
        self.assertTrue(any("verified" in e for e in errors))

    def test_candidate_requires_red_tier_and_reason(self):
        record = {
            "asset_id": "candidate-1",
            "course": "hs-world-history",
            "unit": "unit-01",
            "standard": "W.01",
            "asset_type": "image",
            "title": "Candidate portrait",
            "source_page_url": "https://example.edu/item/1",
            "target_filename": "portrait.jpg",
            "drive_subfolder": "HS World History/Unit 01/W.01",
            "readiness_tier": "RED",
            "review_reason": "Exact rights evidence not yet located"
        }
        self.assertEqual(self.validate(record, "candidate"), [])


if __name__ == "__main__":
    unittest.main()

