#!/usr/bin/env python3
"""Run the complete Phase 0 technical validation suite.

This is the single local/CI entry point for Phase 0 engineering checks.
It intentionally does not build or evaluate the future product.
"""

from __future__ import annotations

import subprocess
import sys
from collections.abc import Callable, Sequence

Command = Sequence[str]
Runner = Callable[..., subprocess.CompletedProcess]


def checks() -> list[tuple[str, list[str]]]:
    python = sys.executable
    return [
        (
            "repository and draft-rule contracts",
            [python, "scripts/validate_phase0.py"],
        ),
        (
            "synthetic evidence-manifest integration",
            [
                python,
                "scripts/validate_evidence_manifest.py",
                "fixtures/phase0/evidence-manifest.synthetic.json",
            ],
        ),
        (
            "synthetic source-snapshot provenance",
            [
                python,
                "scripts/source_snapshot_manifest.py",
                "validate",
                "fixtures/phase0/source-snapshot-manifest.synthetic.json",
            ],
        ),
        (
            "unit tests",
            [
                python,
                "-m",
                "unittest",
                "discover",
                "-s",
                "tests",
                "-p",
                "test_*.py",
            ],
        ),
    ]


def run_checks(runner: Runner = subprocess.run) -> int:
    for label, command in checks():
        print(f"==> {label}")
        result = runner(command, check=False)
        if result.returncode != 0:
            print(f"FAILED: {label} (exit {result.returncode})", file=sys.stderr)
            return result.returncode
    print("All Phase 0 technical checks passed.")
    return 0


def main() -> int:
    return run_checks()


if __name__ == "__main__":
    raise SystemExit(main())
