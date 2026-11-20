---
name: sales-prospecting-automation
description: "This skill should be used when the user asks to \"find leads\", \"build a prospect list\", \"write cold emails\", \"set up an outbound sequence\", \"automate my outreach\", \"enrich these leads\", \"book more meetings\", or needs lead sourcing and outreach automated."
metadata:
  version: "0.1.0"
  area: sales
---

# Automated Prospecting and Outreach

Run a compliant outbound engine that finds accounts matching the ICP, researches each one, sends relevant multi-step outreach, and books meetings with minimal founder time.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- ICP, trigger events, messaging, sending domains and tools
- Suppression list and existing customers

## Workflow

1. Prepare sending infrastructure: separate sending domain, authentication records, warm-up, volume limits per mailbox.
2. Check the outreach rules for each recipient country (consent, legitimate interest, required disclosures, opt-out) and exclude countries or segments where cold outreach is not permitted.
3. Build the account list from ICP filters and trigger events; identify the buying committee per account.
4. Enrich and verify contacts through ~~enrichment; remove invalid, duplicate, suppressed, and customer records.
5. Research each account and write one specific opening line tied to an observable fact.
6. Write the sequence: several touches across email and social over about three weeks, each adding a new reason to reply, with a clear and small ask.
7. Load into the sequencing tool in batches; test subject lines and openers on small samples before scaling.
8. Triage replies daily: interested, referral, objection, not now, unsubscribe. Draft responses, book meetings, and update the CRM.
9. Report weekly: delivery, reply, positive-reply, and meeting rates per segment; retire messages that underperform.

## Deliverables

- Prospect lists with research notes
- Sequences and reply templates
- Sending setup checklist
- Weekly outbound report

## Founder approval gates

- First send of every new sequence and every list
- Daily volume limits
- Any personalised claim about the prospect

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/sales/` with dated filenames.

## Hand-offs

- `sales-qualification-and-discovery` for booked meetings
- `sales-crm-and-funnel` for record updates
