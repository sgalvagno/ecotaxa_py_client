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
from ecotaxa_cli_py.models.sample_model import SampleModel  # noqa: E501
from ecotaxa_cli_py.rest import ApiException

class TestSampleModel(unittest.TestCase):
    """SampleModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SampleModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ecotaxa_cli_py.models.sample_model.SampleModel()  # noqa: E501
        if include_optional :
            return SampleModel(
                sampleid = 100, 
                projid = 4, 
                orig_id = 'dewex_leg2_19', 
                latitude = 42.0231666666667, 
                longitude = 4.71766666666667, 
                dataportal_descriptor = '', 
                free_columns = {"flash_delay":"t01"}
            )
        else :
            return SampleModel(
                sampleid = 100,
                orig_id = 'dewex_leg2_19',
        )

    def testSampleModel(self):
        """Test SampleModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
