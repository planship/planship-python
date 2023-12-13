# SubscriptionWithPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**auto_renew** | **bool** |  | 
**is_active** | **bool** |  | 
**plan_id** | **str** |  | 
**renew_plan_id** | **str** |  | 
**renew_at** | **datetime** |  | 
**last_renewed_at** | **datetime** |  | 
**max_subscribers** | **int** |  | 
**start_at** | **datetime** |  | 
**plan** | [**IdNameSlugOrmBase**](IdNameSlugOrmBase.md) |  | 
**renew_plan** | [**IdNameSlugOrmBase**](IdNameSlugOrmBase.md) |  | 

## Example

```python
from planship_openapi_gen.models.subscription_with_plan import SubscriptionWithPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionWithPlan from a JSON string
subscription_with_plan_instance = SubscriptionWithPlan.from_json(json)
# print the JSON string representation of the object
print SubscriptionWithPlan.to_json()

# convert the object into a dict
subscription_with_plan_dict = subscription_with_plan_instance.to_dict()
# create an instance of SubscriptionWithPlan from a dict
subscription_with_plan_form_dict = subscription_with_plan.from_dict(subscription_with_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


