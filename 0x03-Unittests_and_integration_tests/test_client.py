#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @patch('client.get_json')  # ✅ uses decorator
    def test_org(self, mock_get):
        """Test org method"""
        mock_get.return_value = {"login": "google"}
        client = GithubOrgClient("google")
        self.assertEqual(client.org, {"login": "google"})
        mock_get.assert_called_once_with("https://api.github.com/orgs/google")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)  # ✅ uses decorator
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct value"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')  # ✅ uses decorator
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_url, mock_get):
        """Test that public_repos returns the correct list"""
        mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
        mock_get.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        client = GithubOrgClient("testorg")
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2", "repo3"])


if __name__ == "__main__":
    unittest.main()
