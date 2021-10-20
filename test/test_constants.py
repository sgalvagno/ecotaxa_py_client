# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ecotaxa_cli_py
from ecotaxa_cli_py.models.constants import Constants  # noqa: E501
from ecotaxa_cli_py.rest import ApiException

class TestConstants(unittest.TestCase):
    """Constants unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Constants
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ecotaxa_cli_py.models.constants.Constants()  # noqa: E501
        if include_optional :
            return Constants(
                license_texts = {
                    'key' : ''
                    }, 
                app_manager = [
                    ''
                    ]
            )
        else :
            return Constants(
        )

    def testConstants(self):
        """Test Constants"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
