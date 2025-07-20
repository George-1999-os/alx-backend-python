#!/usr/bin/env python3
""" GithubOrgClient Module """
import requests


def get_json(url):
    """Get JSON from URL"""
    return requests.get(url).json()


class GithubOrgClient:
    """GithubOrgClient class"""
    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Fetch organization data"""
        return get_json(self.ORG_URL.format(self.org_name))
