#!/usr/bin/env python3
"""Validate Phase 0 repository invariants and non-active AWS draft rule contracts.

This script validates structure/provenance only. It MUST NOT calculate customer
eligibility, eligible spend, service credits, or emit financial decisions.
"""

from __future__ import annotations

import json
import re
import subprocess
from decimal import Decimal, InvalidOperation
from pathlib import Path

REQUIRED_REPO_FILES = (
    "README.md",
    "docs/PRODUCT.md",
    "docs/ARCHITECTURE.md",
    "docs/ROADMAP.md",
    "docs/SECURITY.md",
    "docs/THREAT_MODEL.md",
    "docs/DATA_MODEL.md",
    "docs/RULE_ENGINE.md",
    "docs/DECISIONS.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    ".env.example",
    "schemas/phase0-aws-rule-v1.schema.json",
    "schemas/phase0-evidence-manifest-v1.schema.json",
)

RULE_REQUIRED_KEYS = (
    "schema_version",
    "provider",
    "service",
    "ruleset_id",
    "version",
    "status",
    "source_url",
    "source_last_updated",
    "source_version_observed_date",
    "source_version_date_semantics",
    "effective_from",
    "effective_until",
    "source_snapshot_sha256",
    "historical_version_registry",
    "measurement_period",
    "claim_deadline",
    "claim_requirements",
    "notes",
    "activation_blockers",
)

SCHEMA_VERSION = "phase0-aws-rule-v1"
SOURCE_DATE_SEMANTICS = "provider_last_updated_not_proven_effective_from"

TEXT_EXTENSIONS = {
    ".md", ".json", ".py", ".yml", ".yaml", ".toml", ".txt", ".example", ".ini", ".cfg"
}
FORBIDDEN_SECRET_EXTENSIONS = {
    ".pem", ".key", ".p12", ".pfx", ".jks", ".keystore"
}
SENSITIVE_EVIDENCE_EXTENSIONS = {
    ".csv", ".tsv", ".xls", ".xlsx", ".parquet", ".zip", ".tar", ".gz", ".log", ".db", ".sqlite"
}
SENSITIVE_EVIDENCE_NAME = re.compile(
    r"(?:^|[-_.])(invoice|billing|cur|cost[-_]?and[-_]?usage|"
    r"support[-_]?case|raw[-_]?log|customer[-_]?evidence)(?:[-_.]|$)",
    re.IGNORECASE,
)
SECRET_PATTERNS = (
    (
        "AWS access key ID",
        re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    ),
    (
        "AWS secret access key assignment",
        re.compile(
            r"(?i)\bAWS_SECRET_ACCESS_KEY\b\s*[:=]\s*[\"']?"
            r"[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])"
        ),
    ),
    (
        "AWS session token assignment",
        re.compile(
            r"(?i)\bAWS_SESSION_TOKEN\b\s*[:=]\s*[\"']?"
            r"[A-Za-z0-9/+=]{80,}(?![A-Za-z0-9/+=])"
        ),
    ),
    (
        "private key block",
        re.compile(
            r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
        ),
    ),
)


def fail(message: str) -> None:
    raise SystemExit(message)


def require_nonempty_string(data: dict, key: str, path: Path) -> None:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{path}: {key} must be a non-empty string")


def decimal(value: object, label: str, path: Path) -> Decimal:
    if not isinstance(value, (str, int, float)):
        fail(f"{path}: {label} must be decimal-compatible")
    try:
        return Decimal(str(value))
    except InvalidOperation:
        fail(f"{path}: {label} is not a valid decimal")


def validate_tiers(tiers: object, label: str, path: Path) -> None:
    if not isinstance(tiers, list) or not tiers:
        fail(f"{path}: {label} must contain at least one tier")

    seen_lt: set[Decimal] = set()
    previous_gte: Decimal | None = None
    previous_credit = -1

    for index, tier in enumerate(tiers):
        if not isinstance(tier, dict):
            fail(f"{path}: {label}[{index}] must be an object")
        if "uptime_lt" not in tier or "credit_percent" not in tier:
            fail(f"{path}: {label}[{index}] requires uptime_lt and credit_percent")

        upper = decimal(tier["uptime_lt"], f"{label}[{index}].uptime_lt", path)
        if not (Decimal("0") < upper <= Decimal("100")):
            fail(f"{path}: {label}[{index}].uptime_lt must be in (0, 100]")
        if upper in seen_lt:
            fail(f"{path}: {label} has duplicate uptime_lt boundary {upper}")
        seen_lt.add(upper)

        credit = tier["credit_percent"]
        if isinstance(credit, bool) or not isinstance(credit, int) or not 0 <= credit <= 100:
            fail(f"{path}: {label}[{index}].credit_percent must be integer 0..100")
        if credit <= previous_credit:
            fail(f"{path}: {label} credit percentages must strictly increase as uptime decreases")
        previous_credit = credit

        lower_raw = tier.get("uptime_gte")
        lower = None if lower_raw is None else decimal(
            lower_raw, f"{label}[{index}].uptime_gte", path
        )

        if lower is not None:
            if not (Decimal("0") <= lower < upper):
                fail(f"{path}: {label}[{index}] requires uptime_gte < uptime_lt")
            if previous_gte is not None and upper != previous_gte:
                fail(
                    f"{path}: {label} has a tier gap/overlap: "
                    f"expected uptime_lt {previous_gte}, got {upper}"
                )
            previous_gte = lower
        else:
            if index != len(tiers) - 1:
                fail(f"{path}: only the final {label} tier may omit uptime_gte")
            if previous_gte is not None and upper != previous_gte:
                fail(
                    f"{path}: {label} final tier boundary must continue at "
                    f"{previous_gte}, got {upper}"
                )


def unique_ids(items: object, key: str, label: str, path: Path) -> list[dict]:
    if not isinstance(items, list) or not items:
        fail(f"{path}: {label} must be a non-empty array")
    seen: set[str] = set()
    result: list[dict] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            fail(f"{path}: {label}[{index}] must be an object")
        value = item.get(key)
        if not isinstance(value, str) or not value:
            fail(f"{path}: {label}[{index}].{key} must be non-empty")
        if value in seen:
            fail(f"{path}: duplicate {label} {key}={value}")
        seen.add(value)
        result.append(item)
    return result


def validate_service_shape(data: dict, path: Path) -> None:
    service = data["service"]
    if service == "ec2":
        validate_tiers(data.get("credit_tiers"), "credit_tiers", path)
    elif service == "s3":
        families = unique_ids(
            data.get("credit_tier_families"), "family_id", "credit_tier_families", path
        )
        for family in families:
            validate_tiers(
                family.get("tiers"),
                f"credit_tier_families[{family['family_id']}].tiers",
                path,
            )
    elif service == "rds":
        commitments = unique_ids(
            data.get("commitments"), "commitment_id", "commitments", path
        )
        for commitment in commitments:
            validate_tiers(
                commitment.get("tiers"),
                f"commitments[{commitment['commitment_id']}].tiers",
                path,
            )
    else:
        fail(f"{path}: unsupported Phase 0 AWS service {service!r}")


