<a id="planship.planship"></a>

# planship.planship

<a id="planship.planship.Planship"></a>

## Planship Objects

```python
class Planship(Base)
```

<a id="planship.planship.Planship.__init__"></a>

#### \_\_init\_\_

```python
def __init__(url: str, product_slug: str, client_id: str, client_secret: str)
```

Create an instance of the Planship API client class

**Arguments**:

- `url` _str_ - Planship API service endpoint URL (E.g. https://api.planship.io)
- `product_slug` _str_ - Planship product slug
- `client_id` _str_ - Planship API client ID
- `client_secret` _str_ - Planship API client secret

<a id="planship.planship.Planship.get_product"></a>

#### get\_product

```python
def get_product() -> Product
```

Retrive the product summary

**Returns**:

- `Product` - Instance of the Product class

<a id="planship.planship.Planship.list_plans"></a>

#### list\_plans

```python
def list_plans() -> List[Plan]
```

Retrieve a list of plans for the product

**Returns**:

- `List[Plan]` - A list of Plan instances

<a id="planship.planship.Planship.get_plan"></a>

#### get\_plan

```python
def get_plan(plan_slug: str) -> PlanDetails
```

Retrieve detailed information about the plan with a given slug.

**Arguments**:

- `plan_slug` _str_ - plan slug
  

**Returns**:

- `PlanDetails` - Instance of the PlanDetails class

<a id="planship.planship.Planship.create_customer"></a>

#### create\_customer

```python
def create_customer(customer_create_params:
                    CreateCustomerParameters = OrganizationCustomerCreate()
                    ) -> Customer
```

Register a new customer with Planship.

**Arguments**:

- `customer_create_params` _CreateCustomerParameters, optional_ - CreateCustomerParameters object
  

**Returns**:

- `Customer` - Instance of the Customer class

<a id="planship.planship.Planship.delete_customer"></a>

#### delete\_customer

```python
def delete_customer(customer_id: str) -> CustomerInDbBase
```

Delete the customer with a given customer ID from Planship

**Arguments**:

- `customer_id` _str_ - The ID of the customer to remove. The ID can also be an alternative ID.
  

**Returns**:

- `CustomerInDbBase` - Instance of the CustomerInDbBase class.

<a id="planship.planship.Planship.create_subscription"></a>

#### create\_subscription

```python
def create_subscription(
    customer_id: str,
    plan_slug: str,
    create_subscription_params:
    CreateSubscriptionParameters = CreateSubscriptionParameters()
) -> SubscriptionWithPlan
```

Create a new subscription to the plan with a given slug for the customer with a given ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `plan_slug` _str_ - Plan slug
- `create_subscription_params` _CreateSubscriptionParameters, optional_ - CreateSubscriptionParameters object
  

**Returns**:

- `SubscriptionWithPlan` - Instance of the SubscriptionWithPlan class.

<a id="planship.planship.Planship.get_subscription"></a>

#### get\_subscription

```python
def get_subscription(customer_id: str,
                     subscription_id: str) -> CustomerSubscriptionWithPlan
```

Retrieve detailed information about the subscription with a given ID for the customer with a given ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.change_subscription_plan"></a>

#### change\_subscription\_plan

```python
def change_subscription_plan(customer_id: str, subscription_id: str,
                             plan_slug: str) -> CustomerSubscriptionWithPlan
```

Change the plan of the subscription with a given ID for the customer with a given ID.
The new plan is specified with a slug.

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `plan_slug` _str_ - New plan slug
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.change_subscription_renew_plan"></a>

#### change\_subscription\_renew\_plan

```python
def change_subscription_renew_plan(
        customer_id: str, subscription_id: str,
        renew_plan_slug: str) -> CustomerSubscriptionWithPlan
```

Change the renew plan of the subscription with a given ID for the customer with a given ID.
New new renew plan is specified with a slug.

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `renew_plan_slug` _str_ - New renew plan slug
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.change_subscription_max_subscribers"></a>

#### change\_subscription\_max\_subscribers

```python
def change_subscription_max_subscribers(
        customer_id: str, subscription_id: str,
        max_subscribers: int) -> CustomerSubscriptionWithPlan
```

Change the maximum allowed number of subscribers for a subscription with a given ID


**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `max_subscribers` _int_ - New maximum number of subscribers
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.set_subscription_auto_renew"></a>

#### set\_subscription\_auto\_renew

```python
def set_subscription_auto_renew(
        customer_id: str, subscription_id: str,
        auto_renew: bool) -> CustomerSubscriptionWithPlan
```

Set the auto_renew property for a subscription with a given ID


**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `auto_renew` _bool_ - New auto_renew property value
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.set_subscription_is_active"></a>

#### set\_subscription\_is\_active

```python
def set_subscription_is_active(
        customer_id: str, subscription_id: str,
        is_active: bool) -> CustomerSubscriptionWithPlan
```

Set the is_active property value for a subscription with a given ID


**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `is_active` _bool_ - New is_active property value
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.modify_subscription"></a>

#### modify\_subscription

```python
def modify_subscription(
    customer_id: str, subscription_id: str,
    modify_subscription_params: ModifySubscriptionParameters
) -> CustomerSubscriptionWithPlan
```

Modify the subscription with a given ID for the customer with a given ID.
New plan, renew plan and maximum subscribers values are passed via params object.


**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `modify_subscription_params` _ModifySubscriptionParameters_ - ModifySubscriptionParameters object
  

**Returns**:

- `CustomerSubscriptionWithPlan` - Instance of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.list_subscriptions"></a>

#### list\_subscriptions

```python
def list_subscriptions(customer_id: str) -> List[CustomerSubscriptionWithPlan]
```

List subscription for the customer with a given ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
  

**Returns**:

- `List[CustomerSubscriptionWithPlan]` - List of instances of the CustomerSubscriptionWithPlan class

<a id="planship.planship.Planship.get_entitlements"></a>

#### get\_entitlements

```python
def get_entitlements(customer_id: str) -> Dict
```

Retrieve all product entitlements for the customer with a given ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
  

**Returns**:

- `Dict` - Object containing entitlement values keyed by lever slugs

<a id="planship.planship.Planship.get_lever_usage"></a>

#### get\_lever\_usage

```python
def get_lever_usage(customer_id: str, lever_slug: str) -> LeverUsage
```

Retrieve customer usage data for the metered lever with a given slug

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `lever_slug` _str_ - Lever slug
  

**Returns**:

- `LeverUsage` - Instance of the LeverUsage class

<a id="planship.planship.Planship.get_metering_id_usage"></a>

#### get\_metering\_id\_usage

```python
def get_metering_id_usage(customer_id: str,
                          metering_id: str) -> Dict[str, LeverUsage]
```

Retrieve customer usage data for all metered levers with a given metering ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `metering_id` _str_ - Metering ID
  

**Returns**:

  Dict[str, LeverUsage]: Dictonary of LeverUsage instances keyed by lever slugs

<a id="planship.planship.Planship.report_usage"></a>

#### report\_usage

```python
def report_usage(customer_id: str,
                 metering_id: str,
                 usage: int,
                 bucket: Optional[str] = None) -> MeteringRecord
```

Report customer usage for a given metering ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `metering_id` _str_ - Metering ID string
- `usage` _int_ - Amount of usage to report
- `bucket` _Optional[str], optional_ - Optional usage bucket name
  

**Returns**:

- `MeteringRecord` - Instance of the MeteringRecord class

<a id="planship.planship.Planship.list_subscription_customers"></a>

#### list\_subscription\_customers

```python
def list_subscription_customers(
        customer_id: str, subscription_id: str) -> List[SubscriptionCustomer]
```

Retrieve a list of all customers that belong to the subscription with a given ID

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
  

**Returns**:

- `List[SubscriptionCustomer]` - List of instances of SubscriptionCustomer class

<a id="planship.planship.Planship.add_subscription_customer"></a>

#### add\_subscription\_customer

```python
def add_subscription_customer(
        customer_id: str,
        subscription_id: str,
        customer_id_to_add: str,
        *,
        is_subscriber: bool = True,
        is_administrator: bool = False,
        metadata: Optional[Dict[str, str]] = None) -> SubscriptionCustomer
```

Add customer to an existing subscription

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `customer_id_to_add` _str_ - ID of the Planship customer to add to the subscription
- `is_subscriber` _bool, optional_ - Flag to specify if the customer is a subscriber. Defaults to True.
- `is_administrator` _bool, optional_ - Flag to specify if the customer is an administrator. Defaults to False.
- `metadata` _Optional[Dict[str, str]], optional_ - Customer metadata for this subscription. Defaults to None.
  

**Returns**:

- `SubscriptionCustomer` - Instance of the SubscriptionCustomer class

<a id="planship.planship.Planship.remove_subscription_customer"></a>

#### remove\_subscription\_customer

```python
def remove_subscription_customer(
        customer_id: str, subscription_id: str,
        customer_id_to_remove: str) -> SubscriptionCustomerInDbBase
```

Remove Planship customer from a subscription

**Arguments**:

- `customer_id` _str_ - Planship customer ID or alternative ID
- `subscription_id` _str_ - Planship subscription ID
- `customer_id_to_remove` _str_ - ID of the customer to remove from the subscription
  

**Returns**:

- `SubscriptionCustomerInDbBase` - Instance of the SubscriptionCustomerInDbBase class

