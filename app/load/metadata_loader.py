from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)

PIPELINE_NAME = "github_events_pipeline"

def get_last_ingested_timestamp():

    query = text("""
        SELECT last_event_created_at
        FROM ingestion_metadata
        WHERE pipeline_name = :pipeline_name
    """)

    with engine.connect() as connection:

        result = connection.execute(
            query,
            {"pipeline_name": PIPELINE_NAME}
        ).fetchone()

        if result:
            return result[0]

    return None


def update_last_ingested_timestamp(timestamp):

    query = text("""
        INSERT INTO ingestion_metadata (
            pipeline_name,
            last_event_created_at
        )
        VALUES (
            :pipeline_name,
            :timestamp
        )
        ON CONFLICT (pipeline_name)
        DO UPDATE SET
            last_event_created_at = EXCLUDED.last_event_created_at
    """)

    with engine.connect() as connection:

        connection.execute(
            query,
            {
                "pipeline_name": PIPELINE_NAME,
                "timestamp": timestamp
            }
        )

        connection.commit()
