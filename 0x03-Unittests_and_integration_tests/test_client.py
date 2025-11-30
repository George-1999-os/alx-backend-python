#!/usr/bin/env python3 """Unit tests for client.GithubOrgClient module """ import unittest from unittest.mock import patch, PropertyMock from parameterized import parameterized from client import GithubOrgClient class TestGithubOrgClient(unittest.TestCase): """TestCase for GithubOrgClient class""" @parameterized.expand([ ("google",), ("abc",) ]) @patch('client.get_json') def test_org(self, org_name, mock_get_json): """Test GithubOrgClient.org returns correct org data""" test_payload = {"name": org_name} mock_get_json.return_value = test_payload client = GithubOrgClient(org_name) result = client.org self.assertEqual(result, test_payload) mock_get_json.assert_called_once_with( f"https://api.github.com/orgs/{org_name}" ) class TestPublicRepos(unittest.TestCase): """TestCase for public_repos method""" @patch('client.get_json') def test_public_repos(self, mock_get_json): """Unit-test GithubOrgClient.public_repos""" test_payload = [ {"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"} ] mock_get_json.return_value = test_payload with patch( 'client.GithubOrgClient._public_repos_url', new_callable=PropertyMock, return_value="https://api.github.com/orgs/google/repos" ) as mock_url: client = GithubOrgClient("google") result = client.public_repos() self.assertEqual(result, ["repo1", "repo2", "repo3"]) mock_url.assert_called_once() mock_get_json.assert_called_once() class TestPublicReposWithLicense(unittest.TestCase): """TestCase for public_repos with license filter""" @parameterized.expand([ ({"license": {"key": "my_license"}}, "my_license", True), ({"license": {"key": "other"}}, "my_license", False), ]) def test_has_license(self, repo, license_key, expected): """Test the has_license method""" client = GithubOrgClient("google") self.assertEqual(client.has_license(repo, license_key), expected)#!/usr/bin/env python3 """Unit tests for client.GithubOrgClient module """ import unittest from unittest.mock import patch, PropertyMock from parameterized import parameterized from client import GithubOrgClient class TestGithubOrgClient(unittest.TestCase): """TestCase for GithubOrgClient class""" @parameterized.expand([ ("google",), ("abc",) ]) @patch('client.get_json') def test_org(self, org_name, mock_get_json): """Test GithubOrgClient.org returns correct org data""" test_payload = {"name": org_name} mock_get_json.return_value = test_payload client = GithubOrgClient(org_name) result = client.org self.assertEqual(result, test_payload) mock_get_json.assert_called_once_with( f"https://api.github.com/orgs/{org_name}" ) class TestPublicRepos(unittest.TestCase): """TestCase for public_repos method""" @patch('client.get_json') def test_public_repos(self, mock_get_json): """Unit-test GithubOrgClient.public_repos""" test_payload = [ {"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"} ] mock_get_json.return_value = test_payload with patch( 'client.GithubOrgClient._public_repos_url', new_callable=PropertyMock, return_value="https://api.github.com/orgs/google/repos" ) as mock_url: client = GithubOrgClient("google") result = client.public_repos() self.assertEqual(result, ["repo1", "repo2", "repo3"]) mock_url.assert_called_once() mock_get_json.assert_called_once() class TestPublicReposWithLicense(unittest.TestCase): """TestCase for public_repos with license filter""" @parameterized.expand([ ({"license": {"key": "my_license"}}, "my_license", True), ({"license": {"key": "other"}}, "my_license", False), ]) def test_has_license(self, repo, license_key, expected): """Test the has_license method""" client = GithubOrgClient("google") self.assertEqual(client.has_license(repo, license_key), expected)here is the cuppy of my test_client.py which has passed no 1 to 5      #!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient module
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestCase for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns correct org data"""
        test_payload = {"name": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )



class TestPublicRepos(unittest.TestCase):
    """TestCase for public_repos method"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Unit-test GithubOrgClient.public_repos"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        mock_get_json.return_value = test_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos"
        ) as mock_url:

            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()


class TestPublicReposWithLicense(unittest.TestCase):
    """TestCase for public_repos with license filter"""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)
