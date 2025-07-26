#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list of repo names"""
        test_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = (
                "https://api.github.com/orgs/testorg/repos"
            )

            client = GithubOrgClient("testorg")
            result = client.public_repos()

            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/testorg/repos"
            )
            mock_url.assert_called_once()
