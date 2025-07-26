#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests
from functools import lru_cache


def get_json(url):
    """Fetch JSON from a URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Client for GitHub organization info"""

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    @lru_cache()
    def org(self):
        """Memoized org data"""
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

    @property
    def _public_repos_url(self):
        """Extract repos_url from org data"""
        return self.org.get("repos_url")
