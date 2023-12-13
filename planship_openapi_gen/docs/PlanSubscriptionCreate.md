# PlanSubscriptionCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**customer_id** | **str** |  | 
**is_subscriber** | **bool** |  | [optional] [default to True]
**max_subscribers** | **int** |  | [optional] [default to 1]
**renew_at** | **datetime** |  | [optional] 
**auto_renew** | **bool** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.plan_subscription_create import PlanSubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSubscriptionCreate from a JSON string
plan_subscription_create_instance = PlanSubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print PlanSubscriptionCreate.to_json()

# convert the object into a dict
plan_subscription_create_dict = plan_subscription_create_instance.to_dict()
# create an instance of PlanSubscriptionCreate from a dict
plan_subscription_create_form_dict = plan_subscription_create.from_dict(plan_subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


