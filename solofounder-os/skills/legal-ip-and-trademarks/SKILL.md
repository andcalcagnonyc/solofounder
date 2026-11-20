---
name: legal-ip-and-trademarks
description: "This skill should be used when the user asks to \"trademark my name\", \"protect my IP\", \"can I use this open-source library\", \"check this license\", \"who owns the model outputs\", \"should I file a patent\", \"audit my open-source dependencies\", or needs intellectual-property protection and licence compliance."
metadata:
  version: "0.1.0"
  area: legal
---

# Intellectual Property and Trademarks

Protect what the company owns and avoid infringing what it does not: brand, code, data, models, and the open-source and third-party components the product is built on.

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

- Brand names and logos, target markets
- Codebase dependencies, datasets, model providers and their terms

## Workflow

1. Inventory IP assets: brand, domains, code, prompts, evaluation sets, datasets, fine-tuned weights, documentation, and trade secrets.
2. Run a preliminary trademark screen in the priority markets and classes; recommend filing strategy and order of countries; leave formal clearance and filing to a trademark attorney.
3. Audit open-source licences across dependencies; flag copyleft or non-commercial terms and model or dataset licences that restrict commercial use.
4. Review rights in training and retrieval data: source, licence, consent, and customer restrictions.
5. Summarize ownership of inputs and outputs under each model provider's terms and reflect it in customer contracts.
6. Assess patentability and the value of filing versus trade-secret protection; note disclosure deadlines.
7. Set trade-secret hygiene: access control, confidentiality terms, marking, and offboarding.
8. Record renewals and deadlines in the compliance calendar.

## Deliverables

- IP register
- Trademark screening memo and filing plan
- Open-source and data licence report
- Patent versus trade-secret memo

## Founder approval gates

- Any trademark or patent filing and its cost
- Accepting a dependency or dataset with restrictive terms

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `marketing-brand-and-design` for naming
- `legal-founder-equity-and-cap-table` for assignments
- `legal-compliance-calendar` for renewals
