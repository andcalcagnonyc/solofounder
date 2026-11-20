---
name: product-requirements-and-specs
description: "This skill should be used when the user asks to \"write a PRD\", \"write a spec\", \"write user stories\", \"define acceptance criteria\", \"spec this agent\", \"write a feature brief\", or needs build-ready requirements for a feature or an AI agent."
metadata:
  version: "0.1.0"
  area: product
---

# Requirements and Specifications

Turn a roadmap item into a specification precise enough for Claude Code to build and for evaluations to verify.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Roadmap item, customer evidence, design constraints, existing architecture

## Workflow

1. State the problem, the user, the outcome, and how success is measured.
2. Describe the workflow step by step, including inputs, outputs, and systems touched.
3. For AI behavior, specify: task definition, examples of good and bad output, tools the agent may call, permissions and limits, when it must ask a human, how it reports what it did, and failure behavior.
4. Define the evaluation set up front: representative cases, edge cases, adversarial cases, and the pass threshold.
5. Write functional requirements as testable acceptance criteria.
6. Write non-functional requirements: latency, cost per task, reliability, security, privacy, accessibility, audit trail.
7. Describe the user experience: states, errors, confidence and source display, undo and override.
8. List dependencies, open questions, and what is out of scope.
9. Break the work into implementation tasks ordered for incremental delivery.

## Deliverables

- Product requirements document
- Agent behavior specification
- Evaluation case list
- Task breakdown

## Founder approval gates

- Scope and acceptance criteria
- Agent permissions and human-approval points

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/product/` with dated filenames.

## Hand-offs

- `product-ux-design` for flows and screens
- `eng-agent-design` and `eng-build-workflow` for implementation
- `eng-evals` for the evaluation set
