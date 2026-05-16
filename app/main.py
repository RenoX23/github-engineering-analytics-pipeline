from datetime import datetime

from app.extract.extractors import fetch_repo_events
from app.load.raw_loader import store_raw_events
from app.load.metadata_loader import (
    get_last_ingested_timestamp,
    update_last_ingested_timestamp
)
from app.utils.logger import logger

from app.transform.github_transformer import (
    transform_repositories,
    transform_contributors,
    transform_commits,
    transform_pull_requests
)

from app.load.processed_loader import (
    load_repositories,
    load_contributors,
    load_commits,
    load_pull_requests
)

from app.load.raw_reader import fetch_raw_events

def filter_new_events(events, last_timestamp):

    if not last_timestamp:
        return events

    filtered_events = []

    for event in events:

        event_time = datetime.strptime(
            event["created_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        if event_time > last_timestamp:
            filtered_events.append(event)

    return filtered_events


def run_pipeline():

    owner = "apache"
    repo = "airflow"

    logger.info("Starting GitHub ETL pipeline")

    last_timestamp = get_last_ingested_timestamp()

    logger.info(
        f"Last ingested timestamp: {last_timestamp}"
    )

    events = fetch_repo_events(owner, repo)

    new_events = filter_new_events(
        events,
        last_timestamp
    )

    logger.info(
        f"New events after filtering: "
        f"{len(new_events)}"
    )

    if not new_events:

        logger.info(
            "No new events found. "
            "Using existing raw events."
        )

        new_events = fetch_raw_events()

    store_raw_events(new_events)
    repositories = transform_repositories(new_events)
    contributors = transform_contributors(new_events)
    commits = transform_commits(new_events)
    pull_requests = transform_pull_requests(new_events)

    load_repositories(repositories)
    load_contributors(contributors)
    load_commits(commits)
    load_pull_requests(pull_requests)

    latest_timestamp = max(
        datetime.strptime(
            event["created_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )
        for event in new_events
    )

    update_last_ingested_timestamp(
        latest_timestamp
    )

    logger.info(
        "Updated ingestion metadata"
    )

    print("✅ Production-grade pipeline executed!")

if __name__ == "__main__":
    run_pipeline()
