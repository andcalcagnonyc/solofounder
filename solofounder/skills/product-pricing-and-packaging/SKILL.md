---
name: product-pricing-and-packaging
description: "This skill should be used when the user asks to \"price my product\", \"design my pricing tiers\", \"should I charge per seat or per usage\", \"price per outcome\", \"create a pricing page\", \"run a pricing test\", or needs pricing and packaging for an AI product."
metadata:
  version: "0.1.0"
  area: product
---

# Pricing and Packaging

Set a price and package that customers understand, that tracks the value delivered, and that keeps gross margin healthy when cost depends on model usage.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Value delivered per customer, competitor and alternative prices, cost per task, willingness-to-pay evidence

## Workflow

1. Identify the value metric: seat, usage, task completed, or outcome achieved. Prefer the unit the customer already budgets for.
2. Compute cost floor per unit from cost-per-task data and the target gross margin.
3. Research reference prices: competitors, the labor or software being replaced.
4. Design packages: who each is for, limits, included usage, overage, and the upgrade trigger.
5. Decide free tier, trial, or paid pilot based on cost to serve and sales motion.
6. Set discount rules, annual terms, and enterprise add-ons (security, support levels, deployment options).
7. Protect margin: usage caps, fair-use terms, model routing, and price-change clauses.
8. Test with real buyers and revisit quarterly or when model costs shift.

## Deliverables

- Pricing strategy memo with margin analysis
- Package and price table
- Discount and exception rules
- Pricing test plan

## Founder approval gates

- Published prices and package limits
- Any change for existing customers

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/product/` with dated filenames.

## Hand-offs

- `marketing-website` for the pricing page
- `finance-planning-and-runway` for the model
- `legal-commercial-contracts` for terms
