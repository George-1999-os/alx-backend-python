#!/usr/bin/env python3
"""Client module for accessing GitHub organization data."""

from typing import Dict, List
from utils import get_json


class GithubOrgClient:
    """Client for the GitHub organization API."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize GithubOrgClient with an organization name."""
        self._org_name = org_name

    @property
    def org(self) -> Dict:
        """Retrieve organization data from GitHub."""
        url = self.ORG_URL.format(org=self._org_name)
        return get_json(url)

    @property
    def _public_repos_url(self) -> str:
        """Retrieve the URL that lists public repositories."""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """List public repository names, optionally filtered by license."""
        repos = get_json(self._public_repos_url)
        repo_names = [repo.get("name") for repo in repos]

        if license is None:
            return repo_names

        return [
            repo.get("name") for repo in repos
            if self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if a repository has a specific license key."""
        repo_license = repo.get("license", {}).get("key")
        return repo_license == license_key
