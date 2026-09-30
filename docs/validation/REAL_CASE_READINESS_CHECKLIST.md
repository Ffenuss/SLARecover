# Phase 0 Real-Case Readiness Checklist

Use before accepting a design-partner case into a concierge audit.

## Commercial / authorization

- [ ] Partner/customer understands this is a Phase 0 manual audit.
- [ ] No promise of eligibility or recovery has been made.
- [ ] No success/recovery fee is charged under the current conservative Germany/EU Phase 0 boundary.
- [ ] Customer retains submission authority.
- [ ] Evidence-processing purpose is agreed.
- [ ] Sensitive-data handling restrictions are known.

## Historical applicability

- [ ] Incident dates/times are known.
- [ ] Applicable official SLA version can be investigated.
- [ ] Product/resource type appears covered by that historical version.
- [ ] Jurisdiction/account-specific SLA ambiguity is absent or flagged REVIEW_REQUIRED.

## EC2 Instance-Level minimum evidence

- [ ] Region known.
- [ ] Availability Zone known.
- [ ] Instance identifier available privately.
- [ ] Request/application evidence covers the claimed outage.
- [ ] Evidence can support the “no external connectivity” condition.
- [ ] Billing evidence can isolate the affected instance/billing cycle.
- [ ] Relevant support/provider evidence is available if it exists.

CloudWatch/status evidence alone does not satisfy the request/application evidence requirement.

## Evidence operations

- [ ] Private workspace exists outside public Git.
- [ ] Case ID assigned.
- [ ] Raw originals admitted without modification.
- [ ] SHA-256 recorded for every admitted artifact.
- [ ] No live credentials/secrets remain in shared working copies.
- [ ] Redacted copies are distinct artifacts.
- [ ] Timezone/UTC normalization is documented.
- [ ] Retention/deletion instruction is recorded.

## Decision

- [ ] READY — proceed to deterministic audit.
- [ ] PARTIAL — request missing evidence before calculation.
- [ ] INSUFFICIENT — record the evidence gap and stop.
- [ ] REVIEW_REQUIRED — resolve historical/legal/semantic ambiguity first.

A case that fails readiness is still useful Phase 0 evidence: it quantifies the evidence-readiness problem.
