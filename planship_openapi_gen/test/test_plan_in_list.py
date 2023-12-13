# coding: utf-8

"""
    Planship API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from planship_openapi_gen.models.plan_in_list import PlanInList  # noqa: E501

class TestPlanInList(unittest.TestCase):
    """PlanInList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanInList:
        """Test PlanInList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanInList`
        """
        model = PlanInList()  # noqa: E501
        if include_optional:
            return PlanInList(
                slug = '',
                name = '',
                description = '',
                order = 56
            )
        else:
            return PlanInList(
                slug = '',
                name = '',
                description = '',
        )
        """

    def testPlanInList(self):
        """Test PlanInList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
