# AWS SLA Corpus v0

Research verification date: **2026-09-30**.

Phase 0 corpus covers three AWS services/commitment families selected for comparative validation. Every rule remains **DRAFT**.

| Service | Current official SLA | Last updated | Corpus status | First vertical? |
|---|---|---:|---|---|
| EC2 Instance-Level | https://aws.amazon.com/compute/sla/ | 2022-05-25 | DRAFT rule + manual Claim Pack + open questions | **Yes** |
| S3 | https://aws.amazon.com/s3/sla/ | 2023-11-28 | DRAFT rule + boundary fixture plan | No |
| RDS | https://aws.amazon.com/rds/sla/ | 2024-01-22 | DRAFT rule + boundary fixture plan | No |

## Shared claim pattern

All three current SLAs require:
- claim through AWS Support Center;
- provider-specific required fields;
- request logs / corroborating evidence;
- receipt by the end of the second billing cycle after the incident;
- an applicable monthly credit amount greater than USD 1;
- service credits applied to future service payments (subject to AWS terms).

These similarities are useful for the future domain model but do **not** justify a generic formula: measurement units, availability definitions, tier families, billing scopes and exclusions differ materially.

## EC2

Selected first vertical because the Instance-Level formula is comparatively compact and resource-scoped.

Blocking interpretation/evidence items are maintained in:
`docs/research/2026-09-30-ec2-open-questions.md`.

## S3

Current measurement is request-based:
- Error Rate is defined per request type/storage class over 5-minute intervals;
- only `InternalError` and `ServiceUnavailable` internal server errors enter the numerator;
- a 5-minute interval with no requests is treated as 0% Error Rate;
- there are two credit-tier families by storage class/request category;
- S3 Express One Zone changes billing geography from Region to AZ.

The current page does not provide enough implementation detail in the reviewed wording to safely encode every multi-request-type aggregation case. That remains an explicit DRAFT blocker.

## RDS

Current measurement is connection-based:
- Unavailable means **all** connection requests to the running DB resource fail during a 1-minute interval;
- Multi-AZ and Single-DB commitments have different first thresholds;
- the SLA explicitly treats the portion of the month when a DB resource was not running as 100% available;
- exclusions include constrained instance classes, operational-guideline failures, DB-engine crashes and insufficient IO capacity.

This larger exclusion surface is why RDS was not selected first.

## Activation blockers for every corpus rule

A rule may not become ACTIVE until:
- historical/effective version timeline is evidenced;
- official source snapshot strategy and hash are implemented;
- ambiguous semantics are resolved;
- golden tests exist;
- threshold/deadline boundary tests exist;
- reviewer approval is recorded.

Phase 0 corpus completeness therefore means “researched and structured as non-active rules,” not “production-ready”.
