# BucketUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **int** |  | 
**bucket** | **str** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.bucket_usage import BucketUsage

# TODO update the JSON string below
json = "{}"
# create an instance of BucketUsage from a JSON string
bucket_usage_instance = BucketUsage.from_json(json)
# print the JSON string representation of the object
print BucketUsage.to_json()

# convert the object into a dict
bucket_usage_dict = bucket_usage_instance.to_dict()
# create an instance of BucketUsage from a dict
bucket_usage_form_dict = bucket_usage.from_dict(bucket_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


