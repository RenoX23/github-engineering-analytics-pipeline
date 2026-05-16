def transform_repositories(events):

    repositories = {}

    for event in events:

        repo_data = event.get("repo", {})

        repo_name = repo_data.get("name")

        if not repo_name:
            continue

        repositories[repo_name] = {
            "repo_name": repo_name,
            "url": repo_data.get("url")
        }

    return list(repositories.values())


def transform_contributors(events):

    contributors = {}

    for event in events:

        actor = event.get("actor", {})

        username = actor.get("login")

        if not username:
            continue

        contributors[username] = {
            "username": username
        }

    return list(contributors.values())


def transform_commits(events):

    commits = []

    for event in events:

        if event.get("type") != "PushEvent":
            continue

        repo_name = event.get("repo", {}).get("name")

        contributor = (
            event.get("actor", {})
            .get("login")
        )

        created_at = event.get("created_at")

        payload = event.get("payload", {})

        for commit in payload.get("commits", []):

            commits.append({
                "commit_id": commit.get("sha"),
                "repo_name": repo_name,
                "contributor_username": contributor,
                "commit_message": commit.get("message"),
                "commit_timestamp": created_at
            })

    return commits

def transform_pull_requests(events):

    pull_requests = []

    for event in events:

        if event.get("type") != "PullRequestEvent":
            continue

        payload = event.get("payload", {})

        pr = payload.get("pull_request", {})

        pull_requests.append({
            "pr_id": pr.get("id"),
            "repo_name": event.get("repo", {}).get("name"),
            "contributor_username": (
                pr.get("user", {})
                .get("login")
            ),
            "pr_title": pr.get("title"),
            "state": pr.get("state"),
            "created_at": pr.get("created_at"),
            "closed_at": pr.get("closed_at")
        })

    return pull_requests
