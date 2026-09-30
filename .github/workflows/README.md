# GitHub Actions

No executable application code exists in Phase 0, so CI workflows are intentionally not added yet.

When the first executable package lands, the baseline workflow must run only on useful push/PR events and include:
- typecheck;
- lint;
- unit tests;
- rule golden tests;
- build.

Tests will not be disabled or replaced with mock success to make CI green.
