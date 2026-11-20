---
name: sales-crm-and-funnel
description: "This skill should be used when the user asks to \"set up my CRM\", \"define my pipeline stages\", \"build my sales funnel\", \"clean up my CRM\", \"automate my CRM\", \"track my deals\", or needs the CRM configured and kept accurate from lead to won."
metadata:
  version: "0.1.0"
  area: sales
---

# CRM Setup and Funnel Management

Make the CRM the single record of every lead, account, and deal, with stages, fields, and automations that keep it accurate without manual data entry.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Sales playbook, lead sources, tools in the profile
- Existing contacts and deal data to import

## Workflow

1. Select or confirm ~~CRM sized for one seat and API access for automation.
2. Configure the data model: lead, contact, account, opportunity, activity; required fields; lead source and campaign attribution.
3. Configure the funnel using `references/funnel-stages.md`: stage definitions, entry and exit criteria, probability, and time limits per stage.
4. Build capture automations: website forms, inbound email, calendar bookings, product sign-ups, event lists, each creating or updating records without duplicates.
5. Build activity automations: email and meeting logging, call-note summaries written to the record, next-step task creation, stage-change alerts.
6. Set lead scoring and routing: fit plus intent, with thresholds that start a sequence or alert the founder.
7. Import and deduplicate existing data; enrich missing fields through ~~enrichment.
8. Run a weekly hygiene pass: deals with no next step, stale stages, missing amounts or close dates, duplicates.

## Deliverables

- CRM configuration specification and field dictionary
- Funnel definition
- Automation map
- Weekly hygiene report

## Founder approval gates

- CRM vendor and any paid plan
- Bulk imports, merges, and deletions
- Automations that send messages

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/sales/` with dated filenames.

## Hand-offs

- `sales-prospecting-automation` and `sales-qualification-and-discovery` operate inside this setup
- `sales-pipeline-review-and-forecast` reports from it
