# Security Policy

Do not open public issues containing customer credentials, account identifiers, raw billing exports, private logs, personal data or unredacted evidence.

Current Phase 0 rules:
- no secrets in Git;
- no customer AWS access keys;
- evidence must be redacted/minimized before use as a fixture;
- production claim submission is not implemented.

A private vulnerability-reporting channel will be configured before external production use.

## Public-repository CI hygiene

Phase 0 CI scans Git-tracked project text for conservative high-confidence patterns:
- plausible AWS access key IDs;
- assigned AWS secret access keys/session tokens;
- private-key blocks;
- secret-bearing file extensions;
- customer/billing/support evidence-like filenames with high-risk data extensions.

Safe documentation should use obvious placeholders such as `<placeholder>` and must never contain a realistic credential-shaped value.

This scanner is defense in depth, not a substitute for credential rotation, GitHub secret scanning, private evidence handling, or customer-approved storage controls.
