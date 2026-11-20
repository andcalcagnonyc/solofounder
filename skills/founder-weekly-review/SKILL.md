---
name: founder-weekly-review
description: "This skill should be used when the user asks to \"run my weekly review\", \"what should I focus on this week\", \"give me a company status\", \"how is the business doing\", \"prepare my Monday brief\", \"what is slipping\", or needs one cross-functional view of the company and the week's priorities."
metadata:
  version: "0.1.0"
  area: core
---

# Founder Weekly Operating Review

Give the founder one page each week covering every function, the decisions only the founder can make, and the three priorities that matter, so the company runs on a cadence without meetings.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Outputs of the area skills: cash and runway, pipeline, product metrics, operations, support, compliance calendar
- Last week's priorities and decision log

## Workflow

1. Collect the numbers from each area: cash and runway, revenue and pipeline, activation and retention, AI quality and cost per task, uptime and incidents, support volume and satisfaction, deadlines in the next 30 days.
2. Compare with last week and with plan; mark each area green, amber, or red with one sentence of cause.
3. Review last week's priorities: done, moved, dropped, and why.
4. List decisions waiting on the founder with a recommendation for each.
5. List approvals queued by other skills (payments, filings, sends, deployments).
6. Propose the week's three priorities, chosen by effect on the current company milestone, and what will be deliberately ignored.
7. Schedule the work: which skills run when, and which are delegated to scheduled tasks.
8. Write the summary and update the decision log.

## Deliverables

- Weekly one-page review
- Decision and approval queue
- Week plan

## Founder approval gates

- The three priorities
- Each queued approval, individually

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/core/` with dated filenames.

## Hand-offs

- Any area skill for the work chosen
- `stack-and-automation-setup` to schedule recurring runs
