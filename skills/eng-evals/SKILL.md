---
name: eng-evals
description: "This skill should be used when the user asks to \"build evals\", \"test my agent\", \"measure accuracy\", \"create a golden dataset\", \"set up regression tests for prompts\", \"compare models\", \"is my AI good enough to ship\", or needs the quality of AI behavior measured."
metadata:
  version: "0.1.0"
  area: eng
---

# AI Evaluation

Measure whether the AI does its job, on cases that represent real use, so every prompt, model, or tool change is accepted or rejected on evidence.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Agent specification, real or synthetic task examples, production traces

## Workflow

1. Define what good means per task as observable criteria.
2. Build the dataset: typical cases, edge cases, adversarial cases, and cases from production failures. Label expected results or reference answers. Mark synthetic cases as synthetic.
3. Choose graders per criterion: exact or programmatic checks first, model-based grading with a written rubric where judgment is required, human review to calibrate the graders.
4. For agents, grade the outcome and the path: task completed, correct tools, no forbidden action, steps, cost, latency.
5. Run the baseline and record results with prompt, model, and dataset versions.
6. Set release thresholds and wire the suite into continuous integration.
7. Analyze failures by category and feed fixes to agent design.
8. Sample production traces weekly, grade them, and add new failure cases to the dataset.
9. Compare candidate models on the same suite before switching.

## Deliverables

- Versioned evaluation dataset
- Grader code and rubrics
- Baseline report and release thresholds
- Weekly production-quality report

## Founder approval gates

- Release thresholds
- Use of customer data in evaluation sets

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `eng-agent-design` for fixes
- `eng-code-review-and-release` for the release gate
- `ops-observability` for trace sampling
