##!/usr/bin/env python3
"""Client module"""

import requests
from typing import Dict, List
from utils import get_json  # this line is crucial


class GithubOrgClient:
    """GitHub organization client"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        """Initialize with organization name"""
        self.org_name = org_name
        self._public_repos_url = f"https://api.github.com/orgs/{org_name}/repos"

    @property
    def org(self):
        """Fetch and return organization info"""
        return get_json(self.ORG_URL.format(self.org_name))

    def public_repos(self, license=None):
        """Return public repo names, filtered by license if provided"""
        repos = get_json(self._public_repos_url)
        if license is None:
            return [repo["name"] for repo in repos]
        return [
            repo["name"]
            for repo in repos
            if repo.get("license", {}).get("key") == license
        ]
