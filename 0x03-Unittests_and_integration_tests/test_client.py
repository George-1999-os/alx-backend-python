#!/usr/bin/env python3
"""
Integration test for GithubOrgClient.public_repos using fixtures.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class

from client import GithubOrgClient
from fixtures import (
    org_payload,
    repos_payload,
    expected_repos,
    apache2_repos
)


@parameterized_class([{
    "org_payload": org_payload,
    "repos_payload": repos_payload,
    "expected_repos": expected_repos,
    "apache2_repos": apache2_repos
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for public_repos using mocked responses"""

    @classmethod
    def setUpClass(cls):
        """Start patching requests.get with controlled responses."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith('/orgs/google'):
                return FakeResponse(cls.org_payload)
            elif url.endswith('/orgs/google/repos'):
                return FakeResponse(cls.repos_payload)
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns all repositories."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos returns only repos with apache-2.0 license."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


class FakeResponse:
    """Mock class for requests.Response"""
    def __init__(self, json_data):
        self._json_data = json_data

    def json(self):
        return self._json_data
