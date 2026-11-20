# Connectors

## How tool references work

Skill files use `~~category` as a placeholder for whatever tool the founder connects in that category. The plugin is tool-agnostic: skills describe workflows by category, and the `stack-and-automation-setup` skill records the actual tools in `solofounder/company-profile.md`.

When a category has no connected tool, each skill falls back to producing ready-to-use files and exact manual steps.

## Connectors for this plugin

| Category | Placeholder | Example tools | Used by |
| --- | --- | --- | --- |
| CRM | `~~CRM` | HubSpot, Attio, Pipedrive, Salesforce | Sales, Marketing, Support |
| Enrichment | `~~enrichment` | Apollo, Clay, Clearbit | Sales |
| Email marketing | `~~email marketing` | Loops, Customer.io, Mailchimp, Brevo | Marketing |
| Calendar | `~~calendar` | Google Calendar, Outlook | Legal, Sales, Core |
| Accounting system | `~~accounting system` | QuickBooks, Xero, NetSuite, local statutory packages | Finance |
| Payments | `~~payments` | Stripe, Paddle, PayPal, Adyen | Finance, Sales |
| E-signature | `~~e-signature` | DocuSign, Dropbox Sign, PandaDoc | Legal, Sales |
| Cap table tool | `~~cap table tool` | Carta, Pulley, Ledgy, spreadsheet | Legal |
| Design tool | `~~design tool` | Figma, Canva | Marketing, Product |
| CMS | `~~CMS` | Webflow, Framer, WordPress, Next.js repo | Marketing |
| Analytics | `~~analytics` | PostHog, Amplitude, Mixpanel, GA4 | Product, Marketing |
| Code repository | `~~code repository` | GitHub, GitLab | Engineering |
| Project tracker | `~~project tracker` | Linear, GitHub Issues, Jira | Engineering, Product |
| Observability | `~~observability` | Datadog, Grafana, Sentry, Langfuse | Cloud Ops, Engineering |
| Helpdesk | `~~helpdesk` | Intercom, Zendesk, Plain, Help Scout | Support |
| Knowledge base | `~~knowledge base` | Notion, GitBook, Mintlify, helpdesk help center | Support |

Cloud platform, model providers, bank, and payroll provider are recorded in the company profile and reached through their own consoles, APIs, or exports.
