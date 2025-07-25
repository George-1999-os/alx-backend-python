from unittest import TestCase
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):
    """Tests for GithubOrgClient"""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL from org payload"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google/repos")
