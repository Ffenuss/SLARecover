# Rule Engine Contract

No production rule engine is implemented in Phase 0. Phase 0 builds the verified source corpus that later rules depend on.

## Required rule metadata

provider, service, ruleset_id, version, status, effective_from/effective_until, source_url, source snapshot/hash, measurement period, formula, thresholds/credit tiers, exclusions, claim requirements, claim deadline and evidence requirements.

## Lifecycle

DRAFT -> TESTING -> REVIEWED -> ACTIVE -> DEPRECATED/DISABLED.

ACTIVE is forbidden without an official source, source snapshot, golden tests, boundary tests and review.

## Determinism

A historical evaluation must be replayable against the exact historical ruleset and immutable inputs. No AI output may determine eligibility, credit tier or amount.
