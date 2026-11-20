---
name: finance-setup
description: "This skill should be used when the user asks to \"set up my accounting\", \"open a business bank account\", \"create a chart of accounts\", \"choose accounting software\", \"set up payments\", \"register for VAT / sales tax\", or needs the finance foundation for a new company."
metadata:
  version: "0.1.0"
  area: finance
---

# Finance Stack Setup

Stand up the finance foundation in the first days of the company: banking, payments, accounting system, chart of accounts, tax registrations, and the policies that make the monthly cycle run with minimal founder time.

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

- Entity type, jurisdiction, financial year-end, functional currency
- Revenue model (subscription, usage, services) and customer countries
- Expected monthly transaction volume

## Workflow

1. Read `references/country-finance-checklist.md` and research the local requirements: accounting framework, bookkeeping and invoicing rules, e-invoicing mandates, record-retention period, and audit thresholds.
2. Recommend the bank or payment institution, payment processor, accounting system, and expense tool that work in the jurisdiction. Explain the choice in one paragraph each.
3. Design the chart of accounts on the local statutory layout, with dimensions useful to an AI company: model inference and cloud as cost of revenue, R&D, sales and marketing, general and administrative.
4. List required tax registrations (corporate income tax, VAT or GST or sales tax, payroll) with thresholds and deadlines.
5. Define accounting policies: revenue recognition for the pricing model, capitalisation of development costs if permitted, foreign-currency treatment, expense policy.
6. Configure the accounting system: bank feeds, tax codes, invoice template with mandatory local fields, document storage.
7. Set the finance calendar: weekly bookkeeping, monthly close, tax periods, year-end.

## Deliverables

- Finance stack recommendation
- Chart of accounts ready to import
- Tax registration checklist
- Accounting policies memo
- Finance calendar

## Founder approval gates

- Choice of bank, processor, and accounting system
- Any tax registration submission
- Accounting policies

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `finance-bookkeeping-and-close` for the recurring cycle
- `finance-tax-and-statutory-compliance` for filings
- `legal-compliance-calendar` for deadlines
