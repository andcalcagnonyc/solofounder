---
name: stack-and-automation-setup
description: "This skill should be used when the user asks to \"choose my tools\", \"set up my stack\", \"connect my tools to Claude\", \"automate my company\", \"schedule recurring tasks\", \"what should run automatically\", \"set up my agents\", or needs the company's tool stack selected, connected, and put on a schedule."
metadata:
  version: "0.1.0"
  area: core
---

# Tool Stack and Automation Setup

Select the smallest tool stack that covers every function, connect it to Claude, and schedule the recurring work so the company operates between founder sessions.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Company profile, budget, tools already in use
- Connectors available in the founder's Claude environment

## Workflow

1. List the tool categories in `CONNECTORS.md` and record what the founder already uses for each.
2. Recommend one tool per uncovered category, preferring tools with a Claude connector or an API, a free or low entry tier, and availability in the HQ country.
3. Check which connectors are installed and working; guide connection of the missing ones; note categories that will run on file export and manual steps.
4. Write the chosen stack to the company profile.
5. Define the automation schedule: daily (lead response, support triage, outbound replies), weekly (bookkeeping, pipeline review, CRM hygiene, founder review, content), monthly (close, investor update, compliance sweep, cost review), quarterly (health checks, pricing and policy reviews).
6. For each scheduled run, define the trigger, the skill, the inputs, what it may do unattended, and what it must queue for approval.
7. Create the scheduled tasks where the environment supports it; otherwise produce a calendar of manual triggers.
8. Review automation monthly: runs completed, approvals pending, failures, time saved.

## Deliverables

- Tool stack decision table
- Connector status list
- Automation schedule with authority limits

## Founder approval gates

- Any paid tool subscription
- Granting a connector access to email, bank, or production systems
- What each scheduled run may do without approval

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/core/` with dated filenames.

## Hand-offs

- `founder-weekly-review` consumes the scheduled outputs
- Every area skill uses the stack recorded in the profile
