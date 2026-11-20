---
name: marketing-brand-and-design
description: "This skill should be used when the user asks to \"name my company\", \"create a logo brief\", \"define my brand\", \"create brand guidelines\", \"design a pitch deck\", \"make social graphics\", \"create a design system\", or needs brand and design assets."
metadata:
  version: "0.1.0"
  area: marketing
---

# Brand Identity and Design System

Give the company a coherent identity and a reusable design system so a single founder can produce consistent website, product, deck, and social assets quickly.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Positioning and audience
- Names, visual references, or existing assets the founder likes or rejects

## Workflow

1. Generate name candidates and screen each for domain availability, obvious trademark conflicts in the target markets, and meaning in the main customer languages. Leave formal clearance to a trademark professional.
2. Define brand foundations: purpose, personality, voice and tone rules with do and don't examples.
3. Define the visual system: logo direction, color palette with accessibility contrast checked, typography, spacing, iconography, and illustration or imagery style.
4. Express the system as design tokens that both the website and the product UI consume.
5. Produce core templates: pitch deck, one-pager, social post formats, email signature, document template.
6. Write the brand guidelines as a short reference a contractor could follow.
7. Build assets in ~~design tool where connected; otherwise deliver specifications and editable files.

## Deliverables

- Name shortlist with screening notes
- Brand guidelines with voice rules
- Design tokens and component basics
- Deck, one-pager, and social templates

## Founder approval gates

- Company and product name
- Logo and palette
- Purchase of domains or trademark applications

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/marketing/` with dated filenames.

## Hand-offs

- `marketing-website` for implementation
- `eng-build-workflow` for product UI tokens
- `legal-commercial-contracts` or a trademark professional for filings
