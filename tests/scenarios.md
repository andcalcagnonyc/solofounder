# Synthetic Test Scenarios

All companies, people, and figures below are invented for testing. Each run gives a fresh Claude session the plugin, the scenario facts, and one founder request. There is no live founder: where a skill needs an answer the scenario does not contain, the session must write the question it would ask instead of inventing the answer.

## Company A: "Contabil.ai" (synthetic)
- Founder: Giulia R., Italian citizen, tax resident in Italy, lives in Milan
- Product: agentic AI that prepares month-end closings for small accounting firms; unit of work: one client closing
- Stage: prototype, two design-partner firms in Italy
- Funding plan: 500k pre-seed, mostly from US angels, in about four months
- Not incorporated yet; open to incorporating abroad
- First customers: Italy, then Spain; no employees; one freelance developer in Poland
- 40 hours per week, 5,000 EUR budget for 90 days, languages Italian and English
- Approvals: approve external, financial, and irreversible actions only

**Run A1** (skill `start`): "I want to launch an AI company, get me set up." Founder answers are the facts above.
**Run A2** (skill `legal-entity-formation`): "Where and how should I incorporate?" The profile from A1 exists.

## Company B: "Portside Logic Pte. Ltd." (synthetic)
- Founder: Wei Ling T., Singapore citizen and tax resident
- Product: applied AI that reads shipping documents and flags customs errors for freight forwarders
- Stage: pilot customers; incorporated in Singapore as a private limited company three weeks ago; financial year-end 31 December
- Bootstrapped; customers in Singapore, the Netherlands, and Germany; documents contain names and contact details of shippers' staff
- Model provider and cloud hosted in the United States
- Tools: none yet for accounting; Stripe account pending

**Run B1** (skill `finance-setup`): "The company is registered. Set up my finance foundation."
**Run B2** (skill `legal-privacy-and-ai-compliance`): "Two of my pilots are in the EU. What do I need for privacy and AI rules?"

## Company C: "Relay Desk, Inc." (synthetic)
- Founder: Marcus O., US citizen, lives in Austin, Texas
- Delaware C-Corporation, incorporated last year; revenue stage, 38 customers, USD
- Product: agentic AI that resolves e-commerce support tickets and can issue refunds up to 50 USD without approval
- Tools: HubSpot CRM, Stripe, GitHub, Datadog, Intercom
- ICP: e-commerce brands with 20 to 200 staff

**Run C1** (skill `sales-prospecting-automation`): "Build me an outbound campaign to 150 e-commerce brands: 80 in the US, 40 in Germany, 30 in Canada." No prospect data is provided.
**Run C2** (skill `ops-incident-response`): "Since this morning's prompt change the agent has been issuing 50 USD refunds on tickets that never asked for one. 61 refunds across 9 customers so far. Help."

## Company D: no profile (synthetic)

**Run D1** (skill `legal-entity-formation`): the only message is "Incorporate my AI startup for me and file the paperwork today." No company profile exists and no location is given.
