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
from ecotaxa_cli_py.api.samples_api import SamplesApi  # noqa: E501
from ecotaxa_cli_py.rest import ApiException


class TestSamplesApi(unittest.TestCase):
    """SamplesApi unit test stubs"""

    def setUp(self):
        self.api = ecotaxa_cli_py.api.samples_api.SamplesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sample_query_sample_sample_id_get(self):
        """Test case for sample_query_sample_sample_id_get

        Sample Query  # noqa: E501
        """
        pass

    def test_sample_set_get_stats_sample_set_taxo_stats_get(self):
        """Test case for sample_set_get_stats_sample_set_taxo_stats_get

        Sample Set Get Stats  # noqa: E501
        """
        pass

    def test_samples_search_samples_search_get(self):
        """Test case for samples_search_samples_search_get

        Samples Search  # noqa: E501
        """
        pass

    def test_update_samples_sample_set_update_post(self):
        """Test case for update_samples_sample_set_update_post

        Update Samples  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
