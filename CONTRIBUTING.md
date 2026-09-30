# Contributing

## Workflow

- Do not make significant changes directly on `main`.
- Use `feature/<name>` branches.
- Keep each logical task in its own branch/PR.
- Run applicable tests, lint, typecheck and build before merge.
- Never disable a failing correctness/security test to make CI green.
- Review the diff before merge.
- Financial-rule changes require golden and boundary tests plus review.

## Phase discipline

A PR must identify its roadmap phase. Work outside the current phase belongs in `docs/BACKLOG.md` unless it is prerequisite research explicitly allowed by the roadmap.
