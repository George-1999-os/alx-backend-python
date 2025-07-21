#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    def setUp(self):
        """Common test setup"""
        self.org_name = "google"
        self.client = GithubOrgClient(self.org_name)

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that .org returns correct organization data"""
        expected = {"login": "google"}
        mock_get_json.return_value = expected

        result = self.client.org
        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        result = self.client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_url, mock_get_json):
        """Test that public_repos returns list of repo names"""
        mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        result = self.client.public_repos()
        self.assertEqual(result, ["repo1", "repo2", "repo3"])
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")


if __name__ == "__main__":
    unittest.main()
