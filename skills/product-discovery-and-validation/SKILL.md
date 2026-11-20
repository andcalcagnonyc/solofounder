---
name: product-discovery-and-validation
description: "This skill should be used when the user asks to \"validate my idea\", \"plan customer interviews\", \"synthesize these interviews\", \"is this problem worth solving\", \"find my first design partners\", \"test demand\", or needs evidence before building."
metadata:
  version: "0.1.0"
  area: product
---

# Customer Discovery and Validation

Establish with evidence that a specific customer has a costly problem an AI system can solve well enough to pay for, before engineering time is spent.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Idea, target segment, founder's unfair advantages
- Interview notes, transcripts, or survey data as they arrive

## Workflow

1. State the hypotheses: customer, problem, current cost, proposed solution, willingness to pay. Rank them by risk.
2. Check AI suitability of the task: frequency, tolerance for error, availability of ground truth, data access, cost of a wrong action, and whether a human review step is acceptable.
3. Size the opportunity bottom-up from number of customers and value per unit of work.
4. Write an interview guide that asks about past behavior and avoids pitching.
5. Recruit interviewees and design partners from the founder's network and targeted outreach.
6. Synthesize each batch: quotes, patterns, surprises, and how each hypothesis moved.
7. Run a demand test with a real commitment: paid pilot, letter of intent, pre-order, or waitlist with qualifying questions.
8. Conclude with go, change, or stop, and the evidence behind it.

## Deliverables

- Hypothesis table with risk ranking
- Interview guide and recruitment list
- Synthesis report
- Demand-test result and decision memo

## Founder approval gates

- Target segment and problem choice
- Outreach to interviewees
- The go, change, or stop decision

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/product/` with dated filenames.

## Hand-offs

- `product-strategy-and-roadmap` on a go decision
- `marketing-positioning-and-messaging` for customer language
