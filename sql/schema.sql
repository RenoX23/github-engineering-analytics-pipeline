CREATE TABLE IF NOT EXISTS raw_github_events (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(100),
    repo_name VARCHAR(255),
    payload JSONB,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
