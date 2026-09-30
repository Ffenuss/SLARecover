# Phase 0 Manual Evidence Intake Protocol

Status: Phase 0 manual operating procedure.

Purpose: handle the first real customer/design-partner evidence set safely enough for a concierge audit **without** implementing the future Phase 2 evidence engine.

This procedure is intentionally conservative. It does not define the final production retention, DPA, storage, encryption or access-control architecture.

## 1. Scope boundary

This protocol may be used only for:
- a small number of Phase 0 design-partner audits;
- customer-provided historical evidence;
- manual EC2/S3/RDS research/audit work;
- generating factual calculation artifacts and Claim Packs.

It must not be used as a substitute for production evidence storage.

## 2. Absolute prohibitions

Never commit any of the following to the public GitHub repository:
- AWS account IDs tied to a customer;
- EC2/RDS/S3 resource identifiers tied to a customer;
- invoices, CUR exports or billing exports;
- raw request/application logs;
- AWS Support correspondence;
- IAM role ARNs/customer authorization artifacts;
- credentials, access keys, tokens, cookies or secrets;
- unredacted personal data;
- confidential customer documents;
- signed commercial/legal documents.

Git is for templates, redacted aggregate findings and non-sensitive rule/test artifacts only.

## 3. Evidence classes

Every received artifact must be classified as one of:

### RAW_ORIGINAL

Customer-supplied file or export exactly as received.

Rules:
- do not edit;
- do not rename in a way that loses the original filename;
- compute SHA-256 immediately;
- record receipt/provenance;
- preserve original bytes.

### REDACTED_COPY

A copy derived from RAW_ORIGINAL with sensitive fields removed/masked.

Rules:
- new filename;
- new SHA-256;
- explicit parent RAW_ORIGINAL reference;
- list redaction categories;
- never replace the raw original.

### NORMALIZED_DERIVATIVE

A parsed/normalized/structured representation used for calculation.

Examples:
- normalized incident timeline;
- extracted billing rows;
- minute-level availability table.

Rules:
- reference source artifact(s);
- document transformation method;
- compute SHA-256;
- do not present as provider/customer raw evidence.

### CALCULATION_OUTPUT

Derived deterministic outputs:
- uptime calculation;
- eligible spend;
- credit tier;
- deadline calculation;
- Claim Pack.

Rules:
- reference exact input artifact hashes;
- record rule/source version;
- record reviewer and calculation version.

## 4. Evidence workspace

Use a private, access-controlled local/customer-approved workspace outside the public repository.

Recommended logical structure:

```text
case-<redacted-id>/
  00-intake/
  10-raw/
  20-redacted/
  30-normalized/
  40-calculations/
  50-claim-pack/
  manifest/
```

The directory name must not contain a customer legal name, AWS account ID or resource ID if the machine/workspace is not dedicated and access-controlled.

## 5. Case identifier

Create a non-identifying case ID, for example:

`P0-2026-0001`

Mapping from case ID to the actual organization/customer belongs in the private workspace and must not be committed to Git.

## 6. Receipt checklist

Before accepting evidence, record:

- Case ID:
- Design partner/customer:
- Evidence sender/authorized contact:
- Date/time received UTC:
- Transfer method:
- Purpose stated:
- Customer authorized SLA audit:
- Customer authorized processing of supplied logs/billing data:
- Any explicit restrictions:
- Requested retention/deletion date, if any:
- Jurisdiction/data-location concern identified:
- Sensitive categories expected:
- Reviewer receiving evidence:

If authorization/scope is unclear, stop with `REVIEW_REQUIRED` before further processing.

## 7. SHA-256 admission

For each file admitted:

1. preserve the original bytes;
2. calculate SHA-256;
3. record original filename;
4. record size in bytes;
5. record receipt timestamp UTC;
6. record evidence category;
7. record source/provenance;
8. record storage location using a private logical reference, not a public path.

Example commands where available:

Linux:
```bash
sha256sum evidence-file
```

macOS:
```bash
shasum -a 256 evidence-file
```

PowerShell:
```powershell
Get-FileHash evidence-file -Algorithm SHA256
```

Do not rely on filename alone as evidence identity.

## 8. Raw immutability rule

Once a RAW_ORIGINAL hash is recorded:
- never overwrite that file;
- never edit it in place;
- never use an editor that silently rewrites metadata/encoding;
- create a new derivative for every transformation.

