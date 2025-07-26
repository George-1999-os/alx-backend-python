from unittest.mock import patch, PropertyMock

@patch('client.get_json')
def test_public_repos(self, mock_get_json):
    """Test public_repos method with patching"""
    # Set up fake payload to be returned by get_json
    test_payload = [
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ]
    mock_get_json.return_value = test_payload

    # Patch _public_repos_url as a context manager
    with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
        mock_url.return_value = "https://api.github.com/orgs/test_org/repos"
        
        client = GithubOrgClient("test_org")
        result = client.public_repos()

        # Assertions
        self.assertEqual(result, ["repo1", "repo2", "repo3"])
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")
        mock_url.assert_called_once()
