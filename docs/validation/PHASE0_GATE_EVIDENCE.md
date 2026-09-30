# Phase 0 Gate Evidence Register

Status date: **2026-09-30**.

Purpose: make the Phase 0 exit decision evidence-based and prevent internal preparation from being mistaken for external validation.

## Status vocabulary

- **VERIFIED** — concrete evidence exists and the requirement is satisfied.
- **PARTIAL** — meaningful work exists, but the exit requirement itself is not yet satisfied.
- **BLOCKED** — cannot currently be completed because an external dependency/access/input is missing.
- **NOT_STARTED** — no qualifying evidence exists yet.

Internal documents, GitHub activity, competitor research and scenario models are useful preparation, but they do not count as customer validation unless the gate explicitly concerns those artifacts.

## Exit-gate register

| Phase 0 requirement | Status | Evidence now | What is still required |
|---|---|---|---|
| ICP / problem hypothesis documented | VERIFIED | `docs/PRODUCT.md`, validation scorecard, positioning hypotheses | Replace hypotheses with interview evidence over time |
| AWS SLA corpus v0 | VERIFIED for Phase 0 research scope | EC2/S3/RDS DRAFT rules, historical timelines, fixture plans; merged PRs #3, #14, #16 | ACTIVE production rules belong to later phases and require snapshots/tests/review |
| First vertical SLA selected | VERIFIED | ADR-0002 / EC2 Instance-Level; official comparison research | Revisit only if real-case evidence falsifies suitability |
| Design-partner interview process ready | VERIFIED | Interview guide, scorecard, outreach playbook, public target pipeline | Execute interviews |
| Several real design-partner commitments | BLOCKED | 0 commitments recorded; outreach tracker is NOT_CONTACTED | Several organizations must agree to provide/review a real or safely redacted case |
| 15–30 problem interviews | BLOCKED | 0 completed interviews recorded | Conduct and record organization-level/redacted results |
| Real customer incident/evidence set | BLOCKED | No real customer evidence admitted | At least one securely handled real AWS incident with provider-required evidence |
| Manual real-data recovery audit | BLOCKED | Manual EC2 workflow/template exists, but no real case executed | Run actual historical audit on real data |
| Independent replay of real calculation | BLOCKED | Replay procedure exists; no qualifying real calculation exists | Second calculation from preserved inputs must exactly reconcile |
| Manual Claim Pack from real data | BLOCKED | Template exists; no real-data Claim Pack exists | Produce and customer-review a Claim Pack from an actual case |
| Real provider claim/outcome | NOT_STARTED | No claim represented as submitted | Where feasible and approved, customer submits; track accepted/rejected/pending outcome |
| Verified Credits Recovered | NOT_STARTED | €0 verified; no confirmed granted credit | Confirm provider-granted service credit from real claim outcome |
| Threat model v0 | VERIFIED for Phase 0 artifact | `docs/THREAT_MODEL.md` | Update from real access/evidence findings before later gates |
| Legal issue register | VERIFIED as research artifact only | `docs/legal/PHASE0_QUESTIONS.md` | This does **not** satisfy legal clearance |
| Qualified legal review: no blocking prohibition for starting commercial model | BLOCKED | No qualified counsel opinion/review recorded | Jurisdiction-specific review of technical audit, claim assistance, submission, success fee, RDG/GDPR/provider terms |
| Unit-economics sensitivity model | VERIFIED as hypothesis model | `docs/validation/UNIT_ECONOMICS.md` | Scenario values are not measured economics |
| Measured recovery economics | BLOCKED | No real pilot observations | Replace assumptions with monitored spend, credits, hours, acceptance and delivery-cost data |
| Buyer-relevant differentiated wedge | PARTIAL | Competitive scan + H1–H4 positioning hypotheses | Interview/pilot evidence that target buyers value the wedge |
| GO / PIVOT / NO-GO decision | NOT_STARTED | Decision framework prepared separately | Decide only after gate evidence is sufficient |

## Current Phase 0 state

**BLOCKED ON EXTERNAL VALIDATION.**

This means:
- Phase 0 is active.
- Internal research/preparation may continue where it directly reduces Phase 0 uncertainty.
- Phase 1 production development is blocked.
- A CLI engine, AWS account connector, production database, dashboard or deployment must not be started merely because the internal artifacts are ready.

## Current external blockers

### 1. Outbound execution

A public-source outreach pipeline exists, but the repository records every target as `NOT_CONTACTED`.

No authorized outbound email connector is currently available in ChatGPT. Therefore no message is represented as sent.

### 2. Real partner/customer data

No design partner has supplied a real incident/evidence set yet. Consequently:
- no real eligibility finding exists;
- no real credit estimate exists;
- no real Claim Pack exists;
- no recovery economics are measured.

### 3. Qualified legal review

Desktop legal research has identified questions; it has not provided jurisdiction-specific legal clearance.

Until qualified review says otherwise, the conservative Phase 0 boundary remains:
- technical audit;
- factual calculation;
- Claim Pack;
- customer review;
- customer submission;
- no commercial recovery/success fee in a German/EU pilot;
- no auto-submit.

## Evidence rules

The following must **not** be used as substitutes for gate evidence:

- competitor existence -> does not prove SLARecover demand;
- competitor pricing -> does not prove SLARecover willingness-to-pay;
- a scenario recovery rate -> does not prove recovered-credit economics;
- a synthetic fixture -> does not prove a real claim is recoverable;
- AWS Health/CloudWatch alone -> does not prove SLA-defined outage when request evidence is required;
- an internal Claim Pack template -> does not prove provider claim acceptance;
- legal desktop research -> does not equal qualified legal clearance;
- an outreach draft -> does not equal sent outreach;
- a reply expressing interest -> does not equal design-partner commitment.

## Minimum evidence before a GO can be considered

A GO may be evaluated only after all of the following are true:

1. Several genuine design-partner commitments are documented.
2. A real-data manual audit finds recoverable or credibly recoverable value.
3. At least one suitable calculation has been independently replayed and reconciled.
4. Evidence sufficiency/claim requirements are demonstrated on a real case, or the exact evidence gap is empirically established.
5. Measured recovery economics exist; scenario tables are no longer the sole basis.
6. Qualified legal review finds no blocking prohibition for the intended starting commercial model.
7. The buyer-relevant differentiation hypothesis has real interview/pilot support.
8. An explicit GO/PIVOT/NO-GO memo is completed and linked to the evidence.

Until then, the correct Phase 0 status is not GO.
