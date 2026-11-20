---
name: finance-payables-and-payroll
description: "This skill should be used when the user asks to \"pay my bills\", \"process vendor invoices\", \"what do I owe\", \"run payroll\", \"pay contractors\", \"track my subscriptions\", or needs the procure-to-pay and payroll cycles operated."
metadata:
  version: "0.1.0"
  area: finance
---

# Payables, Expenses, and Payroll

Operate procure-to-pay and payroll: capture bills, verify them, schedule payments against cash, pay people correctly, and keep vendor and tool spend under control.

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

- Supplier bills, subscriptions, contractor invoices, receipts
- Payroll data: people, pay, benefits, country
- Cash balance and forecast

## Workflow

1. Capture bills from the inbox or uploads; extract vendor, amount, tax, due date, and service period; detect duplicates.
2. Verify each bill against the contract or order and code it to account, cost centre, and tax code.
3. Maintain the vendor register: tax details, payment terms, contract renewal dates, and withholding obligations for foreign vendors.
4. Propose a weekly payment run ranked by due date and criticality against available cash. Stage payments; never release them.
5. Track recurring SaaS, model-API, and cloud spend; flag unused seats, price changes, and committed-spend opportunities.
6. Prepare payroll per country: gross-to-net, employer contributions, filings, and payslips through the local payroll provider or employer-of-record.
7. Prepare contractor payments with required invoices and year-end reporting forms.
8. Process founder expenses and reimbursements under the expense policy.

## Deliverables

- Coded bills and proposed payment run
- Vendor register and renewal list
- Payroll preparation file and filing checklist
- Monthly spend report with savings actions

## Founder approval gates

- Release of every payment run and payroll
- New vendor bank details or changes to them
- Cancelling or committing to any subscription

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `legal-hiring-and-contractors` for agreements
- `ops-cost-and-finops` for cloud and token spend
- `finance-bookkeeping-and-close` for posting
