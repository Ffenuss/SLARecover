# Design Partner Interview Guide

This is a problem interview, not a product pitch. Ask for concrete recent examples and existing behavior before describing SLARecover.

## Interview metadata

- Interview ID:
- Date:
- Segment: MSP / FinOps / high-spend cloud company / SaaS / other
- Role/function:
- Approximate cloud spend band:
- AWS usage: yes/no
- Manages multiple AWS accounts/customers: yes/no
- AWS support plan known: yes/no/unknown

Do not record personal or customer-identifying data in this public repository.

## Problem discovery

1. Tell me about the last significant AWS outage or degradation you had to investigate.
2. How did you determine which services/resources were affected?
3. What evidence did you have after the incident: request logs, application monitoring, synthetic checks, CloudWatch, support correspondence, billing data?
4. Did anyone check the contractual SLA? Who?
5. How was the applicable SLA version/date determined?
6. Was a service-credit claim considered or submitted? What happened?
7. If no claim was submitted, why not?
8. How often do incidents worth investigating occur?
9. Who owns this process today: SRE, FinOps, procurement, finance, MSP, nobody?
10. How much manual time is spent collecting evidence and reconstructing billing impact?
11. Have you ever discovered an eligible-looking incident after the claim deadline?
12. What makes a claim too small or too painful to pursue?
13. Which evidence is routinely retained for at least 60–90 days?
14. Could a read-only external tool be granted access to billing/monitoring metadata? Under what security conditions?
15. Would you allow a manual historical SLA Recovery Audit using a redacted real incident?
16. If value is found, would you be willing to validate the calculation independently and, where appropriate, submit a claim yourself?
17. What would make you refuse such a pilot?

## Do not lead

Avoid questions such as “Would automation save you money?” or “Would you pay 20% of recovered credits?” until the current workflow/problem has been established.

## Evidence captured after interview

- Problem occurred in last 12 months: yes/no
- Existing SLA review process: systematic/ad hoc/none
- Missed/abandoned claim suspected: yes/no/unknown
- Evidence maturity: high/medium/low
- Willing to provide a real redacted case: yes/no/maybe
- Willing to become design partner: yes/no/maybe
- Main blocker:
- Next factual follow-up:
