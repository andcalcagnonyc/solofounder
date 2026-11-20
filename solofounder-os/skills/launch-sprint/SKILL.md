---
name: launch-sprint
description: "This skill should be used when the user asks to \"launch my company in two weeks\", \"run the launch sprint\", \"give me the 14-day plan\", \"what do I do today\", \"where am I in the sprint\", \"plan my launch end to end\", or wants to take an Applied AI or Agentic AI company from idea to first customers across legal, finance, marketing, sales, product, engineering, operations, and support."
metadata:
  version: "0.1.0"
  area: core
---

# Launch Sprint: Idea to Operating Company in 14 Days

Orchestrate every solofounder-os skill into one 14-day plan with daily goals and exit gates. The sprint produces a company that is formed or in formation, a product in the hands of pilot customers, a working revenue funnel, and operating routines for finance, operations, and support.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, run `start`.
2. Read `references/14-day-plan.md` for the day-by-day plan and gates.
3. Check `solofounder/sprint-status.md` if a sprint is already running.

## Set expectations honestly

State these to the founder at kickoff:

- Fourteen days is achievable for the work Claude and the founder control: validation, product build, website, funnel, finance stack, contracts, and operating routines.
- Steps that depend on third parties run on their clocks: company registration, bank account opening, tax registrations, trademark filings, and enterprise procurement can take from one day to several weeks depending on the country. Start them on day 1 and run everything else in parallel.
- Legal, tax, and accounting outputs are drafts for a locally licensed professional to review. Book that reviewer in the first two days.

## Workflow

1. Tailor the plan: adjust the reference plan to the profile's stage, HQ country, weekly hours, and budget. Remove work already done. If fewer than 30 founder hours per week are available, extend the calendar and say by how much.
2. Identify long-lead items for the jurisdiction and schedule them first.
3. Write `solofounder/sprint-plan.md`: for each day, the goal, the skills to run, the deliverables, the founder decisions needed, and the exit gate.
4. Each day, open with the day brief: today's goal, the skills to run in order, the approvals expected. Run the skills. Close with a status update in `solofounder/sprint-status.md`: done, blocked, moved, and decisions made.
5. Enforce the gates. If a gate fails (for example no customer commitment by day 3), stop and present the options: narrow the scope, change the segment, or extend. Do not proceed on momentum.
6. Keep one risk list across functions and review it at each gate.
7. On day 14, run the launch readiness review and hand over to `founder-weekly-review` for steady-state operation.

## Gates

| Gate | Day | Passes when |
| --- | --- | --- |
| G1 Problem | 3 | A named segment, evidence from real conversations, and at least one design partner or paid-pilot commitment |
| G2 Foundation | 5 | Entity decision made and filing submitted or scheduled; finance stack chosen; MVP scope and architecture approved |
| G3 Product | 10 | MVP completes the core task end to end; evaluation thresholds met; security review passed |
| G4 Go-to-market | 12 | Website live; CRM and funnel working end to end; first outreach sent; pricing published or quoted |
| G5 Launch | 14 | Pilot customers onboarded; monitoring, incident, support, billing, and bookkeeping routines running |

## Deliverables

- `sprint-plan.md` tailored to the company
- Daily `sprint-status.md`
- Gate review notes
- Launch readiness review
- Post-sprint 30-60-90 day plan

## Founder approval gates

- The tailored plan and any extension of the calendar
- Each gate decision
- Every external, financial, or irreversible action raised by the skills run during the sprint

## Guardrails

- Do not mark a gate passed on synthetic or assumed evidence.
- Do not compress legal or tax steps below what the jurisdiction allows.
- Prefer cutting scope to cutting verification: evaluations, security review, and restore test stay in.
- Record every scope cut in `solofounder/decision-log.md`.
