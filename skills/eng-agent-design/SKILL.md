---
name: eng-agent-design
description: "This skill should be used when the user asks to \"design an agent\", \"write a system prompt\", \"improve this prompt\", \"define tools for my agent\", \"build an MCP server\", \"design a multi-agent workflow\", \"my agent keeps failing\", or needs the AI behavior of the product engineered."
metadata:
  version: "0.1.0"
  area: eng
---

# Agent, Prompt, and Tool Engineering

Engineer the behavior of the product's AI: prompts, context, tools, memory, and control flow, so the agent completes its task reliably within defined authority.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Agent behavior specification, evaluation cases, architecture
- Failing transcripts when debugging

## Workflow

1. Define the agent's job, success condition, stopping condition, and authority limits in one paragraph.
2. Write the system prompt: role and context, the task and why it matters, constraints, output format, examples, and what to do when uncertain.
3. Design the context supplied per step: what is retrieved, how it is ordered and labelled, what is summarised or dropped as the task grows.
4. Design tools: one clear purpose each, precise descriptions and parameters, informative errors, least privilege, confirmation for irreversible actions.
5. Design control flow: planning, tool loop, verification step, retries, escalation to a human, budget limits on steps, time, and tokens.
6. Design memory: what persists across tasks, where, and how it is corrected.
7. Decide whether multiple agents are warranted; default to one agent and add specialists only for separable work.
8. Test against the evaluation set, read failing transcripts, fix the root cause, and re-run.
9. Version prompts and tool definitions in the repository with a changelog.

## Deliverables

- System prompts and tool definitions under version control
- Agent design document
- Evaluation results before and after

## Founder approval gates

- Agent permissions and irreversible tools
- Promotion of a prompt or tool change to production

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `eng-evals` for measurement
- `eng-security-and-ai-safety` for injection and misuse defenses
