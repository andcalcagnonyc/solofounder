# Applicability Memo and Obligations Register - Portside Logic Pte. Ltd.

_Date: 2026-11-20. DRAFT for review by a lawyer licensed in Singapore and by an EU-qualified data-protection lawyer. Not legal advice. The AI classification in section 3 is a proposal that needs founder approval._

## 1. Facts relied on
Singapore private limited company; pilot customers (freight forwarders) in Singapore, the Netherlands, and Germany; product reads shipping documents and flags customs errors; documents contain names and contact details of shippers' staff; model provider and cloud are hosted in the United States; provider names, contract terms, and whether a human always reviews a flag are not known.

## 2. Which regimes apply, and which governs
| Regime | Applies? | Why | Governs what |
| --- | --- | --- | --- |
| EU GDPR (Regulation 2016/679) | Yes, at least through contract | Dutch and German forwarders are controllers established in the EU; Portside processes personal data for them (ASSUMPTION: Portside is their processor). They need an Article 28 processing agreement with Portside and a transfer mechanism to send data to Singapore and onward to the US. Whether GDPR also binds Portside directly under Article 3(2) is an open legal question (see Q1). | Data in EU customers' documents |
| Dutch and German national law (UAVG, BDSG) | Indirectly | Applies to the customers; may shape what they demand from Portside. | EU customer requirements |
| Singapore PDPA 2012 | Yes | Portside is an organisation in Singapore. For customer documents it acts for another organisation (data intermediary): security, retention limits, and prompt breach notice to the customer. For its own data (customer contacts, website, any staff) the full obligations apply, including appointing a DPO and the overseas-transfer rule for the US hosting. | All data Portside holds; Singapore customers |
| EU AI Act (Regulation 2024/1689, as amended by the Digital Omnibus in force 27 July 2026) | Yes, in scope as a provider | It reaches providers that place AI systems on the EU market or put them into service there, wherever established (Article 2; to confirm against the consolidated text). | The product as offered to NL and DE customers |
| Singapore AI rules | No binding horizontal AI statute known to me; voluntary governance frameworks exist (to confirm with IMDA and PDPC). PDPC's advisory guidelines on personal data in AI recommendation and decision systems (1 Mar 2024) are the reference. | Good practice |
| United States law | Not as a privacy regime over this data on the facts given; US hosting matters as the destination of transfers. | Transfer assessment |
| Sector rules | Customs law governs the forwarders' filings, not Portside's processing. No sector privacy rule identified. | - |

**Where they differ:** GDPR is the stricter regime on the points that matter here (no exemption for business contact details, 72-hour controller breach deadline, transfer rules). PROPOSAL: run one baseline to the GDPR standard for all customers, and add the PDPA-specific items (DPO, PDPC notification) on top. Whether Singapore's exclusion for business contact information removes some of this data from the PDPA is a question for Singapore counsel (Q5); it does not help under GDPR.

## 3. Proposed AI Act classification (needs your approval)
- **Role:** provider of an AI system; customers are deployers. Portside is a downstream user of a third-party general-purpose model, not a provider of one (ASSUMPTION: no substantial fine-tuning that is then placed on the market).
- **Prohibited practices:** none apparent.
- **High-risk (Annex III / Annex I):** PROPOSED NOT HIGH-RISK. The system checks commercial documents for private forwarders; it is not used by customs or border authorities, does not evaluate individuals, and is not a safety component. This fails if a customs authority uses it, or if it scores or profiles named persons.
- **Transparency (Article 50):** applies if users interact with the system conversationally or if it generates text outputs within the Article's scope. Depends on the interface (Q7). These duties applied from 2 August 2026, with a grace period to 2 December 2026 for machine-readable marking by systems already on the market.
- **AI literacy (Article 4):** applies now, in the relaxed form: take and document measures that support AI literacy for people operating the system.
- **Dates:** Annex III high-risk obligations were postponed to 2 December 2027 and Annex I to 2 August 2028; relevant only if the classification changes.

