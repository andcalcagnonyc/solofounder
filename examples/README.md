# Example Outputs

These are the unedited outputs of the scenario tests described in [`tests/RESULTS.md`](../tests/RESULTS.md). Each was produced by a fresh Claude session following one skill for an invented company.

**Everything here is synthetic.** The companies, founders, customers, and figures do not exist. The legal, tax, and privacy content was generated during testing, was not reviewed by any professional, may be wrong or out of date, and is not advice. It is published to show what the skills produce, including their flaws: four graded criteria failed, and those failures are visible in these files.

| Run | Skill | Scenario | Response | Working folder |
| --- | --- | --- | --- | --- |
| A1 | `start` | Italian founder, US angels, not yet incorporated | [A1.md](A1.md) | [A/solofounder](A/solofounder) |
| A2 | `legal-entity-formation` | Same company: where and how to incorporate | [A2.md](A2.md) | [A/solofounder/legal](A/solofounder/legal) |
| B1 | `finance-setup` | Singapore company, EU customers | [B1.md](B1.md) | [B/solofounder/finance](B/solofounder/finance) |
| B2 | `legal-privacy-and-ai-compliance` | Same company: EU privacy and AI rules | [B2.md](B2.md) | [B/solofounder/legal](B/solofounder/legal) |
| C1 | `sales-prospecting-automation` | Delaware company, outbound to US, Germany, Canada | [C1.md](C1.md) | [C/solofounder/sales](C/solofounder/sales) |
| C2 | `ops-incident-response` | Same company: agent issuing refunds in error | [C2.md](C2.md) | [C/solofounder/ops](C/solofounder/ops) |
| D1 | `legal-entity-formation` | "Incorporate my startup today", no location given | [D1.md](D1.md) | none (the session stopped to ask) |

Paths inside the files that begin `examples/` refer to this folder.
