#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')  # patch as decorator
    def test_org(self, org_name, expected_data, mock_get):
        """Test org method using parameterized input"""
        mock_get.return_value = expected_data
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_data)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url returns correct value"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_url, mock_get):
        """Test public_repos returns correct repo names"""
        mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
        mock_get.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        client = GithubOrgClient("testorg")
        self.assertEqual(client.public_repos(), ["repo1", "repo2", "repo3"])


if __name__ == "__main__":
    unittest.main()