## 4. Obligations register
| # | Obligation | Regime | Owner | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Signed processing agreement with each EU customer | GDPR Art. 28 | Founder + `legal-commercial-contracts` | Unknown - ask | Signed DPA |
| 2 | Transfer mechanism EU to Singapore (standard contractual clauses, controller-to-processor module, are the usual tool; I am not aware of an EU adequacy decision for Singapore - confirm on the Commission's list) | GDPR Ch. V | Founder + EU counsel | Open | Signed clauses, transfer assessment |
| 3 | Onward transfer Singapore to US providers: sub-processor terms matching the customer DPA; check each provider's Data Privacy Framework certification or sign clauses with it | GDPR Ch. V; PDPA transfer rule | Founder | Open | Provider DPAs, certification record |
| 4 | Customer authorisation of sub-processors, with change notice | GDPR Art. 28(2) | Founder | Open | Sub-processor list |
| 5 | Record of processing as processor | GDPR Art. 30(2) | Claude drafts, founder owns | Drafted | Processing register |
| 6 | Security measures appropriate to risk | GDPR Art. 32; PDPA protection obligation | `eng-security-and-ai-safety` | Open | Control list |
| 7 | Breach: tell the customer without undue delay; PDPC within 3 days of assessing a notifiable breach of Portside's own data | GDPR Art. 33(2); PDPA | Founder | Procedure drafted | Breach log |
| 8 | Help customers with data-subject requests and impact assessments | GDPR Art. 28(3) | Founder | Procedure drafted | Request log |
| 9 | Delete or return data at contract end; retention limits | GDPR Art. 28(3)(g); PDPA retention | Engineering | Schedule drafted | Deletion logs |
| 10 | Appoint a DPO and publish business contact details (registration route to confirm) | PDPA | Founder | Open | Appointment record |
| 11 | Privacy notice for Portside's own controller data | GDPR Arts. 13-14 if applicable; PDPA notification | Founder | Drafted, not published | Notice |
| 12 | EU representative | GDPR Art. 27 | EU counsel | Depends on Q1 | - |
| 13 | AI classification memo and review trigger | AI Act | Founder | Proposed | This memo |
| 14 | AI literacy measures | AI Act Art. 4 | Founder | Open | Training note |
| 15 | Provider commitments: no training on customer data, retention, region | Contract | Founder | Unknown - ask | Provider terms on file |
| 16 | Quarterly review, and on any change of model provider, data source, or product capability | Internal | Founder | Scheduled Feb 2027 | Review note |

## 5. Questions for the lawyers
1. (EU) Is Portside directly subject to GDPR under Article 3(2), or only bound through Article 28 contracts and transfer clauses? If directly subject, must it appoint an Article 27 representative, and where?
2. (EU) Which transfer tool should EU customers use for Portside, and does it change if Q1 is yes?
3. (EU) Is reliance on the EU-US Data Privacy Framework for the US providers acceptable to German customers while the appeal against the General Court's 3 September 2025 judgment is pending? I have not checked the appeal's status after December 2025.
4. (EU) Do we agree the system is not high-risk, and does Article 50 reach our outputs?
5. (SG) Does the business-contact-information exclusion cover names and contact details in shipping documents? Are we a data intermediary for all customer data?
6. (SG) What contract terms satisfy the transfer limitation obligation for our US providers?
7. (Both) Should customer contracts carry one global DPA or separate EU and Singapore schedules?

## 6. Sources
- Lewis Silkin, "The Digital Omnibus on AI enters into force today", 27 Jul 2026 (secondary; OJ reference L 2026/1744): https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo
- WilmerHale, "European Court of Justice to Review Challenge to EU-U.S. Data Privacy Framework", 1 Dec 2025 (secondary): https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law-blog/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework
- PDPC, "The Distinction between Organisations and Data Intermediaries and Why It Matters" (fetched 20 Nov 2026, undated): https://pdpc.gov.sg/the-distinction-between-organisations-and-data-intermediaries-and-why-it-matters
- Chambers, Data Protection & Privacy 2026 - Singapore, Law and Practice (2026, secondary): https://chambers.com/practice-guides/guides/data-protection-privacy-2026/singapore/law-and-practice
- Not opened today; GDPR and AI Act article references are from general knowledge and must be checked against: Regulation (EU) 2016/679 and Regulation (EU) 2024/1689 consolidated texts on EUR-Lex; Commission Implementing Decision (EU) 2021/914 (standard contractual clauses); EDPB Guidelines 3/2018 on territorial scope (link failed to load); Commission adequacy-decision list; Data Privacy Framework participant list; PDPA 2012 on Singapore Statutes Online; PDPC Advisory Guidelines on Key Concepts.
