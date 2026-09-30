# Manual Calculation Worksheet — AWS EC2 Instance-Level SLA

Research/source verification date: **2026-09-30**.

Normative source for a current incident:
https://aws.amazon.com/compute/sla/

For a historical incident, stop and identify the official historical SLA version first:
https://aws.amazon.com/compute/sla/historical/

This worksheet is for Phase 0 concierge audits. It is not the future production rule engine.

## 0. Decision states

Only these outputs are permitted:

- `ELIGIBLE`
- `NOT_ELIGIBLE`
- `INSUFFICIENT_EVIDENCE`
- `REVIEW_REQUIRED`

Do not force a binary answer when a source fact is missing or ambiguous.

## 1. Ruleset identity

- Provider: AWS
- Service: Amazon EC2
- SLA scope: Instance-Level
- Incident date:
- Official SLA URL:
- SLA page/version date:
- Effective-from basis:
- Source snapshot identifier:
- Source SHA-256:
- Reviewer:
- Review date:

If the applicable historical version is not established, return `REVIEW_REQUIRED`.

## 2. Customer/resource facts

Keep sensitive values outside the public repository.

- Organization/customer reference:
- AWS account reference:
- Region:
- Availability Zone:
- EC2 instance ID:
- Monthly billing cycle start UTC:
- Monthly billing cycle end UTC:
- Incident window(s) UTC:
- Instance lifecycle facts relevant to the month:
- AWS Support/event references:

The current Instance-Level SLA requires the affected Region, AZ, resource IDs, incident dates/times, and request logs/other validation data.

## 3. Evidence inventory

| Evidence | Present | Coverage | Hash/reference | Assessment |
|---|---|---|---|---|
| Request/application logs | | | | |
| Independent/synthetic monitoring | | | | |
| EC2/CloudWatch status evidence | | | | |
| AWS Health/Support evidence | | | | |
| Billing invoice/CUR detail | | | | |
| Resource lifecycle/configuration evidence | | | | |

### Evidence gate

The SLA defines Instance-Level Unavailability as the Single EC2 Instance having **no external connectivity**.

CloudWatch/status evidence can corroborate the timeline but must not be substituted for request/application evidence merely because it is easier to retrieve.

If the evidence cannot support the SLA-defined condition, return `INSUFFICIENT_EVIDENCE`.

## 4. Exclusion review

For every candidate unavailability interval, assess the current/historical SLA exclusions:

| Exclusion category | Applies? | Evidence/reasoning |
|---|---|---|
| Factor outside AWS reasonable control | | |
| Internet/access problem beyond AWS demarcation point | | |
| Customer action/inaction | | |
| Failure to acknowledge recovery/respond to resource health concern | | |
| Customer equipment/software/technology | | |
| AWS suspension/termination under Agreement | | |
| Other exclusion in applicable historical SLA | | |

Any material unresolved exclusion -> `REVIEW_REQUIRED`.

## 5. Minute determination

Current formula:

`Instance-Level Uptime Percentage = 100% - percentage of minutes during the month in which the Single EC2 Instance was Unavailable`.

Record:

- Total minutes in applicable monthly billing cycle: `T =`
- Candidate unavailable minutes from evidence:
- Minutes removed because an SLA exclusion applies:
- SLA-unavailable minutes after exclusions: `U =`

Then calculate using exact decimal/rational arithmetic:

`Uptime = 100 * (T - U) / T`

Do not use binary floating point for the authoritative result.

### Partial-minute ambiguity

If the evidence starts/stops inside a minute and the applicable SLA does not specify the normalization/rounding convention needed to decide whether that minute counts, preserve the raw timestamps and return `REVIEW_REQUIRED` for the disputed minutes rather than inventing a rounding rule.

## 6. Credit tier

Current 2022-05-25 Instance-Level thresholds:

| Instance-Level Uptime Percentage | Service Credit |
|---|---:|
| < 99.5% and >= 99.0% | 10% |
| < 99.0% and >= 95.0% | 30% |
| < 95.0% | 100% |
| >= 99.5% | 0% under the Instance-Level monthly SLA |

Boundary values are literal. For example, exactly 99.5% does not enter the first credit tier; exactly 99.0% does.

Record:
- Exact uptime:
- Applicable comparison:
- Credit percentage:

## 7. Eligible spend

AWS states the Service Credit is a percentage of the monthly bill for the affected Single EC2 Instance in the affected Region, excluding one-time payments such as upfront Reserved Instance payments.

Use customer billing evidence, not a reconstruction from public list prices.

Record:
- Billing source:
- Billing period:
- Currency:
- Gross affected-instance amount:
- One-time/upfront amounts excluded:
- Other adjustments already present on the invoice:
- Candidate eligible spend:
- Exact representation / minor units:
- Rounding rule/source:

If the affected-instance spend cannot be isolated reliably, return `INSUFFICIENT_EVIDENCE` or `REVIEW_REQUIRED` as appropriate.

## 8. Automatic >6-minute clockhour no-charge provision

The current SLA separately states that AWS will not charge for a Single EC2 Instance that is Unavailable for more than six minutes of a clockhour, and no request is required for that hourly treatment.

This is **not** the same field as the requested monthly Service Credit.

For each affected clockhour:
- Clockhour:
- SLA-unavailable minutes:
- > 6 minutes?:
- Automatic no-charge visible in billing evidence?:
- Billing adjustment reference:

Until actual billing exports demonstrate how AWS represents this adjustment relative to the monthly bill used for Service Credit, do not add an independently reconstructed hourly amount on top of the claim estimate.

If interaction is material and cannot be reconciled, return `REVIEW_REQUIRED`.

## 9. Estimated Service Credit

Only after Sections 1–8 are resolved:

- Eligible spend exact amount: `S`
- Service Credit percentage: `P`
- Raw credit: `S * P / 100`
- Provider/billing rounding treatment:
- Estimated Service Credit:
- Credit > USD 1 minimum condition verified?:

The current SLA says a Service Credit is issued only when the applicable monthly credit amount is greater than USD 1.

Do not convert currencies silently. Record any provider/invoice conversion separately.

## 10. Claim deadline

Current SLA: AWS must receive the request by the **end of the second billing cycle after the incident occurred**.

Use actual customer billing-cycle boundaries.

- Incident billing cycle end:
- First subsequent billing cycle end:
- Second subsequent billing cycle end:
- Claim deadline:
- Current/audit date:
- Status: OPEN / EXPIRED / REVIEW_REQUIRED

Do not replace this with an assumed “60 days” rule.

## 11. Non-stacking check

AWS says a particular Single EC2 Instance may be claimed under either the Region-Level SLA or Instance-Level SLA; the claims cannot be combined/stacked for that instance.

- Region-Level claim also contemplated?:
- Instance-Level selected?:
- Non-stacking conflict resolved?:

## 12. Final decision

- Decision:
- Measured uptime:
- Credit tier:
- Eligible spend:
- Estimated Service Credit:
- Evidence status:
- Claim deadline:
- Applied exclusions:
- Unresolved questions:

## 13. Independent replay

Second reviewer/replay must calculate from the preserved inputs without copying the first arithmetic.

- Replay reviewer:
- Replay result:
- Matches first calculation exactly?:
- Difference:
- Resolution:

A discrepancy blocks the Claim Pack.
