# GitHub Actions

`phase0-validation.yml` runs only for relevant pull-request paths (or manual dispatch) and validates the Phase 0 repository skeleton and draft rule JSON.

It intentionally does not fake application checks before application code exists.

When the first executable package lands, CI must expand to include:
- typecheck;
- lint;
- unit tests;
- rule golden tests;
- build.

Tests will not be disabled or replaced with mock success to make CI green.
