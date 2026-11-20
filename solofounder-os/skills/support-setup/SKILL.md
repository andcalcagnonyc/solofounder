---
name: support-setup
description: "This skill should be used when the user asks to \"set up customer support\", \"choose a helpdesk\", \"define my support SLAs\", \"create a support process\", \"set up a support inbox\", \"write support macros\", or needs the support function designed."
metadata:
  version: "0.1.0"
  area: support
---

# Support Operations Setup

Design a support operation one founder can sustain: clear channels, published commitments, automation for the routine, and a fast path to the founder for what matters.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Customer segments and plans, product complexity, time zones, tools in the profile

## Workflow

1. Choose channels by segment: in-product chat, email, shared channel for enterprise, community forum; avoid channels that cannot be staffed.
2. Set service commitments per plan: hours, first-response and resolution targets, severity definitions.
3. Configure ~~helpdesk: inbox, forms that collect the needed details, tags, priorities, routing, and customer context from the CRM and product.
4. Define the ticket lifecycle and escalation path, including engineering bugs and security or privacy reports.
5. Write saved replies for the common cases in the brand voice.
6. Define support metrics: volume by category, response and resolution times, deflection rate, satisfaction, and contact rate per active customer.
7. Publish the support policy and how to reach support.

## Deliverables

- Support policy and service commitments
- Helpdesk configuration specification
- Saved replies
- Metrics definition

## Founder approval gates

- Published service commitments
- Helpdesk vendor and paid plan

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/support/` with dated filenames.

## Hand-offs

- `support-ai-agent` for automation
- `support-knowledge-base` for self-service
- `legal-commercial-contracts` for service-level terms
