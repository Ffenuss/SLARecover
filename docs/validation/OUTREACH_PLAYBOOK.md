# Phase 0 Design-Partner Outreach Playbook

## Objective

Obtain real evidence for or against the SLARecover thesis, not sales meetings.

The offer is a **free Historical SLA Recovery Audit** for one or two AWS EC2 incidents. During Phase 0:
- no platform installation is required;
- no AWS access keys are accepted;
- no claim is submitted by SLARecover;
- no success fee is charged;
- the partner/customer reviews the calculation and submits any live claim themselves;
- sensitive evidence stays outside the public repository.

## Primary ask

Ask for a 20–30 minute problem interview with the person responsible for AWS operations, FinOps, managed services or cloud commercial management.

Only after confirming the problem/evidence pattern, ask for one real/redacted incident for the audit.

## First-contact email — English

Subject: AWS SLA credits — free evidence-based audit for one real incident

Hello,

I’m validating SLARecover, a deterministic SLA recovery workflow for AWS teams and MSPs.

The question we are testing is narrow: when an AWS incident may qualify for a service credit, can the applicable SLA version, customer evidence, billing basis, deadline and credit calculation be reconstructed reliably enough for finance/operations to act on it?

We are looking for a small number of design partners for a free manual audit of one or two EC2 incidents. There is no software deployment, no AWS access-key request, no auto-submission and no recovery fee in this validation phase.

The useful outcome can be either:
- a reproducible Claim Pack / potential credit; or
- a clear finding that the evidence is insufficient, together with exactly what was missing.

Would someone responsible for AWS operations or FinOps be open to a 20–30 minute problem interview?

Best regards,
SLARecover

## First-contact email — German

Subject: AWS-SLA-Gutschriften — kostenloser evidenzbasierter Audit eines realen Incidents

Guten Tag,

ich validiere derzeit SLARecover, einen deterministischen Workflow zur Prüfung und Aufbereitung von AWS-SLA-Gutschriften für Cloud-Teams und MSPs.

Wir testen eine konkrete Frage: Lässt sich nach einem AWS-Incident die damals gültige SLA-Version zusammen mit Kundenevidenz, Abrechnungsbasis, Frist und Credit-Berechnung so reproduzierbar rekonstruieren, dass Operations/FinOps damit belastbar weiterarbeiten können?

Dafür suchen wir wenige Design Partner für einen kostenlosen manuellen Audit von ein bis zwei EC2-Incidents. In dieser Validierungsphase gibt es keine Software-Installation, keine Anfrage nach AWS Access Keys, kein Auto-Submit und keine Recovery Fee.

Ein valides Ergebnis kann auch sein, dass die vorhandene Evidenz nicht ausreicht — dann dokumentieren wir exakt, welche Nachweise fehlen.

Wäre jemand aus AWS Operations, Managed Services oder FinOps für ein 20–30-minütiges Problem-Interview offen?

Viele Grüße
SLARecover

## Follow-up after 4–7 business days

Keep the follow-up factual and short:

- remind them that this is a research/design-partner audit;
- emphasize that an “insufficient evidence” result is still useful;
- offer a redacted/synthetic walkthrough if customer evidence cannot initially be shared;
- do not create urgency or imply money has definitely been left unclaimed.

## Interview-to-audit conversion

Before requesting evidence, confirm:
- they operate/manage meaningful AWS workloads or multiple customer accounts;
- they have had at least one material AWS incident;
- someone can identify affected resources and billing period;
- request/application telemetry may exist;
- they are willing to review a deterministic calculation.

If these are absent, record the reason and do not force an audit.

## Evidence request

For EC2 Instance-Level cases request the minimum set:
- incident timestamp/window in UTC;
- Region and Availability Zone;
- affected instance ID, redacted if necessary for initial screening;
- request/application logs or equivalent evidence of external-connectivity failure;
- supporting CloudWatch/status data if available;
- affected-instance billing detail for the billing cycle;
- support/event references if available.

Do not ask for credentials.

## Success criteria for outreach

Track separately:
- contacted;
- replied;
- problem interview completed;
- real incident available;
- evidence READY/PARTIAL/INSUFFICIENT;
- audit completed;
- calculation independently replayed;
- Claim Pack reviewed;
- live claim submitted by customer;
- outcome confirmed.

The Phase 0 target is several genuine commitments, not a vanity response rate.
