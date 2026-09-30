# SLARecover Roadmap

Source: Master Phase Roadmap v1.0 and Release Gates, dated 2026-09-30.

## Normative phase order

0. Validation
1. Product/Architecture Foundation
2. AWS Connectivity & Evidence
3. SLA Engine & Claim Pack MVP
4. Closed Pilot
5. Submission Workflow + Legal/Compliance
6. Commercial Launch + MSP Platform
7. GCP + Azure
8. SaaS Providers
9. Auto-submit
10. Enterprise Readiness
11. Contract Obligation Recovery
12. Scale & Platform

The older pre-project master document contains a superseded phase numbering. When it conflicts with Master Phase Roadmap v1.0, the v1.0 roadmap and phase-specific documents govern.

## Current phase: Phase 0 — Validation

Goal: prove real recoverable value exists, customers will provide acceptable access/evidence, and the starting legal/commercial model is viable.

### Entry status

- ICP/business hypothesis: documented.
- Access to several potential design partners: **not yet evidenced; outreach pipeline prepared but not executed**.
- GitHub repository: available.
- AWS SLA corpus v0: researched/structured as non-active DRAFT rules for EC2, S3 and RDS.
- Current gate status: **BLOCKED ON EXTERNAL VALIDATION**; see `docs/validation/PHASE0_GATE_EVIDENCE.md`.

### Required Phase 0 artifacts

- ICP/persona brief.
- Interview notes + problem-frequency matrix.
- Design partner commitments.
- AWS SLA corpus v0.
- Manual Claim Packs from real data.
- Legal memo/questions register.
- Threat model v0.
- Unit economics model.
- GO/PIVOT/NO-GO memo.

### Exit gate

Phase 0 closes only when several real design-partner commitments exist, a manual audit on real data finds recoverable or credibly recoverable value, legal review finds no blocking prohibition, and an explicit GO/PIVOT/NO-GO decision is recorded.

Until then, Phase 1 production development does not start.

The formal gate evidence register is `docs/validation/PHASE0_GATE_EVIDENCE.md`. The decision artifact template is `docs/validation/GO_PIVOT_NO_GO_TEMPLATE.md`.
