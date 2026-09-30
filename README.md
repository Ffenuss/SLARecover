# SLARecover

SLARecover is a B2B SaaS project for deterministic SLA recovery: identify the applicable SLA version, preserve evidence, calculate availability and eligible spend reproducibly, prepare a Claim Pack, and track the outcome.

## Current status

- Current phase: **Phase 0 — Validation**
- Development spend target before commercial validation: **€0**
- Provider focus: **AWS**
- First vertical prototype candidate: **Amazon EC2 Instance-Level SLA**
- Auto-submit: **out of scope**
- Production deployment: **out of scope**
- AI verdicts for eligibility/credit: **prohibited**

The EC2 selection is a Phase 0 research decision, not an ACTIVE production rule. Activation requires an immutable official-source snapshot, effective dating, golden/boundary tests and review in the appropriate later phase.

## Source of truth

1. `docs/ROADMAP.md` — stage-gated delivery sequence.
2. `docs/DECISIONS.md` and `docs/ADR/` — architectural/business decisions.
3. `docs/research/` — dated primary-source research.
4. GitHub Issues/PRs — executable work tracking.
5. Versioned `rules/` and `fixtures/` — deterministic SLA artifacts.

The uploaded legacy documents use the working name **ClaimGuard**. The repository/product working name is **SLARecover**.

## Engineering principles

Correctness > Security > Evidence > Reliability > UX polish > coverage count.

Financial outputs must be deterministic and reproducible from versioned rules, immutable evidence and billing snapshots. No customer cloud access keys are to be stored; future AWS connectivity uses cross-account IAM roles, STS AssumeRole and ExternalId.

## License

No license has been selected. Repository visibility is currently public, but public visibility is not treated as a licensing decision.
