from unittest import TestCase
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):
    """Unit tests for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repo names"""
        # Mock payload returned by get_json
        mock_get_json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]

        # Mock _public_repos_url property using patch as context manager
        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
            client = GithubOrgClient("testorg")
            result = client.public_repos()

            # Assertions
            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")
            mock_url.assert_called_once()
