---
name: sales-qualification-and-discovery
description: "This skill should be used when the user asks to \"qualify this lead\", \"prepare for a sales call\", \"prep my demo\", \"summarize this call\", \"write a follow-up email\", \"respond to this inbound lead\", or needs help moving a lead from first response to a qualified opportunity."
metadata:
  version: "0.1.0"
  area: sales
---

# Lead Qualification, Discovery, and Demo

Respond to every lead fast, qualify consistently, and run discovery and demo meetings that end with a documented next step.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Lead record, source, messages so far
- Call recording, transcript, or notes after each meeting

## Workflow

1. Respond to inbound leads within minutes during working hours: acknowledge, answer the question asked, and offer booking times.
2. Score the lead for fit and intent; decline or redirect poor fits politely and record the reason.
3. Prepare a meeting brief: company background, people attending, likely use case, relevant proof, questions to ask, risks.
4. Run discovery against the qualification framework in the playbook: problem and cost, current process, decision process, criteria, timeline, budget, champion.
5. Tailor the demo to the buyer's task; show the product on their example where possible and state limits honestly.
6. After the meeting, summarise from the transcript: needs, objections, stakeholders, agreed next steps with dates.
7. Send the follow-up with the summary and next step within the same day; update fields and stage in the CRM.
8. Create a mutual action plan for opportunities that pass qualification.

## Deliverables

- Inbound responses
- Meeting briefs
- Call summaries and follow-up emails
- Mutual action plans
- Updated CRM records

## Founder approval gates

- Follow-up emails until a standing rule is approved
- Disqualifying a lead
- Commitments on features, dates, or price

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/sales/` with dated filenames.

## Hand-offs

- `sales-proposal-and-close` for qualified opportunities
- `product-discovery-and-validation` for product feedback captured in calls
