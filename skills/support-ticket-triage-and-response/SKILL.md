---
name: support-ticket-triage-and-response
description: "This skill should be used when the user asks to \"triage my tickets\", \"answer this customer\", \"draft a support reply\", \"handle this complaint\", \"escalate this bug\", \"clear my support inbox\", or needs incoming customer requests classified and answered."
metadata:
  version: "0.1.0"
  area: support
---

# Ticket Triage and Response

Classify every incoming request, answer what can be answered, and escalate the rest with everything the next person needs.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Ticket queue, customer and account context, knowledge base, known issues

## Workflow

1. Read the queue; classify each ticket by category, severity, customer tier, and sentiment; detect duplicates and incident clusters.
2. Order work by service commitment and severity.
3. Research each ticket: account history, product logs, known issues, documentation.
4. Draft the reply: answer first, clear steps, honest status when there is no fix yet, and the next update time.
5. For bugs, reproduce where possible and write the engineering report: steps, expected and actual, evidence, impact.
6. For feature requests, log with customer and context to the feedback store.
7. For billing, legal, security, or privacy matters, route to the matching skill and tell the customer what happens next.
8. Close with confirmation; tag the root cause; record whether documentation would have prevented the ticket.

## Deliverables

- Triage summary of the queue
- Draft or sent replies
- Bug reports and feature-request entries

## Founder approval gates

- Sending replies until a standing rule is approved per category
- Refunds, credits, and exceptions
- Any admission of fault or liability

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/support/` with dated filenames.

## Hand-offs

- `eng-build-workflow` for bugs
- `product-analytics-and-feedback` for requests
- `ops-incident-response` for clusters
