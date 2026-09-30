# S3 Phase 0 fixture plan

No customer fixtures are committed.

Planned synthetic/golden boundary cases for a later tested rule:
- standard-family uptime exactly 99.9%, immediately below 99.9%, exactly/below 99.0%, exactly/below 95.0%;
- IA-family uptime exactly 99.0%, immediately below 99.0%, exactly/below 98.0%, exactly/below 95.0%;
- 5-minute interval with zero requests -> 0% Error Rate;
- InternalError / ServiceUnavailable numerator handling;
- excluded errors removed from numerator;
- multiple request types/storage classes -> REVIEW_REQUIRED until aggregation semantics are resolved;
- Region vs S3 Express One Zone AZ billing basis;
- insufficient request denominator/log evidence;
- claim deadline -1 day / exact / +1 day.

Current normative source: https://aws.amazon.com/s3/sla/
