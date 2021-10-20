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
from ecotaxa_cli_py.models.import_req import ImportReq  # noqa: E501
from ecotaxa_cli_py.rest import ApiException

class TestImportReq(unittest.TestCase):
    """ImportReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImportReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ecotaxa_cli_py.models.import_req.ImportReq()  # noqa: E501
        if include_optional :
            return ImportReq(
                source_path = '', 
                taxo_mappings = {
                    'key' : ''
                    }, 
                skip_loaded_files = True, 
                skip_existing_objects = True, 
                update_mode = ''
            )
        else :
            return ImportReq(
                source_path = '',
        )

    def testImportReq(self):
        """Test ImportReq"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
