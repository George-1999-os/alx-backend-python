#!/usr/bin/env python3
"""Integration test for GithubOrgClient.public_repos"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class

from client import GithubOrgClient

@parameterized_class([
    {
        "org_payload": {"login": "google"},
        "repos_payload": [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "apache-2", "license": {"key": "apache-2.0"}}
        ],
        "expected_repos": ["repo1", "repo2", "apache-2"],
        "apache2_repos": ["repo2", "apache-2"]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up patcher for get_json before all tests"""
        cls.get_patcher = patch('client.get_json', return_value=cls.repos_payload)
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down patcher after all tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns expected repositories"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that public_repos filters by license key"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
