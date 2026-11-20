---
name: eng-security-and-ai-safety
description: "This skill should be used when the user asks to \"review security\", \"threat model my app\", \"protect against prompt injection\", \"add guardrails\", \"secure my agent\", \"do a security review\", \"red team my agent\", or needs application security and AI-specific safety controls."
metadata:
  version: "0.1.0"
  area: eng
---

# Application Security and AI Safety

Protect customers, their data, and their systems from attack and from the agent's own mistakes, in proportion to what the product can touch.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Architecture, agent permissions, data classification, integrations

## Workflow

1. Threat-model the system: assets, entry points, trust boundaries, and abuse cases, including untrusted content reaching the model.
2. Apply application-security baselines: authentication, authorization per tenant, input validation, secrets management, dependency and supply-chain scanning, encryption in transit and at rest.
3. Defend against prompt injection: treat retrieved and tool-returned content as data, separate it from instructions, restrict tools available when untrusted content is in context, and require approval for sensitive actions.
4. Limit agent authority: least-privilege credentials, scoped tokens, spend and action limits, allow-lists, sandboxed execution, and a kill switch.
5. Control outputs: validation against schemas, sensitive-data filters, content policy, and citations where facts matter.
6. Log every agent action with who, what, when, and why for audit.
7. Red-team before launch with a written attack list; fix or accept each finding explicitly.
8. Define responsible-use limits and how misuse is detected and handled.

## Deliverables

- Threat model
- Security and safety control checklist with status
- Red-team report
- Agent permission matrix

## Founder approval gates

- Accepting any high-severity finding
- Granting the agent write or payment authority

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `ops-security-and-reliability` for infrastructure controls
- `legal-privacy-and-ai-compliance` for regulatory mapping
