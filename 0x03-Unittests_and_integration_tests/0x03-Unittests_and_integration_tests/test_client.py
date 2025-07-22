#!/usr/bin/env python3
"""
Unittest module for GithubOrgClient
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns expected value
        when GithubOrgClient.org is mocked
        """
        test_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("testorg")
        result = client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
