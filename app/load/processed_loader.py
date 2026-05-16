from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

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

def load_repositories(repositories):

    with engine.connect() as connection:

        for repo in repositories:

            query = text("""
                INSERT INTO repositories (
                    repo_name,
                    url
                )
                VALUES (
                    :repo_name,
                    :url
                )
                ON CONFLICT (repo_name)
                DO NOTHING
            """)

            connection.execute(query, repo)

        connection.commit()

    logger.info(
        f"Loaded {len(repositories)} repositories"
    )


def load_contributors(contributors):

    with engine.connect() as connection:

        for contributor in contributors:

            query = text("""
                INSERT INTO contributors (
                    username
                )
                VALUES (
                    :username
                )
                ON CONFLICT (username)
                DO NOTHING
            """)

            connection.execute(query, contributor)

        connection.commit()

    logger.info(
        f"Loaded {len(contributors)} contributors"
    )


def load_commits(commits):

    with engine.connect() as connection:

        for commit in commits:

            query = text("""
                INSERT INTO commits (
                    commit_id,
                    repo_name,
                    contributor_username,
                    commit_message,
                    commit_timestamp
                )
                VALUES (
                    :commit_id,
                    :repo_name,
                    :contributor_username,
                    :commit_message,
                    :commit_timestamp
                )
                ON CONFLICT (commit_id)
                DO NOTHING
            """)

            connection.execute(query, commit)

        connection.commit()

    logger.info(
        f"Loaded {len(commits)} commits"
    )


def load_pull_requests(pull_requests):

    with engine.connect() as connection:

        for pr in pull_requests:

            query = text("""
                INSERT INTO pull_requests (
                    pr_id,
                    repo_name,
                    contributor_username,
                    pr_title,
                    state,
                    created_at,
                    closed_at
                )
                VALUES (
                    :pr_id,
                    :repo_name,
                    :contributor_username,
                    :pr_title,
                    :state,
                    :created_at,
                    :closed_at
                )
                ON CONFLICT (pr_id)
                DO NOTHING
            """)

            connection.execute(query, pr)

        connection.commit()

    logger.info(
        f"Loaded {len(pull_requests)} pull requests"
    )
