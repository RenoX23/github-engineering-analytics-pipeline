from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import json

from app.utils.logger import logger

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)

def store_raw_events(events):

    inserted_count = 0

    with engine.connect() as connection:

        for event in events:

            query = text("""
                INSERT INTO raw_github_events (
                    github_event_id,
                    event_type,
                    repo_name,
                    payload,
                    created_at
                )
                VALUES (
                    :github_event_id,
                    :event_type,
                    :repo_name,
                    :payload,
                    :created_at
                )
                ON CONFLICT (github_event_id)
                DO NOTHING
            """)

            result = connection.execute(
                query,
                {
                    "github_event_id": event.get("id"),
                    "event_type": event.get("type"),
                    "repo_name": event.get("repo", {}).get("name"),
                    "payload": json.dumps(event),
                    "created_at": event.get("created_at")
                }
            )

            inserted_count += result.rowcount

        connection.commit()

    logger.info(
        f"Inserted {inserted_count} new events"
    )
