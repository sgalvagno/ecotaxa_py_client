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
from ecotaxa_cli_py.models.directory_model import DirectoryModel  # noqa: E501
from ecotaxa_cli_py.rest import ApiException

class TestDirectoryModel(unittest.TestCase):
    """DirectoryModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DirectoryModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ecotaxa_cli_py.models.directory_model.DirectoryModel()  # noqa: E501
        if include_optional :
            return DirectoryModel(
                path = '', 
                entries = [
                    ecotaxa_cli_py.models.directory_entry_model.DirectoryEntryModel(
                        name = '', 
                        type = '', 
                        size = 56, 
                        mtime = '', )
                    ]
            )
        else :
            return DirectoryModel(
                path = '',
                entries = [
                    ecotaxa_cli_py.models.directory_entry_model.DirectoryEntryModel(
                        name = '', 
                        type = '', 
                        size = 56, 
                        mtime = '', )
                    ],
        )

    def testDirectoryModel(self):
        """Test DirectoryModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
