from app.config.settings import GITHUB_TOKEN

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

BASE_URL = "https://api.github.com"
