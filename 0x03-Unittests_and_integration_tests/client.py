#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests


def get_json(url):
    """Returns the JSON content of a given URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Github organization client"""

    def __init__(self, org_name):
        """Initialize with organization name"""
        self.org_name = org_name

    @property
    def org(self):
        """Fetch organization details from GitHub API"""
        url = f"https://api.github.com/orgs/{self.org_name}"
        return get_json(url)

    @property
    def _public_repos_url(self):
        """Extract repos_url from organization payload"""
        return self.org.get("repos_url")

    def public_repos(self):
        """Fetch list of public repositories"""
        repos = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos]
