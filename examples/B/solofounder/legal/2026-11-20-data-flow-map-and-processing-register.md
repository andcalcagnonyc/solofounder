# Data-Flow Map, Processing Register, and Retention Schedule - Portside Logic Pte. Ltd.

_Date: 2026-11-20. DRAFT for lawyer review. Built only from the company profile; every [TBD] is a fact I need from the founder, not an assumption._

## Data-flow map
```
Shipper's staff details (names, contact details)
  -> appear in shipping documents held by the freight forwarder (controller; SG, NL, DE)
  -> uploaded or sent to Portside [channel TBD: upload, email, API]
  -> stored in cloud [provider TBD], United States [region TBD]
  -> text extraction / OCR [tool TBD]
  -> prompt to model provider [TBD], United States  (retention by provider: TBD; training use: TBD)
  -> flagged-error output stored in cloud, returned to forwarder's user
  -> application logs, prompt logs, analytics [tools TBD]
  -> backups [TBD]
Access from Singapore by the founder counts as processing in Singapore.
```

## Processing register
| # | Activity | Portside's role | Data subjects | Data | Purpose | Legal basis | Recipients / location | Retention (proposed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Checking shipping documents for customs errors | Processor (GDPR) / data intermediary (PDPA) - ASSUMPTION | Shippers' staff; possibly consignees, drivers, signatories [TBD] | Names, business contact details; anything else printed on the documents [TBD] | Deliver the service on the customer's instructions | Set by the customer as controller; Portside acts on documented instructions | Cloud provider (US), model provider (US) | Source documents and outputs: 90 days after processing, or the customer's instruction; deleted within 30 days of contract end |
| 2 | Prompt and application logs | Processor | As above | Extracts of the above inside prompts and logs | Debugging, quality, security | As above; any use to improve the product needs the customer's written permission | Cloud (US), observability tool [TBD] | 30 days; redact personal data from logs where feasible |
| 3 | Model evaluation and improvement using customer documents | Not permitted until agreed in the customer contract | - | - | - | - | - | - |
| 4 | Customer account and billing contacts | Controller | Customers' staff | Name, work email, phone, role | Contract, invoicing, support | Contract / legitimate interests (GDPR, if applicable); PDPA treatment to confirm | Accounting system [TBD], Stripe (pending), email | Life of contract + statutory accounting period |
| 5 | Sales and marketing contacts | Controller | Prospects' staff | Name, work email, company | Outreach | Legitimate interests or consent depending on channel and country [to confirm] | CRM [TBD] | 24 months from last contact |
| 6 | Website visitors | Controller | Visitors | Cookies, IP, analytics events [TBD whether any exist] | Site operation, analytics | Consent for non-essential cookies (EU visitors) | Analytics tool [TBD] | Per tool; 13 months maximum proposed |

## Provider commitments to collect (step 6 of the workflow)
| Provider | Role | Location | DPA signed | Trains on our data | Retention of prompts | Transfer tool | DPF certified |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model provider [TBD] | Sub-processor | United States | [TBD] | [TBD] | [TBD] | [TBD] | [check participant list] |
| Cloud provider [TBD] | Sub-processor | United States | [TBD] | n/a | [TBD] | [TBD] | [check participant list] |
