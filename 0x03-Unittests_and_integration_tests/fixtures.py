#!/usr/bin/env python3
# fixtures.py

org_payload = {
    "login": "testorg",
    "id": 1,
    "url": "https://api.github.com/orgs/testorg",
    "repos_url": "https://api.github.com/orgs/testorg/repos"
}

repos_payload = [
    {"id": 101, "name": "repo1", "license": {"key": "mit"}},
    {"id": 102, "name": "repo2", "license": {"key": "apache-2.0"}},
    {"id": 103, "name": "repo3", "license": {"key": "apache-2.0"}},
]

expected_repos = ["repo1", "repo2", "repo3"]
apache2_repos = ["repo2", "repo3"]
