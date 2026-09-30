# Phase 0 Validation Scorecard

Use one row per interview/design-partner candidate. Store redacted identifiers only.

## ICP fit fields

| Field | Values |
|---|---|
| Segment | MSP / FinOps / high-spend company / SaaS / other |
| AWS annual spend band | <€100k / €100k–€1m / €1m–€10m / >€10m / unknown |
| Accounts/customers managed | 1 / 2–10 / 11–100 / >100 / unknown |
| Incident frequency | none / rare / quarterly / monthly+ / unknown |
| Current SLA recovery process | systematic / ad hoc / none |
| Historical evidence retention | strong / partial / weak / unknown |
| Billing evidence available | yes / partial / no |
| Request/application logs available | yes / partial / no |
| Read-only pilot feasible | yes / maybe / no |
| Real-case audit commitment | yes / maybe / no |
| Design-partner commitment | yes / maybe / no |

## Problem-frequency matrix

For each interview, record:
- number of material cloud incidents in the last 12 months;
- number reviewed against SLA;
- number of claims submitted;
- number accepted/rejected/pending;
- number missed because of deadline;
- number abandoned because evidence/calculation effort was too high;
- approximate engineering/FinOps hours per investigated claim.

Unknown is preferable to an invented estimate.

## Evidence-readiness classification

**READY** — candidate incident has the provider-required identifiers, time window, billing basis and request/application evidence sufficient to attempt deterministic SLA reconstruction.

**PARTIAL** — some material evidence exists, but one or more provider-required elements must be recovered before calculation can be trusted.

**INSUFFICIENT** — the incident cannot currently support the SLA definition or provider validation requirements. Do not convert provider-health/status signals into inferred eligibility.

## Design-partner commitment threshold

Count a partner as committed only if they agree to provide a real or safely redacted incident/evidence set for a manual audit and to review the resulting calculation. General interest alone does not count.

## Phase 0 falsification signals

Escalate toward PIVOT/NO-GO if repeated real interviews show one or more of these patterns:
- material SLA incidents are too rare in the target ICP to support meaningful recovery economics;
- customers systematically lack evidence needed before claim deadlines;
- eligible credits are consistently too small relative to recovery effort;
- security/access requirements make a lightweight read-only pilot unacceptable;
- provider processes reject well-supported claims at a rate that destroys expected value;
- customers are unwilling to provide data or act on generated Claim Packs;
- legal/commercial review blocks the proposed operating model.

Do not decide GO from interview enthusiasm. Use real cases, reproducible calculations and claim outcomes.
