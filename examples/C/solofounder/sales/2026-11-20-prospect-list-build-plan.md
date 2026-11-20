# Prospect list build plan (no prospect data was supplied; the list is empty until sourced)

No account or contact below is invented. The CSV `2026-11-20-prospect-list-template.csv` holds the columns only.

## Account filters (from the profile ICP)
- E-commerce brand selling online, 20 to 200 staff, HQ in US (80), Germany (40), Canada (30)
- Exclude: the 38 existing customers, open deals in HubSpot, anyone on the suppression list

## Trigger events to look for (each must have a source URL and date)
- Open job posts for support or customer-experience roles
- A helpdesk chat widget or help center visible on the storefront
- Announced peak-season, new-market, or new-channel launch
- Public reviews mentioning slow support replies or refund delays

## Buying committee per account
- Primary: head of customer support / customer experience
- Secondary: head of e-commerce or operations
- Under about 50 staff: founder or CEO

## Steps
1. Source accounts with the filters above. No enrichment tool is in the profile: either connect one (cost needs approval) or build manually from public storefronts and company pages.
2. Verify emails; drop invalid, duplicate, role-only, suppressed, and customer records.
3. Canada: fill the three `casl_` columns or mark the contact `excluded`.
4. Germany: set `status = held_no_email`.
5. Write one opening line per account tied to the trigger; store the fact URL. Lines without a URL are not sent.
6. Founder reviews the list and every opening line before any send.
