"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.21
    Generated by: https://openapi-generator.tech
"""


import unittest

import ecotaxa_cli_py
from ecotaxa_cli_py.api.acquisitions_api import AcquisitionsApi  # noqa: E501


class TestAcquisitionsApi(unittest.TestCase):
    """AcquisitionsApi unit test stubs"""

    def setUp(self):
        self.api = AcquisitionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acquisition_query(self):
        """Test case for acquisition_query

        Acquisition Query  # noqa: E501
        """
        pass

    def test_acquisitions_search(self):
        """Test case for acquisitions_search

        Acquisitions Search  # noqa: E501
        """
        pass

    def test_update_acquisitions(self):
        """Test case for update_acquisitions

        Update Acquisitions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()