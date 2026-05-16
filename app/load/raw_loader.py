from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import json

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

    with engine.connect() as connection:

        for event in events:

            query = text("""
                INSERT INTO raw_github_events (
                    event_type,
                    repo_name,
                    payload
                )
                VALUES (
                    :event_type,
                    :repo_name,
                    :payload
                )
            """)

            connection.execute(
                query,
                {
                    "event_type": event.get("type"),
                    "repo_name": event.get("repo", {}).get("name"),
                    "payload": json.dumps(event)
                }
            )

        connection.commit()
