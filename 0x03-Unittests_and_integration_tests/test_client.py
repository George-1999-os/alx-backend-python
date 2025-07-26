#!/usr/bin/env python3
"""Unit tests for GithubOrgClient._public_repos_url"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for _public_repos_url"""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL from org"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        client = GithubOrgClient("test_org")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
