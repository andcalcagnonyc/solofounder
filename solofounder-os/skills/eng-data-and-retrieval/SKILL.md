---
name: eng-data-and-retrieval
description: "This skill should be used when the user asks to \"build a RAG pipeline\", \"ingest customer documents\", \"set up a vector database\", \"improve retrieval quality\", \"design my data model\", \"connect to the customer's data\", or needs the data and retrieval layer of an AI product."
metadata:
  version: "0.1.0"
  area: eng
---

# Data Pipelines, Retrieval, and Knowledge

Get the right information to the model at the right time: ingestion, storage, retrieval, and freshness, with tenant isolation and measurable retrieval quality.

## Before starting

1. Read `solofounder/company-profile.md`. If it does not exist, stop, tell the founder that the `start` intake comes first, name the `start` skill, and run it before anything else.
2. Take HQ country, entity type, stage, currency, and tool stack from the profile. Never assume a jurisdiction, a currency, or a tool.
3. Check `solofounder/decision-log.md` for earlier decisions that constrain this work.

## Inputs

- Data sources, formats, volumes, update frequency, access rights
- Questions or tasks the product must support

## Workflow

1. Inventory sources with owner, rights to use, sensitivity, and update pattern.
2. Design the application data model and tenant-isolation scheme.
3. Build ingestion: connectors, parsing, cleaning, chunking suited to the content, metadata, deduplication, incremental updates, deletion propagation.
4. Choose the retrieval method: keyword, vector, hybrid, structured query, or agentic search; add reranking only when measured to help.
5. Enforce permissions at retrieval time so users only see what they are entitled to.
6. Build a retrieval evaluation set and measure recall and precision before tuning generation.
7. Present retrieved context with sources so answers can cite them.
8. Monitor freshness, ingestion failures, and index drift.

## Deliverables

- Data model and source inventory
- Ingestion and retrieval design with code
- Retrieval evaluation results

## Founder approval gates

- Use of any customer or third-party data source
- Data location and retention settings

## Guardrails

- Act through connected tools where they exist (see `CONNECTORS.md`); otherwise produce ready-to-use files and exact manual steps.
- Ask before any action that contacts someone outside the company, spends money, or cannot be undone.
- Mark assumptions as assumptions. State a fact about the company only when it is in the profile or the founder said it in this session; otherwise ask. Never invent facts, metrics, customers, quotes, or citations.
- Append each material decision to `solofounder/decision-log.md` with date, options considered, and rationale.
- Save deliverables under `solofounder/eng/` with dated filenames.

## Hand-offs

- `legal-privacy-and-ai-compliance` for data rights
- `eng-evals` for end-to-end quality
