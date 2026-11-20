---
name: legal-entity-formation
description: "This skill should be used when the user asks to \"incorporate the company\", \"form the entity\", \"which legal structure should I use\", \"set up a Delaware C-Corp / Ltd / SRL / GmbH / Pte Ltd\", \"register my startup\", or needs to choose a jurisdiction and legal form and complete company formation anywhere in the world."
metadata:
  version: "0.1.0"
  area: legal
---

# Entity Formation

Choose the right jurisdiction and legal form for an Applied AI or Agentic AI company and take the founder from decision to a registered, bankable entity. Always ask where the HQ will be before recommending anything; the answer drives every downstream legal and finance skill.

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

- HQ country (and state or province), founder citizenship and tax residence
- Fundraising intent (bootstrapped, angels, venture) and expected investor geography
- Target customer geography and whether enterprise buyers require a local entity
- Planned hiring countries in the next 12 months

## Workflow

1. Confirm the HQ location and founder tax residence. If either is missing from the profile, ask and write the answer to the profile.
2. Shortlist two or three structures (for example local entity only, foreign holding plus local subsidiary, or a common venture vehicle) using `references/jurisdiction-playbook.md` as the starting map.
3. Research current formation rules for each shortlisted option: minimum capital, director and residency requirements, registered-office and agent needs, timeline, cost, and ongoing obligations.
4. Compare the options in a decision table: investor familiarity, founder tax exposure, administrative load, time to bank account, and cost to unwind.
5. Recommend one option and state what would change the recommendation.
6. Draft the formation pack as document text ready for a lawyer to mark up, not as a list of items: name-availability check, constitutional documents (articles, bylaws, or deed), initial director and officer appointments, share issuance to the founder, registered office, and beneficial-ownership filings.
7. Produce the post-formation checklist: tax ID, bank account, statutory registers, founder share payment, IP assignment, and the first board resolutions.
8. Give a realistic timeline. Flag when registration or banking will take longer than the 14-day sprint and list what can proceed in parallel.

## Deliverables

- `entity-decision-memo.md` with comparison table and recommendation
- Draft formation documents and filing checklist for the chosen jurisdiction
- Post-formation checklist with owners and dates
- Questions for the local lawyer and for the tax adviser

## Founder approval gates

- Choice of jurisdiction and legal form
- Submission of any registry filing and payment of any fee
- Share numbers, par value, and capital contributed

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `legal-founder-equity-and-cap-table` for vesting, IP assignment, and the cap table
- `finance-setup` for bank account, tax registrations, and chart of accounts
- `legal-compliance-calendar` to register recurring obligations
