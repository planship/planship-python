from typing import Dict, List, Optional

from planship_openapi_gen.api import (
    CustomersApi,
    CustomerSubscriptionsApi,
    EntitlementsApi,
    MeteredUsageApi,
    ProductsApi,
    SubscriptionCustomersApi,
)
from planship_openapi_gen.models import (
    Customer,
    CustomerInDbBase,
    CustomerSubscriptionWithPlan,
    LeverUsage,
    MeteredUsageIn,
    MeteringRecord,
    OrganizationCustomerCreate,
)
from planship_openapi_gen.models import Plan as PlanDetails
from planship_openapi_gen.models import PlanInList as Plan
from planship_openapi_gen.models import (
    PlanSubscriptionCreate,
    Product,
    SubscriptionCustomer,
    SubscriptionCustomerAdd,
    SubscriptionCustomerInDbBase,
    SubscriptionUpdateWithSlugs,
    SubscriptionWithPlan,
)

from .base import Base
from .models import (
    CreateCustomerParameters,
    CreateSubscriptionParameters,
    ModifySubscriptionParameters,
)


class Planship(Base):
    def __init__(self, product_slug: str, url: str, client_id: str, client_secret: str):
        """Create an instance of the Planship API client class

        Args:
            product_slug (str): Planship product slug
            url (str): Planship API service endpoint URL (E.g. https://api.planship.io)
            client_id (str): Planship API client ID
            client_secret (str): Planship API client secret
        """
        super().__init__(url=url, client_id=client_id, client_secret=client_secret)
        self.product_slug = product_slug

    def get_product(self) -> Product:
        """Retrive the product summary

        Returns:
            Product: Instance of the Product class
        """
        return self.get_api_instance(ProductsApi).get_product(self.product_slug)

    def list_plans(self) -> List[Plan]:
        """Retrieve a list of plans for the product

        Returns:
            List[Plan]: A list of Plan instances
        """
        return self.get_api_instance(ProductsApi).list_product_plans(self.product_slug)

    def get_plan(self, plan_slug: str) -> PlanDetails:
        """Retrieve detailed information about the plan with a given slug.

        Args:
            plan_slug (str): plan slug

        Returns:
            PlanDetails: Instance of the PlanDetails class
        """
        return self.get_api_instance(ProductsApi).get_product_plan(
            self.product_slug, plan_slug
        )

    def create_customer(
        self,
        customer_create_params: CreateCustomerParameters = OrganizationCustomerCreate(),
    ) -> Customer:
        """Register a new customer with Planship.

        Args:
            customer_create_params (CreateCustomerParameters, optional): CreateCustomerParameters object

        Returns:
            Customer: Instance of the Customer class
        """
        return self.get_api_instance(CustomersApi).create_customer(
            customer_create_params
        )

    def delete_customer(self, customer_id: str) -> CustomerInDbBase:
        """Delete the customer with a given customer ID from Planship

        Args:
            customer_id (str): The ID of the customer to remove. The ID can also be an alternative ID.

        Returns:
            CustomerInDbBase: Instance of the CustomerInDbBase class.
        """
        return self.get_api_instance(CustomersApi).delete_customer(customer_id)

    def create_subscription(
        self,
        customer_id: str,
        plan_slug: str,
        create_subscription_params: CreateSubscriptionParameters = CreateSubscriptionParameters(),
    ) -> SubscriptionWithPlan:
        """Create a new subscription to the plan with a given slug for the customer with a given ID

        Args:
            customer_id (str): Planship customer ID or alternative ID
            plan_slug (str): Plan slug
            create_subscription_params (CreateSubscriptionParameters, optional): CreateSubscriptionParameters object

        Returns:
            SubscriptionWithPlan: Instance of the SubscriptionWithPlan class.
        """
        return self.get_api_instance(ProductsApi).create_plan_subscription(
            self.product_slug,
            plan_slug,
            PlanSubscriptionCreate(
                customer_id=customer_id, **create_subscription_params.dict()
            ),
        )

    def get_subscription(
        self, customer_id: str, subscription_id: str
    ) -> CustomerSubscriptionWithPlan:
        """Retrieve detailed information about the subscription with a given ID for the customer with a given ID

        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).get_customer_plan_subscription(
            customer_id,
            subscription_id,
        )

    def change_subscription_plan(
        self, customer_id: str, subscription_id: str, plan_slug: str
    ) -> CustomerSubscriptionWithPlan:
        """Change the plan of the subscription with a given ID for the customer with a given ID.
        The new plan is specified with a slug.

        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            plan_slug (str): New plan slug

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).modify_customer_plan_subscription(
            customer_id,
            subscription_id,
            SubscriptionUpdateWithSlugs(plan_slug=plan_slug),
        )

    def change_subscription_renew_plan(
        self, customer_id: str, subscription_id: str, renew_plan_slug: str
    ) -> CustomerSubscriptionWithPlan:
        """Change the renew plan of the subscription with a given ID for the customer with a given ID.
        New new renew plan is specified with a slug.

        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            renew_plan_slug (str): New renew plan slug

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).modify_customer_plan_subscription(
            customer_id,
            subscription_id,
            SubscriptionUpdateWithSlugs(renew_plan_slug=renew_plan_slug),
        )

    def change_subscription_max_subscribers(
        self, customer_id: str, subscription_id: str, max_subscribers: int
    ) -> CustomerSubscriptionWithPlan:
        """Change the maximum allowed number of subscribers for a subscription with a given ID


        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            max_subscribers (int): New maximum number of subscribers

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).modify_customer_plan_subscription(
            customer_id,
            subscription_id,
            SubscriptionUpdateWithSlugs(max_subscribers=max_subscribers),
        )

    def set_subscription_auto_renew(
        self, customer_id: str, subscription_id: str, auto_renew: bool
    ) -> CustomerSubscriptionWithPlan:
        """Set the auto_renew property for a subscription with a given ID


        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            auto_renew (bool): New auto_renew property value

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).modify_customer_plan_subscription(
            customer_id,
            subscription_id,
            SubscriptionUpdateWithSlugs(auto_renew=auto_renew),
        )

    def set_subscription_is_active(
        self, customer_id: str, subscription_id: str, is_active: bool
    ) -> CustomerSubscriptionWithPlan:
        """Set the is_active property value for a subscription with a given ID


        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            is_active (bool): New is_active property value

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).modify_customer_plan_subscription(
            customer_id,
            subscription_id,
            SubscriptionUpdateWithSlugs(is_active=is_active),
        )

    def modify_subscription(
        self,
        customer_id: str,
        subscription_id: str,
        modify_subscription_params: ModifySubscriptionParameters,
    ) -> CustomerSubscriptionWithPlan:
        """Modify the subscription with a given ID for the customer with a given ID.
        New plan, renew plan and maximum subscribers values are passed via params object.


        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            modify_subscription_params (ModifySubscriptionParameters): ModifySubscriptionParameters object

        Returns:
            CustomerSubscriptionWithPlan: Instance of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).modify_customer_plan_subscription(
            customer_id,
            subscription_id,
            modify_subscription_params,
        )

    def list_subscriptions(
        self, customer_id: str
    ) -> List[CustomerSubscriptionWithPlan]:
        """List subscription for the customer with a given ID

        Args:
            customer_id (str): Planship customer ID or alternative ID

        Returns:
            List[CustomerSubscriptionWithPlan]: List of instances of the CustomerSubscriptionWithPlan class
        """
        return self.get_api_instance(
            CustomerSubscriptionsApi
        ).list_customer_plan_subscriptions(
            customer_id,
        )

    def get_entitlements(self, customer_id: str) -> Dict:
        """Retrieve all product entitlements for the customer with a given ID

        Args:
            customer_id (str): Planship customer ID or alternative ID

        Returns:
            Dict: Object containing entitlement values keyed by lever slugs
        """
        return self.get_api_instance(
            EntitlementsApi
        ).get_product_entitlements_for_customer(
            self.product_slug,
            customer_id,
        )

    def get_lever_usage(self, customer_id: str, lever_slug: str) -> LeverUsage:
        """Retrieve customer usage data for the metered lever with a given slug

        Args:
            customer_id (str): Planship customer ID or alternative ID
            lever_slug (str): Lever slug

        Returns:
            LeverUsage: Instance of the LeverUsage class
        """
        return self.get_api_instance(MeteredUsageApi).get_lever_usage_for_customer(
            customer_id,
            self.product_slug,
            lever_slug,
        )

    def get_metering_id_usage(
        self, customer_id: str, metering_id: str
    ) -> Dict[str, LeverUsage]:
        """Retrieve customer usage data for all metered levers with a given metering ID

        Args:
            customer_id (str): Planship customer ID or alternative ID
            metering_id (str): Metering ID

        Returns:
            Dict[str, LeverUsage]: Dictonary of LeverUsage instances keyed by lever slugs
        """
        return self.get_api_instance(
            MeteredUsageApi
        ).get_metering_id_levers_usage_for_customer(
            customer_id,
            self.product_slug,
            metering_id,
        )

    def report_usage(
        self,
        customer_id: str,
        metering_id: str,
        usage: int,
        bucket: Optional[str] = None,
    ) -> MeteringRecord:
        """Report customer usage for a given metering ID

        Args:
            customer_id (str): Planship customer ID or alternative ID
            metering_id (str): Metering ID string
            usage (int): Amount of usage to report
            bucket (Optional[str], optional): Optional usage bucket name

        Returns:
            MeteringRecord: Instance of the MeteringRecord class
        """
        return self.get_api_instance(MeteredUsageApi).report_metered_usage_for_customer(
            customer_id,
            self.product_slug,
            metering_id,
            MeteredUsageIn(usage=usage, bucket=bucket),
        )

    def list_subscription_customers(
        self, customer_id: str, subscription_id: str
    ) -> List[SubscriptionCustomer]:
        """Retrieve a list of all customers that belong to the subscription with a given ID

        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID

        Returns:
            List[SubscriptionCustomer]: List of instances of SubscriptionCustomer class
        """
        return self.get_api_instance(
            SubscriptionCustomersApi
        ).list_subscription_customers(
            customer_id,
            subscription_id,
        )

    def add_subscription_customer(
        self,
        customer_id: str,
        subscription_id: str,
        customer_id_to_add: str,
        *,
        is_subscriber: bool = True,
        is_administrator: bool = False,
        metadata: Optional[Dict[str, str]] = None
    ) -> SubscriptionCustomer:
        """Add customer to an existing subscription

        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            customer_id_to_add (str): ID of the Planship customer to add to the subscription
            is_subscriber (bool, optional): Flag to specify if the customer is a subscriber. Defaults to True.
            is_administrator (bool, optional): Flag to specify if the customer is an administrator. Defaults to False.
            metadata (Optional[Dict[str, str]], optional): Customer metadata for this subscription. Defaults to None.

        Returns:
            SubscriptionCustomer: Instance of the SubscriptionCustomer class
        """
        return self.get_api_instance(
            SubscriptionCustomersApi
        ).add_customer_to_subscription(
            customer_id,
            subscription_id,
            SubscriptionCustomerAdd(
                customer_id=customer_id_to_add,
                is_administrator=is_administrator,
                is_subscriber=is_subscriber,
                metadata=metadata,
            ),
        )

    def remove_subscription_customer(
        self, customer_id: str, subscription_id: str, customer_id_to_remove: str
    ) -> SubscriptionCustomerInDbBase:
        """Remove Planship customer from a subscription

        Args:
            customer_id (str): Planship customer ID or alternative ID
            subscription_id (str): Planship subscription ID
            customer_id_to_remove (str): ID of the customer to remove from the subscription

        Returns:
            SubscriptionCustomerInDbBase: Instance of the SubscriptionCustomerInDbBase class
        """
        return self.get_api_instance(
            SubscriptionCustomersApi
        ).remove_customer_from_subscription(
            customer_id, subscription_id, customer_id_to_remove
        )
