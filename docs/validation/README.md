# Phase 0 Validation Kit

Purpose: collect real market and recovery evidence without building the SaaS before the Phase 0 gate is passed.

## Required outputs

1. 15–30 problem interviews across the priority ICP.
2. Several design-partner commitments; target 5–10, with at least one strong MSP/FinOps path if available.
3. Real historical incident candidates suitable for a manual EC2 Instance-Level SLA audit.
4. At least two calculations repeated independently when suitable real cases exist.
5. Evidence-completeness and recovery-economics observations.
6. Inputs for the GO / PIVOT / NO-GO memo.

## Data handling

This repository is public. Do **not** commit:
- customer names unless explicitly cleared for publication;
- AWS account IDs or resource IDs;
- invoices/CUR exports;
- raw request/application logs;
- credentials, role ARNs tied to a customer, tokens or support-case data;
- personal data.

Record only redacted/aggregated validation observations here. Keep raw partner evidence outside Git until a private, access-controlled evidence workflow exists.

## Workflow

Problem interview -> score ICP fit -> ask for design-partner commitment -> screen incident/evidence -> run manual concierge audit -> calculate twice -> build manual Claim Pack -> record outcome/economics -> update Phase 0 decision evidence.
