#!/usr/bin/env python3
"""
GithubOrgClient module.
Provides functionality to interact with a GitHub organization's public data.
"""

import requests


def get_json(url):
    """
    Fetch JSON data from a given URL.
    Args:
        url (str): The URL to send the GET request to.
    Returns:
        dict: The JSON response from the API.
    """
    return requests.get(url).json()


class GithubOrgClient:
    """Client for GitHub organization information."""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        """
        Initialize the GithubOrgClient.
        Args:
            org_name (str): The GitHub organization name.
        """
        self._org_name = org_name

    @property
    def org(self):
        """
        Retrieve the organization data.
        Returns:
            dict: JSON response containing organization data.
        """
        return get_json(self.ORG_URL.format(self._org_name))

    @property
    def _public_repos_url(self):
        """
        Get the URL to the public repositories of the organization.
        Returns:
            str: The URL string for public repos.
        """
        return self.org.get("repos_url")

    def public_repos(self):
        """
        Fetch the list of public repository names.
        Returns:
            list: A list of repository names.
        """
        url = self._public_repos_url
        repos_data = get_json(url)
        return [repo["name"] for repo in repos_data]
