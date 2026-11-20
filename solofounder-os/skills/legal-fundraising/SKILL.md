---
name: legal-fundraising
description: "This skill should be used when the user asks to \"raise a round\", \"draft a SAFE\", \"review a term sheet\", \"prepare a convertible note\", \"build a data room\", \"close an angel round\", or needs the legal mechanics of raising capital from pre-seed to a priced round."
metadata:
  version: "0.1.0"
  area: legal
---

# Fundraising Legal Workflow

Run the legal side of a raise end to end: pick the instrument, prepare the documents and data room, review investor terms, obtain approvals, and close with the cap table updated.

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

- Target amount, valuation expectations, investor list and their countries
- Current cap table and constitutional documents
- Any existing convertible instruments or side letters

## Workflow

1. Select the instrument suited to the jurisdiction and stage: SAFE or local equivalent, convertible note, or priced equity round. Explain the trade-offs in plain language.
2. Check securities-law constraints on who may be offered shares and what filings follow a closing in the company's and each investor's jurisdiction.
3. Model the round: cap, discount, pool top-up, pro-rata rights, and resulting ownership under three price scenarios.
4. Assemble the data room: corporate records, cap table, IP assignments, key contracts, financials, product and security documentation, and AI-specific items (model providers, data sources, evaluation results).
5. Review any term sheet clause by clause: economics, control, protective provisions, liquidation preference, anti-dilution, founder vesting resets, information rights. Rate each clause standard, negotiable, or unusual.
6. Draft the closing set: investment agreement or instrument, board and shareholder approvals, updated constitutional documents if required, and disclosure schedule.
7. Run the closing checklist: signatures, funds received, shares or instruments issued, registers and cap table updated, regulatory filings made.
8. Prepare the investor-update template for after closing.

## Deliverables

- Round model and instrument recommendation
- Data-room index with gaps flagged
- Term-sheet review memo with negotiation positions
- Closing checklist and draft approvals

## Founder approval gates

- Instrument, valuation cap, and total amount
- Any term rated unusual
- Signature of every investor document

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `legal-corporate-governance` for resolutions and minutes
- `legal-founder-equity-and-cap-table` to record the issuance
- `finance-fundraising-and-investor-relations` for the deck, investor pipeline, and updates
- `finance-planning-and-runway` for the financial model investors will ask for
