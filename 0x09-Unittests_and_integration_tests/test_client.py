#!/usr/bin/env python3
"""class to test clients module"""

import unittest
from unittest import mock
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class to test github
    org client class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org):
        """test org method"""
        with patch('client.GithubOrgClient.org') as mock_:
            test = GithubOrgClient(org_name=org)
            self.assertEqual(test.org.return_value, mock_.return_value)

    def test_public_repos_url(self):
        """test public repos url method"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) \
                as mock_:
            mock_.return_value = {'repos_url': True}
            github = GithubOrgClient('org')
            self.assertEqual(github._public_repos_url, True)

    @patch('client.get_json')
    def test_public_repos(self, mocked):
        """test public repos"""
        Dict = [{'name': 'repo_0'}, {'name': 'repo_1'}]
        mocked.return_value = Dict
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_:
            mock_.return_value = 'World'
            github = GithubOrgClient('test').public_repos()
            self.assertEqual(github, ['repo_0', 'repo_1'])
            mock_.assert_called_once()
            mock_.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """test has license method"""
        fn = GithubOrgClient.has_license(repo, license)
        self.assertEqual(fn, expected)
