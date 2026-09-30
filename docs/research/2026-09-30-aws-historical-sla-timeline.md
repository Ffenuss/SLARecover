# AWS Historical SLA Timeline — EC2, S3, RDS

Research date: **2026-09-30**.

Official sources:
- https://aws.amazon.com/compute/sla/
- https://aws.amazon.com/compute/sla/historical/
- https://aws.amazon.com/s3/sla/
- https://aws.amazon.com/s3/sla/historical/
- https://aws.amazon.com/rds/sla/
- https://aws.amazon.com/rds/sla/historical/

## Evidence rule

AWS labels the entries below with **Last Updated** dates. SLARecover must not silently treat a page's Last Updated date as a legally proven `effective_from` timestamp.

For a historical audit:
1. identify the incident timestamp;
2. identify the AWS historical page/version that appears applicable;
3. preserve the relevant official page/snapshot;
4. record the basis for applicability;
5. if the boundary/effective date cannot be established with sufficient confidence, return `REVIEW_REQUIRED`.

The timeline below is therefore an **observed version timeline**, not a legal effective-date opinion.

## Amazon EC2 / Compute

### Current — Last Updated May 25, 2022

Current Amazon Compute SLA covers Amazon EC2 and contains two distinct commitments:
- Region-Level: 99.99% monthly;
- Instance-Level: 99.5% monthly for a Single EC2 Instance.

Current Instance-Level tiers:
- <99.5% and >=99.0% -> 10%;
- <99.0% and >=95.0% -> 30%;
- <95.0% -> 100%.

It also separately states that AWS will not charge for a Single EC2 Instance that is Unavailable for more than six minutes of a clockhour.

### Prior — Last Updated May 5, 2022

AWS's official historical page shows essentially the same two-commitment shape for Included Services, including the 99.5% monthly Instance-Level SLA, the same 10/30/100 Instance-Level tiers, the >6-minutes-per-clockhour automatic no-charge treatment, and separate Region-Level/Instance-Level claim subjects.

**Implication:** a May-2022-or-later-looking historical case may fit the current manual Instance-Level workflow, but the observed page date alone is not enough to prove the exact effective boundary.

### Prior — Last Updated July 22, 2020

This version did **not** use the current monthly 99.5% Instance-Level credit model.

For a Single EC2 Instance it instead states:
- Hourly Uptime Percentage >= 90% of deployed time during each clock hour;
- if the Hourly Commitment is not met, the customer is not charged for that instance hour.

The broader Included Service commitment remained a 99.99% monthly Region-level style commitment with 10/30/100 tiers.

**Implication:** a 2020 Single EC2 incident must not be evaluated with the current monthly 99.5% Instance-Level tiers. It needs a legacy hourly-rule path.

### Prior — Last Updated March 19, 2019

The same material split is visible:
- general 99.99% monthly service commitment;
- Single EC2 Instance Hourly Uptime Percentage >=90%;
- failure of the hourly commitment results in no charge for that instance hour.

**Implication:** current Instance-Level monthly Claim Pack arithmetic is inapplicable to this legacy Single EC2 mechanism.

### Prior — Last Updated February 12, 2018

The public historical version is Region-level in substance:
- 99.99% monthly service commitment;
- Monthly Uptime depends on Region Unavailability;
- individual instance/volume failures not attributable to Region Unavailability are explicitly within the exclusions.

No separate monthly Single EC2 Instance credit commitment is shown.

**Implication:** an isolated single-instance failure cannot be assumed eligible from current Instance-Level logic.

### Older observed versions

AWS's public historical page also lists:
- December 1, 2017 — 99.99% Region-style commitment; 10% / 30% tiers;
- November 15, 2017 — EC2/EBS 99.99% Region-style commitment;
- June 1, 2013 — EC2/EBS 99.95% monthly service commitment.

These versions require their own source-specific interpretation before any historical calculation.

## Amazon S3

### Current — Last Updated November 28, 2023

The current page:
- scopes billing credit to the applicable S3 storage class;
- adds S3 Express One Zone with affected-AZ billing geography;
- includes S3 Express One Zone and S3 Glacier Flexible Retrieval in the first credit-tier family;
- retains the two credit-tier families and request-based 5-minute Error Rate model.

### Prior public version — Last Updated May 5, 2022

The official historical page currently exposes a May 5, 2022 version.

Materially:
- first tier family listed S3 Standard, S3 Glacier, S3 Glacier Deep Archive and other requests;
- second tier family listed Intelligent-Tiering, Standard-IA, One Zone-IA and Glacier Instant Retrieval;
- billing basis was the applicable Amazon S3 Service in the affected Region;
- same end-of-second-billing-cycle deadline and request-log requirement are visible.

**Implication:** current S3 Express One Zone/AZ-specific logic must not be projected backward into the May 2022 version.

### Earlier history

The current AWS historical page reviewed on 2026-09-30 exposes only the May 5, 2022 prior version. SLARecover must not invent older S3 versions from absence on that page. A pre-May-2022 case is `REVIEW_REQUIRED` until an authoritative archived source is obtained.

## Amazon RDS

### Current — Last Updated January 22, 2024

The current RDS SLA contains two commitment families:
- Multi-AZ DB Instance / Multi-AZ DB Cluster;
- Single-DB Instance.

Current tiers:
- Multi-AZ first threshold: 99.95%;
- Single-DB first threshold: 99.5%;
- both have 10% / 25% / 100% credit tiers.

Claims under the two commitment families cannot be stacked.

### Prior — Last Updated March 21, 2019

The historical version is Multi-AZ-only:
- 99.95% monthly commitment;
- 10% / 25% / 100% tiers;
- one-minute Unavailability when all connection requests to the running Multi-AZ instance fail;
- partial-month rule: the resource is assumed 100% available for the portion of the month it was not running;
- request logs, DB Instance IDs and Regions required.

The definition covers MySQL, MariaDB, Oracle, PostgreSQL and SQL Server Multi-AZ instances.

**Implication:** the current Single-DB commitment must not be applied to an incident governed by this older version.

### Prior — Last Updated October 26, 2018

This version is also Multi-AZ-only with a 99.95% monthly commitment and the explicit partial-month 100%-available rule.

The visible tier table on the historical page shows:
- <99.95% and >=99.0% -> 10%;
- <99.0% -> 25%.

Do not infer a 100% tier for this version merely because later versions contain one.

The Multi-AZ definition visible in this version lists MySQL, MariaDB, Oracle and PostgreSQL.

### February 21, 2017 entry

The historical page contains an entry tied to the AWS agreement for Beijing Sinnet / aws.amazon.cn.

**Implication:** do not treat this as the global commercial AWS RDS rule without jurisdiction/account evidence.

### Older global observed versions

The historical page also lists global versions:
- March 25, 2016;
- June 1, 2013.

Both are Multi-AZ-oriented 99.95% commitments and require source-specific review for any actual historical case.

## Product consequences

1. Historical rule selection is a first-class correctness problem, not a metadata nicety.
2. A rule registry needs an observed source-version date and a separately proven `effective_from/effective_until`.
3. Historical replay must pin the exact ruleset, not “latest for service”.
4. The current EC2 manual Instance-Level worksheet is only valid after a reviewer establishes that the monthly Instance-Level commitment applies.
5. If the historical source boundary is ambiguous, the financial decision state is `REVIEW_REQUIRED`.
