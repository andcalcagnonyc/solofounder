---
name: support-ai-agent
description: "This skill should be used when the user asks to \"build a support bot\", \"automate support\", \"deflect tickets\", \"set up an AI support agent\", \"auto-reply to support emails\", \"improve my bot's answers\", or needs first-line support automated with an AI agent."
metadata:
  version: "0.1.0"
  area: support
---

# AI Support Agent

Resolve routine customer questions instantly and correctly with an AI agent, and hand everything else to the founder with full context.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Knowledge base, product documentation, past tickets, support policy
- Systems the agent may read or act on

## Workflow

1. Select the ticket categories suitable for automation by volume, risk, and availability of a documented answer.
2. Define agent scope: what it answers, what it may do (look up status, reset, refund within limits), and what it must never do.
3. Ground the agent in the knowledge base and account data; require an answer to be supported by a source or else hand off.
4. Write hand-off rules: frustration, repeated contact, billing disputes, legal or security topics, low confidence, or customer request for a person.
5. Make the hand-off complete: summary, steps tried, account context, suggested reply.
6. Disclose that the customer is talking to an AI where required or expected.
7. Evaluate before launch on past tickets; set accuracy and escalation thresholds.
8. Review weekly: resolved without human, wrong answers, hand-off reasons; fix the knowledge gap or the prompt.

## Deliverables

- Support agent specification and prompts
- Hand-off rules
- Evaluation results
- Weekly automation report

## Founder approval gates

- Actions the agent may take on accounts or money
- Launch to customers

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/support/` with dated filenames.

## Hand-offs

- `support-setup` for channels, commitments, and escalation paths
- `eng-agent-design` and `eng-evals` for build and measurement
- `support-knowledge-base` for content gaps
