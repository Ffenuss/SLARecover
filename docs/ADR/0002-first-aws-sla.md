# ADR-0002: First AWS SLA for vertical prototype

- Date: 2026-09-30
- Status: Accepted for Phase 0 research/prototyping

## Context

Phase 0 requires a small, end-to-end SLA recovery slice before broad provider coverage. EC2, S3 and RDS were compared using current official AWS SLA and service documentation.

## Decision

Use the **Amazon EC2 Instance-Level SLA** as the first vertical prototype rule.

This is not a production ACTIVE rule. Evidence sufficiency remains a blocking condition for every real claim.

## Rationale

- Single-resource measurement scope.
- Simple monthly minute-based formula and clear threshold boundaries.
- Explicit billing basis and claim fields.
- Easier golden/boundary fixtures than S3 request-rate aggregation.
- Smaller exclusion/deployment-mode surface than RDS.
- Forces the product to handle the key evidence problem correctly: AWS requires request logs/validation data, and EC2 status checks alone are not equivalent to “no external connectivity.”

## Alternatives

### Amazon S3

Rejected for the first slice because the SLA uses 5-minute Error Rate averaging by request type/storage class. Server access logging is not enabled by default and request metrics require opt-in.

### Amazon RDS

Rejected for the first slice because Multi-AZ vs Single-DB branching and additional exclusions increase interpretation surface. RDS events are available from DescribeEvents for only 14 days unless exported elsewhere.

## Consequences

- Phase 0 concierge audits must select EC2 cases with existing request/application monitoring evidence.
- Missing evidence returns INSUFFICIENT_EVIDENCE.
- Future evidence-readiness design must snapshot minute-resolution data before CloudWatch aggregation.
- Region-Level EC2 SLA is excluded from the first prototype.
