---
name: support-knowledge-base
description: "This skill should be used when the user asks to \"write a help article\", \"create documentation\", \"build a knowledge base\", \"write an FAQ\", \"write onboarding docs\", \"document the API\", \"update the docs for this release\", or needs customer-facing documentation."
metadata:
  version: "0.1.0"
  area: support
---

# Knowledge Base and Documentation

Maintain documentation that answers customers' questions before they ask, and that the support agent and AI answer engines can rely on.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Product, release notes, ticket categories, search queries with no result

## Workflow

1. Structure the knowledge base: getting started, how-to guides by task, reference, troubleshooting, account and billing, security and data.
2. Prioritize articles by ticket volume and onboarding drop-off.
3. Write each article for one task: outcome, prerequisites, numbered steps, expected result, common errors.
4. Explain AI behavior plainly: what the product can and cannot do, how to review its work, how data is used.
5. Document the API and integrations with working examples.
6. Review every article against the product before publishing and on every release that touches it.
7. Publish through ~~knowledge base and make the content available to the support agent.
8. Measure: views, helpfulness ratings, searches without results, tickets per article topic.

## Deliverables

- Knowledge-base structure
- Articles and API documentation
- Content gap list and review schedule

## Founder approval gates

- Publishing articles
- Statements about data handling or guarantees

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/support/` with dated filenames.

## Hand-offs

- `support-ai-agent` consumes the content
- `marketing-seo-geo` for public discoverability
