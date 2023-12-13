# SubscriptionUpdateWithSlugs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | [optional] 
**renew_plan_id** | **str** |  | [optional] 
**plan_slug** | **str** |  | [optional] 
**renew_plan_slug** | **str** |  | [optional] 
**max_subscribers** | **int** |  | [optional] [default to 1]
**is_active** | **bool** |  | [optional] [default to True]
**auto_renew** | **bool** |  | [optional] 
**renew_at** | **datetime** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.subscription_update_with_slugs import SubscriptionUpdateWithSlugs

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUpdateWithSlugs from a JSON string
subscription_update_with_slugs_instance = SubscriptionUpdateWithSlugs.from_json(json)
# print the JSON string representation of the object
print SubscriptionUpdateWithSlugs.to_json()

# convert the object into a dict
subscription_update_with_slugs_dict = subscription_update_with_slugs_instance.to_dict()
# create an instance of SubscriptionUpdateWithSlugs from a dict
subscription_update_with_slugs_form_dict = subscription_update_with_slugs.from_dict(subscription_update_with_slugs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


