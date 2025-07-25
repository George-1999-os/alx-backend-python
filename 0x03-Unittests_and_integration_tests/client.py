#!/usr/bin/env python3
"""Client module to interact with GitHub API"""

from typing import Dict, List
import requests
from functools import lru_cache


def get_json(url: str) -> Dict:
    """Return the JSON content of a GET request"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """GitHub Organization client"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name: str) -> None:
        """Initialize with organization name"""
        self.org_name = org_name

    @property
    @lru_cache()
    def org(self) -> Dict:
        """Return the organization info"""
        return get_json(self.ORG_URL.format(self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the public repos URL"""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Return a list of public repos"""
        repos_data = get_json(self._public_repos_url)
        repo_names = [repo["name"] for repo in repos_data]
        if license:
            return [
                repo["name"]
                for repo in repos_data
                if repo.get("license", {}).get("key") == license
            ]
        return repo_names
