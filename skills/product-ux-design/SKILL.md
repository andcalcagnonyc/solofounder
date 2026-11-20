---
name: product-ux-design
description: "This skill should be used when the user asks to \"design the UI\", \"create wireframes\", \"design the user flow\", \"mock up this screen\", \"design the agent experience\", \"improve my onboarding UX\", \"review my design\", or needs the product's user experience and interface designed."
metadata:
  version: "0.1.0"
  area: product
---

# Product UX and Interface Design

Design an interface in which users understand what the AI is doing, trust it appropriately, and stay in control, and hand engineering a build-ready design.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Requirements, user personas, brand tokens, existing screens

## Workflow

1. Map the user journey from sign-up to first successful task; remove every step that does not serve it.
2. Define the interaction model: chat, form with AI assistance, background agent with an inbox of results, or embedded in the user's existing tool.
3. Design AI-specific states: working and progress, plan preview, approval request, result with sources and confidence, partial failure, undo and correction, feedback capture.
4. Design the control surface for agents: what it may do, activity log, pause and stop, and settings for autonomy level.
5. Produce wireframes for each screen and state, then high-fidelity designs using the design tokens through ~~design tool or code.
6. Write interface copy: labels, empty states, errors, and explanations of AI limits.
7. Check accessibility: contrast, keyboard use, screen-reader labels, motion.
8. Test with five target users on a prototype; record where they hesitate or misread the AI; revise.
9. Hand off: component specifications, states, and acceptance criteria.

## Deliverables

- User journey and flow diagrams
- Wireframes and high-fidelity designs or coded prototype
- Interface copy
- Usability test findings
- Design hand-off specification

## Founder approval gates

- Interaction model and autonomy controls
- Final designs before build

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/product/` with dated filenames.

## Hand-offs

- `eng-build-workflow` for implementation
- `marketing-brand-and-design` for the design system
- `product-requirements-and-specs` for requirement changes
