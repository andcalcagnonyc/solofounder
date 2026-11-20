# Funnel Stages: Lead to Won

Default funnel. Adjust probabilities after 20 or more closed deals using actual conversion.

| # | Stage | Definition | Exit criteria (buyer evidence) | Automation | Max days |
| --- | --- | --- | --- | --- | --- |
| 0 | Lead | Person or account captured from any source | Fit score above threshold | Create record, enrich, score, start sequence or alert | 2 |
| 1 | Engaged | Replied, booked, signed up, or requested a demo | Meeting scheduled or qualifying answers given | Instant response, booking link, meeting brief | 7 |
| 2 | Qualified | Discovery held; problem, authority, and timing confirmed | Buyer agrees a next step and names decision process | Call summary to CRM, follow-up email, mutual action plan | 14 |
| 3 | Solution validated | Demo or pilot shows the product does the buyer's task | Success criteria met or pilot accepted | Pilot tracker, usage alerts | 21 |
| 4 | Proposal | Proposal and quote delivered | Buyer confirms commercial terms in principle | Proposal generation, reminder tasks | 14 |
| 5 | Negotiation / procurement | Legal, security, and purchasing review | Contract final, signer identified | Questionnaire answers, redline tracking, e-signature | 21 |
| 6 | Closed won | Contract signed or payment received | — | Create billing customer, onboarding kickoff, account brief | — |
| 7 | Closed lost | Buyer declined or went silent past limit | Reason and competitor recorded | Revisit task at 90 days, nurture enrolment | — |

## Required fields by stage

- **Lead**: source, campaign, company, role, country
- **Engaged**: use case, first-response time
- **Qualified**: problem and cost, decision process, timeline, budget range, champion, competitors
- **Solution validated**: success criteria, pilot dates, result
- **Proposal**: amount, term, package, discount and approval
- **Negotiation**: signer, legal status, security status, expected signature date
- **Closed**: won or lost reason, contract start, renewal date

## Self-serve variant

Visitor → Sign-up → Activated (first successful task) → Paying → Expanded. Product-qualified leads (activation plus fit) enter the sales funnel at stage 1.

## Core metrics

Conversion by stage, time in stage, win rate, average deal value, sales-cycle length, pipeline coverage (open pipeline divided by target), lead-response time, and source-to-revenue attribution.
