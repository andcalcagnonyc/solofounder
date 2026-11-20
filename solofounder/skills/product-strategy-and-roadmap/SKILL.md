---
name: product-strategy-and-roadmap
description: "This skill should be used when the user asks to \"define my product strategy\", \"scope my MVP\", \"build a roadmap\", \"prioritize features\", \"plan the next sprint\", \"what should I build first\", or needs product planning."
metadata:
  version: "0.1.0"
  area: product
---

# Product Strategy and Roadmap

Decide what to build, in what order, and what to leave out, so the first version ships inside the sprint and each later release moves one metric.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Discovery evidence, positioning, technical constraints, time and budget

## Workflow

1. Write the strategy on one page: target customer, job to be done, wedge use case, why now, differentiation, and what the product will not do.
2. Choose the autonomy level for launch: assistant that drafts, copilot that acts with approval, or agent that acts within limits. Tie the choice to error cost and customer trust.
3. Define the MVP as the smallest workflow that delivers the outcome end to end for one customer type.
4. Set the north-star metric and input metrics, including task success rate and cost per successful task.
5. Build the roadmap as now, next, later, with the problem each item solves and the evidence for it.
6. Prioritize with a stated method (value, confidence, effort) and record what was cut and why.
7. Plan each week: goal, committed items, acceptance criteria, risks.
8. Review monthly against metrics and customer feedback; revise.

## Deliverables

- One-page strategy
- MVP scope with exclusions
- Roadmap
- Weekly plan

## Founder approval gates

- MVP scope and launch autonomy level
- Roadmap changes that affect customer commitments

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/product/` with dated filenames.

## Hand-offs

- `product-requirements-and-specs` for each roadmap item
- `eng-architecture` for feasibility
