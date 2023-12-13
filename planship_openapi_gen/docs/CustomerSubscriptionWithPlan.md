# CustomerSubscriptionWithPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_** | **object** |  | [optional] 
**is_administrator** | **bool** |  | [optional] [default to False]
**is_subscriber** | **bool** |  | [optional] [default to True]
**customer_id** | **str** |  | 
**subscription_id** | **str** |  | 
**max_subscribers** | **int** |  | [optional] [default to 1]
**auto_renew** | **bool** |  | 
**is_active** | **bool** |  | 
**renew_at** | **datetime** |  | 
**last_renewed_at** | **datetime** |  | 
**plan** | [**IdNameSlugOrmBase**](IdNameSlugOrmBase.md) |  | 
**renew_plan** | [**IdNameSlugOrmBase**](IdNameSlugOrmBase.md) |  | 

## Example

```python
from planship_openapi_gen.models.customer_subscription_with_plan import CustomerSubscriptionWithPlan

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerSubscriptionWithPlan from a JSON string
customer_subscription_with_plan_instance = CustomerSubscriptionWithPlan.from_json(json)
# print the JSON string representation of the object
print CustomerSubscriptionWithPlan.to_json()

# convert the object into a dict
customer_subscription_with_plan_dict = customer_subscription_with_plan_instance.to_dict()
# create an instance of CustomerSubscriptionWithPlan from a dict
customer_subscription_with_plan_form_dict = customer_subscription_with_plan.from_dict(customer_subscription_with_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


