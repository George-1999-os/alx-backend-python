#!/usr/bin/env python3
"""
Unittest module for GithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct org data
        and get_json is called once with the right URL
        """
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

from parameterized import parameterized_class
import fixtures


class MockResponse:
    """Mocked response object"""
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos,
    }
])

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for public_repos method"""

    @classmethod
    def setUpClass(cls):
        """Start patcher and define fixture response"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Replace the following with actual fixture values if needed
        cls.org_payload = {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        cls.repos_payload = [
            {
                "id": 1,
                "name": "repo1",
                "license": {"key": "apache-2.0"}
            },
            {
                "id": 2,
                "name": "repo2",
                "license": {"key": "mit"}
            }
        ]
        cls.expected_repos = ["repo1", "repo2"]
        cls.apache2_repos = ["repo1"]

        def side_effect(url):
            mock_response = Mock()
            if url.endswith("/orgs/google"):
                mock_response.json.return_value = cls.org_payload
            elif url.endswith("/orgs/google/repos"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()


