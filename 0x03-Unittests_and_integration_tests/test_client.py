#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_org_property(self, mock_org):
        """Test the org property with mocked return value"""
        mock_org.return_value = {"login": "google"}
        client = GithubOrgClient("google")
        self.assertEqual(client.org, {"login": "google"})
