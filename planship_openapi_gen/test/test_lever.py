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

from planship_openapi_gen.models.lever import Lever  # noqa: E501

class TestLever(unittest.TestCase):
    """Lever unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Lever:
        """Test Lever
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Lever`
        """
        model = Lever()  # noqa: E501
        if include_optional:
            return Lever(
                slug = '',
                id = '',
                display_order = 56,
                display_name = '',
                display_description = '',
                display_extra_attributes = {
                    'key' : ''
                    },
                configuration = planship_openapi_gen.models.configuration.Configuration(),
                description = '',
                name = '',
                entitlement_display_value_template = '',
                entitlement_display_name_template = '',
                entitlement_display_description_template = '',
                lever_type_id = '',
                product_id = '',
                metering_ids = [
                    ''
                    ],
                entitlement_schema_json = planship_openapi_gen.models.entitlement_schema_json.Entitlement Schema Json()
            )
        else:
            return Lever(
                slug = '',
                id = '',
                name = '',
                lever_type_id = '',
                product_id = '',
                metering_ids = [
                    ''
                    ],
        )
        """

    def testLever(self):
        """Test Lever"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
