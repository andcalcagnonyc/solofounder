---
name: ops-infrastructure-and-deploy
description: "This skill should be used when the user asks to \"deploy my app\", \"set up hosting\", \"set up infrastructure\", \"create staging and production\", \"set up CI/CD\", \"write Terraform\", \"configure my domain\", or needs cloud infrastructure and deployment pipelines."
metadata:
  version: "0.1.0"
  area: ops
---

# Infrastructure and Deployment

Provision reproducible environments and a deployment pipeline that takes a merged change to production safely with no manual steps.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Architecture, cloud platform in the profile, data-location requirements, expected load

## Workflow

1. Choose the hosting model favoring managed platforms: application hosting, database, queue, storage, model access.
2. Define environments: local, preview per change, staging, production, with separate accounts or projects and separate credentials.
3. Express infrastructure as code and keep it in the repository.
4. Configure networking, domains, certificates, and edge protection.
5. Manage configuration and secrets through the platform's secret store with rotation.
6. Build the deployment pipeline: build, test, evaluate, deploy to staging, promote to production, with progressive rollout and automatic rollback.
7. Configure database migrations, backups, and restore procedure; test a restore.
8. Document the environment in a runbook: how to deploy, roll back, scale, and access logs.

## Deliverables

- Infrastructure code
- Deployment pipeline
- Environment runbook
- Restore test record

## Founder approval gates

- Creating paid cloud resources
- Production deployments until a standing rule is approved
- Destructive changes to infrastructure or data

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/ops/` with dated filenames.

## Hand-offs

- `ops-observability` for monitoring
- `ops-security-and-reliability` for hardening
- `ops-cost-and-finops` for budgets
