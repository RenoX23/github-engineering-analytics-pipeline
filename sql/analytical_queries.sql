SELECT
    contributor_username,
    COUNT(*) AS total_commits
FROM commits
GROUP BY contributor_username
ORDER BY total_commits DESC
LIMIT 10;


SELECT
    repo_name,
    COUNT(*) AS total_events
FROM raw_github_events
GROUP BY repo_name
ORDER BY total_events DESC;

SELECT
    state,
    COUNT(*) AS total_prs
FROM pull_requests
GROUP BY state;
