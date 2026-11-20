---
name: finance-invoicing-and-collections
description: "This skill should be used when the user asks to \"send an invoice\", \"set up billing\", \"set up subscriptions\", \"chase overdue invoices\", \"who owes me money\", \"recognize revenue\", or needs the order-to-cash cycle operated."
metadata:
  version: "0.1.0"
  area: finance
---

# Invoicing, Revenue, and Collections

Operate order-to-cash: turn closed deals into compliant invoices or subscriptions, recognise revenue correctly, collect on time, and report recurring revenue.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Jurisdiction protocol

- Take the governing jurisdictions from the profile: country (and state or province) of incorporation, founder tax residence, and every country where customers, employees, or contractors sit.
- Research the current rules for those jurisdictions from primary sources (company registry, tax authority, regulator) before drafting. Cite each source with its date in the output.
- Where jurisdictions differ, state which one governs and why.
- Label every output as a draft for review by a locally licensed accountant or tax adviser, and list the specific questions to put to them. Never present output as tax or accounting advice.
- Never file, sign, pay, or submit anything on the founder's behalf without explicit approval of that specific action.

## Inputs

- Signed order or checkout record, price, term, billing frequency, customer tax details
- Usage data for metered pricing
- Receivables ageing

## Workflow

1. Create the customer and the contract record with billing terms, tax treatment by customer location, and purchase-order or portal requirements.
2. Issue invoices that meet local mandatory content and any e-invoicing channel; for self-serve, configure plans, metering, proration, and dunning in ~~payments.
3. Determine indirect tax per sale (place of supply, reverse charge, marketplace or digital-services rules, exemption certificates).
4. Build the revenue schedule: performance obligations, deferred revenue, usage true-ups.
5. Run collections weekly: ageing review, reminder sequence at set intervals, escalation, and dispute log. Draft each reminder for approval.
6. Process refunds, credit notes, and chargebacks with an audit trail.
7. Report monthly: recurring revenue movements (new, expansion, contraction, churn), days sales outstanding, and cash collected.

## Deliverables

- Invoices, credit notes, and billing configuration
- Revenue recognition schedule
- Ageing report and collections log
- Recurring-revenue report

## Founder approval gates

- Sending invoices and reminders until the founder approves a standing rule
- Credit notes, refunds, write-offs
- Tax treatment of a new country or product

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `sales-proposal-and-close` supplies closed-won data
- `finance-bookkeeping-and-close` for posting
- `support-customer-success` for accounts with payment risk
