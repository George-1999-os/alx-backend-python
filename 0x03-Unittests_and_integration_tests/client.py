#!/usr/bin/env python3
"""Client module for interacting with GitHub"""

import requests

class GithubOrgClient:
    """GitHub Organization Client"""

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Fetch organization data"""
        url = f"https://api.github.com/orgs/{self.org_name}"
        return requests.get(url).json()

    @property
    def _public_repos_url(self):
        """Return the public repositories URL"""
        return self.org.get("repos_url")
