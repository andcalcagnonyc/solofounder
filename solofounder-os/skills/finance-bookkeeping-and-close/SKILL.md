---
name: finance-bookkeeping-and-close
description: "This skill should be used when the user asks to \"do my bookkeeping\", \"categorize these transactions\", \"reconcile the bank\", \"close the month\", \"prepare financial statements\", \"post a journal entry\", or needs the recurring accounting cycle run end to end."
metadata:
  version: "0.1.0"
  area: finance
---

# Bookkeeping and Month-End Close

Run the record-to-report cycle: capture and code every transaction, reconcile, post accruals, and produce management accounts within five working days of month-end.

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

- Bank, card, and payment-processor feeds or exports
- Sales invoices, supplier bills, receipts, payroll reports
- Prior-period trial balance

## Workflow

1. Weekly: pull transactions from ~~accounting system or exports, match each to a document, code to account and tax code, and list items that need the founder's answer.
2. Reconcile every bank, card, and processor account to statement balance. Explain every reconciling item.
3. Reconcile processor payouts to gross sales, fees, refunds, and chargebacks.
4. Post month-end entries: accruals, prepayments, depreciation, deferred revenue release, payroll, foreign-exchange revaluation, and usage-based costs from model and cloud providers.
5. Review the trial balance: variance to prior month and to budget, with an explanation for every movement above the materiality set in the profile.
6. Produce the management pack: profit and loss, balance sheet, cash flow, cash runway, and key metrics.
7. Lock the period and archive supporting documents under the local retention rules.
8. Keep a close checklist with sign-off per step and a list of open questions for the accountant.

## Deliverables

- Coded and reconciled ledger
- Journal entries with support
- Monthly management pack and variance commentary
- Close checklist with open items

## Founder approval gates

- Posting of manual journals
- Any transaction the documents do not explain
- Period lock

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `finance-planning-and-runway` for forecast updates
- `finance-tax-and-statutory-compliance` for returns built on the ledger