def validate_rule(path: Path) -> tuple[str, str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON: {exc}")

    if not isinstance(data, dict):
        fail(f"{path}: rule root must be an object")

    missing = [key for key in RULE_REQUIRED_KEYS if key not in data]
    if missing:
        fail(f"{path}: missing required keys {missing}")

    for key in (
        "schema_version", "provider", "service", "ruleset_id", "version", "status",
        "source_url", "source_last_updated", "source_version_observed_date",
        "source_version_date_semantics", "historical_version_registry",
        "measurement_period", "claim_deadline",
    ):
        require_nonempty_string(data, key, path)

    if data["schema_version"] != SCHEMA_VERSION:
        fail(f"{path}: unsupported schema_version {data['schema_version']!r}")
    if data["provider"] != "aws":
        fail(f"{path}: Phase 0 rule contract currently supports provider=aws only")
    if data["status"] != "DRAFT":
        fail(f"{path}: Phase 0 rule files must remain DRAFT")
    if not data["version"].startswith("draft-"):
        fail(f"{path}: DRAFT rule version must start with 'draft-'")
    if ".draft." not in path.name:
        fail(f"{path}: Phase 0 DRAFT rule filename must contain '.draft.'")

    service_dir = path.parent.name
    if service_dir != data["service"]:
        fail(f"{path}: service={data['service']!r} does not match directory {service_dir!r}")

    if not data["source_url"].startswith("https://aws.amazon.com/"):
        fail(f"{path}: normative source_url must use official aws.amazon.com SLA source")
    if data["source_version_observed_date"] != data["source_last_updated"]:
        fail(f"{path}: observed source date must equal recorded provider Last Updated date")
    if data["source_version_date_semantics"] != SOURCE_DATE_SEMANTICS:
        fail(f"{path}: source_version_date_semantics must preserve Last Updated != effective_from")

    registry = Path(data["historical_version_registry"])
    if not registry.is_file():
        fail(f"{path}: historical_version_registry does not exist: {registry}")

    for key in ("claim_requirements", "notes", "activation_blockers"):
        value = data[key]
        if not isinstance(value, list) or not value or not all(
            isinstance(item, str) and item.strip() for item in value
        ):
            fail(f"{path}: {key} must be a non-empty array of strings")

    # Current Phase 0 rules are intentionally not activatable. If these blockers
    # are resolved later, that requires explicit rule-review work rather than
    # silently weakening this validator.
    if data["effective_from"] is not None:
        fail(f"{path}: effective_from must remain unresolved (null) in current Phase 0 DRAFT")
    if data["effective_until"] is not None:
        fail(f"{path}: effective_until must remain unresolved (null) in current Phase 0 DRAFT")
    if data["source_snapshot_sha256"] is not None:
        fail(f"{path}: source_snapshot_sha256 must remain unresolved (null) in current Phase 0 DRAFT")

    validate_service_shape(data, path)
    return data["ruleset_id"], data["service"]



def tracked_files() -> list[Path]:
    """Return Git-tracked files so local caches/venvs are not scanned."""
    try:
        output = subprocess.check_output(
            ["git", "ls-files", "-z"], stderr=subprocess.DEVNULL
        )
        return [
            Path(item.decode("utf-8"))
            for item in output.split(b"\0")
            if item
        ]
    except (FileNotFoundError, subprocess.CalledProcessError):
        return [
            path
            for path in Path(".").rglob("*")
            if path.is_file() and ".git" not in path.parts
        ]


def secret_findings(text: str) -> list[str]:
    findings = []
    for label, pattern in SECRET_PATTERNS:
        if pattern.search(text):
            findings.append(label)
    return findings


def validate_repository_hygiene(paths: list[Path] | None = None) -> None:
    paths = tracked_files() if paths is None else paths
    findings: list[str] = []

    for path in paths:
        if ".git" in path.parts or not path.is_file():
            continue

        suffix = path.suffix.lower()
        if suffix in FORBIDDEN_SECRET_EXTENSIONS:
            findings.append(f"{path}: forbidden secret-bearing file extension {suffix}")
            continue

        if suffix in SENSITIVE_EVIDENCE_EXTENSIONS and SENSITIVE_EVIDENCE_NAME.search(path.name):
            findings.append(
                f"{path}: customer/billing/support evidence-like file is forbidden in public Git"
            )

        if suffix not in TEXT_EXTENSIONS and path.name != ".env.example":
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for label in secret_findings(text):
            findings.append(f"{path}: detected {label}")

    if findings:
        fail("Repository hygiene violations:\n- " + "\n- ".join(findings))


def main() -> None:
    missing = [p for p in REQUIRED_REPO_FILES if not Path(p).is_file()]
    if missing:
        fail(f"Missing required files: {missing}")

    rule_files = sorted(Path("rules/aws").rglob("*.draft.json"))
    if not rule_files:
        fail("No AWS DRAFT rule JSON files found")

    ruleset_ids: set[str] = set()
    services: set[str] = set()
    for path in rule_files:
        ruleset_id, service = validate_rule(path)
        if ruleset_id in ruleset_ids:
            fail(f"{path}: duplicate ruleset_id {ruleset_id}")
        ruleset_ids.add(ruleset_id)
        services.add(service)

    expected_services = {"ec2", "s3", "rds"}
    if services != expected_services:
        fail(f"Phase 0 AWS corpus services mismatch: expected {expected_services}, got {services}")

    real_env_files = [
        str(p) for p in Path(".").rglob(".env") if ".git" not in p.parts
    ]
    if real_env_files:
        fail(f"Real .env files are forbidden: {real_env_files}")

    validate_repository_hygiene()

    print(
        f"Validated {len(REQUIRED_REPO_FILES)} required files and "
        f"{len(rule_files)} AWS DRAFT rule contracts: {sorted(ruleset_ids)}"
    )


if __name__ == "__main__":
    main()
