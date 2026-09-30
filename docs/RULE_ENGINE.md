# Rule Engine Contract

No production rule engine is implemented in Phase 0. Phase 0 builds the verified source corpus that later rules depend on.

## Required rule metadata

provider, service, ruleset_id, version, status, effective_from/effective_until, source_url, source snapshot/hash, measurement period, formula, thresholds/credit tiers, exclusions, claim requirements, claim deadline and evidence requirements.

## Lifecycle

DRAFT -> TESTING -> REVIEWED -> ACTIVE -> DEPRECATED/DISABLED.

ACTIVE is forbidden without an official source, source snapshot, golden tests, boundary tests and review.

## Determinism

A historical evaluation must be replayable against the exact historical ruleset and immutable inputs. No AI output may determine eligibility, credit tier or amount.

## Historical source dating

Provider labels such as `Last Updated` are source metadata, not automatically legal effective dates.

A ruleset stores these separately:
- source/version observed date;
- `effective_from`;
- `effective_until`;
- applicability evidence/rationale.

If a historical incident cannot be mapped to a rule version without importing assumptions from a later version, evaluation returns `REVIEW_REQUIRED`.
