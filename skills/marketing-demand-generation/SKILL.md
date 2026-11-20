---
name: marketing-demand-generation
description: "This skill should be used when the user asks to \"generate leads\", \"plan a campaign\", \"run ads\", \"build an email nurture sequence\", \"create a lead magnet\", \"grow my waitlist\", \"plan my launch campaign\", or needs pipeline created through marketing programs."
metadata:
  version: "0.1.0"
  area: marketing
---

# Demand Generation

Create qualified pipeline with a small number of repeatable programs, each with a budget, a target, and a measured cost per qualified lead.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- ICP, messaging, offer (trial, demo, assessment, waitlist), budget, pipeline target
- Channel access and historical performance if any

## Workflow

1. Set the funnel targets backward from the revenue goal: customers, opportunities, qualified leads, visitors.
2. Choose two or three channels that fit the buyer and budget: founder-led content, outbound, paid search or social, communities, partnerships, product-led loops, webinars.
3. Design the offer and the conversion path for each program.
4. Build campaign assets: ads, landing page, emails, lead magnet, and follow-up sequence.
5. Set lifecycle stages and lead scoring shared with sales; define when a lead is routed to a sales sequence.
6. Build nurture sequences by segment and stage in ~~email marketing, with unsubscribe and consent handling valid in the recipient's country.
7. Launch with tracking parameters on every link and budget caps on every paid channel.
8. Review weekly: spend, leads, qualified rate, cost per opportunity; cut, fix, or scale each program.

## Deliverables

- Demand plan with targets and budget
- Campaign briefs and assets
- Nurture sequences
- Weekly performance report

## Founder approval gates

- Budget and any paid spend
- Sending to any list
- Launching ads

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/marketing/` with dated filenames.

## Hand-offs

- `sales-prospecting-automation` for outbound execution
- `marketing-field-and-partners` for events, community, and partner programs
- `sales-crm-and-funnel` for routing
- `finance-planning-and-runway` for acquisition-cost inputs
