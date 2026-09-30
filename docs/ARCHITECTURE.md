# Architecture

## Phase 0 position

No production architecture is deployed in Phase 0. Architecture work is limited to constraints that protect future correctness and validation.

## Target domain flow

Provider/customer evidence -> normalization -> incident model -> immutable evidence -> versioned SLA rules -> deterministic evaluation -> credit estimate -> Claim Pack -> human review -> outcome tracking.

## Non-negotiable boundaries

- Core domain logic remains independent of HTTP frameworks and cloud SDKs.
- Rules are versioned data/DSL, not scattered application conditionals.
- Raw evidence is immutable; normalized artifacts are derived.
- Every financial result records ruleset version, engine version, evidence/input hashes and billing snapshot.
- Money uses decimal-safe or integer-minor-unit representations; never binary floating point.
- Internal timestamps are UTC.
- Tenant-owned objects are tenant-scoped.
- Submission permissions are separate from monitoring permissions.
- Auto-submit remains off until its dedicated phase and legal/security gates.

## Candidate future stack

TypeScript/Node.js, PostgreSQL, CLI first, Next.js later, provider adapters around cloud SDKs. Durable workflow technology is deferred until demonstrated necessary.
