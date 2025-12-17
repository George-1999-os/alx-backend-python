#!/usr/bin/env python3
"""Github organization client module."""

from typing import List, Dict
from utils import get_json


class GithubOrgClient:
    """Client for interacting with GitHub organizations."""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name: str) -> None:
        """Initialize GithubOrgClient with organization name."""
        self._org_name = org_name

    @property
    def org(self):
        """Get organization data."""
        return get_json(self.ORG_URL.format(self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the organization's public repositories."""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Return the list of public repository names.

        Args:
            license (str): Optional license key to filter repos.

        Returns:
            List[str]: List of repo names.
        """
        repos = get_json(self._public_repos_url)

        return [
            repo.get("name")
            for repo in repos
            if license is None or self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if a repository has a specific license."""
        return repo.get("license", {}).get("key") == license_key
