# Phase 0 Evidence Manifest Template

Store the completed manifest in the private case workspace. Do **not** commit a completed customer manifest to the public repository.

## Case

- Case ID:
- Provider:
- Service:
- Incident reference:
- Customer reference (private):
- Intake opened UTC:
- Intake owner:
- Customer authorization reference:
- Retention/deletion instruction:

## Artifact register

| Evidence ID | Class | Original filename / logical name | Source | Received UTC | Size bytes | SHA-256 | Parent evidence ID | Timezone | Redaction/transformation | Private storage ref | Status |
|---|---|---|---|---|---:|---|---|---|---|---|---|
| E-001 | RAW_ORIGINAL | | | | | | — | | none | | ADMITTED |

Allowed classes:
- RAW_ORIGINAL
- REDACTED_COPY
- NORMALIZED_DERIVATIVE
- CALCULATION_OUTPUT

Allowed statuses:
- RECEIVED
- ADMITTED
- QUARANTINED
- SUPERSEDED
- DELETED
- RETURNED

## Evidence sufficiency

- Incident timestamp/window supported:
- Region/AZ/resource identifiers supported:
- Request/application evidence supported:
- Provider evidence supported:
- Billing evidence supported:
- Historical SLA version established:
- Exclusion evidence available:
- Final evidence readiness: READY / PARTIAL / INSUFFICIENT / REVIEW_REQUIRED
- Missing items:

## Derivation record

For every derived file:

- Output Evidence ID:
- Parent Evidence IDs:
- Transformation:
- Operator:
- Tool/version or manual method:
- Created UTC:
- Output SHA-256:
- Reproducibility notes:

## Calculation input lock

Before the first authoritative manual calculation:

- Evidence IDs locked for calculation:
- Ruleset/source version:
- Source URL:
- Source snapshot/hash:
- Billing period:
- Calculation workbook/template version:
- Lock timestamp UTC:
- Reviewer:

If inputs change, create a new calculation version. Do not overwrite the prior result.

## Independent replay

- Replay input evidence IDs:
- Replay ruleset/version:
- Replay operator:
- Replay timestamp UTC:
- First result hash:
- Replay result hash:
- Results reconcile exactly: YES / NO
- Difference/resolution:

## Claim Pack

- Claim Pack Evidence ID:
- Claim Pack SHA-256:
- Customer review date:
- Customer approval status:
- Provider submission authorized: YES / NO
- Submitted by:
- Submission date:
- Provider case reference:

## Outcome

- Status: NOT_SUBMITTED / PENDING / ACCEPTED / REJECTED
- Credit requested:
- Credit granted:
- Currency:
- Provider outcome evidence ID:
- Verified Credits Recovered:
- Outcome date:

## Deletion / return log

| Evidence ID | Action | UTC timestamp | Performed by | Reason/authorization |
|---|---|---|---|---|
| | | | | |

## Manifest integrity

- Manifest version:
- Manifest SHA-256:
- Last updated UTC:
- Reviewer:
