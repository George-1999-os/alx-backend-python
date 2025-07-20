#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_org(self, mock_get):
        mock_get.return_value = {"login": "alx"}
        client = GithubOrgClient("alx")
        self.assertEqual(client.org(), {"login": "alx"})
        mock_get.assert_called_once_with("https://api.github.com/orgs/alx")

if __name__ == '__main__':
    unittest.main()
