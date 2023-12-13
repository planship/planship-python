# Lever


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**id** | **str** |  | 
**display_order** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] [default to '']
**display_description** | **str** |  | [optional] [default to '']
**display_extra_attributes** | **Dict[str, str]** |  | [optional] 
**configuration** | **object** |  | [optional] 
**description** | **str** |  | [optional] [default to '']
**name** | **str** |  | 
**entitlement_display_value_template** | **str** |  | [optional] [default to '']
**entitlement_display_name_template** | **str** |  | [optional] [default to '']
**entitlement_display_description_template** | **str** |  | [optional] [default to '']
**lever_type_id** | **str** |  | 
**product_id** | **str** |  | 
**metering_ids** | **List[str]** |  | 
**entitlement_schema_json** | **object** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.lever import Lever

# TODO update the JSON string below
json = "{}"
# create an instance of Lever from a JSON string
lever_instance = Lever.from_json(json)
# print the JSON string representation of the object
print Lever.to_json()

# convert the object into a dict
lever_dict = lever_instance.to_dict()
# create an instance of Lever from a dict
lever_form_dict = lever.from_dict(lever_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


