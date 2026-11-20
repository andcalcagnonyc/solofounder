# Outreach rules by recipient country (draft for review by a locally licensed lawyer; not legal advice)

Checked 2026-11-20. Sender: Relay Desk, Inc. (Delaware C-Corporation).

| Country | Accounts requested | Cold email verdict | Rule found | Source |
| --- | --- | --- | --- | --- |
| United States | 80 | Permitted, with conditions | CAN-SPAM covers business-to-business email with no exception. Each email needs accurate header information, a non-deceptive subject line, disclosure that it is an advertisement, a valid physical postal address, and a working opt-out. The opt-out must work for at least 30 days after sending and be honored within 10 business days. Maximum civil penalty stated: 53,088 USD per email. Hiring a vendor to send does not remove our responsibility. | FTC, "CAN-SPAM Act: A Compliance Guide for Business", https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business (published August 2023; penalty figure edited January 2024; read 2026-11-20) |
| Germany | 40 | Not permitted without prior express consent: EXCLUDED from cold email | Section 7(2) no. 2 UWG treats advertising by electronic mail without the recipient's prior express consent as an unreasonable nuisance in every case. The only exception, section 7(3), is for existing customers whose address was obtained in a sale, for similar own products, with no objection and a clear opt-out notice each time. The text contains no carve-out for business recipients (my reading; lawyer to confirm). | Gesetz gegen den unlauteren Wettbewerb, section 7, https://www.gesetze-im-internet.de/uwg_2004/__7.html (official consolidated text; page shows no version date; read 2026-11-20) |
| Canada | 30 | Permitted only per contact where implied consent can be proven | CASL requires consent, express or implied. The sender carries the burden of proving it. Implied consent by "conspicuous publication" needs both: the address is published without a statement that the person does not want commercial messages, and the message relates to the recipient's business role or duties. Every message needs sender identification and an unsubscribe mechanism; unsubscribe requests honored within 10 business days. | CRTC, "CASL Guidance on Implied Consent", https://crtc.gc.ca/eng/com500/guide.htm (page shows no modification date; read 2026-11-20) |

## Consequences for this campaign
- US (up to 80): email and social touches allowed with the footer in the sequence file.
- Germany (40): no cold email. Assumption until a German lawyer answers: LinkedIn direct messages are treated the same way, so they are also held. The accounts stay on the list for research only.
- Canada (up to 30): a contact enters the sequence only if we store proof: the URL where the address is published, capture date, a screenshot, and a note that no "no solicitation" statement appears. Addresses guessed or inferred by an enrichment tool do not qualify. The final Canadian count will likely be below 30.

## Not verified today (assumptions)
- That CASL applies to a US sender emailing recipients in Canada. Assumed yes; the CRTC page read today does not address it.
- US state laws layered on CAN-SPAM.
- GDPR duties for storing German contacts' personal data in HubSpot, even without emailing them.
- German rules for phone and postal approaches to businesses.

## Questions for lawyers
1. Germany: is there any lawful cold route to business contacts (phone on presumed consent, post, LinkedIn connection request without a pitch)? What GDPR notice is owed if we only store and research contacts?
2. Canada: does CASL reach our US-sent messages; does a LinkedIn message count as a commercial electronic message; is our evidence record sufficient; is any contact detail beyond identification and unsubscribe required in each message?
3. US: any state-level rule that changes the footer or the opt-out handling?
