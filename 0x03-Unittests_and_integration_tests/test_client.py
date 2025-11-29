#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestCase for GithubOrgClient"""

    @parameterized.expand([
    ("google",),
    ("abc",)
])
@patch('client.get_json')  # innermost
def test_org(self, org_name, mock_get_json):
    ...

        """Test org returns correct value"""
        mock_payload = {"repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, mock_payload)

    def test_public_repos_url(self):
        """Test _public_repos_url property"""
        with patch.object(
            GithubOrgClient,
            'org',
            return_value={"repos_url": "http://example.com/repos"},
        ):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns repo names"""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]

        client = GithubOrgClient("google")

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_repo_url:
            mock_repo_url.return_value = "https://api.github.com/orgs/google/repos"
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )
