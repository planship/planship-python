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

from planship_openapi_gen.models.subscription_update_with_slugs import SubscriptionUpdateWithSlugs  # noqa: E501

class TestSubscriptionUpdateWithSlugs(unittest.TestCase):
    """SubscriptionUpdateWithSlugs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionUpdateWithSlugs:
        """Test SubscriptionUpdateWithSlugs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionUpdateWithSlugs`
        """
        model = SubscriptionUpdateWithSlugs()  # noqa: E501
        if include_optional:
            return SubscriptionUpdateWithSlugs(
                plan_id = '',
                renew_plan_id = '',
                plan_slug = '',
                renew_plan_slug = '',
                max_subscribers = 56,
                is_active = True,
                auto_renew = True,
                renew_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return SubscriptionUpdateWithSlugs(
        )
        """

    def testSubscriptionUpdateWithSlugs(self):
        """Test SubscriptionUpdateWithSlugs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
