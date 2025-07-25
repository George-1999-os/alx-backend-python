#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that org property returns the correct value"""
        expected = {"login": "google"}
        mock_get_json.return_value = expected
        client = GithubOrgClient("google")
        self.assertEqual(client.org, expected)

    def test_public_repos_url(self):
        """Test _public_repos_url returns the correct URL using a context manager"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
