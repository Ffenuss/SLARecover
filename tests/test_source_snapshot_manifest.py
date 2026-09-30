import importlib.util
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "source_snapshot_manifest",
    Path("scripts/source_snapshot_manifest.py"),
)
source_manifest = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(source_manifest)


def valid_manifest():
    return {
        "manifest_version": "phase0-source-snapshot-v1",
        "provider": "aws",
        "service": "ec2",
        "source_url": "https://aws.amazon.com/compute/sla/",
        "source_last_updated": "2022-05-25",
        "source_version_date_semantics": "provider_last_updated_not_proven_effective_from",
        "retrieved_at_utc": "2026-09-30T12:00:00Z",
        "filename": "compute-sla.html",
        "size_bytes": 3,
        "sha256": "0" * 64,
        "storage_scope": "PRIVATE_CONTROLLED",
        "effective_from": None,
        "effective_until": None,
        "applicability_status": "UNPROVEN",
    }


class SourceSnapshotManifestTests(unittest.TestCase):
    def test_valid_manifest_passes(self):
        source_manifest.validate_manifest(valid_manifest())

    def test_service_url_mismatch_fails(self):
        data = valid_manifest()
        data["source_url"] = "https://aws.amazon.com/s3/sla/"
        with self.assertRaises(source_manifest.SourceManifestError):
            source_manifest.validate_manifest(data)

    def test_unproven_manifest_cannot_set_effective_from(self):
        data = valid_manifest()
        data["effective_from"] = "2022-05-25"
        with self.assertRaises(source_manifest.SourceManifestError):
            source_manifest.validate_manifest(data)

    def test_retrieved_timestamp_must_be_utc(self):
        data = valid_manifest()
        data["retrieved_at_utc"] = "2026-09-30T15:00:00+03:00"
        with self.assertRaises(source_manifest.SourceManifestError):
            source_manifest.validate_manifest(data)

    def test_invalid_provider_date_fails(self):
        data = valid_manifest()
        data["source_last_updated"] = "2026-02-31"
        with self.assertRaises(source_manifest.SourceManifestError):
            source_manifest.validate_manifest(data)

    def test_filename_cannot_contain_private_path(self):
        data = valid_manifest()
        data["filename"] = "/private/snapshots/compute-sla.html"
        with self.assertRaises(source_manifest.SourceManifestError):
            source_manifest.validate_manifest(data)

    def test_create_manifest_hashes_local_bytes_and_emits_basename_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            nested = Path(tmp) / "private" / "snapshots"
            nested.mkdir(parents=True)
            path = nested / "compute-sla.html"
            path.write_bytes(b"abc")

            data = source_manifest.create_manifest(
                path=path,
                service="ec2",
                source_url="https://aws.amazon.com/compute/sla/",
                source_last_updated="2022-05-25",
                retrieved_at_utc="2026-09-30T12:00:00Z",
            )

            self.assertEqual(data["filename"], "compute-sla.html")
            self.assertNotIn(str(nested), data["filename"])
            self.assertEqual(
                data["sha256"],
                "ba7816bf8f01cfea414140de5dae2223"
                "b00361a396177a9cb410ff61f20015ad",
            )
            self.assertIsNone(data["effective_from"])
            self.assertEqual(data["applicability_status"], "UNPROVEN")


if __name__ == "__main__":
    unittest.main()
