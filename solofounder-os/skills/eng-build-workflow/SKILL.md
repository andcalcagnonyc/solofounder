---
name: eng-build-workflow
description: "This skill should be used when the user asks to \"set up my repo\", \"start building\", \"implement this feature\", \"set up CI\", \"write a CLAUDE.md\", \"plan the implementation\", \"scaffold the project\", or needs the development workflow for building the product with Claude."
metadata:
  version: "0.1.0"
  area: eng
---

# Build Workflow with Claude Code

Set up and run a development workflow in which one founder directs Claude Code to build production software quickly without losing control of quality.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Specification, architecture, task breakdown
- Repository access through ~~code repository

## Workflow

1. Scaffold the repository: structure, language and framework choices from the architecture, dependency management, environment configuration, secrets kept out of the repository.
2. Write the project instruction file for Claude Code: purpose, architecture summary, commands, conventions, testing rules, and what must never be done.
3. Set up automated checks: formatting, linting, type checks, unit tests, evaluations, and security scans, run locally and in continuous integration.
4. Work in small increments: plan the task, write or update tests, implement, run checks, review the diff, commit with a clear message.
5. Use branches and pull requests even when working alone, so every change has a reviewable record.
6. Parallelize independent tasks across separate work trees or sessions; keep each task's scope narrow.
7. Keep documentation current in the same change: readme, decision records, runbooks, API reference.
8. Track work in ~~project tracker with status tied to pull requests.

## Deliverables

- Repository scaffold with instruction file
- Continuous-integration pipeline
- Working increments merged with tests

## Founder approval gates

- Pushing to the main branch and merging pull requests
- Adding dependencies with restrictive licenses
- Any command that deletes data or rewrites history

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `eng-code-review-and-release` before merge
- `eng-qa-testing` and `eng-evals` for verification
