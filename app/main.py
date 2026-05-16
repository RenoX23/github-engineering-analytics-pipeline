from app.extract.extractors import fetch_repo_events
from app.load.raw_loader import store_raw_events
from app.utils.logger import logger

def run_pipeline():

    owner = "apache"
    repo = "airflow"

    logger.info("Starting GitHub ETL pipeline")

    events = fetch_repo_events(owner, repo)

    store_raw_events(events)

    logger.info("Raw events stored successfully")

    print("✅ Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()
