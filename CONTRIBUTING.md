# Contributing

## Workflow

- Do not make significant changes directly on `main`.
- Use `feature/<name>` branches.
- Keep each logical task in its own branch/PR.
- Run the current phase's reproducible local check before merge. For Phase 0: `python scripts/check_phase0.py`.
- Run applicable lint, typecheck and build once those toolchains exist for the active phase.
- Never disable a failing correctness/security test to make CI green.
- Review the diff before merge.
- Financial-rule changes require golden and boundary tests plus review.

## Phase discipline

A PR must identify its roadmap phase. Work outside the current phase belongs in `docs/BACKLOG.md` unless it is prerequisite research explicitly allowed by the roadmap.

## Phase 0 local checks

Prerequisite: Python 3.11+ and Git.

From the repository root:

```bash
python scripts/check_phase0.py
```

This is intentionally the same command used by GitHub Actions. It runs:
1. repository and AWS DRAFT-rule contract validation;
2. the synthetic evidence-manifest integration path;
3. the full standard-library unittest suite.

No package installation is required for the current Phase 0 check suite.
