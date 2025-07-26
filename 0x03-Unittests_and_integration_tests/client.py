#!/usr/bin/env python3
"""GithubOrgClient module for interacting with GitHub organizations."""

import requests


def get_json(url):
    """
    Fetch and return the JSON data from a given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: JSON response.
    """
    return requests.get(url).json()


class GithubOrgClient:
    """
    GithubOrgClient class for interacting with GitHub organization data.

    Attributes:
        org_name (str): GitHub organization name.
    """

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        """
        Initialize the client with a GitHub organization name.

        Args:
            org_name (str): GitHub organization name.
        """
        self._org_name = org_name

    @property
    def org(self):
        """
        Retrieve organization information from GitHub API.

        Returns:
            dict: GitHub organization data.
        """
        return get_json(self.ORG_URL.format(self._org_name))

    @property
    def _public_repos_url(self):
        """
        Return the URL to public repositories for the organization.

        Returns:
            str: URL to public repos.
        """
        return self.org.get("repos_url")

    def public_repos(self):
        """
        Return a list of public repository names.

        Returns:
            list: List of public repo names.
        """
        repos_url = self._public_repos_url
        repos_data = get_json(repos_url)
        return [repo["name"] for repo in repos_data]
