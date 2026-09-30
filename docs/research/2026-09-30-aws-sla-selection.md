# AWS EC2 vs S3 vs RDS SLA selection

Research date: **2026-09-30**.

Primary sources: current official AWS SLA pages and AWS documentation only.

## Current official SLA versions observed

| Service | Current page | Page last updated |
|---|---|---|
| EC2 / Amazon Compute SLA | https://aws.amazon.com/compute/sla/ | 2022-05-25 |
| Amazon S3 | https://aws.amazon.com/s3/sla/ | 2023-11-28 |
| Amazon RDS | https://aws.amazon.com/rds/sla/ | 2024-01-22 |

Historical AWS SLA pages exist and must be checked before evaluating incidents that predate the current version.

## Comparison matrix

| Criterion | EC2 Instance-Level | S3 | RDS |
|---|---|---|---|
| Measurement formula | 100% minus percentage of minutes in the monthly billing cycle when one EC2 instance is Unavailable; Unavailable means no external connectivity. | 100% minus the average Error Rate from each 5-minute interval; Error Rate is internal server errors divided by total requests per request type/storage class. | 100% minus percentage of 1-minute intervals in which all connection requests to the running DB resource fail. |
| Current credit tiers | <99.5% and >=99.0%: 10%; <99.0% and >=95.0%: 30%; <95.0%: 100%. | Standard/Express/Glacier family: <99.9%/>=99.0%: 10%; <99.0%/>=95.0%: 25%; <95.0%: 100%. IA family starts at 99.0% and 98.0%. | Multi-AZ: <99.95%/>=99.0%: 10%; <99.0%/>=95.0%: 25%; <95.0%: 100%. Single-DB: <99.5%/>=99.0%: 10%; then 25%/100%. |
| Evidence required by SLA | Subject, incident dates/times, region+AZ, instance IDs, request logs and other data needed to validate outage. | Subject, billing cycle/region, incident dates/times for non-zero Error Rates, request logs. | Subject, dates/times, DB IDs/regions, request logs corroborating outage. |
| Billing basis | Monthly bill for the affected Single EC2 Instance in the affected Region; excludes one-time payments such as upfront Reserved Instance payments. | Total charges for the applicable S3 storage class in the affected Region/AZ for the billing cycle. | Charges for the affected DB Instance/Cluster in the affected Region for the billing cycle. |
| Claim deadline | End of the second billing cycle after the incident. | End of the second billing cycle after the incident. | End of the second billing cycle after the incident. |
| Exclusions | Outside AWS control; customer actions/inactions; customer equipment/software/technology; suspension/termination. | Similar broad categories. | Broader surface, including constrained instance classes, failure to follow operational guidance, DB engine crashes and insufficient IO capacity. |
| Retrospective evidence | Automatic EC2 status checks exist at 1-minute frequency at no charge, but 1-minute CloudWatch resolution is retained only 15 days, then aggregated. Status checks are corroborating evidence, not proof of “no external connectivity”. Existing customer request/application logs remain necessary. | Server access logging is not collected by default. Request metrics require opt-in and are billed as CloudWatch custom metrics; CloudWatch metrics are best-effort and are not a complete accounting of requests. If durable server access logs already exist, they can be strong retrospective evidence. | RDS sends metrics at 1-minute periods by default, but 1-minute resolution is retained only 15 days; DescribeEvents exposes only the past 14 days. SLA still requires request logs, and generic DB metrics do not prove all connection attempts failed. |
| Rule implementation complexity | Low for Instance-Level scope. Region-Level is deliberately excluded from the first slice. | High: 5-minute aggregation, request-type/storage-class branches and complete request denominator. | Medium-high: simple minute intervals but additional deployment-mode and exclusion branches. |
| Synthetic/golden testability | Excellent. | Good but fixture-heavy. | Good, with more exclusion fixtures. |

## Decision

**Select Amazon EC2 Instance-Level SLA for the first vertical prototype.**

Why:
1. The rule itself is compact, deterministic and has clear threshold boundaries.
2. The covered object is a single instance, avoiding Region-Level multi-AZ concurrency semantics.
3. The billing scope and provider-required claim fields are explicit.
4. Golden and boundary fixtures are substantially simpler than S3 request aggregation or the RDS exclusion matrix.
5. It exposes the core product risk early: SLA eligibility cannot be inferred from provider health/status alone; request/application evidence must be present.

## Evidence gate

EC2 is selected for rule-engine prototyping, **not because AWS automatically retains enough evidence for historical recovery**. For Phase 0 concierge audits, a candidate case is acceptable only when the design partner already has sufficient request/application monitoring evidence or equivalent data AWS can validate. Missing evidence must produce `INSUFFICIENT_EVIDENCE`, never inferred downtime.

A product requirement follows from this finding: for future connected accounts, SLARecover will need an evidence-readiness check and timely evidence snapshotting before CloudWatch minute-level resolution is aggregated.

## Support/API constraint

Current AWS documentation says AWS Support API and AWS Health API require Business Support+, Enterprise Support, or Unified Operations (with legacy-plan fallbacks in some regions/accounts). Therefore API-based submission/Health collection cannot be assumed for every customer. Manual/assisted Support Center submission is the baseline.

Official sources:
- https://aws.amazon.com/compute/sla/
- https://aws.amazon.com/compute/sla/historical/
- https://aws.amazon.com/s3/sla/
- https://aws.amazon.com/s3/sla/historical/
- https://aws.amazon.com/rds/sla/
- https://aws.amazon.com/rds/sla/historical/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudwatch-monitoring.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html
- https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html
- https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html
- https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html
