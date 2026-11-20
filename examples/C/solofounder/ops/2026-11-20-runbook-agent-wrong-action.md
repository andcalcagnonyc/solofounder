# Runbook: the agent took an action it should not have (refunds, replies, account changes)

1. Declare. Open a timeline file in `solofounder/ops/`, set severity. SEV1 if money moved or the behaviour is ongoing.
2. Stop the action for ALL customers: kill switch, or set the no-approval limit to 0. Do not wait for a diagnosis.
3. Roll back the last change (prompt, model, tool config) in GitHub and deploy.
4. Confirm the stop: zero new actions of that type for 30 minutes in Datadog or logs.
5. Export every action of that type from change time to stop time, for all customers. Classify each as legitimate, erroneous, or unclear.
6. Draft customer notices. Founder approves before anything is sent.
7. Do not reverse actions that touch customers' shoppers or money without the customer's instruction.
8. Investigate with evidence: diff, deploy history, traces, replay on old versus new version.
9. Check notice duties: contracts, insurer, payment provider, regulators if personal data is involved.
10. Verify recovery, close, and write the blameless review within 5 working days.
11. Add the failing cases to evals; add or tune the alert that would have caught it.

## Additions from INC-2026-11-20-01 (proposed)
- Eval: tickets with no refund request must produce zero refund calls. Blocks release on any failure.
- Test: refund tool rejects calls without a detected refund request and eligible order.
- Alert: refund count or refund-to-ticket ratio per customer above baseline (threshold TBD from the last 30 days of data).
- Limit: per-customer hourly and daily refund caps (values TBD with Marcus).
