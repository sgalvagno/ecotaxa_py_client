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
from ecotaxa_cli_py.api.authentification_api import AuthentificationApi  # noqa: E501
from ecotaxa_cli_py.rest import ApiException


class TestAuthentificationApi(unittest.TestCase):
    """AuthentificationApi unit test stubs"""

    def setUp(self):
        self.api = ecotaxa_cli_py.api.authentification_api.AuthentificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_login_post(self):
        """Test case for login_login_post

        Login  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
