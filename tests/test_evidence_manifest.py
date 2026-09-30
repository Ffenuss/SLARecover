import copy
import importlib.util
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "validate_evidence_manifest",
    Path("scripts/validate_evidence_manifest.py"),
)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


def valid_manifest():
    return {
        "manifest_version": "phase0-evidence-manifest-v1",
        "case_id": "P0-2026-0001",
        "provider": "aws",
        "service": "ec2",
        "opened_utc": "2026-09-30T12:00:00Z",
        "artifacts": [
            {
                "evidence_id": "E-001",
                "class": "RAW_ORIGINAL",
                "filename": "request-log.txt",
                "source": "synthetic",
                "received_utc": "2026-09-30T12:01:00Z",
                "size_bytes": 3,
                "sha256": "0" * 64,
                "status": "ADMITTED",
            },
            {
                "evidence_id": "E-002",
                "class": "NORMALIZED_DERIVATIVE",
                "filename": "timeline.json",
                "source": "synthetic",
                "received_utc": "2026-09-30T12:02:00Z",
                "size_bytes": 2,
                "sha256": "1" * 64,
                "status": "ADMITTED",
                "parent_evidence_ids": ["E-001"],
                "transformation": "normalize timestamps",
            },
            {
                "evidence_id": "E-003",
                "class": "CALCULATION_OUTPUT",
                "filename": "calculation.json",
                "source": "synthetic",
                "received_utc": "2026-09-30T12:03:00Z",
                "size_bytes": 2,
                "sha256": "2" * 64,
                "status": "ADMITTED",
                "input_evidence_ids": ["E-002"],
                "transformation": "manual deterministic calculation provenance",
                "ruleset_id": "aws-ec2-instance-level-compute-sla",
                "ruleset_version": "draft-2026-09-30",
            },
        ],
    }


class EvidenceManifestTests(unittest.TestCase):
    def test_valid_manifest_passes(self):
        validator.validate_manifest(valid_manifest())

    def test_duplicate_evidence_id_fails(self):
        data = valid_manifest()
        duplicate = copy.deepcopy(data["artifacts"][0])
        data["artifacts"].append(duplicate)
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_dangling_reference_fails(self):
        data = valid_manifest()
        data["artifacts"][1]["parent_evidence_ids"] = ["E-999"]
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_raw_original_cannot_have_parent(self):
        data = valid_manifest()
        data["artifacts"][0]["parent_evidence_ids"] = ["E-002"]
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_derivative_requires_parent(self):
        data = valid_manifest()
        del data["artifacts"][1]["parent_evidence_ids"]
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_calculation_requires_ruleset(self):
        data = valid_manifest()
        del data["artifacts"][2]["ruleset_id"]
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_invalid_sha256_fails(self):
        data = valid_manifest()
        data["artifacts"][0]["sha256"] = "not-a-digest"
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_non_utc_timestamp_fails(self):
        data = valid_manifest()
        data["opened_utc"] = "2026-09-30T12:00:00+03:00"
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_provenance_cycle_fails(self):
        data = valid_manifest()
        data["artifacts"][1]["parent_evidence_ids"] = ["E-003"]
        data["artifacts"][2]["input_evidence_ids"] = ["E-002"]
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)

    def test_filename_must_not_leak_path(self):
        data = valid_manifest()
        data["artifacts"][0]["filename"] = "/private/customer/request-log.txt"
        with self.assertRaises(validator.ManifestError):
            validator.validate_manifest(data)


if __name__ == "__main__":
    unittest.main()
