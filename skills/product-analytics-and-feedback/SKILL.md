---
name: product-analytics-and-feedback
description: "This skill should be used when the user asks to \"set up product analytics\", \"define my metrics\", \"what should I track\", \"analyze usage\", \"why are users churning\", \"summarize customer feedback\", or needs measurement and feedback synthesis."
metadata:
  version: "0.1.0"
  area: product
---

# Product Analytics and Feedback Loop

Measure whether the product does its job and feed what is learned from usage, support, and sales back into the roadmap every week.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Product events, AI traces, support tickets, sales notes, survey responses

## Workflow

1. Define the metric tree: north star, activation, engagement, retention, revenue, and AI quality (task success, human-override rate, cost and latency per task).
2. Write the tracking plan: events, properties, identities, and privacy treatment.
3. Implement tracking through ~~analytics and verify data quality.
4. Build the core views: activation funnel, retention cohorts, feature usage, quality and cost by task type.
5. Collect feedback into one place from support, sales calls, interviews, and in-product ratings; tag by theme and customer value.
6. Each week, summarize what changed, the top themes with evidence, and recommended roadmap actions.
7. Design experiments with a hypothesis, metric, sample, and decision rule.

## Deliverables

- Metric tree and tracking plan
- Dashboard specifications
- Weekly insights summary
- Experiment designs

## Founder approval gates

- Collection of any personal data in analytics
- Roadmap changes proposed from the analysis

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/product/` with dated filenames.

## Hand-offs

- `product-strategy-and-roadmap` for prioritization
- `ops-observability` for trace data
- `support-customer-success` for churn signals
