---
name: support-customer-success
description: "This skill should be used when the user asks to \"onboard this customer\", \"create an onboarding plan\", \"which customers are at risk\", \"reduce churn\", \"prepare a business review\", \"plan this renewal\", \"find expansion opportunities\", \"collect NPS\", or needs customers made successful and retained."
metadata:
  version: "0.1.0"
  area: support
---

# Customer Onboarding, Success, and Retention

Get each customer to the outcome they bought, keep them, and grow the account, using health signals and automation in place of a success team.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Closed-won hand-over brief, usage and quality data, support history, contract dates

## Workflow

1. Define the onboarding path per segment: milestones to first value, owner of each step, target days.
2. Run onboarding: kickoff, setup and integration, first successful task, training, hand-over to steady state; automate reminders and checks.
3. Define the health score: usage, task success, breadth of adoption, support load, sentiment, payment behavior, champion status.
4. Review health weekly; act on declines with a specific play.
5. Run lifecycle communications: tips, new capabilities, results achieved.
6. Prepare business reviews that show outcomes in the customer's terms.
7. Manage renewals from 90 days out; identify expansion from usage and unmet needs.
8. Collect satisfaction and reference willingness; ask satisfied customers for reviews, referrals, and case studies.
9. On churn, interview and record the cause.

## Deliverables

- Onboarding plans and trackers
- Health score definition and weekly risk list
- Business-review decks
- Renewal and expansion plan
- Churn analysis

## Founder approval gates

- Customer communications until a standing rule is approved
- Commercial offers for renewals or saves

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/support/` with dated filenames.

## Hand-offs

- `sales-proposal-and-close` for expansion deals
- `finance-invoicing-and-collections` for renewals
- `marketing-communications` for case studies
