#!/usr/bin/env python3
"""Validate a private Phase 0 evidence manifest.

This validates provenance structure only. It does not inspect evidence contents,
store artifacts, or make SLA eligibility / financial decisions.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

MANIFEST_VERSION = "phase0-evidence-manifest-v1"
ARTIFACT_CLASSES = {
    "RAW_ORIGINAL",
    "REDACTED_COPY",
    "NORMALIZED_DERIVATIVE",
    "CALCULATION_OUTPUT",
}
ARTIFACT_STATUSES = {
    "RECEIVED",
    "ADMITTED",
    "QUARANTINED",
    "SUPERSEDED",
    "DELETED",
    "RETURNED",
}
SERVICES = {"ec2", "s3", "rds"}
CASE_ID_RE = re.compile(r"^P0-[0-9]{4}-[0-9]{4}$")
EVIDENCE_ID_RE = re.compile(r"^E-[0-9]{3,}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ManifestError(ValueError):
    pass


def require_utc(value: object, label: str) -> None:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ManifestError(f"{label} must be an ISO-8601 UTC timestamp ending in Z")
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise ManifestError(f"{label} is not a valid ISO-8601 timestamp") from exc


def require_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{label} must be a non-empty string")
    return value


def reference_list(artifact: dict, key: str, label: str) -> list[str]:
    value = artifact.get(key, [])
    if not isinstance(value, list):
        raise ManifestError(f"{label}.{key} must be an array")
    if len(value) != len(set(value)):
        raise ManifestError(f"{label}.{key} contains duplicate references")
    for item in value:
        if not isinstance(item, str) or not EVIDENCE_ID_RE.fullmatch(item):
            raise ManifestError(f"{label}.{key} contains invalid evidence ID {item!r}")
    return value


def validate_artifact_shape(artifact: object, index: int) -> dict:
    label = f"artifacts[{index}]"
    if not isinstance(artifact, dict):
        raise ManifestError(f"{label} must be an object")

    required = (
        "evidence_id",
        "class",
        "filename",
        "source",
        "received_utc",
        "size_bytes",
        "sha256",
        "status",
    )
    missing = [key for key in required if key not in artifact]
    if missing:
        raise ManifestError(f"{label} missing required fields {missing}")

    evidence_id = require_string(artifact["evidence_id"], f"{label}.evidence_id")
    if not EVIDENCE_ID_RE.fullmatch(evidence_id):
        raise ManifestError(f"{label}.evidence_id has invalid format")

    artifact_class = artifact["class"]
    if artifact_class not in ARTIFACT_CLASSES:
        raise ManifestError(f"{label}.class is unsupported: {artifact_class!r}")

    filename = require_string(artifact["filename"], f"{label}.filename")
    if "/" in filename or "\\" in filename:
        raise ManifestError(f"{label}.filename must not contain a filesystem path")

    require_string(artifact["source"], f"{label}.source")
    require_utc(artifact["received_utc"], f"{label}.received_utc")

    size = artifact["size_bytes"]
    if isinstance(size, bool) or not isinstance(size, int) or size < 0:
        raise ManifestError(f"{label}.size_bytes must be an integer >= 0")

    digest = artifact["sha256"]
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        raise ManifestError(f"{label}.sha256 must be 64 lowercase hex characters")

    if artifact["status"] not in ARTIFACT_STATUSES:
        raise ManifestError(f"{label}.status is unsupported: {artifact['status']!r}")

    parents = reference_list(artifact, "parent_evidence_ids", label)
    inputs = reference_list(artifact, "input_evidence_ids", label)

    if artifact_class == "RAW_ORIGINAL":
        if parents or inputs:
            raise ManifestError(f"{label}: RAW_ORIGINAL cannot have provenance parents/inputs")
    elif artifact_class in {"REDACTED_COPY", "NORMALIZED_DERIVATIVE"}:
        if not parents:
            raise ManifestError(f"{label}: {artifact_class} requires parent_evidence_ids")
        require_string(artifact.get("transformation"), f"{label}.transformation")
    elif artifact_class == "CALCULATION_OUTPUT":
        if not inputs:
            raise ManifestError(f"{label}: CALCULATION_OUTPUT requires input_evidence_ids")
        require_string(artifact.get("ruleset_id"), f"{label}.ruleset_id")
        require_string(artifact.get("ruleset_version"), f"{label}.ruleset_version")
        require_string(artifact.get("transformation"), f"{label}.transformation")

    return artifact


def validate_acyclic(references: dict[str, set[str]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            raise ManifestError(f"provenance graph contains a cycle at {node}")
        if node in visited:
            return
        visiting.add(node)
        for target in references.get(node, set()):
            visit(target)
        visiting.remove(node)
        visited.add(node)

    for node in references:
        visit(node)


def validate_manifest(data: object) -> dict:
    if not isinstance(data, dict):
        raise ManifestError("manifest root must be an object")

    required = ("manifest_version", "case_id", "provider", "service", "opened_utc", "artifacts")
    missing = [key for key in required if key not in data]
    if missing:
        raise ManifestError(f"manifest missing required fields {missing}")

    if data["manifest_version"] != MANIFEST_VERSION:
        raise ManifestError(f"unsupported manifest_version {data['manifest_version']!r}")

    case_id = require_string(data["case_id"], "case_id")
    if not CASE_ID_RE.fullmatch(case_id):
        raise ManifestError("case_id must match P0-YYYY-NNNN")

    if data["provider"] != "aws":
        raise ManifestError("Phase 0 evidence manifest currently supports provider=aws only")
    if data["service"] not in SERVICES:
        raise ManifestError(f"unsupported Phase 0 service {data['service']!r}")
    require_utc(data["opened_utc"], "opened_utc")

    artifacts = data["artifacts"]
    if not isinstance(artifacts, list) or not artifacts:
        raise ManifestError("artifacts must be a non-empty array")

    validated: list[dict] = []
    by_id: dict[str, dict] = {}
    for index, raw in enumerate(artifacts):
        artifact = validate_artifact_shape(raw, index)
        evidence_id = artifact["evidence_id"]
        if evidence_id in by_id:
            raise ManifestError(f"duplicate evidence_id {evidence_id}")
        by_id[evidence_id] = artifact
        validated.append(artifact)

    references: dict[str, set[str]] = {}
    for artifact in validated:
        evidence_id = artifact["evidence_id"]
        refs = set(artifact.get("parent_evidence_ids", [])) | set(
            artifact.get("input_evidence_ids", [])
        )
        if evidence_id in refs:
            raise ManifestError(f"{evidence_id} cannot reference itself")
        missing_refs = sorted(ref for ref in refs if ref not in by_id)
        if missing_refs:
            raise ManifestError(
                f"{evidence_id} references missing evidence IDs {missing_refs}"
            )
        references[evidence_id] = refs

    validate_acyclic(references)
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate one private Phase 0 evidence manifest JSON file.")
    parser.add_argument("manifest", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
        validate_manifest(data)
    except (OSError, json.JSONDecodeError, ManifestError) as exc:
        raise SystemExit(f"ERROR: {exc}") from exc

    print(f"Valid Phase 0 evidence manifest: {args.manifest.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
