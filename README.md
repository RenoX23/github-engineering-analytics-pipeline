# GitHub Engineering Analytics Pipeline

Production-style ETL pipeline for ingesting and analyzing GitHub engineering activity using Python, PostgreSQL, and Docker.

## Tech Stack

- Python
- PostgreSQL
- Docker
- SQLAlchemy
- Pandas

## Features

- GitHub API ingestion
- Incremental ETL
- Structured logging
- Retry handling
- Dockerized PostgreSQL

## Setup

```bash
docker compose up -d
pip install -r requirements.txt
python app/main.py


---

# ✅ PHASE 1 SUCCESS CHECKLIST

You are DONE with Phase 1 only if:

| Check | Status |
|---|---|
| Repo created | ⬜ |
| Folder structure exists | ⬜ |
| Virtual environment works | ⬜ |
| requirements.txt exists | ⬜ |
| .env exists | ⬜ |
| docker-compose works | ⬜ |
| PostgreSQL container running | ⬜ |
| Python connects to PostgreSQL | ⬜ |
| README exists | ⬜ |

---

# 🚀 WHAT COMES NEXT

ONLY after this works perfectly:

# Phase 2 — Schema + Raw Data Layer

Next phase will include:
- schema.sql
- raw ingestion tables
- GitHub API connector
- first extraction pipeline
- raw JSON persistence

Do NOT jump ahead before infrastructure is stable.
