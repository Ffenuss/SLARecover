import importlib.util
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "hash_artifact", Path("scripts/hash_artifact.py")
)
hash_artifact = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(hash_artifact)


class ArtifactManifestTests(unittest.TestCase):
    def test_sha256_known_vector(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "artifact.bin"
            path.write_bytes(b"abc")
            self.assertEqual(
                hash_artifact.sha256_file(path),
                "ba7816bf8f01cfea414140de5dae2223"
                "b00361a396177a9cb410ff61f20015ad",
            )

    def test_manifest_does_not_modify_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "request-log.txt"
            original = b"immutable evidence bytes\n"
            path.write_bytes(original)
            before = path.stat()

            manifest = hash_artifact.artifact_manifest(path, "RAW_ORIGINAL")

            after = path.stat()
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(after.st_mtime_ns, before.st_mtime_ns)
            self.assertEqual(after.st_size, before.st_size)
            self.assertEqual(manifest["filename"], "request-log.txt")
            self.assertEqual(manifest["size_bytes"], len(original))
            self.assertEqual(manifest["artifact_class"], "RAW_ORIGINAL")

    def test_manifest_timestamps_are_utc(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "artifact.txt"
            path.write_text("x", encoding="utf-8")
            manifest = hash_artifact.artifact_manifest(path)
            self.assertTrue(manifest["observed_mtime_utc"].endswith("Z"))
            self.assertTrue(manifest["hashed_at_utc"].endswith("Z"))

    def test_missing_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError):
                hash_artifact.artifact_manifest(Path(tmp) / "missing.bin")

    def test_directory_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                hash_artifact.artifact_manifest(Path(tmp))

    def test_unknown_artifact_class_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "artifact.txt"
            path.write_text("x", encoding="utf-8")
            with self.assertRaises(ValueError):
                hash_artifact.artifact_manifest(path, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
