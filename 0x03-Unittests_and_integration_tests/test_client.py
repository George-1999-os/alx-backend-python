#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class in client module."""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the expected list of repository names.

        Mocks:
            - get_json to return a list of repository dicts.
            - _public_repos_url property to return a test URL.
        """
        mock_get_json.return_value = [
            {'name': 'alx'},
            {'name': 'backend'},
            {'name': 'python'}
        ]

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"

            client = GithubOrgClient("testorg")
            result = client.public_repos()

            self.assertEqual(result, ['alx', 'backend', 'python'])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/testorg/repos"
            )
            mock_url.assert_called_once()
