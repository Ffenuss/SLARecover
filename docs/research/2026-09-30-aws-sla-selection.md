# AWS EC2 vs S3 vs RDS SLA selection

Research date: **2026-09-30**.

Only current official AWS sources were used.

## Current official SLA versions observed

| Service | Current page | Page last updated |
|---|---|---|
| EC2 / Amazon Compute SLA | https://aws.amazon.com/compute/sla/ | 2022-05-25 |
| Amazon S3 | https://aws.amazon.com/s3/sla/ | 2023-11-28 |
| Amazon RDS | https://aws.amazon.com/rds/sla/ | 2024-01-22 |

Historical AWS SLA pages exist for all three and must be checked before evaluating incidents that predate the current version.

## Comparison matrix

| Criterion | EC2 Instance-Level | S3 | RDS |
|---|---|---|---|
| Measurement formula | Monthly uptime = 100% minus percentage of minutes in which the single instance is unavailable. AWS defines unavailable as no external connectivity. | Monthly uptime = 100% minus average Error Rate across each 5-minute interval; Error Rate is computed per request type/storage class. | Monthly/instance uptime = 100% minus percentage of 1-minute intervals in which all connection requests to the running DB resource fail. |
| Current credit tiers | <99.5% and >=99.0%: 10%; <99.0% and >=95.0%: 30%; <95.0%: 100%. | Two storage-class/request families. Common family: <99.9%/>=99.0%: 10%; <99.0%/>=95.0%: 25%; <95.0%: 100%. | Multi-AZ: <99.95%/>=99.0%: 10%; <99.0%/>=95.0%: 25%; <95.0%: 100%. Single DB starts at 99.5%. |
| Evidence required by SLA | Subject, dates/times, region+AZ, instance IDs, request logs and other validation data. | Subject, billing cycle/region, dates/times of non-zero Error Rate incidents, request logs. | Subject, dates/times, DB IDs/regions, request logs corroborating outage. |
| Billing basis | Monthly EC2 bill for affected single instance/region under selected SLA; one-time upfront RI payments excluded. | Total charges for applicable storage class in affected Region/AZ for billing cycle. | Charges paid for affected DB instance/cluster in affected Region for billing cycle. |
| Claim deadline | End of second billing cycle after incident. | End of second billing cycle after incident. | End of second billing cycle after incident. |
| Exclusions | Outside AWS control; customer actions/inactions; customer equipment/software/technology; suspension/termination. | Similar broad exclusions. | Broader operational/configuration exclusion surface, including constrained instance classes, guideline violations, engine crashes and insufficient IO capacity. |
| Historical evidence practicality | Best of the three for a first prototype. EC2 status-check metrics are automatically available at 1-minute frequency at no charge and CloudWatch instance metrics are retained for 15 months. They are supporting evidence, not a substitute for request logs. | Weakest retrospectively. S3 server access logging is not collected by default; 1-minute request metrics require opt-in and are billed. | Moderate. RDS sends 1-minute CloudWatch metrics by default, but RDS events are retrievable only up to 14 days unless forwarded elsewhere. Request logs are still required. |
| Implementation complexity | Low for Instance-Level scope. Region-Level is excluded from first vertical slice. | High: 5-minute aggregation, request types, storage-class variants, full request denominator. | Medium-high: simple intervals but more exclusions and deployment-mode branching. |
| Synthetic/golden testability | Excellent. | Good but fixture-heavy. | Good, with more exclusion fixtures. |

## Decision

**Select Amazon EC2 Instance-Level SLA for the first vertical end-to-end prototype.**

Rationale:
1. Compact deterministic formula and boundaries.
2. Single-resource scope avoids Region-Level multi-AZ concurrency semantics.
3. Automatic 1-minute EC2 status checks and 15-month CloudWatch metric retention improve retrospective triage.
4. Billing can be scoped to the affected instance; claim requirements explicitly name identifiers and request-log evidence.
5. Golden and boundary fixtures are straightforward compared with S3 aggregation and RDS exclusion breadth.

## Important limitation

EC2 status-check failures are **not equivalent** to the SLA definition of “no external connectivity.” They can corroborate an incident, but a valid Claim Pack still needs the request logs/other data AWS requires. A Phase 0 audit must return insufficient evidence rather than infer eligibility from status checks alone.

## Support/API constraint

Current AWS Support API and AWS Health API documentation requires qualifying AWS Support plans (Business Support+, Enterprise Support, or Unified Operations, with legacy-plan fallbacks in some regions/accounts). API submission/Health collection cannot be assumed for every customer. Manual/assisted Support Center submission remains the baseline.

Official sources:
- https://aws.amazon.com/compute/sla/
- https://aws.amazon.com/compute/sla/historical/
- https://aws.amazon.com/s3/sla/
- https://aws.amazon.com/s3/sla/historical/
- https://aws.amazon.com/rds/sla/
- https://aws.amazon.com/rds/sla/historical/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-configurations.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html
- https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html
- https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html
- https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html
