#!/usr/bin/env python3
"""Create or validate Phase 0 provider source-snapshot provenance manifests.

No network fetch occurs here. Real provider source bytes remain in a private,
controlled workspace; only synthetic fixtures belong in public Git.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

try:
    from scripts.hash_artifact import artifact_manifest
except ModuleNotFoundError:  # direct execution: python scripts/source_snapshot_manifest.py
    from hash_artifact import artifact_manifest

MANIFEST_VERSION = "phase0-source-snapshot-v1"
DATE_SEMANTICS = "provider_last_updated_not_proven_effective_from"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
SERVICE_URL_PREFIX = {
    "ec2": "https://aws.amazon.com/compute/sla/",
    "s3": "https://aws.amazon.com/s3/sla/",
    "rds": "https://aws.amazon.com/rds/sla/",
}


class SourceManifestError(ValueError):
    pass


def require_utc(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise SourceManifestError(f"{label} must be ISO-8601 UTC ending in Z")
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise SourceManifestError(f"{label} is not valid ISO-8601") from exc
    return value


def require_date(value: object, label: str) -> str:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        raise SourceManifestError(f"{label} must be YYYY-MM-DD")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise SourceManifestError(f"{label} is not a real calendar date") from exc
    return value


def validate_manifest(data: object) -> dict:
    if not isinstance(data, dict):
        raise SourceManifestError("manifest root must be an object")

    required = (
        "manifest_version","provider","service","source_url","source_last_updated",
        "source_version_date_semantics","retrieved_at_utc","filename","size_bytes",
        "sha256","storage_scope","effective_from","effective_until","applicability_status",
    )
    missing = [key for key in required if key not in data]
    if missing:
        raise SourceManifestError(f"missing required fields {missing}")

    if data["manifest_version"] != MANIFEST_VERSION:
        raise SourceManifestError("unsupported manifest_version")
    if data["provider"] != "aws":
        raise SourceManifestError("Phase 0 source contract currently supports aws only")

    service = data["service"]
    if service not in SERVICE_URL_PREFIX:
        raise SourceManifestError(f"unsupported service {service!r}")

    source_url = data["source_url"]
    if not isinstance(source_url, str) or not source_url.startswith(SERVICE_URL_PREFIX[service]):
        raise SourceManifestError(
            f"source_url does not match official AWS SLA path for service {service}"
        )

    require_date(data["source_last_updated"], "source_last_updated")
    if data["source_version_date_semantics"] != DATE_SEMANTICS:
        raise SourceManifestError(
            "source_version_date_semantics must preserve Last Updated != effective_from"
        )
    require_utc(data["retrieved_at_utc"], "retrieved_at_utc")

    filename = data["filename"]
    if not isinstance(filename, str) or not filename or "/" in filename or "\\" in filename:
        raise SourceManifestError("filename must be a basename, not a local path")

    size = data["size_bytes"]
    if isinstance(size, bool) or not isinstance(size, int) or size < 0:
        raise SourceManifestError("size_bytes must be an integer >= 0")

    digest = data["sha256"]
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        raise SourceManifestError("sha256 must be 64 lowercase hex characters")

    if data["storage_scope"] != "PRIVATE_CONTROLLED":
        raise SourceManifestError("real source snapshots must use PRIVATE_CONTROLLED storage scope")

    if data["applicability_status"] not in {"UNPROVEN", "REVIEWED"}:
        raise SourceManifestError("unsupported applicability_status")

    for key in ("effective_from", "effective_until"):
        if data[key] is not None:
            require_date(data[key], key)

    if data["applicability_status"] == "UNPROVEN":
        if data["effective_from"] is not None or data["effective_until"] is not None:
            raise SourceManifestError(
                "UNPROVEN source applicability cannot populate effective_from/effective_until"
            )

    return data


def create_manifest(
    path: Path,
    service: str,
    source_url: str,
    source_last_updated: str,
    retrieved_at_utc: str,
) -> dict:
    if service not in SERVICE_URL_PREFIX:
        raise SourceManifestError(f"unsupported service {service!r}")
    require_date(source_last_updated, "source_last_updated")
    require_utc(retrieved_at_utc, "retrieved_at_utc")

    artifact = artifact_manifest(path, "SOURCE_SNAPSHOT")
    data = {
        "manifest_version": MANIFEST_VERSION,
        "provider": "aws",
        "service": service,
        "source_url": source_url,
        "source_last_updated": source_last_updated,
        "source_version_date_semantics": DATE_SEMANTICS,
        "retrieved_at_utc": retrieved_at_utc,
        "filename": artifact["filename"],
        "size_bytes": artifact["size_bytes"],
        "sha256": artifact["sha256"],
        "storage_scope": "PRIVATE_CONTROLLED",
        "effective_from": None,
        "effective_until": None,
        "applicability_status": "UNPROVEN",
    }
    return validate_manifest(data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create/validate Phase 0 source provenance.")
    sub = parser.add_subparsers(dest="command", required=True)

    create = sub.add_parser("create", help="Hash a local snapshot and emit provenance JSON.")
    create.add_argument("path", type=Path)
    create.add_argument("--service", required=True, choices=sorted(SERVICE_URL_PREFIX))
    create.add_argument("--source-url", required=True)
    create.add_argument("--source-last-updated", required=True)
    create.add_argument("--retrieved-at-utc", required=True)
    create.add_argument("--pretty", action="store_true")

    validate = sub.add_parser("validate", help="Validate an existing provenance JSON manifest.")
    validate.add_argument("manifest", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "create":
            data = create_manifest(
                args.path,
                args.service,
                args.source_url,
                args.source_last_updated,
                args.retrieved_at_utc,
            )
            if args.pretty:
                print(json.dumps(data, indent=2, sort_keys=True))
            else:
                print(json.dumps(data, separators=(",", ":"), sort_keys=True))
        else:
            data = json.loads(args.manifest.read_text(encoding="utf-8"))
            validate_manifest(data)
            print(f"Valid Phase 0 source snapshot manifest: {args.manifest.name}")
    except (OSError, json.JSONDecodeError, SourceManifestError, FileNotFoundError, ValueError, RuntimeError) as exc:
        raise SystemExit(f"ERROR: {exc}") from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
