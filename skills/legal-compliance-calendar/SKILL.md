---
name: legal-compliance-calendar
description: "This skill should be used when the user asks \"what filings are due\", \"what are my legal obligations\", \"build a compliance calendar\", \"what do I need to renew\", \"run a legal health check\", or needs a single view of recurring corporate, tax, and regulatory obligations."
metadata:
  version: "0.1.0"
  area: legal
---

# Compliance Calendar and Corporate Housekeeping

Maintain one calendar of every recurring obligation the company has, with owners, lead times, and evidence, so nothing lapses while the founder is building.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Jurisdiction protocol

- Take the governing jurisdictions from the profile: country (and state or province) of incorporation, founder tax residence, and every country where customers, employees, or contractors sit.
- Research the current rules for those jurisdictions from primary sources (company registry, tax authority, regulator) before drafting. Cite each source with its date in the output.
- Where jurisdictions differ, state which one governs and why.
- Label every output as a draft for review by a locally licensed lawyer, and list the specific questions to put to them. Never present output as legal advice.
- Never file, sign, pay, or submit anything on the founder's behalf without explicit approval of that specific action.

## Inputs

- Entity type and jurisdiction, registration dates, financial year-end
- Licences, registrations, trademarks, domains, insurance policies
- Outputs of the other legal and finance skills

## Workflow

1. List obligations by source: company law (annual return, accounts, meetings), tax (returns, payments, registrations), employment, privacy and AI regulation, licences, IP renewals, insurance, and contractual commitments.
2. For each, record the rule source, due date or recurrence, lead time, preparer, approver, and where the evidence is filed.
3. Create the entries in ~~calendar with reminders at the lead time.
4. Run a monthly sweep: what is due in the next 60 days, what is overdue, what changed in the law or the business.
5. Run a quarterly health check: registers current, minute book complete, contracts register current, policies reviewed, trademark and domain status.
6. Report exceptions to the founder with the consequence of missing each one.

## Deliverables

- Compliance calendar (spreadsheet plus calendar entries)
- Monthly 60-day outlook
- Quarterly legal health-check report

## Founder approval gates

- Creation of calendar entries in the founder's calendar
- Any filing or payment arising from the calendar

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `finance-tax-and-statutory-compliance` for tax and accounts deadlines
- `legal-corporate-governance` for meetings and filings
