# Finance Stack Recommendation - Portside Logic Pte. Ltd.

_Date: 2026-11-20. DRAFT for review by a Singapore-licensed accountant or tax adviser. Not tax or accounting advice. Nothing here has been opened, signed, or submitted._

Governing jurisdiction: Singapore (place of incorporation and founder tax residence). Dutch and German rules matter only for how EU customers are invoiced.

## 1. Bank - recommendation: one Singapore-licensed bank account with multi-currency sub-accounts (SGD, EUR, USD)
The company bills in Singapore and the euro area and pays its largest suppliers (model and cloud) in the United States, so the account must hold and pay in three currencies without forced conversion. A locally licensed bank is the safest base for IRAS payments and refunds by GIRO, CPF contributions later, and Stripe payouts. A multi-currency payment institution account can be added for cheaper EUR collection and USD card spend, but it should be the second account, not the only one. I have not compared named banks' current fees or onboarding rules; shortlist two banks and one payment institution and I will build the comparison from their published fee schedules. Documents usually requested: ACRA business profile, constitution, director and shareholder identification, and a description of the business and expected flows (confirm each bank's own list).

## 2. Payment processor - recommendation: finish the pending Stripe account; treat bank transfer as the default for pilots
The profile already shows a Stripe account pending, so no second processor is needed. Pilot contracts with freight forwarders are business invoices that are normally paid by bank transfer; use Stripe for card and for subscription billing once pricing is fixed. Post Stripe activity through a clearing account (1050) and reconcile to payout reports so fees and currency conversion are visible. Verify on Stripe's own site that the settlement currencies you need (SGD, and EUR if wanted) are supported for a Singapore account.

## 3. Accounting system - recommendation: a cloud ledger that is on IRAS's accounting-software register and is InvoiceNow-ready
No accounting tool is recorded in the profile. Selection criteria, in order: (a) multi-currency ledger with bank feeds for the chosen bank; (b) listed by IRAS for direct filing and by IMDA as InvoiceNow-ready, because any voluntary GST registration now carries an InvoiceNow obligation (see tax checklist); (c) Stripe feed; (d) tracking categories for customer country and function; (e) accountant access. Xero and QuickBooks are common candidates named in the plugin's connector list; I have not verified either one's current listing status, so check the IRAS and IMDA lists before choosing.

## 4. Expense tool - recommendation: none yet
With one founder and no employees recorded, a company card plus the accounting system's receipt capture is enough. Revisit when a second person spends company money.

## Setup steps once you approve (manual, no tool is connected)
1. Open the bank account; note account numbers for SGD, EUR, USD.
2. Create the accounting file: base currency per the functional-currency decision, year-end 31 December, lock date policy on.
3. Import `2026-11-20-chart-of-accounts.md`; map tax codes after the GST decision.
4. Connect bank feeds and the Stripe feed; set the clearing-account rule.
5. Build the invoice template: company name, UEN, registered address, invoice number in unbroken sequence, date, customer legal name and address, customer VAT ID for EU customers, description, currency, payment terms, bank details. If not GST-registered, the invoice must not show GST or be titled "tax invoice" (confirm wording with the accountant).
6. Create a document store with one folder per month: bank statements, sales invoices, supplier bills, contracts, payroll, tax.

## Sources
- IRAS, Record keeping requirements (updated 22 Jan 2026): https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/record-keeping-requirements
- IRAS, GST InvoiceNow Requirement (updated 8 Oct 2026): https://iras.gov.sg/taxes/goods-services-tax-(gst)/gst-invoicenow-requirement
- Not researched, consult directly: MAS Financial Institutions Directory; each bank's and Stripe's published account requirements; IRAS accounting software register; IMDA InvoiceNow solution-provider list.
