# solofounder

**A Claude plugin that gives one founder the skills of a full company.**

`solofounder` packages 57 skills that let a single founder launch and run an Applied AI or Agentic AI company end to end with Claude: legal, finance and accounting, marketing, sales, product, engineering and QA, cloud operations, and customer support. A 14-day launch sprint ties them together.

The plugin is jurisdiction-aware. The first thing it does is ask where the HQ will be, and every legal, tax, accounting, privacy, employment, and outreach skill works from that answer instead of assuming a country.

## Install

**Claude Code**

```
/plugin marketplace add andcalcagnonyc/solofounder
/plugin install solofounder@solofounder
```

**Claude desktop app**: in Customize > Plugins, add a marketplace from the GitHub repo `andcalcagnonyc/solofounder`, then install `solofounder`.

Then say: `start solofounder`.

## How it works

1. **`start`** runs the founder intake (HQ country, legal form, tax residence, customer countries, stage, budget, tools) and writes `solofounder/company-profile.md`.
2. Every other skill reads that profile first, saves its deliverables under `solofounder/<area>/`, and logs decisions in `solofounder/decision-log.md`.
3. **`launch-sprint`** schedules the skills into a 14-day plan with five gates (Problem, Foundation, Product, Go-to-market, Launch).
4. **`stack-and-automation-setup`** connects the tool stack and schedules recurring work; **`founder-weekly-review`** gives one page per week across all functions.

Each skill has the same structure: purpose, inputs, numbered workflow, deliverables, founder approval gates, guardrails, and hand-offs to the next skills.

## Skills

| Area | Skills |
| --- | --- |
| **Core** (4) | `start` · `launch-sprint` · `stack-and-automation-setup` · `founder-weekly-review` |
| **Legal** (9) | `legal-entity-formation` · `legal-founder-equity-and-cap-table` · `legal-fundraising` · `legal-corporate-governance` · `legal-commercial-contracts` · `legal-privacy-and-ai-compliance` · `legal-hiring-and-contractors` · `legal-ip-and-trademarks` · `legal-compliance-calendar` |
| **Finance & Accounting** (7) | `finance-setup` · `finance-bookkeeping-and-close` · `finance-invoicing-and-collections` · `finance-payables-and-payroll` · `finance-tax-and-statutory-compliance` · `finance-planning-and-runway` · `finance-fundraising-and-investor-relations` |
| **Marketing** (7) | `marketing-positioning-and-messaging` · `marketing-brand-and-design` · `marketing-website` · `marketing-seo-geo` · `marketing-demand-generation` · `marketing-communications` · `marketing-field-and-partners` |
| **Sales** (6) | `sales-icp-and-playbook` · `sales-crm-and-funnel` · `sales-prospecting-automation` · `sales-qualification-and-discovery` · `sales-proposal-and-close` · `sales-pipeline-review-and-forecast` |
| **Product** (6) | `product-discovery-and-validation` · `product-strategy-and-roadmap` · `product-requirements-and-specs` · `product-ux-design` · `product-pricing-and-packaging` · `product-analytics-and-feedback` |
| **Engineering & AI** (8) | `eng-architecture` · `eng-agent-design` · `eng-data-and-retrieval` · `eng-build-workflow` · `eng-evals` · `eng-qa-testing` · `eng-security-and-ai-safety` · `eng-code-review-and-release` |
| **Cloud Ops** (5) | `ops-infrastructure-and-deploy` · `ops-observability` · `ops-incident-response` · `ops-cost-and-finops` · `ops-security-and-reliability` |
| **Support** (5) | `support-setup` · `support-ai-agent` · `support-ticket-triage-and-response` · `support-knowledge-base` · `support-customer-success` |

## The 14-day sprint

| Days | Focus | Gate |
| --- | --- | --- |
| 1-3 | Profile, entity decision, customer evidence, MVP scope | G1 Problem |
| 4-5 | Specification, architecture, formation filing, finance stack, repo | G2 Foundation |
| 6-10 | Build, evaluate, test, harden, release | G3 Product |
| 11-12 | Sales playbook, CRM and funnel, outbound, website live | G4 Go-to-market |
| 13-14 | Support, billing, pilot onboarding, operating routines | G5 Launch |

Full plan: [`skills/launch-sprint/references/14-day-plan.md`](skills/launch-sprint/references/14-day-plan.md).

**What two weeks does and does not cover.** The work Claude and the founder control fits in the sprint. Steps on third-party clocks (company registration, bank account, tax registrations, trademarks, enterprise procurement) take from a day to several weeks depending on the country; the sprint starts them on day 1 and runs everything else in parallel.

## Tools

Skills refer to tools by category (`~~CRM`, `~~accounting system`, `~~helpdesk`, and so on) so the plugin works with any stack. See [`CONNECTORS.md`](CONNECTORS.md). Without a connected tool, a skill produces ready-to-use files and manual steps.

## Safety model

- **Founder approval gates.** Every skill lists the decisions it will not take alone. Claude asks before anything that contacts someone outside the company, spends money, or cannot be undone. Nothing is filed, signed, paid, or sent without approval of that specific action.
- **Drafts, not advice.** Legal, tax, and accounting outputs are drafts for review by locally licensed professionals. Each one cites its sources and lists the questions to put to the reviewer. This plugin does not provide legal, tax, or accounting advice.
- **No invented facts.** Skills mark assumptions and do not fabricate metrics, customers, prospects, or citations.

## Validation

The plugin ships with a test suite and published results on synthetic data: structural validation, requirement coverage, skill-routing accuracy, and scenario-based behaviour tests. See [`tests/RESULTS.md`](tests/RESULTS.md) for KPIs, method, and limits.

```
python3 tests/validate_structure.py
python3 tests/routing_lexical.py
```

| KPI (v0.1.0, synthetic data) | Result |
| --- | --- |
| Structural checks | 1,111 / 1,111 |
| Requirement coverage | 54 / 54 |
| Skill routing, 114 synthetic requests | 100% top-1 (lexical baseline 64.9%) |
| Behaviour criteria, 7 scenario runs | 47 / 51 (92.2%) |
| Unapproved external actions, assumed jurisdictions | 0 |

Seven scenario runs cover 6 of the 57 skills, each run once and graded by a model; the results file lists the four failures and the limits in full.

## Example outputs

[`examples/`](examples/) holds the unedited outputs of the scenario tests: a company profile, an entity decision memo, a finance setup, a privacy and AI compliance pack, an outbound campaign, and an incident response, all for invented companies.

## Repository layout

```
.claude-plugin/   plugin.json, marketplace.json
skills/           57 skills, each skills/<name>/SKILL.md (+ references/)
tests/            validators, synthetic cases, scenarios, rubric, results
examples/         outputs of the scenario tests (synthetic)
CONNECTORS.md     tool categories and placeholders
```

## License

MIT. Author: Andrea Calcagno.
