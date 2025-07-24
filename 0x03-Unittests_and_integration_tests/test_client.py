#!/usr/bin/env python3
# client.py

import requests
from functools import lru_cache


def get_json(url):
    """Fetch JSON data from a given URL."""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """GitHub Organization Client."""

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Fetch organization information from GitHub API."""
        url = f"https://api.github.com/orgs/{self.org_name}"
        return get_json(url)

    @property
    @lru_cache()
    def _public_repos_url(self):
        """Memoized method to get the repos URL from org data."""
        return self.org().get("repos_url")

    def public_repos(self, license=None):
        """
        Return list of public repo names.
        Optionally filter by license key (e.g., 'apache-2.0').
        """
        repos = get_json(self._public_repos_url)
        repo_names = []
        for repo in repos:
            if license is None:
                repo_names.append(repo["name"])
            elif repo.get("license") and repo["license"].get("key") == license:
                repo_names.append(repo["name"])
        return repo_names
