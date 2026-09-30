# Phase 0 GO / PIVOT / NO-GO Decision Memo

Status: **template — no decision yet**.

Do not populate a final decision until `PHASE0_GATE_EVIDENCE.md` contains enough qualifying external evidence.

## 1. Decision

Choose exactly one:

- GO
- PIVOT
- NO-GO

Decision date:

Decision owner/reviewers:

Evidence cutoff date:

## 2. Executive evidence summary

Summarize facts only:

- interviews completed:
- design partners committed:
- real incidents audited:
- evidence-ready incidents:
- calculations independently replayed:
- Claim Packs completed:
- claims submitted by customers:
- claims accepted:
- claims rejected:
- credits actually granted:
- annual spend represented:
- Verified Credits Recovered / €1M ASUM:
- Recoverable Credits Detected / €1M ASUM:
- manual analyst hours per audit/claim:
- customer hours per audit/claim:
- qualified legal review status:
- differentiated-wedge evidence status:

Unknown values must remain unknown. Do not fill gaps with scenario assumptions.

## 3. Problem validation

Answer from interviews/real cases:

1. How often do material SLA-relevant incidents occur in the target ICP?
2. How often are SLAs actually reviewed today?
3. Why are claims missed/abandoned?
4. Which evidence is normally retained?
5. How often is evidence insufficient?
6. Who owns the workflow internally?
7. Does claim deadline management matter empirically?
8. Do customers act on a technically complete Claim Pack?

### Evidence

Link/redacted references:

### Conclusion

- validated;
- partially validated;
- falsified.

## 4. Recovery mechanism validation

For each real audited case record:

- provider/service/ruleset:
- applicable historical SLA established:
- evidence state:
- measured availability:
- eligible/not eligible/review required:
- eligible spend:
- estimated credit:
- deadline:
- independent replay result:
- customer review result:
- provider outcome if available:

### Mechanism conclusion

Can the recovery workflow produce a reproducible, actionable result from real customer data?

## 5. Economics

Use measured values first.

### Observed

- monitored annual spend:
- covered-service spend:
- recoverable credits detected:
- verified credits granted:
- delivery hours:
- direct delivery cost:
- customer effort:
- acceptance rate:
- evidence-ready rate:

### Derived

- Verified Credits Recovered / €1M ASUM:
- Recoverable Credits Detected / €1M ASUM:
- analyst hours / €1k detected:
- analyst hours / €1k verified:
- estimated contribution at candidate pricing:

### Scenario sensitivity

Scenario models may be included only after observed values and must be labelled as sensitivity, not forecast.

## 6. Differentiation validation

Test the current candidate wedge:

> Audit-grade SLA recovery for high-spend cloud/MSP environments where finance, security and legal teams need every credit decision to be reproducible.

For H1–H4 record:
- supporting interview/case evidence;
- contradicting evidence;
- result: supported / mixed / falsified.

Do not claim uniqueness from a limited competitor scan.

## 7. Security / access validation

Record real partner feedback:

- acceptable read-only access model:
- unacceptable permissions:
- evidence sharing constraints:
- required retention/redaction controls:
- MSP/downstream-tenant concerns:
- blockers discovered:

Update threat model references.

## 8. Legal/commercial validation

Record qualified review only:

- jurisdiction:
- reviewer/counsel:
- scope reviewed:
- technical audit model:
- customer-submission model:
- assisted submission:
- success/recovery fee:
- data protection roles:
- provider authorization:
- blocking issues:
- required mitigations:

Desktop research alone cannot mark this section clear.

## 9. Decision criteria

### GO

GO requires evidence that:
- real customers/partners have the problem;
- several partners commit real cases;
- at least one real recovery audit produces credible recoverable value;
- calculations are reproducible;
- evidence can be obtained at acceptable operational/security cost;
- measured economics support a plausible business;
- the starting commercial/legal model has no blocking issue after qualified review;
- the target segment values a defensible wedge.

GO authorizes **Phase 1 only**, not later-phase scope.

### PIVOT

Choose PIVOT when the underlying recovery opportunity appears real but one or more major assumptions must change, for example:
- EC2 evidence is systematically unavailable but another SLA/service has better evidence;
- direct customer acquisition is weak but MSP distribution is strong, or vice versa;
- claim recovery alone is too sparse but evidence-readiness/contract-obligation workflow has stronger value;
- success-fee economics/legal structure is weak but subscription/audit pricing is viable;
- auto-filing is unwanted while Claim Pack/human-review demand is strong.

A PIVOT memo must define:
- assumption being changed;
- evidence causing the change;
- new bounded hypothesis;
- new validation gate;
- what work is discarded versus retained.

It must not silently begin Phase 1.

### NO-GO

Choose NO-GO when evidence indicates no credible path to a profitable, lawful, operationally acceptable product, for example:
- target customers rarely have economically meaningful recoverable incidents;
- evidence is usually unavailable before claim deadlines and cannot feasibly be made ready;
- well-supported claims are not accepted often enough to create value;
- delivery cost exceeds credible willingness-to-pay/recovery value;
- customers will not provide required data or permissions;
- qualified legal review identifies a blocking model with no practical alternative;
- no buyer-relevant differentiation remains after validation.

## 10. Contradictory evidence

List evidence that argues against the preferred decision.

A decision memo that records only supporting evidence is incomplete.

## 11. Final rationale

State:
- decision;
- decisive evidence;
- largest remaining uncertainty;
- risks accepted;
- risks not accepted;
- next phase/task authorized.

## 12. Gate signature

- Phase 0 Exit Gate: PASSED / FAILED / PIVOTED
- Evidence register version:
- Git commit:
- Linked issues/PRs:
- Date:

Only write **PHASE 0 ЗАКРЫТА** after this section is completed with supporting evidence.
