---
name: legal-privacy-and-ai-compliance
description: "This skill should be used when the user asks to \"write a privacy policy\", \"am I GDPR compliant\", \"do I need a DPA\", \"does the EU AI Act apply to me\", \"map my data flows\", \"run a DPIA\", \"answer a security questionnaire\", or needs privacy and AI-regulatory compliance for an AI product."
metadata:
  version: "0.1.0"
  area: legal
---

# Privacy, Data Protection, and AI Regulation

Establish the privacy and AI-regulatory baseline for a product that processes customer data through models and autonomous agents, and keep the evidence a customer or regulator will ask for.

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

- Data categories processed, sources, and data subjects' locations
- Model providers, hosting regions, sub-processors
- What the product or agent decides or does without a human

## Workflow

1. Determine which regimes apply from where the company, customers, and data subjects are: general privacy law, sector rules, and AI-specific regulation.
2. Map data flows: collection, prompts, retrieval stores, model calls, logs, analytics, and retention. Record legal basis and purpose for each.
3. Classify the AI use case under the applicable AI regulation and list the resulting obligations (transparency, human oversight, documentation, prohibited uses).
4. Draft the public documents: privacy notice, cookie notice, AI transparency statement, and sub-processor list.
5. Draft internal records: processing register, impact assessment for high-risk processing, data-retention schedule, incident and breach procedure, and data-subject request procedure.
6. Set cross-border transfer mechanisms and document provider commitments on training use and retention.
7. Prepare a reusable answer bank for customer security and privacy questionnaires.
8. Schedule a review each quarter and on any change of model provider, data source, or agent capability.

## Deliverables

- Applicability memo and obligations register
- Data-flow map and processing register
- Privacy notice, AI transparency statement, sub-processor list
- Impact assessment and breach procedure
- Questionnaire answer bank

## Founder approval gates

- Publication of any public policy
- Classification of the AI use case
- Any notification to a regulator or to customers

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/legal/` with dated filenames.

## Hand-offs

- `eng-security-and-ai-safety` for technical controls
- `ops-security-and-reliability` for access, logging, and backup evidence
- `legal-commercial-contracts` for DPA terms
