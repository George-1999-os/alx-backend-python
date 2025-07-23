#!/usr/bin/env python3
"""Client module"""

import requests
from typing import Dict, List
from utils import get_json  # this line is crucial


class GithubOrgClient:
    """GitHub organization client"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str):
        """Initialize with organization name"""
        self.org_name = org_name

    @property
    def org(self) -> Dict:
        """Return organization data"""
        url = self.ORG_URL.format(org=self.org_name)
        return get_json(url)

    @property
    def _public_repos_url(self) -> str:
        """Return public repos URL from org data"""
        return self.org.get("repos_url")

    def public_repos(self) -> List[str]:
        """Return list of public repo names"""
        repos = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos]
 