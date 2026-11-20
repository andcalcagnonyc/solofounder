---
name: sales-pipeline-review-and-forecast
description: "This skill should be used when the user asks to \"review my pipeline\", \"forecast revenue\", \"which deals should I focus on\", \"why am I losing deals\", \"run a win/loss analysis\", \"what are my conversion rates\", or needs pipeline inspection and forecasting."
metadata:
  version: "0.1.0"
  area: sales
---

# Pipeline Review and Forecast

Tell the founder each week which deals to work, what will close, where the funnel leaks, and what to change.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- CRM pipeline, activity history, targets

## Workflow

1. Pull open pipeline by stage with amount, age, last activity, and next step.
2. Flag risk: no next step, past close date, stalled beyond stage limit, single-threaded, missing decision process.
3. Rank the week's priorities: the specific action for each of the top deals.
4. Forecast: commit, best case, and pipeline, using stage conversion history once enough data exists and judgment labels until then.
5. Compute funnel metrics: conversion by stage, cycle length, win rate, average value, pipeline coverage against target, by source and segment.
6. Run win and loss analysis monthly; extract patterns into playbook and product feedback.
7. Send the weekly sales summary to the founder review.

## Deliverables

- Weekly pipeline review with priority actions
- Forecast
- Funnel metrics dashboard specification or report
- Monthly win/loss analysis

## Founder approval gates

- Forecast figures shared with investors or the board
- Closing out stale deals in bulk

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/sales/` with dated filenames.

## Hand-offs

- `finance-planning-and-runway` for revenue forecast inputs
- `marketing-demand-generation` when coverage is short
- `founder-weekly-review` for the operating summary
