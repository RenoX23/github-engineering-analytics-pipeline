CREATE TABLE IF NOT EXISTS raw_github_events (
    id SERIAL PRIMARY KEY,
    github_event_id VARCHAR(255) UNIQUE,
    event_type VARCHAR(100),
    repo_name VARCHAR(255),
    payload JSONB,
    created_at TIMESTAMP,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ingestion_metadata (
    id SERIAL PRIMARY KEY,
    pipeline_name VARCHAR(100) UNIQUE,
    last_event_created_at TIMESTAMP
);
