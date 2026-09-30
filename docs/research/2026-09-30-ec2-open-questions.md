# EC2 Instance-Level Rule — Open Questions

Research date: **2026-09-30**.

Official source rechecked:
https://aws.amazon.com/compute/sla/

These questions block promotion of the draft rule to ACTIVE unless resolved through authoritative provider documentation, reproducible billing evidence, or an explicit reviewed rule interpretation.

## OQ-1 — Partial minute normalization

The SLA defines uptime as the percentage of minutes during the month in which a Single EC2 Instance was Unavailable, but the reviewed page does not specify in the definition how a partial-minute outage is rounded/counts.

Decision: preserve exact timestamps. Do not invent a normalization rule. Boundary/partial-minute cases remain REVIEW_REQUIRED until resolved.

## OQ-2 — Instance lifecycle within the monthly denominator

The wording uses “minutes during the month” while customer-triggered downtime can fall under exclusions. A newly launched, terminated or intentionally stopped instance can create denominator/exclusion questions.

Decision: capture lifecycle evidence and do not assume that every calendar minute is a chargeable/covered minute when lifecycle facts make the result material. Resolve before ACTIVE implementation.

## OQ-3 — Automatic hourly no-charge interaction

The current SLA says AWS will not charge for a Single EC2 Instance that is Unavailable for more than six minutes of a clockhour, automatically and without a credit request.

The SLA separately defines the requested Service Credit as a percentage of the monthly bill for the affected instance.

Open question: how is the automatic hourly treatment represented in actual billing data, and therefore what amount forms the correct monthly-bill basis without double counting?

Decision: inspect real billing artifacts in the first suitable pilot. Until then, keep the mechanisms separate and return REVIEW_REQUIRED if the distinction changes the estimate.

## OQ-4 — Currency / USD minimum

The SLA defines a Service Credit as a dollar credit and states that the credit for the applicable monthly billing cycle must be greater than USD 1. Customers may receive invoices in other currencies.

Decision: do not invent an FX conversion rule. Record invoice currency, AWS credit representation and any actual provider conversion from real cases before automating the USD-minimum check for non-USD billing.

## OQ-5 — “Other data necessary for AWS to validate”

The claim procedure explicitly allows AWS to require request logs and other data necessary to validate the claimed outage.

Decision: rule eligibility and evidence readiness must remain separate. A mathematically eligible case may still be INSUFFICIENT_EVIDENCE for submission.

## OQ-6 — Historical source effective dating

The current page is marked “Last Updated: May 25, 2022,” and AWS exposes prior versions. Before treating that page date as a formal effective-from boundary, historical pages/source snapshots should be mapped into an explicit version timeline.

Decision: `effective_from` remains unresolved in the DRAFT rule; no ACTIVE status until the version timeline is evidenced.
