#!/usr/bin/env python3
import requests

def get_json(url):
    return requests.get(url).json()

class GithubOrgClient:
    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        return get_json(f"https://api.github.com/orgs/{self.org_name}")
