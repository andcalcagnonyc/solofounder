---
name: finance-planning-and-runway
description: "This skill should be used when the user asks to \"build a financial model\", \"how much runway do I have\", \"what is my burn\", \"create a budget\", \"calculate unit economics\", \"what is my gross margin on AI costs\", \"write an investor update\", or needs planning, forecasting, and metrics."
metadata:
  version: "0.1.0"
  area: finance
---

# Financial Model, Budget, and Runway

Give the founder a current view of cash, runway, and unit economics, with a model that reflects how AI companies actually earn and spend: usage-driven revenue and inference-driven cost of revenue.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Jurisdiction protocol

- Take the governing jurisdictions from the profile: country (and state or province) of incorporation, founder tax residence, and every country where customers, employees, or contractors sit.
- Research the current rules for those jurisdictions from primary sources (company registry, tax authority, regulator) before drafting. Cite each source with its date in the output.
- Where jurisdictions differ, state which one governs and why.
- Label every output as a draft for review by a locally licensed accountant or tax adviser, and list the specific questions to put to them. Never present output as tax or accounting advice.
- Never file, sign, pay, or submit anything on the founder's behalf without explicit approval of that specific action.

## Inputs

- Actuals from the ledger, pipeline from the CRM, pricing and packaging
- Token, model, and cloud cost per unit of product usage
- Hiring and spend plans

## Workflow

1. Build a driver-based model: leads to customers through funnel conversion, price and usage per customer, churn and expansion.
2. Model cost of revenue per unit of work: tokens per task, model mix, caching and batch discounts, retries, human-in-the-loop time, cloud, and support.
3. Compute unit economics: gross margin per customer and per task, acquisition cost, payback, lifetime value, and sensitivity to model price changes.
4. Build the 13-week cash forecast and the 24-month plan with base, downside, and upside cases.
5. State runway in months and the date cash reaches the founder's minimum buffer. List the three levers with the largest effect.
6. Set the budget and compare actuals monthly, explaining variances.
7. Produce the monthly investor or board update: metrics, cash, wins, problems, asks.

## Deliverables

- Financial model workbook with assumptions tab
- 13-week cash forecast
- Unit-economics summary
- Monthly budget-versus-actual and investor update

## Founder approval gates

- Core assumptions (pricing, conversion, churn, cost per task)
- Anything sent to investors or the board

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `product-pricing-and-packaging` for price changes
- `ops-cost-and-finops` for cost-per-task data
- `legal-fundraising` when runway triggers a raise
