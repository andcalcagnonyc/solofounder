---
name: finance-tax-and-statutory-compliance
description: "This skill should be used when the user asks to \"file my VAT return\", \"prepare taxes\", \"what taxes do I owe\", \"prepare annual accounts\", \"claim R&D tax credits\", \"do I need an audit\", \"prepare for year-end\", or needs tax and statutory reporting for the company's legal form and country."
metadata:
  version: "0.1.0"
  area: finance
---

# Tax and Statutory Compliance

Prepare every tax return and statutory report the company's legal form and country require, on time, with a file a local accountant can review and submit quickly.

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

- Closed ledger for the period
- Registrations held and filing frequencies
- Cross-border sales, purchases, staff, and related-party transactions

## Workflow

1. Build the obligations list for the entity and jurisdiction: corporate income tax, indirect tax, payroll taxes, withholding, statutory accounts, annual return, and any startup-specific regime.
2. For each indirect-tax period, reconcile the return to the ledger, apply cross-border rules, and prepare the return workpaper.
3. Estimate corporate tax quarterly and at year-end, including loss carry-forwards and instalments.
4. Identify incentives the company may qualify for (R&D credits, innovation or startup status, grants) and assemble the technical and cost evidence as work happens.
5. Assess cross-border exposure: taxable presence created by remote staff or agents, transfer pricing between group entities, and digital-services rules.
6. Prepare year-end: cut-off, accrual review, fixed assets, equity movements, notes, and the statutory-format accounts in the local framework.
7. Assemble the accountant pack: trial balance, reconciliations, workpapers, and open questions.
8. Record filing confirmations and payments in the compliance calendar.

## Deliverables

- Tax and statutory obligations list
- Return workpapers per period
- Year-end accounts pack in statutory format
- Incentive eligibility memo and evidence file

## Founder approval gates

- Every submission to a tax authority or registry
- Every tax payment
- Positions involving judgment (incentive claims, cross-border treatment)

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `legal-compliance-calendar` for deadlines
- `legal-corporate-governance` for approval of annual accounts
