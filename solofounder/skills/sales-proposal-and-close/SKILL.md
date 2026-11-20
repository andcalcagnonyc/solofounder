---
name: sales-proposal-and-close
description: "This skill should be used when the user asks to \"write a proposal\", \"create a quote\", \"respond to an RFP\", \"answer a security questionnaire\", \"negotiate this deal\", \"close this deal\", \"mark this deal won\", or needs help taking an opportunity to signature and handing it over."
metadata:
  version: "0.1.0"
  area: sales
---

# Proposal, Negotiation, and Close

Take a qualified opportunity to a signed contract and a clean hand-over: proposal, pilot conversion, procurement and security review, negotiation, signature, and closed-won processing.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Opportunity record, discovery notes, pilot results
- Pricing and discount rules, contract templates, playbook positions

## Workflow

1. Write the proposal: buyer's problem in their words, solution scope, pilot evidence, commercial terms, implementation plan, and success measures.
2. Build the quote within the pricing and discount rules; record any exception requested.
3. Complete procurement artefacts from the answer bank: security questionnaire, vendor forms, compliance documents.
4. Map stakeholders and the paper process: who signs, legal review, purchasing steps, and dates.
5. Prepare negotiation positions with the give-and-get for each likely request.
6. Issue the order form or contract for signature through ~~e-signature; track status and nudge.
7. On signature, mark closed-won and run the hand-over: create the customer in billing, schedule onboarding, write the account brief for success and support.
8. On loss, record the reason and competitor, and schedule a revisit.

## Deliverables

- Proposal and quote
- Completed questionnaires
- Negotiation brief
- Signed contract record
- Closed-won hand-over brief or closed-lost analysis

## Founder approval gates

- Price, discount, and any non-standard term
- Sending the proposal and the contract
- Legal exceptions beyond the contract playbook

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/sales/` with dated filenames.

## Hand-offs

- `legal-commercial-contracts` for redlines
- `finance-invoicing-and-collections` for billing
- `support-customer-success` for onboarding
