# SubscriptionCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew** | **bool** |  | 
**is_active** | **bool** |  | 
**plan_id** | **str** |  | 
**renew_plan_id** | **str** |  | 
**renew_at** | **datetime** |  | 
**last_renewed_at** | **datetime** |  | 
**max_subscribers** | **int** |  | [optional] [default to 1]
**start_at** | **datetime** |  | 

## Example

```python
from planship_openapi_gen.models.subscription_create import SubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCreate from a JSON string
subscription_create_instance = SubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print SubscriptionCreate.to_json()

# convert the object into a dict
subscription_create_dict = subscription_create_instance.to_dict()
# create an instance of SubscriptionCreate from a dict
subscription_create_form_dict = subscription_create.from_dict(subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


