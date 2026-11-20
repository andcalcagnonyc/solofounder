# Impact Assessment, Breach Procedure, and Data-Subject Request Procedure - Portside Logic Pte. Ltd.

_Date: 2026-11-20. DRAFT for lawyer review. No notification to a regulator or customer is made without founder approval of that specific notification._

## A. Impact assessment (screening + transfer risk)
**Is a formal DPIA required?** Under GDPR that duty sits with the controller (the forwarder); Portside must assist. On the facts given the processing looks low risk: ordinary business contact details, no special categories known, no decisions about individuals. ASSUMPTION pending answers: documents carry no identity-document numbers, no private individuals' home addresses, and no criminal or health data. A screening record is still worth keeping because EU customers will ask for it.

| Risk | Likelihood | Severity | Mitigation | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| Personal data sent to a US model provider that retains or trains on it | [depends on terms] | Medium | Zero-retention or no-training terms; record in provider table | Founder | Open |
| Access by US authorities to data hosted in the US | Low | Medium | Encryption at rest and in transit; transfer assessment; consider EU region for EU customers | Founder / engineering | Open |
| Documents contain more personal data than expected | Medium | Medium | Sample documents from each pilot; redact fields the model does not need before the prompt | Engineering | Open |
| Personal data lingering in prompt logs and backups | Medium | Low | 30-day log retention, log redaction | Engineering | Open |
| Wrong flag leads to a wrong customs filing | Medium | Medium (commercial, not privacy) | Human review before filing; contract disclaimer | Founder | To confirm |
| One customer's documents exposed to another | Low | High | Tenant isolation, access tests | Engineering | Open |
| Single-person company: no backup for incident response | Medium | Medium | Written procedure, named alternate contact | Founder | Open |

**Transfer assessment outline (to complete with counsel):** data and volumes; route EU -> Singapore -> US; tool for each leg; each provider's certification or clauses; technical measures; conclusion and review date.

## B. Incident and breach procedure
1. **Detect and log (hour 0).** Anyone who suspects an incident records time, what was seen, and systems affected in the breach log.
2. **Contain (hours 0-4).** Revoke keys, isolate systems, preserve logs. Hand to `ops-incident-response`.
3. **Assess (within 24 hours).** Whose data, which customers, how many people, what categories, is it still exposed.
4. **Notify customers.** For data processed on a customer's behalf, tell the customer without undue delay (PROPOSED internal target: 24 hours from awareness; use the shorter of this and the contract) so an EU controller can meet its own 72-hour deadline to its supervisory authority. Founder approves each message before it is sent.
5. **Notify regulators, only where Portside itself must.** For Portside's own controller data under the PDPA: assess promptly, and if the breach is notifiable (significant harm, or 500 or more individuals) notify the PDPC within 3 days of that assessment and affected individuals where required. Founder approves; Singapore counsel reviews first where time allows.
6. **Close.** Root cause, fixes, update this assessment and the answer bank.

## C. Data-subject request procedure
1. Log every request with date received and channel.
2. If it concerns data in a customer's documents: do not answer on the merits; forward to the customer within 2 working days and assist as the DPA requires.
3. If it concerns Portside's own data: verify identity, locate the data (CRM, email, billing), respond within one month (GDPR standard, used as the baseline; PDPA timing to confirm).
4. Record the outcome and what was disclosed, corrected, or deleted.

## D. Review
Next review: February 2027, and on any change of model provider, cloud region, data source, or if the product starts acting without human review.
