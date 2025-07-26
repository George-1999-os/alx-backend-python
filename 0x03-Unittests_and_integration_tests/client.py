#!/usr/bin/env python3
"""
GithubOrgClient module
"""
import requests


def get_json(url):
    """Fetch JSON data from a URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Github Organization client"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org):
        self._org_name = org  # ✅ Store it under a different internal variable

    @property
    def org(self):
        """Return organization data from GitHub"""
        return get_json(self.ORG_URL.format(self._org_name))