If the customer re-sends a corrected/exported file, admit it as a new evidence artifact with a new ID/hash.

## 9. Time handling

For each evidence source record:
- original timezone if known;
- original timestamp string;
- normalized UTC timestamp;
- normalization rule;
- DST/ambiguous-local-time handling if relevant.

Do not silently reinterpret timestamps.

If timezone cannot be established and this changes SLA minute classification, return `REVIEW_REQUIRED`.

## 10. Minimal data principle

Before making a REDACTED_COPY:
- remove fields not required for SLA validation/calculation;
- preserve only identifiers necessary to correlate the case;
- replace customer/resource identifiers with stable case-local aliases when possible;
- remove credentials/secrets even if they appear accidentally in logs;
- avoid retaining application payload/body content when status/time/request metadata is sufficient.

Redaction must not destroy evidence required to validate the SLA condition.

## 11. Secret detection

Every received file must be manually screened before sharing beyond the smallest authorized team.

Potential secret patterns include:
- AWS access key IDs;
- secret access keys;
- session tokens;
- Authorization headers;
- cookies;
- signed URLs;
- private keys;
- database credentials;
- API tokens.

If a live credential is discovered:
1. stop distribution;
2. notify the customer contact;
3. request rotation/revocation as appropriate;
4. do not commit/share the credential;
5. document only that a secret-handling incident occurred, without preserving the secret in project docs.

## 12. Evidence manifest

Use `PHASE0_EVIDENCE_MANIFEST_TEMPLATE.md`.

Every calculation/Claim Pack must be traceable to the exact evidence IDs/hashes it used.

## 13. Evidence sufficiency decision

After intake, classify:

### READY

Provider-required identifiers, relevant time range, billing basis and request/application evidence are sufficient to attempt deterministic reconstruction.

### PARTIAL

Material evidence exists but one or more required items must still be recovered.

### INSUFFICIENT

The provider-defined SLA condition cannot be established with available evidence.

Do not convert PARTIAL/INSUFFICIENT into ELIGIBLE through inference.

## 14. Handoff to audit

Only READY evidence enters the deterministic audit.

For EC2:
- follow `HISTORICAL_RULE_SELECTION.md`;
- follow `EC2_MANUAL_CALCULATION.md`;
- create `CLAIM_PACK_EC2_TEMPLATE.md` output;
- perform independent replay.

## 15. Derived artifact provenance

Every normalized/calculation artifact must record:
- source evidence IDs;
- source SHA-256 hashes;
- transformation description;
- tool/manual method used;
- operator/reviewer;
- creation timestamp UTC;
- output SHA-256.

A derived artifact without traceable inputs cannot support a final Claim Pack.

## 16. Customer-visible evidence list

The customer-facing Claim Pack should list evidence references/hashes, not expose internal storage paths.

Where raw evidence contains sensitive information:
- provide hash/reference;
- provide redacted copy where sufficient;
- submit original evidence to provider only when the customer authorizes it and provider requirements justify it.

## 17. Retention and deletion

Final Phase 0 retention policy is **not yet legally approved**.

Until qualified review establishes a production policy:
- retain only what is necessary for the agreed audit/review;
- honor explicit customer deletion/return instructions where legally/technically permissible;
- do not create indefinite archives by default;
- record deletion date/action in the private manifest;
- keep only non-sensitive aggregate learning in the public project.

Any need to retain evidence beyond the agreed audit/claim window requires explicit review.

## 18. Backups and copies

During Phase 0:
- minimize the number of evidence copies;
- know where every copy exists;
- do not sync raw evidence into personal/public cloud drives by default;
- do not send raw evidence through unapproved chat/email channels;
- if backup is necessary, use an access-controlled encrypted location approved for the case.

Production backup/restore controls belong to later phases.

## 19. Incident response

If evidence is accidentally exposed:
- stop further sharing;
- identify affected artifacts;
- preserve incident facts without further copying sensitive data;
- notify the authorized customer contact;
- assess credential rotation and data-protection obligations;
- record remediation;
- do not hide the incident.

## 20. Phase 0 completion condition

This protocol is considered operationally validated only after:
- at least one real evidence set is processed;
- manifest/hash references reconcile;
- the audit can be replayed from preserved inputs;
- no sensitive data enters the public repository;
- customer handling constraints are captured;
- lessons are incorporated into the Phase 2 evidence-engine requirements.

Until then this is a prepared procedure, not proven evidence operations.
