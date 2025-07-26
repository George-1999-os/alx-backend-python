#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests


def get_json(url):
    """Mocked in tests"""
    return requests.get(url).json()


class GithubOrgClient:
    """Github Org Client"""
    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self._org_name = org_name

    @property
    def org(self):
        """Return org data"""
        return get_json(self.ORG_URL.format(self._org_name))

    @property
    def _public_repos_url(self):
        """Return the URL to public repos"""
        return self.org.get("repos_url")
