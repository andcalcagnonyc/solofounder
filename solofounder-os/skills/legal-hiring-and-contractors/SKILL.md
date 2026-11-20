---
name: legal-hiring-and-contractors
description: "This skill should be used when the user asks to \"hire a contractor\", \"draft a contractor agreement\", \"write an employment contract\", \"hire someone in another country\", \"should I use an EOR\", \"write an offer letter\", or needs the legal setup for engaging people."
metadata:
  version: "0.1.0"
  area: legal
---

# Employment, Contractors, and Advisors

Engage contractors, employees, and advisors correctly in each person's country, with IP and confidentiality secured and misclassification risk controlled.

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

- Role, country of the worker, expected hours and duration, compensation
- Whether the company has an entity in that country

## Workflow

1. Determine the engagement model allowed for the facts: contractor, employee through the company's entity, or employer-of-record. Apply the local tests for employee status and state the misclassification risk.
2. Research mandatory local terms: notice, probation, leave, social contributions, working time, and termination rules.
3. Draft the agreement with IP assignment, confidentiality, data protection, AI-tool usage rules, and post-termination restrictions that are enforceable locally.
4. Draft the offer letter and equity grant summary where relevant.
5. Produce the onboarding compliance checklist: right-to-work checks, registrations, payroll setup, policies to acknowledge.
6. Produce the offboarding checklist: access removal, IP and asset return, final pay, equity treatment.

## Deliverables

- Engagement-model memo
- Agreement and offer letter drafts
- Onboarding and offboarding checklists

## Founder approval gates

- Engagement model for each person
- Compensation and equity terms
- Sending any offer or agreement

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `finance-payables-and-payroll` for payroll and contractor payments
- `legal-founder-equity-and-cap-table` for equity grants
