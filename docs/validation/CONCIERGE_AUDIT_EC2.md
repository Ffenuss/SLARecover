# Concierge Audit — AWS EC2 Instance-Level

Use this checklist for a **real historical case** during Phase 0. It is not an automated production claim decision.

## 1. Case intake

Record privately, not in public Git:
- customer/account;
- EC2 instance ID;
- AWS Region and Availability Zone;
- incident start/end timestamps in UTC;
- relevant billing cycle;
- request/application logs covering the incident;
- CloudWatch/status-check evidence if available;
- billing detail for the affected instance;
- AWS Support correspondence/event references if available.

## 2. SLA version check

Before calculating:
- establish the incident date;
- open the official current/historical Amazon Compute SLA;
- identify the SLA version effective for that incident;
- preserve a snapshot/hash in the controlled evidence workspace;
- record effective dates and source URL.

If the historical effective version cannot be established, classify the case as **REVIEW_REQUIRED**.

## 3. Evidence sufficiency

For the EC2 Instance-Level SLA, verify at minimum:
- incident dates/times are known;
- Region and AZ are known;
- affected EC2 instance resource ID is known;
- request/application logs or equivalent validation data support the claimed absence of external connectivity;
- billing data identifies charges for the affected instance and billing cycle.

CloudWatch EC2 status checks may corroborate the incident, but they are not a substitute for evidence of the SLA-defined condition.

If request/application evidence is missing or cannot support the SLA definition, stop with **INSUFFICIENT_EVIDENCE**.

## 4. Exclusion screen

Check whether the incident may be attributable to:
- factors outside AWS reasonable control;
- customer action/inaction;
- customer equipment, software or other technology;
- suspension/termination under the AWS agreement;
- any exclusion in the historical SLA version actually applicable to the incident.

Ambiguous exclusions -> **REVIEW_REQUIRED**.

## 5. Deterministic calculation worksheet

Record:
- total minutes in the applicable monthly billing cycle:
- SLA-unavailable minutes:
- measured uptime percentage:
- threshold/tier:
- eligible instance spend:
- excluded one-time/upfront amounts:
- estimated credit:
- currency:
- rounding rule used:

Never use binary floating point for the final money calculation. For Phase 0 manual work, preserve the exact arithmetic steps.

## 6. Claim deadline

Determine the end of the second billing cycle after the incident using the customer's actual billing-cycle boundaries. Record:
- incident billing cycle:
- first subsequent billing cycle end:
- second subsequent billing cycle end / claim deadline:
- audit date:
- deadline status: open / expired / ambiguous.

## 7. Manual Claim Pack fields

Include:
- provider/service;
- customer/account (private copy only);
- affected instance, Region and AZ;
- incident timeline;
- applicable SLA source/version;
- formula and arithmetic;
- exclusion analysis;
- evidence inventory and hashes;
- eligible spend;
- estimated credit;
- claim deadline;
- provider-required subject/fields;
- evidence gaps.

## 8. Independent replay

For suitable real cases, perform the calculation a second time from the preserved inputs without copying the first result. Any discrepancy blocks the case until reconciled.

## 9. Outcome capture

After customer review/submission, record:
- claim submitted: yes/no;
- accepted/rejected/pending;
- credit requested;
- credit actually granted;
- reason for rejection if known;
- manual hours spent;
- lessons for rules/evidence/product;
- verified recovered credit.

Only **credit actually granted/confirmed** contributes to the North Star: Verified Credits Recovered.
