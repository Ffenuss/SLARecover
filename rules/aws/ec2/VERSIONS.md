# EC2 observed SLA versions

Source: https://aws.amazon.com/compute/sla/historical/
Research date: 2026-09-30.

These are provider **Last Updated** observations, not automatically legal effective-from dates.

| Observed version date | Material commitment shape | Phase 0 handling |
|---|---|---|
| 2022-05-25 current | Region-Level 99.99% + monthly Instance-Level 99.5%; 10/30/100; automatic >6 min clockhour no-charge | Current DRAFT rule; applicability still must be established |
| 2022-05-05 prior | Region-Level + monthly Instance-Level 99.5%; same Instance-Level tiers/no-charge shape | Historical source candidate; do not alias silently to current |
| 2020-07-22 | 99.99% monthly broader commitment + Single EC2 hourly >=90%; failed hour not charged | Legacy hourly path required |
| 2019-03-19 | 99.99% monthly broader commitment + Single EC2 hourly >=90%; failed hour not charged | Legacy hourly path required |
| 2018-02-12 | Region-Unavailability 99.99%; individual instance failures not attributable to Region Unavailability excluded | Do not use Instance-Level rule |
| 2017-12-01 | Region-style 99.99%; 10%/30% tiers | Source-specific review |
| 2017-11-15 | EC2/EBS 99.99% Region-style | Source-specific review |
| 2013-06-01 | EC2/EBS 99.95% monthly | Source-specific review |

No historical version is ACTIVE in SLARecover yet.
