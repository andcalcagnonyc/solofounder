---
name: eng-architecture
description: "This skill should be used when the user asks to \"design the architecture\", \"choose my tech stack\", \"which model should I use\", \"design the system\", \"write an architecture decision record\", \"should I use RAG or fine-tuning\", or needs the technical design of an AI or agentic product."
metadata:
  version: "0.1.0"
  area: eng
---

# AI System Architecture

Design a system a single engineer working with Claude Code can build, run, and change: the simplest architecture that meets the specification, with explicit decisions on models, data, orchestration, and cost.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Product requirements, agent specification, non-functional targets
- Data sources and customer systems to integrate, compliance constraints, budget

## Workflow

1. Restate requirements and constraints; identify the three hardest technical risks.
2. Choose the interaction pattern: single model call, workflow of fixed steps, or agent loop with tools. Use the least autonomous pattern that meets the task.
3. Select models per task by quality, latency, and cost; define routing, fallback, caching, and batch use. Keep the provider behind an abstraction.
4. Design the data layer: system of record, retrieval stores, tenant isolation, retention.
5. Design the tool and integration layer: APIs and protocols the agent uses, authentication, permissions, rate limits, idempotency.
6. Design state and control: task queue, long-running jobs, checkpoints, human-approval steps, audit log.
7. Choose managed services over self-hosted wherever one person must operate the result.
8. Estimate cost per task and capacity at 10 and 100 times launch volume.
9. Write architecture decision records for each significant choice with alternatives rejected.

## Deliverables

- Architecture document with diagram
- Decision records
- Cost and capacity estimate
- Risk list with spikes to run first

## Founder approval gates

- Model providers and cloud platform
- Any choice that locks in a vendor or data location

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `eng-agent-design` and `eng-data-and-retrieval` for detailed design
- `ops-infrastructure-and-deploy` for environments
- `finance-planning-and-runway` for cost per task
