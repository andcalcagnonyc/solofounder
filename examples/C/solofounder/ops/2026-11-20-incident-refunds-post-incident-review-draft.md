# Post-incident review (blameless), INC-2026-11-20-01: DRAFT, incident still open

## Summary
After a prompt change on the morning of 2026-11-20, the support agent issued 50 USD refunds on tickets that did not ask for one. Reported at declaration: 61 refunds across 9 customers. Final numbers: TBD.

## Impact
- Customers affected: 9 reported of 38; full check of all 38: TBD
- Erroneous refunds: 61 reported; amount up to 3,050 USD if each was 50 USD; verified total: TBD
- Duration: TBD (deploy time to stop time)
- Data exposure: none reported. Assumption, to confirm.

## Timeline
See `2026-11-20-incident-refunds-timeline-and-status.md`.

## What the evidence shows (fill in; do not conclude before then)
| Hypothesis | Evidence that would support it | Status |
| --- | --- | --- |
| H1: the prompt change caused the behaviour | First bad refund follows the deploy; prompt diff touches refund guidance; replay of the 61 tickets refunds on the new prompt and not on the old | Reported by founder; unverified |
| H2: another change the same morning (model version, tool config, limit setting) | Deploy and config history shows a second change | Not checked |
| H3: the behaviour existed before at a lower rate | Unrequested refunds in the prior 7 days | Not checked |

## Contributing factors to examine (system, not people)
- A prompt change reached all customers at once, with no staged rollout
- No evaluation case blocked "refund on a ticket with no refund request"
- The only control on refunds was the 50 USD per-refund limit; no code check for a refund request, no cap on count per customer per hour
- No alert on refund volume; detection path and time to detect: TBD
- All refunds at exactly the limit suggests the limit acted as a target: to verify

## What worked
TBD after closing.

## Corrective actions (owners and dates are proposals for Marcus to confirm)
| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Keep refunds on "approval required" until actions 2 to 5 are done | Marcus | Now |
| 2 | Add the 61 tickets to the eval set as "must not refund"; add requested-refund cases as "must refund" | Marcus, Claude drafts via `eng-evals` | 2026-11-24 |
| 3 | Code-level guard: refund tool refuses unless the ticket contains a refund request and an eligible order | Marcus | 2026-11-27 |
| 4 | Caps: refunds per customer per hour and per day; breach pauses the action and pages Marcus | Marcus | 2026-11-27 |
| 5 | Datadog monitor on refund count and refund-to-ticket ratio per customer | Marcus, via `ops-observability` | 2026-11-24 |
| 6 | Release gate: prompt changes pass evals, then go to one customer or a small share of traffic first | Marcus, via `eng-code-review-and-release` | 2026-12-04 |
| 7 | Document and test the kill switch | Marcus | 2026-11-24 |
| 8 | Check customer contracts, insurance, and payment-provider terms for notice duties | Marcus with lawyer, via `legal-commercial-contracts` | 2026-11-23 |
