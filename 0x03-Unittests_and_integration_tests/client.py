#!/usr/bin/env python3
# client.py

import requests


class GithubOrgClient:
    """GitHub Organization Client"""

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Fetch organization information"""
        url = f"https://api.github.com/orgs/{self.org_name}"
        return requests.get(url).json()

    @property
    def _public_repos_url(self):
        """Fetch URL to list public repos"""
        return self.org().get("repos_url")

    def public_repos(self, license=None):
        """List public repo names, optionally filtered by license"""
        repos = requests.get(self._public_repos_url).json()
        repo_names = [
            repo["name"]
            for repo in repos
            if license is None or (
                repo.get("license") and repo["license"].get("key") == license
            )
        ]
        return repo_nam