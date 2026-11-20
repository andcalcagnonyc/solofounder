---
name: legal-commercial-contracts
description: "This skill should be used when the user asks to \"draft terms of service\", \"write an MSA\", \"create an order form\", \"review this customer contract\", \"draft an NDA\", \"write a DPA\", \"define an SLA\", \"review a vendor agreement\", or needs customer and supplier contracts for an AI product."
metadata:
  version: "0.1.0"
  area: legal
---

# Commercial Contracts

Build and operate the contract stack an AI company sells and buys on: templates, review of counterparty paper, negotiation positions, signature, and a contract register.

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

- Product description, pricing model, and delivery model (SaaS, API, agent acting on customer systems)
- Customer type (consumer, SMB, enterprise, public sector) and countries
- Model and infrastructure providers and their terms

## Workflow

1. Define the contract stack for the business model: terms of service or master agreement, order form, data processing agreement, service levels, acceptable use policy, NDA, and partner or reseller terms.
2. Draft each template under the governing law chosen in the profile, with AI-specific clauses: customer data and training use, output ownership, accuracy disclaimers, human-oversight responsibilities, agent action authority and limits, and sub-processors.
3. Align the templates with upstream provider terms so the company never promises what its model or cloud provider does not allow.
4. Write a negotiation playbook: preferred position, fallback, and walk-away for liability cap, indemnity, IP, data, termination, and payment.
5. For counterparty paper, review clause by clause against the playbook and return a redline with a short issues list ranked by risk.
6. Route for signature through ~~e-signature and store the executed copy.
7. Maintain the contract register: parties, value, term, renewal and notice dates, unusual obligations.

## Deliverables

- Template set and negotiation playbook
- Redlines and issues lists for reviewed contracts
- Contract register

## Founder approval gates

- Any deviation beyond the playbook fallback
- Uncapped liability, exclusivity, or IP transfer
- Sending for signature

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `legal-privacy-and-ai-compliance` for the DPA and transfer mechanisms
- `sales-proposal-and-close` for deal paperwork
- `legal-ip-and-trademarks` for licence and ownership questions
- `finance-invoicing-and-collections` for payment terms
