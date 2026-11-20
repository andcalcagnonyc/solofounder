---
name: legal-founder-equity-and-cap-table
description: "This skill should be used when the user asks to \"set up my cap table\", \"issue founder shares\", \"create a vesting schedule\", \"assign IP to the company\", \"create an option pool\", \"add an advisor with equity\", or needs to manage shareholders, share classes, and ownership records."
metadata:
  version: "0.1.0"
  area: legal
---

# Founder Equity, IP Assignment, and Cap Table

Keep ownership clean from day one: founder shares, vesting, intellectual-property assignment, option pool, advisor grants, and a cap table that reconciles to the statutory share register.

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

- Entity documents and share capital from formation
- Everyone who has contributed code, design, data, or prompts so far, and under what terms
- Planned advisors, early hires, and pool size

## Workflow

1. Build the cap table: holders, share class, number, price paid, date, vesting terms, and fully diluted percentages. Reconcile it to the share register.
2. Draft the founder share subscription or purchase agreement with a vesting or reverse-vesting mechanism valid in the jurisdiction.
3. Identify tax elections or filings with hard deadlines tied to the grant date (for example an election on restricted stock) and put them at the top of the task list.
4. Draft the IP assignment covering all pre-incorporation work, including code, models, prompts, datasets, domains, and brand assets. List any third-party or prior-employer IP risk.
5. Design the equity incentive pool: size, instrument suited to the jurisdiction, approval steps, and valuation requirement.
6. Draft advisor and early-contributor agreements with vesting and IP clauses.
7. Model dilution for the next round and present pre- and post-money tables.
8. Set the update procedure: every issuance, transfer, or grant updates the cap table, the register, and the board approval record in the same session.

## Deliverables

- Cap table (spreadsheet or ~~cap table tool) with fully diluted view
- Founder share agreement and vesting schedule draft
- IP assignment agreement draft and IP inventory
- Option or incentive plan summary and approval checklist
- Dilution scenarios

## Founder approval gates

- Vesting terms and any acceleration
- Pool size and each individual grant
- Signing of the IP assignment

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `legal-corporate-governance` for the board and shareholder approvals each issuance needs
- `legal-fundraising` for round modelling
- `finance-tax-and-statutory-compliance` for equity-related tax filings
