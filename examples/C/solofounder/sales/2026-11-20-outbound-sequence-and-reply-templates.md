# Outbound sequence and reply templates (drafts; nothing is sent without founder approval)

Segments: US and proven-consent Canada only. About three weeks, six touches. Fields in double braces are filled per contact or by the founder. No metric, customer name, or result appears unless the founder supplies and verifies it.

## Product claims to confirm before any send (assumptions)
- The profile only says the agent resolves tickets and can refund up to 50 USD without approval. The lines about configurable limits and per-action approval in touches 1 and 3 and in the objection reply are my assumption about the product. Marcus: confirm or correct each.

## Footer on every email
This is a sales email from Relay Desk, Inc., {{postal_address}}. Not relevant? Reply "unsubscribe" or use this link and you will not hear from us again: {{unsubscribe_link}}

## Touch 1: day 1, email
Subject A: {{trigger_short}} at {{account_name}}
Subject B: Support tickets at {{account_name}}

Hi {{first_name}},

{{opening_line}}

Relay Desk is an AI agent that resolves e-commerce support tickets end to end, rather than drafting replies for a person to send. You set the limits it works within.

Would it be useful if I sent a two-minute walkthrough of how it handles an order-status ticket?

Marcus, founder, Relay Desk

## Touch 2: day 3, LinkedIn connection request, no pitch
Hi {{first_name}}, I work on support automation for e-commerce brands and follow {{account_name}}. Glad to connect.
(Canada: connection request only, with no commercial content, until the lawyer answers the CASL question.)

## Touch 3: day 6, email, new reason: control
Subject: Who approves what

Hi {{first_name}},

The usual worry about an agent that acts is control. In Relay Desk you decide which actions it may take alone and which wait for a person, including a money limit on refunds.

If you tell me the two ticket types that eat most of your team's time, I will show you how each would be configured.

Marcus

## Touch 4: day 10, email, new reason: proof
Subject: How {{similar_brand_type}} brands use it

Hi {{first_name}},

{{proof_point: founder to supply, verified, with the customer's permission}}

Worth a 15-minute call? {{booking_link}}

Marcus

## Touch 5: day 14, LinkedIn message (US only)
{{first_name}}, I sent a couple of notes about support tickets at {{account_name}}. If someone else owns this, who should I ask?

## Touch 6: day 20, email, close the loop
Subject: Closing the loop

Hi {{first_name}},

I will stop here. If ticket volume becomes a priority, reply with "later" and a month, and I will write then and not before.

Marcus

## Reply templates
- Interested: "Thanks, {{first_name}}. Here are two times: {{slot_1}}, {{slot_2}}, or pick one here: {{booking_link}}. To prepare: which helpdesk do you use, and roughly how many tickets a month?" Then create the deal in HubSpot and hand off to `sales-qualification-and-discovery`.
- Referral: "Thank you. I will write to {{referral_name}} and mention you pointed me their way, unless you would rather I did not." Add the new contact; rerun the country check before any send.
- Objection, AI acting alone: "Fair concern. Every action has a limit you set, and any action can be set to wait for approval. Happy to show the controls before anything else."
- Objection, already have a tool: "Understood. Which part still takes your team the most manual time?"
- Not now: "No problem. I will check back in {{month}} and not before." Set a HubSpot task; stop the sequence.
- Unsubscribe: "Done. You will not hear from us again." Add to the suppression list the same day (legal outer limit is 10 business days in the US and Canada).
