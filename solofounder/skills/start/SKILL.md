---
name: start
description: "This skill should be used when the user says \"start solofounder\", \"set up my company profile\", \"I want to launch an AI company\", \"where do I begin\", \"onboard me\", \"update my company profile\", or invokes any solofounder skill before a company profile exists. It runs the founder intake, asks where the HQ will be, and routes to the right skills."
metadata:
  version: "0.1.0"
  area: core
---

# Start: Founder Intake and Company Profile

Create the single source of truth every other solofounder skill reads: `solofounder/company-profile.md`. Legal, tax, accounting, privacy, employment, and outreach rules all depend on where the company and its customers are, so collect that first and never assume it.

## When to run

- First use of the plugin.
- Any time another skill finds the profile missing or a required field empty.
- When facts change: new HQ, new entity, new market, new pricing, new tools.

## Workflow

### 1. Intake

Ask in small batches (use a multiple-choice question tool where available) and accept "not decided yet". Skip anything the founder has already stated.

**Batch 1: Location and legal (always ask)**

1. Where will the company HQ be? Country, plus state, province, or city where relevant.
2. Is the company already incorporated? If yes: legal form, registration date, financial year-end. If no: is the founder open to incorporating in a different country from where they live?
3. Founder citizenship and country of tax residence.
4. Countries of the first customers, and of any employees or contractors.

**Batch 2: Company**

5. One sentence: what the product does, for whom.
6. Company type: Applied AI (AI embedded in a product or workflow) or Agentic AI (autonomous agents completing tasks), and the unit of work it performs.
7. Stage: idea, prototype, pilot customers, revenue.
8. Funding plan: bootstrapped, angels, venture, grants; amount and timing if known.

**Batch 3: Operating constraints**

9. Launch target date and weekly hours available.
10. Budget for tools and services in the first 90 days, and currency.
11. Tools already in use (see `CONNECTORS.md` categories).
12. Languages for customer-facing material.
13. Approval preference: approve everything, or approve only external, financial, and irreversible actions.

### 2. Build the profile

1. Write `solofounder/company-profile.md` from `references/company-profile-template.md`. Mark unknown fields `TBD` and list them under Open Questions.
2. Create `solofounder/decision-log.md` with the first entries (HQ choice, company type).
3. Derive and record the jurisdiction set: incorporation, tax residence, customer countries, worker countries. State which professional reviews will be needed (lawyer, accountant, tax adviser) and in which countries.
4. Flag facts that change the plan materially, for example: founder living in a different country from the entity, regulated sector, customers in the EU, public-sector buyers, health or financial data.
5. Show the founder the profile and confirm it.

### 3. Route

Recommend the next step based on stage:

| Situation | Next skill |
| --- | --- |
| New company, wants to launch fast | `launch-sprint` |
| Idea not validated | `product-discovery-and-validation` |
| Not incorporated | `legal-entity-formation` |
| Incorporated, no finance setup | `finance-setup` |
| Product built, no customers | `marketing-positioning-and-messaging`, then `sales-icp-and-playbook` |
| Operating, wants cadence | `stack-and-automation-setup`, then `founder-weekly-review` |

## Deliverables

- `solofounder/company-profile.md`
- `solofounder/decision-log.md`
- Jurisdiction set and list of professional reviews needed
- Recommended next skill

## Founder approval gates

- The completed profile before any other skill relies on it
- Any later change to HQ country, legal form, or approval rules

## Guardrails

- Never infer the HQ country from language, currency, time zone, or name. Ask.
- Do not store identity numbers, bank details, or passwords in the profile.
- Legal, tax, and accounting outputs across the plugin are drafts for review by locally licensed professionals. Say so once, plainly, when the profile is created.
- If file storage is not available in the session, output the profile in full and ask the founder to keep it in the project knowledge and supply it in later sessions.
