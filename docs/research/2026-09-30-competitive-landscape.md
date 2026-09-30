# Competitive Landscape — SLA / Service Credit Recovery

Research date: **2026-09-30**.

This document records public product/marketing claims. Customer counts, recovery rates, approval rates and savings claims are **not independently verified** unless explicitly stated otherwise.

## Finding

SLA/service-credit recovery is already an identifiable software category in 2026. SLARecover must therefore validate a differentiated reason to exist; “providers do not pay credits automatically” is not itself a differentiated product thesis.

## Direct / adjacent products observed

| Product | Public positioning | Submission model | Public pricing observed | Notes relevant to SLARecover |
|---|---|---|---|---|
| Complaya | SLA credit recovery across SaaS/cloud; contract analysis, monitoring, auto-file | Claims may be submitted/notified on customer behalf depending on configuration | Platform fee + 20% Core / 18% Advanced / 15% Enterprise recovery success fee | Strong automation/AI positioning. Terms page observed as limiting eligibility to US and excluding EU/UK and other jurisdictions; re-check before relying on this commercially. |
| Next Signal | Purpose-built automated SLA refund recovery for AWS/Azure/GCP and other providers | Team review or configurable auto-approval workflow | Annual platform license + success fee; percentage not public on pricing page | Cloud-specific recovery is the core value proposition, not an incidental FinOps feature. CloudSLACredit is its free educational/calculator property. |
| Ontracko | Vendor accountability/SLA monitoring, breach detection and claim kits across many SaaS/cloud vendors | Generates claim kits; customer filing model is prominently described | Free + 8% of recovered credits; optional $99/month Capacity; partner rev-share | Explicit MSP/consultancy partner/white-label strategy means MSP positioning alone is not differentiation. |
| Fintropy (Nuvika) | Multi-cloud FinOps plus automated SLA breach recovery | Publicly claims automated filing and tracking | Core approx. $128/mo; SLA add-on ₹8,000/mo; Growth approx. $372/mo; 15% recovered-credit share | Deterministic-rule language and hybrid subscription/success-fee model overlap SLARecover's working thesis. |
| AllCaps | Contract/invoice recovery platform; AWS SLA evidence audit plus broader contract-rights recovery | AWS tool emphasizes read/quantify only; broader SLA product says monitor/calculate/claim | Free AWS finding; broader Vendor Invoice Audit advertised at $15k fixed fee | Especially close to an evidence-first historical audit thesis; supports EC2 single-instance and request-log evidence framing. |

## Sources

- https://complaya.ai/
- https://complaya.ai/prices
- https://complaya.ai/terms-of-service
- https://nextsignal.io/pricing
- https://nextsignal.io/resources/next-signal-platform-faqs
- https://www.cloudslacredit.com/about
- https://www.ontracko.com/pricing
- https://www.nuvikatech.com/Fintropy_Overview.html
- https://www.nuvikatech.com/pricing.html
- https://studio.allcaps.ai/products/aws-sla-recovery
- https://www.allcaps.ai/sla-credit-recovery

## What is not differentiated by itself

The following are already publicly claimed by one or more competitors:
- breach detection;
- SLA rule calculation;
- evidence-pack/claim-kit generation;
- deadline tracking;
- AWS/Azure/GCP coverage;
- success-fee pricing;
- hybrid platform + success fee;
- automated filing;
- read-only cloud access;
- deterministic-rule language;
- MSP/partner/white-label positioning;
- historical/evidence audit.

## Differentiation hypotheses to test, not assume

### H1 — Audit-grade reproducibility is valuable

Hypothesis: regulated/enterprise/MSP buyers will value immutable evidence hashes, historical SLA-version selection, exact rule provenance, deterministic replay and four-eyes rule activation enough to prefer SLARecover over faster AI-first automation.

Test: during interviews, show the output contract and ask which evidence/calculation artifacts are required for internal finance/legal approval. Do not describe competitors first.

Falsifier: buyers consistently treat provider claim acceptance as sufficient and do not care about reproducibility/audit trail.

### H2 — Evidence readiness is a separate product problem

Hypothesis: a meaningful share of lost credits is caused by missing/expired customer-side evidence, and an “evidence readiness + capture” workflow creates value before an outage occurs.

Test: measure what telemetry/logs prospects actually retain and for how long; record how many historical cases are impossible to prove.

Falsifier: most target accounts already retain sufficient SLA-grade evidence and missing evidence is rare.

### H3 — High-assurance assisted submission can beat auto-file for EU/enterprise buyers

Hypothesis: customers with stricter legal/security governance prefer Detect -> Calculate -> Claim Pack -> Human Review over immediate auto-submit.

Test: ask security/legal/FinOps stakeholders which permissions and approvals are acceptable for a pilot.

Falsifier: target buyers strongly prefer end-to-end auto-file and see human approval as unacceptable friction.

### H4 — A specific narrow ICP can outperform generic vendor breadth

Hypothesis: one high-spend/MSP segment with repeatable AWS evidence patterns yields better economics than a broad “144+ vendors” catalog.

Test: compare recoverable value, evidence completeness and sales friction by segment.

Falsifier: recovery is too sparse within the narrow ICP and economic value requires broad multi-vendor coverage immediately.

## Phase 0 consequence

Competition validates category existence but raises the evidence bar for GO. Phase 0 must now prove both:
1. real recoverable value; and
2. a buyer-relevant differentiated wedge that is not already commodity functionality.
