#!/usr/bin/env python3
"""
Unittest module for GithubOrgClient
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


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
        """Start patcher and set up mock responses"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock_response = Mock()
            if url == f"https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == f"https://api.github.com/orgs/google/repos":
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repo names"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters by apache-2.0 license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)
