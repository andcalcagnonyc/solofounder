---
name: eng-code-review-and-release
description: "This skill should be used when the user asks to \"review this code\", \"review my PR\", \"is this ready to ship\", \"cut a release\", \"write release notes\", \"write a changelog\", \"run the release checklist\", \"roll back\", or needs changes reviewed and released safely."
metadata:
  version: "0.1.0"
  area: eng
---

# Code Review and Release Management

Give every change an independent review and every release a gate, so a solo founder ships daily without shipping regressions.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Pull request or diff, specification, test and evaluation results

## Workflow

1. Review the change with fresh context: correctness against the specification, security, error handling, data migrations, performance, readability, and test coverage.
2. Report findings by severity with file and line and a suggested fix; separate must-fix from optional.
3. Verify the gates: automated checks green, evaluation thresholds met, migrations reversible, feature flags in place, documentation updated.
4. Prepare the release: version, changelog, customer-facing release notes, and support briefing.
5. Deploy progressively: staging, then a small share of traffic or a pilot customer, then all.
6. Watch the release against health, quality, and cost metrics for a set period.
7. Roll back on defined triggers and record what happened.

## Deliverables

- Review report
- Release checklist result
- Changelog and release notes

## Founder approval gates

- Merge to main and production deployment
- Rollback or forward-fix decision

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `ops-infrastructure-and-deploy` for the deployment
- `support-knowledge-base` for documentation updates
- `marketing-communications` for announcements
