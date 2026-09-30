# RDS Phase 0 fixture plan

No customer fixtures are committed.

Planned synthetic/golden boundary cases for a later tested rule:
- Multi-AZ exactly 99.95%, immediately below, exactly/below 99.0%, exactly/below 95.0%;
- Single-DB exactly 99.5%, immediately below, exactly/below 99.0%, exactly/below 95.0%;
- one 1-minute interval where all connection requests fail;
- interval where at least one connection request succeeds -> not Unavailable under the SLA definition;
- DB resource running for only part of month -> non-running portion assumed 100% available;
- Micro/similarly constrained instance-class exclusion;
- operational-guideline exclusion;
- engine-crash exclusion;
- insufficient IO capacity exclusion;
- insufficient request-log evidence;
- non-stacking between Multi-AZ and Single-DB claims;
- claim deadline -1 day / exact / +1 day.

Current normative source: https://aws.amazon.com/rds/sla/
