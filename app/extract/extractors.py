import requests

from app.extract.github_client import BASE_URL, HEADERS
from app.utils.logger import logger

def fetch_repo_events(owner, repo):

    url = f"{BASE_URL}/repos/{owner}/{repo}/events"

    response = requests.get(url, headers=HEADERS)

    response.raise_for_status()

    logger.info(f"Fetched events for {owner}/{repo}")

    return response.json()
