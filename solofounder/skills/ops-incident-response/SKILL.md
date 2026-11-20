---
name: ops-incident-response
description: "This skill should be used when the user asks \"production is down\", \"we have an incident\", \"help me debug this outage\", \"write a postmortem\", \"create a runbook\", \"customers are reporting errors\", \"the agent did something wrong\", or needs an incident managed from detection to review."
metadata:
  version: "0.1.0"
  area: ops
---

# Incident Response

Restore service fast, tell customers the truth, and learn from each incident, including incidents where the AI acted wrongly.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Alert or report, dashboards, logs, recent changes

## Workflow

1. Declare the incident, set severity, and start a timeline.
2. Stabilize first: roll back the last change, disable the affected feature or agent action, or fail over. Diagnose after impact stops.
3. For AI incidents, stop the behavior with the kill switch or by reducing autonomy, then identify affected customers and actions taken.
4. Investigate with evidence: what changed, what the metrics and traces show, which hypothesis each fact supports.
5. Communicate at set intervals: status page, affected customers, and internal log. Draft each message for approval.
6. Verify recovery against the service indicators and close the incident.
7. Assess notification duties (customers, regulators, insurers) with the legal skills when data or regulated activity is involved.
8. Write a blameless review: timeline, impact, root causes, what worked, and corrective actions with owners and dates.
9. Update runbooks, alerts, tests, and evaluations from the review.

## Deliverables

- Incident timeline and status updates
- Post-incident review
- Runbook and test updates

## Founder approval gates

- Customer and public communications
- Destructive remediation steps
- Regulatory notifications

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/ops/` with dated filenames.

## Hand-offs

- `marketing-communications` for public statements
- `legal-privacy-and-ai-compliance` for breach assessment
- `support-ticket-triage-and-response` for affected customers
