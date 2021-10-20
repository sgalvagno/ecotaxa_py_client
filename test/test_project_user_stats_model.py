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
from ecotaxa_cli_py.models.project_user_stats_model import ProjectUserStatsModel  # noqa: E501
from ecotaxa_cli_py.rest import ApiException

class TestProjectUserStatsModel(unittest.TestCase):
    """ProjectUserStatsModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUserStatsModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ecotaxa_cli_py.models.project_user_stats_model.ProjectUserStatsModel()  # noqa: E501
        if include_optional :
            return ProjectUserStatsModel(
                projid = 56, 
                annotators = [
                    ecotaxa_cli_py.models.minimal_user_bo.MinimalUserBO(
                        id = 56, 
                        name = '', )
                    ], 
                activities = [
                    ecotaxa_cli_py.models.user_activity.UserActivity(
                        id = 56, 
                        nb_actions = 56, 
                        last_annot = '', )
                    ]
            )
        else :
            return ProjectUserStatsModel(
        )

    def testProjectUserStatsModel(self):
        """Test ProjectUserStatsModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
