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

CREATE TABLE IF NOT EXISTS repositories (
    repo_id SERIAL PRIMARY KEY,
    repo_name VARCHAR(255) UNIQUE,
    url TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);


CREATE TABLE IF NOT EXISTS contributors (
    contributor_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS commits (
    commit_id VARCHAR(255) PRIMARY KEY,
    repo_name VARCHAR(255),
    contributor_username VARCHAR(255),
    commit_message TEXT,
    commit_timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pull_requests (
    pr_id BIGINT PRIMARY KEY,
    repo_name VARCHAR(255),
    contributor_username VARCHAR(255),
    pr_title TEXT,
    state VARCHAR(50),
    created_at TIMESTAMP,
    closed_at TIMESTAMP
);
