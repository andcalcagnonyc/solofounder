---
name: ops-cost-and-finops
description: "This skill should be used when the user asks to \"reduce my cloud bill\", \"why is my API bill so high\", \"track token costs\", \"what is my cost per task\", \"set a budget alert\", \"optimize inference cost\", or needs cloud and model spend measured and controlled."
metadata:
  version: "0.1.0"
  area: ops
---

# Cloud and AI Cost Management

Keep the cost of running the product visible per customer and per task, and lower it without lowering quality.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Cloud and model-provider billing, usage traces, pricing and margin targets

## Workflow

1. Tag and attribute spend by environment, service, customer, and task type.
2. Compute cost per successful task and gross margin per customer; rank the outliers.
3. Set budgets and alerts per provider and hard limits per tenant.
4. Reduce model cost in order of safety: remove waste (retries, oversized context), cache, batch non-urgent work, route simple steps to smaller models, then renegotiate or commit.
5. Verify each change against the evaluation suite before and after.
6. Right-size infrastructure, remove idle resources, and use commitments only for stable baseline load.
7. Forecast spend against growth and feed the financial model.
8. Report monthly: spend, unit cost trend, savings made, next actions.

## Deliverables

- Cost attribution report
- Unit-cost dashboard specification
- Optimization plan with measured results

## Founder approval gates

- Committed-spend contracts
- Changes that trade quality for cost
- Deleting resources

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/ops/` with dated filenames.

## Hand-offs

- `finance-planning-and-runway` for margin and forecast
- `product-pricing-and-packaging` when unit cost shifts
