#!/usr/bin/env python3
"""Create deterministic SHA-256 provenance metadata for a local Phase 0 artifact.

The utility is intentionally local-only:
- it does not upload, copy, move, redact, or modify the source file;
- it emits metadata to stdout only;
- it does not make SLA eligibility or financial decisions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ARTIFACT_CLASSES = (
    "RAW_ORIGINAL",
    "REDACTED_COPY",
    "NORMALIZED_DERIVATIVE",
    "CALCULATION_OUTPUT",
    "SOURCE_SNAPSHOT",
)

CHUNK_SIZE = 1024 * 1024


def utc_iso(timestamp: float | None = None) -> str:
    dt = (
        datetime.now(timezone.utc)
        if timestamp is None
        else datetime.fromtimestamp(timestamp, timezone.utc)
    )
    return dt.isoformat(timespec="microseconds").replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def artifact_manifest(path: Path, artifact_class: str | None = None) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"artifact does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"artifact must be a regular file: {path}")
    if artifact_class is not None and artifact_class not in ARTIFACT_CLASSES:
        raise ValueError(f"unsupported artifact class: {artifact_class}")

    before = path.stat()
    digest = sha256_file(path)
    after = path.stat()

    if before.st_size != after.st_size or before.st_mtime_ns != after.st_mtime_ns:
        raise RuntimeError(
            "artifact changed while being hashed; discard this manifest and retry"
        )

    manifest: dict[str, object] = {
        "manifest_version": "phase0-artifact-manifest-v1",
        "filename": path.name,
        "size_bytes": before.st_size,
        "sha256": digest,
        "observed_mtime_utc": utc_iso(before.st_mtime),
        "hashed_at_utc": utc_iso(),
    }
    if artifact_class is not None:
        manifest["artifact_class"] = artifact_class
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Hash one local artifact and emit Phase 0 provenance JSON."
    )
    parser.add_argument("path", type=Path, help="Local file to hash.")
    parser.add_argument(
        "--class",
        dest="artifact_class",
        choices=ARTIFACT_CLASSES,
        help="Optional Phase 0 evidence/source artifact class.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON instead of one compact line.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = artifact_manifest(args.path, args.artifact_class)
    except (FileNotFoundError, ValueError, RuntimeError, OSError) as exc:
        raise SystemExit(f"ERROR: {exc}") from exc

    if args.pretty:
        print(json.dumps(manifest, indent=2, sort_keys=True))
    else:
        print(json.dumps(manifest, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
