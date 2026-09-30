# Threat Model v0

## Critical assets

Customer/provider credentials and authorizations, raw evidence and hashes, billing snapshots, rulesets, evaluation results, claim approvals/submissions, and tenant boundaries.

| Threat | Severity | Primary controls |
|---|---|---|
| Cross-tenant data exposure | Critical | Tenant scope on all owned objects; negative isolation tests. |
| Unauthorized claim submission | Critical | Separate submission role, MFA, explicit approval, kill switches. |
| Evidence tampering | High | Immutable raw evidence, SHA-256, append-only audit. |
| Systemic financial miscalculation | Critical | Versioned deterministic rules, golden/boundary tests, replay. |
| Static credential compromise | Critical | Federation/STS; no customer access keys. |
| Provider outage blinds monitoring | High | Independent/customer telemetry; provider signal is not sole evidence. |
| Rule/source drift | High | Official-source registry, immutable versions, review before activation. |

Phase 0 must validate which evidence can actually be obtained from design partners before permission scopes are finalized.
