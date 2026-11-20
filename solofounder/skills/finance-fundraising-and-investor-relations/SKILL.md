---
name: finance-fundraising-and-investor-relations
description: "This skill should be used when the user asks to \"build my pitch deck\", \"find investors\", \"build an investor list\", \"prepare for investor meetings\", \"write an investor update\", \"run my fundraising process\", \"apply for grants or accelerators\", or needs the commercial side of raising and managing capital."
metadata:
  version: "0.1.0"
  area: finance
---

# Fundraising Process and Investor Relations

Run the raise as a managed pipeline and keep investors informed afterwards: narrative, deck, target list, outreach, meetings, diligence, and regular updates. The legal mechanics sit in `legal-fundraising`.

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

- Traction, metrics, financial model, amount and use of funds
- Founder's network and target investor geography

## Workflow

1. Decide whether and when to raise from runway, milestones, and alternatives (revenue, grants, non-dilutive programs available in the HQ country).
2. Write the narrative: problem, insight, product, proof, market, business model, why this founder, and what the money achieves.
3. Build the deck and a short memo; one message per slide; every number sourced from the model.
4. Build the investor list by stage, sector, geography, and cheque size; find the warmest path to each.
5. Run the process in a pipeline with stages, next steps, and dates; batch meetings to create momentum.
6. Prepare for each meeting: investor background, likely questions, and honest answers to the hard ones.
7. Manage diligence requests from the data room and track open items.
8. After closing, send a monthly update: metrics, cash, wins, problems, asks.

## Deliverables

- Raise decision memo
- Pitch deck and memo
- Investor pipeline tracker
- Question-and-answer bank
- Investor update template and monthly updates

## Founder approval gates

- Amount, valuation expectations, and timing
- Any material sent to investors
- Metrics and forward-looking statements shared externally

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/finance/` with dated filenames.

## Hand-offs

- `legal-fundraising` for instruments, term sheets, and closing
- `finance-planning-and-runway` for the model
