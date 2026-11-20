---
name: eng-qa-testing
description: "This skill should be used when the user asks to \"write tests\", \"create a test plan\", \"run QA\", \"test this feature\", \"set up end-to-end tests\", \"do a bug bash\", \"write a regression suite\", \"load test\", or needs software quality assurance."
metadata:
  version: "0.1.0"
  area: eng
---

# Quality Assurance and Testing

Verify that the software works as specified before customers find out otherwise, with an automated suite one person can maintain.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Specification with acceptance criteria, code, environments

## Workflow

1. Write the test strategy: what is covered by unit, integration, end-to-end, and manual exploratory testing, and what is deliberately not covered.
2. Derive test cases from acceptance criteria, including error paths and permission boundaries.
3. Implement unit and integration tests alongside the code; isolate model calls behind fakes for deterministic tests and cover real model behavior in the evaluation suite.
4. Implement end-to-end tests for the critical user journeys in a production-like environment.
5. Test non-functional requirements: load, latency, failure of dependencies, rate limits, and recovery.
6. Run exploratory testing before each release against a checklist and record findings.
7. Triage defects by severity; add a regression test with every fix.
8. Report release readiness: tests passed, known issues, risk assessment.

## Deliverables

- Test strategy and cases
- Automated test suites
- Defect log
- Release readiness report

## Founder approval gates

- Accepting known defects into a release
- Tests that run against production data

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `eng-evals` for AI quality
- `eng-code-review-and-release` for the go or no-go decision
