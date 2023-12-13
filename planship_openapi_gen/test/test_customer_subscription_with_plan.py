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

from planship_openapi_gen.models.customer_subscription_with_plan import CustomerSubscriptionWithPlan  # noqa: E501

class TestCustomerSubscriptionWithPlan(unittest.TestCase):
    """CustomerSubscriptionWithPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerSubscriptionWithPlan:
        """Test CustomerSubscriptionWithPlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerSubscriptionWithPlan`
        """
        model = CustomerSubscriptionWithPlan()  # noqa: E501
        if include_optional:
            return CustomerSubscriptionWithPlan(
                metadata_ = planship_openapi_gen.models.metadata_.Metadata (),
                is_administrator = True,
                is_subscriber = True,
                customer_id = '',
                subscription_id = '',
                max_subscribers = 56,
                auto_renew = True,
                is_active = True,
                renew_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_renewed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                plan = planship_openapi_gen.models.id_name_slug_orm_base.IdNameSlugOrmBase(
                    id = '', 
                    name = '', 
                    slug = '', ),
                renew_plan = planship_openapi_gen.models.id_name_slug_orm_base.IdNameSlugOrmBase(
                    id = '', 
                    name = '', 
                    slug = '', )
            )
        else:
            return CustomerSubscriptionWithPlan(
                customer_id = '',
                subscription_id = '',
                auto_renew = True,
                is_active = True,
                renew_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_renewed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                plan = planship_openapi_gen.models.id_name_slug_orm_base.IdNameSlugOrmBase(
                    id = '', 
                    name = '', 
                    slug = '', ),
                renew_plan = planship_openapi_gen.models.id_name_slug_orm_base.IdNameSlugOrmBase(
                    id = '', 
                    name = '', 
                    slug = '', ),
        )
        """

    def testCustomerSubscriptionWithPlan(self):
        """Test CustomerSubscriptionWithPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
