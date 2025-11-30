#!/usr/bin/env python3
"""GithubOrgClient module
"""

from typing import List, Dict
from utils import get_json


class GithubOrgClient:
    """Client for interacting with GitHub organizations"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize GithubOrgClient with organization name"""
        self._org_name = org_name

    @property
    def org(self) -> Dict:
        """Fetch organization information from GitHub"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the organization's public repositories"""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Return the list of public repository names

        Args:
            license (str): Optional license key to filter repos.

        Returns:
            List[str]: List of repo names
        """
        repos = get_json(self._public_repos_url)
        repo_names = [repo["name"] for repo in repos]

        if license is None:
            return repo_names

        return [
            repo["name"] for repo in repos
            if self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if a repository has a specific license

        Args:
            repo (Dict): Repo metadata
            license_key (str): License key to check for

        Returns:
            bool: True if repo has matching license
        """
        repo_license = repo.get("license", {}).get("key")
        return repo_license == license_key
