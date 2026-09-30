# Security Architecture

## Phase 0 constraints

- No customer secrets in Git.
- No stored AWS access keys.
- No production auto-submit.
- No broad/admin permissions for validation.
- Customer evidence must be minimized and redacted before use as project fixtures.

## Target AWS identity

Future AWS connectivity uses cross-account IAM Role + STS AssumeRole + ExternalId.

Monitoring and claim-submission authority are separate roles. Claim write permissions are never a prerequisite for monitoring.

## Required controls by later gates

MFA, RBAC, tenant isolation, TLS, encryption at rest, short-lived credentials, append-only audit events, secret/dependency scanning, rate limiting, backups/restore tests and kill switches.
