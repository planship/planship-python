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

from planship_openapi_gen.models.customer import Customer  # noqa: E501

class TestCustomer(unittest.TestCase):
    """Customer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Customer:
        """Test Customer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Customer`
        """
        model = Customer()  # noqa: E501
        if include_optional:
            return Customer(
                id = '',
                metadata_ = planship_openapi_gen.models.metadata_.Metadata (),
                name = '',
                email = '',
                alternative_id = '',
                organization_id = '',
                subscriptions = [
                    planship_openapi_gen.models.subscription_customer.SubscriptionCustomer(
                        metadata_ = planship_openapi_gen.models.metadata_.Metadata (), 
                        is_administrator = True, 
                        is_subscriber = True, 
                        customer_id = '', 
                        subscription_id = '', 
                        plan = planship_openapi_gen.models.plan_in_db_base.PlanInDbBase(
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
                            duration_unit = null, 
                            id = '', ), )
                    ]
            )
        else:
            return Customer(
                id = '',
                organization_id = '',
                subscriptions = [
                    planship_openapi_gen.models.subscription_customer.SubscriptionCustomer(
                        metadata_ = planship_openapi_gen.models.metadata_.Metadata (), 
                        is_administrator = True, 
                        is_subscriber = True, 
                        customer_id = '', 
                        subscription_id = '', 
                        plan = planship_openapi_gen.models.plan_in_db_base.PlanInDbBase(
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
                            duration_unit = null, 
                            id = '', ), )
                    ],
        )
        """

    def testCustomer(self):
        """Test Customer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()