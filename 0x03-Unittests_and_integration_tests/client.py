#!/usr/bin/env python3
"""Client module for accessing GitHub organization data."""

import requests


def get_json(url):
    """Fetch JSON content from a given URL using GET request."""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Client for the GitHub organization API."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name):
        """Initialize the GithubOrgClient with an organization name."""
        self.org_name = org_name

    def org(self):
        """Retrieve the organization data from GitHub."""
        url = self.ORG_URL.format(org=self.org_name)
        return get_json(url)

    @property
    def _public_repos_url(self):
        """Retrieve the URL to fetch public repositories."""
        return self.org().get("repos_url")

    def public_repos(self):
        """Get a list of public repository names."""
        return [
            repo.get("name") for repo in get_json(self._public_repos_url)
        ]
