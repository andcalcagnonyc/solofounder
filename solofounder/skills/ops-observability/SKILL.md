---
name: ops-observability
description: "This skill should be used when the user asks to \"set up monitoring\", \"set up alerts\", \"add logging\", \"trace my LLM calls\", \"build an ops dashboard\", \"define SLOs\", \"why is my app slow\", or needs visibility into system and AI behavior in production."
metadata:
  version: "0.1.0"
  area: ops
---

# Observability and Monitoring

See what the system and the AI are doing in production, and be alerted only when a customer is affected or is about to be.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Architecture, critical user journeys, service commitments

## Workflow

1. Define service-level indicators and objectives for the critical journeys: availability, latency, task success.
2. Instrument the application: structured logs, metrics, and traces with tenant and request identifiers and no sensitive data.
3. Instrument AI calls: prompt and model version, tokens, cost, latency, tool calls, outcome, and user feedback, with privacy controls on stored content.
4. Build dashboards: system health, AI quality and cost, business activity.
5. Configure alerts on objective burn and hard failures, routed to the founder's phone with a link to the runbook; remove alerts that never lead to action.
6. Add external uptime checks and a public status page.
7. Review weekly: incidents, slow paths, error classes, cost anomalies.

## Deliverables

- Objectives document
- Instrumentation and dashboards through ~~observability
- Alert rules with runbook links
- Weekly operations report

## Founder approval gates

- Storing prompt or response content
- Alert routing and quiet hours

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/ops/` with dated filenames.

## Hand-offs

- `ops-incident-response` for alerts that fire
- `eng-evals` for trace sampling
- `product-analytics-and-feedback` for usage data
