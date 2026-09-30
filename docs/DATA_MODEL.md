# Data Model

Phase 0 does not create a production database. This file records target invariants only.

## Core entities

Partner -> Organization -> Provider Account -> Resource.

Additional entities: service catalog, SLA ruleset/version, incident, observation, evidence artifact, billing record/snapshot, evaluation, credit estimate, claim, claim event, recovery, audit event.

## Invariants

- Every tenant-owned record carries tenant scope.
- Raw evidence is immutable.
- Historical rules are immutable.
- Evaluations reference exact ruleset/engine/input/evidence/billing versions.
- Money records currency, exact amount representation, rounding rule and billing period.
- Timestamps are stored in UTC.
