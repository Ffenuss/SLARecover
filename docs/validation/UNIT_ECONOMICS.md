# Phase 0 Unit Economics

Status: hypothesis model. Replace assumptions with pilot observations as soon as real data exists.

## North-star denominator

Use **Recovered Credits per €1M Annual Spend Under Monitoring (ASUM)**.

Do not infer this number from competitor marketing claims.

## Recovery scenarios per €1M monitored spend

| Recovery rate | Credits recovered |
|---:|---:|
| 0.25% | €2,500 |
| 0.50% | €5,000 |
| 1.00% | €10,000 |
| 3.00% | €30,000 |

The 3% case is an optimistic sensitivity scenario, not a forecast.

## Success-fee-only revenue sensitivity

Revenue below is shown only to expose the economics. It is not a pricing decision.

| Recovered / €1M | 5% fee | 8% fee | 10% fee | 15% fee | 20% fee |
|---:|---:|---:|---:|---:|---:|
| €2,500 | €125 | €200 | €250 | €375 | €500 |
| €5,000 | €250 | €400 | €500 | €750 | €1,000 |
| €10,000 | €500 | €800 | €1,000 | €1,500 | €2,000 |
| €30,000 | €1,500 | €2,400 | €3,000 | €4,500 | €6,000 |

## Interpretation

A success-fee-only model can be structurally weak at low recovery rates, even with €1M of monitored spend. This supports the existing hypothesis of:
- a subscription/platform component for monitoring, evidence readiness, deadline control and audit;
- plus an optional recovery fee only after legal validation.

Competitor public pricing as of the research date confirms that hybrid and success-fee models already exist:
- Ontracko: free base with 8% of recovered credits; optional $99/month Capacity.
- Fintropy: subscription plus 15% recovery share.
- Complaya: platform fee plus public 15–20% success-fee tiers.
- Next Signal: annual platform license plus an undisclosed success fee.

These competitor prices are market observations, not evidence that SLARecover can charge the same.

## Pilot fields required to replace assumptions

For every design partner:
- annual monitored cloud/vendor spend;
- covered-service spend;
- incident count;
- cases with sufficient evidence;
- recoverable credits detected;
- claims created;
- claims accepted/rejected;
- credits actually granted;
- manual analyst hours;
- customer engineering/FinOps hours;
- elapsed days to claim;
- support burden;
- any direct delivery cost.

## Metrics

- Verified Credits Recovered / €1M ASUM.
- Recoverable Credits Detected / €1M ASUM.
- Claims / €1M ASUM.
- Claim acceptance rate.
- Evidence-ready incident rate.
- Manual hours / claim.
- Revenue / €1M ASUM.
- Gross contribution / €1M ASUM once actual delivery costs exist.

## Economic falsification signals

PIVOT/NO-GO should be considered if real pilots repeatedly show:
- recovered value is too small to pay for support/analysis at target pricing;
- evidence-ready incidents are too rare;
- claim acceptance is too low after high-quality evidence preparation;
- the viable customer must have such high spend that addressable sales volume becomes impractically small;
- MSP/FinOps partners cannot aggregate enough spend to improve the model.

No Phase 0 GO should be based on the 0.25/0.5/1/3% scenario table alone.
