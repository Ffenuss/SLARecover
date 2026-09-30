# Historical SLA Rule Selection Procedure

Use this procedure before any Phase 0 historical concierge calculation.

## Inputs

- provider;
- service;
- incident start/end UTC;
- account/contract jurisdiction if relevant;
- region;
- resource/deployment type;
- preserved provider SLA sources.

## Procedure

### 1. Pin the incident

Record exact incident timestamps in UTC. If the incident spans a provider SLA version boundary, split the analysis or return `REVIEW_REQUIRED` until the applicable treatment is established.

### 2. Retrieve official current + historical sources

Use the provider's official SLA and historical-version pages first.

For AWS Phase 0:
- EC2: https://aws.amazon.com/compute/sla/ and /historical/
- S3: https://aws.amazon.com/s3/sla/ and /historical/
- RDS: https://aws.amazon.com/rds/sla/ and /historical/

### 3. Distinguish observed page date from effective date

Store separately:
- `source_last_updated`: date printed by provider;
- `effective_from`: only when supported by an authoritative basis;
- `effective_until`: only when supported by an authoritative basis.

Do **not** set `effective_from = source_last_updated` by convention.

If the incident falls near a version boundary and no authoritative effective date is available, return `REVIEW_REQUIRED`.

### 4. Select the commitment family

Selection must use the source version's own covered-resource definitions.

Examples:
- EC2 current/May-2022 style: monthly Region-Level vs monthly Instance-Level;
- EC2 2019/2020: monthly broader service commitment plus a separate Single EC2 hourly 90% no-charge mechanism;
- EC2 2018: Region-Unavailability model; isolated instance failures were excluded;
- RDS current: Multi-AZ versus Single-DB;
- RDS 2019: Multi-AZ only;
- S3 current: current storage-class families including Express One Zone;
- S3 May 2022: no current Express One Zone/AZ-specific treatment.

### 5. Pin claim procedure and billing basis from that version

Never combine:
- a current formula with a historical claim subject;
- a historical threshold with current billing scope;
- a current exclusion list with an older version;
- a current storage/deployment class with a historical version where it was not covered.

### 6. Preserve provenance

For the selected source record:
- URL;
- provider page title;
- observed Last Updated date;
- retrieval date;
- snapshot identifier;
- SHA-256 when snapshot storage exists;
- reviewer;
- applicability rationale.

### 7. Fail closed

Return `REVIEW_REQUIRED` when:
- the applicable version cannot be established;
- the case crosses an unresolved version boundary;
- the product/resource was not clearly covered in that version;
- jurisdiction/account-specific historical terms are ambiguous;
- an exact financial rule would require importing a later version's semantics.

## Phase 0 rule

A real historical case is preferable to a synthetic “perfect” case, but uncertainty is not permission to guess. A correct `REVIEW_REQUIRED` result is valid validation evidence.

## Source snapshot provenance

A provider page's visible `Last Updated` label is not enough to establish legal applicability.

When an official source snapshot has been captured in the private workspace, create provenance metadata locally:

```bash
python scripts/source_snapshot_manifest.py create /private/source/compute-sla.html \
  --service ec2 \
  --source-url https://aws.amazon.com/compute/sla/ \
  --source-last-updated 2022-05-25 \
  --retrieved-at-utc 2026-09-30T12:00:00Z \
  --pretty
```

The generated manifest:
- hashes the local bytes with SHA-256;
- emits only the basename, not the full private path;
- records the official URL and provider-observed date;
- sets `applicability_status=UNPROVEN`;
- leaves `effective_from/effective_until` null.

A reviewer must separately establish historical applicability before those dates can be populated in a reviewed record. Real source bytes and completed provenance records stay in the controlled private workspace unless their publication rights are separately established.
