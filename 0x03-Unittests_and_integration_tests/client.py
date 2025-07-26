#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests
from typing import Dict, List
from functools import lru_cache


def get_json(url: str) -> Dict:
    """Make a GET request and return the JSON response"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Client for GitHub organization"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize with organization name"""
        self._org_name = org_name

    @property
    @lru_cache()
    def org(self) -> Dict:
        """Get organization details"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the repos_url from the org payload"""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Get list of public repo names, filtered by license if specified"""
        repos = get_json(self._public_repos_url)
        repo_names = [repo["name"] for repo in repos]

        if license:
            repo_names = [
                repo["name"]
                for repo in repos
                if repo.get("license", {}).get("key") == license
            ]

        return repo_names
