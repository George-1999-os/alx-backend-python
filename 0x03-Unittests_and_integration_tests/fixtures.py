#!/usr/bin/env python3
"""
Fixtures for integration testing GithubOrgClient.
"""

# Mocked response for org info
org_payload = {
    "login": "google",
    "id": 123456,
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "description": "Google's GitHub organization"
}

# Mocked list of public repositories
repos_payload = [
    {
        "id": 1,
        "name": "repo1",
        "full_name": "google/repo1",
        "license": {"key": "apache-2.0", "name": "Apache License 2.0"}
    },
    {
        "id": 2,
        "name": "repo2",
        "full_name": "google/repo2",
        "license": {"key": "mit", "name": "MIT License"}
    },
    {
        "id": 3,
        "name": "repo3",
        "full_name": "google/repo3",
        "license": {"key": "apache-2.0", "name": "Apache License 2.0"}
    },
    {
        "id": 4,
        "name": "repo4",
        "full_name": "google/repo4",
        "license": None  # No license
    }
]

# What public_repos() should return (all repo names)
expected_repos = ["repo1", "repo2", "repo3", "repo4"]

# What public_repos("apache-2.0") should return
apache2_repos = ["repo1", "repo3"]
