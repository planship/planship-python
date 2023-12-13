# MeteredUsageIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **int** |  | 
**subscription_id** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.metered_usage_in import MeteredUsageIn

# TODO update the JSON string below
json = "{}"
# create an instance of MeteredUsageIn from a JSON string
metered_usage_in_instance = MeteredUsageIn.from_json(json)
# print the JSON string representation of the object
print MeteredUsageIn.to_json()

# convert the object into a dict
metered_usage_in_dict = metered_usage_in_instance.to_dict()
# create an instance of MeteredUsageIn from a dict
metered_usage_in_form_dict = metered_usage_in.from_dict(metered_usage_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


