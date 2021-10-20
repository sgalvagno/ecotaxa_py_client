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
from ecotaxa_cli_py.models.taxonomy_tree_status import TaxonomyTreeStatus  # noqa: E501
from ecotaxa_cli_py.rest import ApiException

class TestTaxonomyTreeStatus(unittest.TestCase):
    """TaxonomyTreeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaxonomyTreeStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ecotaxa_cli_py.models.taxonomy_tree_status.TaxonomyTreeStatus()  # noqa: E501
        if include_optional :
            return TaxonomyTreeStatus(
                last_refresh = ''
            )
        else :
            return TaxonomyTreeStatus(
        )

    def testTaxonomyTreeStatus(self):
        """Test TaxonomyTreeStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
