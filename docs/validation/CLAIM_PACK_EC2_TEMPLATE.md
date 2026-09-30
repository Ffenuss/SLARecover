# Manual Claim Pack Template — AWS EC2 Instance-Level

Status: Phase 0 manual template.

This is a factual technical package for customer review. It is not legal representation and SLARecover does not submit it during Phase 0.

## 1. Executive summary

- Provider: AWS
- Service: Amazon EC2
- SLA type: Instance-Level
- Customer/account reference:
- Region / AZ:
- Affected instance:
- Incident billing cycle:
- Applicable SLA version:
- Required availability:
- Measured availability:
- Decision: ELIGIBLE / NOT_ELIGIBLE / INSUFFICIENT_EVIDENCE / REVIEW_REQUIRED
- Credit tier:
- Eligible spend:
- Estimated Service Credit:
- Evidence status:
- Claim deadline:

## 2. Official SLA provenance

- Current/historical source URL:
- Applicable version/date:
- Why this version applies to the incident:
- Preserved source snapshot:
- SHA-256:
- Ruleset/workbook version:

Do not cite the current SLA for a historical incident unless it was actually the applicable version.

## 3. Incident timeline

| UTC timestamp/window | Observation | Evidence ref/hash | Classification |
|---|---|---|---|
| | | | |

State separately:
- customer-observed impact;
- provider evidence;
- independent monitoring;
- inferred/derived facts.

Do not present an inference as raw evidence.

## 4. Affected resource

- AWS account reference:
- Region:
- AZ:
- EC2 instance ID:
- Instance lifecycle/configuration facts relevant to incident:
- Related resource IDs if necessary:

## 5. Evidence list

| Evidence ID | Category | Original source | Timestamp | SHA-256 | Redaction status | Coverage |
|---|---|---|---|---|---|---|
| | Provider evidence | | | | | |
| | Customer telemetry | | | | | |
| | Independent monitoring | | | | | |
| | Financial evidence | | | | | |

Raw evidence is immutable once admitted to the controlled evidence workspace.

## 6. SLA-condition analysis

Current Instance-Level definition to test: whether the Single EC2 Instance had no external connectivity.

For each claimed interval:
- evidence supporting the condition;
- contradictory evidence;
- excluded minutes;
- unresolved gaps.

Conclusion must be evidence-derived, not based solely on AWS Health/status signals.

## 7. Exclusions analysis

Document every current/historical exclusion checked and the evidence for the conclusion.

- Outside AWS reasonable control:
- Internet/access beyond AWS demarcation:
- Customer action/inaction:
- Resource-health/recovery response:
- Customer equipment/software/technology:
- Suspension/termination:
- Historical-version-specific exclusions:
- Result:

Unresolved material exclusion -> REVIEW_REQUIRED.

## 8. Availability calculation

Attach the completed `EC2_MANUAL_CALCULATION.md`.

Record the final exact values:
- total billing-cycle minutes:
- SLA-unavailable minutes:
- exact uptime fraction:
- displayed uptime percentage:
- tier boundary applied:
- credit percentage:

## 9. Billing calculation

- Billing evidence reference/hash:
- Affected-instance monthly bill:
- Excluded upfront/one-time amount:
- Existing automatic hourly no-charge adjustments:
- Eligible spend:
- Credit percentage:
- Estimated Service Credit:
- Currency:
- Rounding/conversion rule:

The automatic >6-minute clockhour no-charge provision must not be blindly added again if already reflected in the monthly bill.

## 10. Deadline

- Incident billing cycle:
- First subsequent billing cycle:
- Second subsequent billing cycle:
- Provider receipt deadline:
- Deadline state:

## 11. Provider-required request fields

For the current Instance-Level SLA verify:

- Subject exactly contains: `Amazon Compute SLA Credit Request – Instance-Level Claim`
- Incident dates/times:
- Affected AWS Region:
- Affected AZ:
- Affected Single EC2 Instance resource ID(s):
- Request logs:
- Other data necessary for AWS validation:
- Sensitive/confidential data redacted as AWS directs:

Missing provider-required information blocks a ready-to-submit status.

## 12. Draft factual claim narrative

Keep this section factual and derived from the pack:

- what resource was affected;
- when;
- what the request/application evidence shows;
- which SLA version/formula is applied;
- resulting uptime calculation;
- claimed Service Credit tier;
- billing basis;
- evidence attachments/references.

Do not add legal conclusions or unsupported causal claims.

## 13. Customer review

- Technical reviewer:
- Finance/FinOps reviewer:
- Customer-authorized submitter:
- Calculation independently replayed:
- Evidence complete:
- Deadline open:
- Customer approves submission: YES / NO / PENDING

Phase 0 submission, if any, is performed by the customer.

## 14. Outcome

Populate only after a real outcome exists.

- Submitted date:
- AWS case reference:
- AWS response:
- Accepted / rejected / pending:
- Credit requested:
- Credit actually granted:
- Grant/credit evidence:
- Rejection reason:
- Manual SLARecover hours:
- Customer hours:
- Lessons:
- Verified Credits Recovered:

Only a confirmed granted credit counts as Verified Credits Recovered.
