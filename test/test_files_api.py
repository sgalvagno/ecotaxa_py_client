# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ecotaxa_cli_py
from ecotaxa_cli_py.api.files_api import FilesApi  # noqa: E501
from ecotaxa_cli_py.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = ecotaxa_cli_py.api.files_api.FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_common_files(self):
        """Test case for list_common_files

        List Common Files  # noqa: E501
        """
        pass

    def test_list_user_files(self):
        """Test case for list_user_files

        List User Files  # noqa: E501
        """
        pass

    def test_post_user_file(self):
        """Test case for post_user_file

        Put User File  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
