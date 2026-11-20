---
name: ops-security-and-reliability
description: "This skill should be used when the user asks to \"harden my infrastructure\", \"prepare for SOC 2\", \"get ISO 27001 ready\", \"set up backups\", \"write a disaster recovery plan\", \"manage access\", \"build a trust center\", or needs operational security and reliability controls."
metadata:
  version: "0.1.0"
  area: ops
---

# Infrastructure Security, Reliability, and Compliance Readiness

Run infrastructure to the standard enterprise customers audit against, sized for a one-person company, with evidence collected as work happens.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Infrastructure, customer security requirements, target frameworks

## Workflow

1. Set the control baseline: single sign-on and multi-factor everywhere, least-privilege roles, no shared accounts, device security, logging of administrative actions.
2. Manage secrets and keys: storage, rotation, and removal on offboarding.
3. Manage vulnerabilities: patching cadence, dependency and image scanning, external scan or penetration test before enterprise sales.
4. Define reliability targets: recovery time and recovery point; implement backups, redundancy, and a tested disaster-recovery procedure.
5. Write the minimum policy set that matches actual practice: access, change, incident, vendor, data handling, business continuity.
6. Map controls to the target framework and identify gaps; automate evidence collection.
7. Maintain the vendor and sub-processor inventory with security review notes.
8. Publish a trust page: practices, sub-processors, certifications in progress, contact.

## Deliverables

- Control checklist with evidence links
- Policies
- Disaster-recovery plan and test record
- Framework gap analysis
- Trust page content

## Founder approval gates

- Engaging auditors or testers
- Access changes for production
- Published security claims

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/ops/` with dated filenames.

## Hand-offs

- `legal-privacy-and-ai-compliance` for regulatory alignment
- `sales-proposal-and-close` for security questionnaires
