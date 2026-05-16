import requests

from app.extract.github_client import BASE_URL, HEADERS
from app.utils.logger import logger
from app.utils.retry_handler import retry_api_call

def get_request(url):

    response = requests.get(url, headers=HEADERS)

    response.raise_for_status()

    return response

def fetch_repo_events(owner, repo, pages=3):

    all_events = []

    for page in range(1, pages + 1):

        url = (
            f"{BASE_URL}/repos/{owner}/{repo}/events"
            f"?per_page=100&page={page}"
        )

        logger.info(f"Fetching page {page}")

        response = retry_api_call(get_request, url)

        events = response.json()

        if not events:
            break

        all_events.extend(events)

    logger.info(f"Fetched {len(all_events)} total events")

    return all_events
