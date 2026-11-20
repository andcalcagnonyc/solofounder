# INC-2026-11-20-01: agent issuing unrequested 50 USD refunds

- Severity: SEV1 (proposed). An AI agent is taking unauthorised financial actions on customers' accounts and impact was still running when reported.
- Status: OPEN, not yet stabilized (no confirmation that the refund action is off)
- Incident lead: Marcus O. Scribe and drafts: Claude (no tool is connected; Claude cannot act in GitHub, Datadog, Stripe, or Intercom)
- Reported impact: 61 refunds across 9 customers "so far". Up to 3,050 USD if each was exactly 50 USD (to verify).

## Timeline (all times TBD until Marcus supplies them; none are invented)
| Time (state time zone) | Event | Evidence |
| --- | --- | --- |
| TBD, morning 2026-11-20 | Prompt change deployed | GitHub commit / deploy log: TBD |
| TBD | First unrequested refund | Refund log: TBD |
| TBD | Problem noticed; by whom and how | TBD |
| TBD | Reported to Claude: 61 refunds, 9 customers | Founder message |
| 2026-11-20 | Incident declared SEV1; stabilization steps issued | This file |
| TBD | Refund action disabled | TBD |
| TBD | Prompt change reverted and deployed | TBD |
| TBD | Stop confirmed: zero new agent refunds for 30 minutes | Datadog / logs |
| TBD | First customer notice sent (after approval) | TBD |

## Stabilization steps (do in this order, before any diagnosis)
1. Turn off the agent's refund action for ALL 38 customers, not only the 9. Use the kill switch, or set the no-approval refund limit from 50 USD to 0 so every refund waits for a person. If neither exists, revoke the agent's refund credential or pause the agent.
2. Revert the morning's prompt change in GitHub (`git revert <commit>` on the prompt commit, or redeploy the previous prompt version) and deploy.
3. Confirm the stop: no new agent-issued refunds for 30 minutes. Record the time above.
4. Keep the refund action off after the revert. It returns only after the checks in the review pass and Marcus approves.

Do NOT yet: reverse or re-charge any refund, delete logs, or contact shoppers. Those are destructive or external and need a decision per customer.

## Affected customers and actions (to pull once stable)
Export every agent-issued refund from the deploy time to the stop time, for all customers: refund ID, customer, ticket ID, shopper, amount, currency, timestamp, ticket text, agent reasoning trace. Mark each: refund requested (legitimate) / not requested / unclear. Compare with the same weekday last week for a baseline.

## Status updates (internal log)
| # | Time | Update |
| --- | --- | --- |
| 1 | TBD | Declared. 61 refunds, 9 customers reported. Stabilization in progress. Next update in 30 minutes. |

Cadence: internal every 30 minutes until stable, then every 2 hours until closed. Customers: first notice within 1 hour of confirmed stop, follow-up when the per-customer list is ready, final when the review is done.

## Recovery checks before closing
- Zero unrequested refunds since the revert, checked against every agent refund attempt
- Replay of the 61 tickets against the reverted prompt in a test environment: no refund on tickets that did not ask for one
- Refund-rate monitor live in Datadog
- All 9 customers have received their list and a remediation decision
