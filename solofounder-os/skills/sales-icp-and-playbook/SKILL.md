---
name: sales-icp-and-playbook
description: "This skill should be used when the user asks to \"build a sales playbook\", \"define my sales process\", \"write a pitch\", \"create a demo script\", \"write discovery questions\", \"handle objections\", or needs the selling motion defined for an AI product."
metadata:
  version: "0.1.0"
  area: sales
---

# Sales Playbook

Define one repeatable selling motion from first touch to signed customer that a founder can run alone with automation, and that proves an AI product's value before the buyer commits.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- ICP, messaging, pricing, competitor battlecards
- Notes or recordings from sales conversations so far

## Workflow

1. Choose the motion that fits price and buyer: self-serve, sales-assisted, or enterprise. State average deal size and target cycle length.
2. Define account and persona tiers and the trigger events that make an account worth contacting now.
3. Write the stage-by-stage process with buyer exit criteria, required fields, and the next step at each stage (see `sales-crm-and-funnel`).
4. Write the talk tracks: opening, discovery question set, value narrative, demo flow built around the buyer's own data or task, and close.
5. Write objection responses for the recurring AI concerns: accuracy, security and data use, control over agent actions, integration effort, price versus headcount.
6. Design the proof step: pilot or trial with success criteria, duration, and conversion terms agreed up front.
7. Assemble the asset kit: deck, one-pager, security overview, return-on-investment calculator, case study format, proposal template.
8. Update the playbook monthly from won and lost deals.

## Deliverables

- Sales playbook
- Discovery guide and demo script
- Objection handbook
- Pilot template with success criteria

## Founder approval gates

- Sales motion and pilot terms
- Any claim about results or return on investment

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/sales/` with dated filenames.

## Hand-offs

- `sales-crm-and-funnel` to encode the process
- `sales-prospecting-automation` to start outreach
