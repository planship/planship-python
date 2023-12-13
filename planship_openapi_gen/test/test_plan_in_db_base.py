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

from planship_openapi_gen.models.plan_in_db_base import PlanInDbBase  # noqa: E501

class TestPlanInDbBase(unittest.TestCase):
    """PlanInDbBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanInDbBase:
        """Test PlanInDbBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanInDbBase`
        """
        model = PlanInDbBase()  # noqa: E501
        if include_optional:
            return PlanInDbBase(
                slug = '',
                display_order = 56,
                display_name = '',
                display_description = '',
                display_extra_attributes = {
                    'key' : ''
                    },
                description = '',
                name = '',
                max_subscribers = 56,
                is_self_serve = True,
                is_public = True,
                auto_renew = True,
                duration_period = 56,
                duration_unit = 'minute',
                id = ''
            )
        else:
            return PlanInDbBase(
                slug = '',
                name = '',
                id = '',
        )
        """

    def testPlanInDbBase(self):
        """Test PlanInDbBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
