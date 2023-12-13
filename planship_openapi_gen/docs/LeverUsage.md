# LeverUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**by_bucket** | **Dict[str, int]** |  | 
**by_subscription** | **Dict[str, List[BucketUsage]]** |  | 

## Example

```python
from planship_openapi_gen.models.lever_usage import LeverUsage

# TODO update the JSON string below
json = "{}"
# create an instance of LeverUsage from a JSON string
lever_usage_instance = LeverUsage.from_json(json)
# print the JSON string representation of the object
print LeverUsage.to_json()

# convert the object into a dict
lever_usage_dict = lever_usage_instance.to_dict()
# create an instance of LeverUsage from a dict
lever_usage_form_dict = lever_usage.from_dict(lever_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


