# Phase 0 Legal / Commercial Question Register

Research date: **2026-09-30**.

This is a technical/product legal-issues register based on official sources. It is **not a qualified legal opinion** and does not close the Phase 0 legal gate.

## Starting-jurisdiction status

No launch jurisdiction is yet approved. Because an EU/Germany launch is plausible, Germany/EU is used as an early risk screen. US and other jurisdictions require separate review.

## Germany — legal-service / collection boundary

Official German RDG sources raise a material question for any commercial workflow that evaluates and pursues another company's contractual claim.

### Facts from the statute

- RDG §2(1) defines a legal service as an activity in a concrete third-party matter when it requires a legal assessment of the individual case.
- RDG §2(2) treats collection of another person's claim, when operated as an independent business, as an Inkassodienstleistung.
- RDG §3 generally prohibits independent out-of-court legal services unless an authorization/exception applies.
- RDG §5 permits some legal services as ancillary services to another activity, depending on content, scope, factual connection and required legal knowledge.
- RDG §10 provides a registration route for, among other things, collection services based on special expertise.
- RDG §13c regulates remuneration agreements for collection services, including requirements for success-fee agreements.

Official sources:
- https://www.gesetze-im-internet.de/rdg/__2.html
- https://www.gesetze-im-internet.de/rdg/__3.html
- https://www.gesetze-im-internet.de/rdg/__5.html
- https://www.gesetze-im-internet.de/rdg/__10.html
- https://www.gesetze-im-internet.de/rdg/__13c.html

### Questions for qualified German counsel

1. Does deterministic SLA eligibility analysis for a customer's concrete AWS incident constitute a Rechtsdienstleistung under RDG §2(1), or can a purely technical calculation/Claim Pack remain outside that definition?
2. At what point does submitting or negotiating a service-credit claim on a customer's behalf become Inkassodienstleistung under §2(2)?
3. Can a “technical audit + customer reviews/submits” model fall within an allowed ancillary-service structure under §5, and under what limits?
4. Would accepting a percentage of recovered service credits alter the characterization or require RDG registration?
5. If Inkasso registration is required, what entity, expertise, insurance/process and disclosure requirements apply?
6. Does it matter that AWS service credits are account credits against future charges rather than ordinary cash damages?
7. What wording should Terms/authorization use to avoid representing SLARecover as providing legal advice before it is authorized to do so?
8. Can SLARecover communicate factual provider-rule outputs and draft support-case text while the customer retains the legal decision and submission?
9. What liability allocation is enforceable for missed deadlines, incorrect calculations and incomplete evidence?
10. What changes if the client is an MSP acting for downstream customers?

## GDPR / EU data protection

Likely Phase 0/production evidence can contain identifiers in logs, support correspondence and billing records. The data-role analysis therefore cannot be postponed until enterprise launch.

Official sources indicate:
- GDPR Article 5 includes data minimisation.
- EDPB guidance says controller/processor roles are functional and that a controller-processor relationship must be governed by a contract documenting processing responsibilities.
- EDPB security guidance states controllers and processors must implement technical and organisational measures appropriate to risk.
- GDPR Chapter V governs transfers of personal data outside the EEA.

Sources:
- https://eur-lex.europa.eu/eli/reg/2016/679
- https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en
- https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en
- https://www.edpb.europa.eu/sme/be-compliant/secure-personal-data_en

Questions:
1. For customer billing/log/evidence data, is SLARecover a processor, independent controller, or different role per processing purpose?
2. Which data in request logs is actually necessary for provider validation, and what must be redacted/minimised before ingestion?
3. What retention period is justified by claim deadlines, audit/replay needs and dispute windows?
4. Which subprocessors/transfers would be required under the eventual hosting architecture?
5. Is a DPIA required for any proposed telemetry/log collection pattern?
6. What breach-notification and customer-assistance commitments belong in the DPA/security addendum?

## AWS provider terms / authorization

Current official AWS documentation confirms:
- Support API access requires Business Support+, Enterprise Support or Unified Operations, with legacy-plan fallbacks for customers/regions not yet transitioned.
- AWS Health API has the same qualifying-plan gate.
- `CreateCase` can create support cases programmatically where the account is eligible.

Sources:
- https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html
- https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html
- https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html

Open questions:
1. What customer authorization is sufficient for SLARecover to prepare versus submit a Support case?
2. What IAM actions are minimally necessary for read-only monitoring and, separately, submission?
3. Are there AWS Customer Agreement / Support terms restricting third-party submission, automated case creation or attachment handling?
4. Can an MSP/partner submit for linked customers under its existing authority, or is per-account authorization required?
5. How should accounts without qualifying Support API/Health API plans be handled without reducing evidence standards?

## Current safe Phase 0 operating boundary

Until qualified legal review says otherwise:
- perform technical research and manual calculation;
- create a factual Claim Pack;
- do not hold customer funds;
- do not purchase/receive assignment of claims;
- do not promise legal representation;
- keep auto-submit disabled;
- have the customer review and submit any real provider claim itself;
- do not charge a recovery/success fee in a German/EU commercial pilot without counsel confirming the model.

This boundary is conservative product-risk management, not a statement that the broader model is unlawful.
