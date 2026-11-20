---
name: legal-corporate-governance
description: "This skill should be used when the user asks to \"write board minutes\", \"draft a board resolution\", \"prepare a shareholder meeting\", \"write a written consent\", \"hold the annual general meeting\", \"update the statutory registers\", or needs to run board and shareholder governance."
metadata:
  version: "0.1.0"
  area: legal
---

# Board, Shareholders, Minutes, and Resolutions

Run corporate governance for a company with one founder and a growing set of shareholders and directors: decide which body must approve what, prepare meetings or written consents, record minutes, and keep the statutory books current.

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

- Constitutional documents and any shareholders' agreement
- Current directors, officers, and shareholders
- The action that needs approval, or the meeting date

## Workflow

1. Classify the action: director decision, shareholder decision, or both, using the constitutional documents and local company law. State the required majority, notice period, and quorum.
2. Choose the route allowed locally: meeting, written resolution, or unanimous consent. Note where a notary or registry filing is required.
3. Draft the notice, agenda, and board pack (CEO report, financials, key metrics, decisions requested).
4. Draft the resolutions in the local form, with recitals, the operative decision, and authority to execute.
5. After the meeting or consent, write minutes: attendees, quorum, conflicts declared, discussion summary, decisions, votes, and action items.
6. Update the statutory registers (directors, shareholders, beneficial owners, charges) and file any registry notifications within the deadline.
7. Store signed records in the corporate minute book with an index.
8. Maintain a standing calendar: board cadence, annual general meeting, accounts approval, and annual return.

## Deliverables

- Notice, agenda, and board pack
- Resolutions or written consents ready to sign
- Minutes
- Updated registers and minute-book index

## Founder approval gates

- Content of every resolution before circulation
- Sending notices to directors or shareholders
- Any registry filing

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `legal-compliance-calendar` for recurring governance dates
- `finance-planning-and-runway` for the financial section of the board pack
