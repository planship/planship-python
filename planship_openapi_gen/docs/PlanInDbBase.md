# PlanInDbBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**display_order** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] [default to '']
**display_description** | **str** |  | [optional] [default to '']
**display_extra_attributes** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] [default to '']
**name** | **str** |  | 
**max_subscribers** | **int** |  | [optional] [default to 1]
**is_self_serve** | **bool** |  | [optional] [default to True]
**is_public** | **bool** |  | [optional] [default to False]
**auto_renew** | **bool** |  | [optional] [default to True]
**duration_period** | **int** |  | [optional] [default to 1]
**duration_unit** | [**TimeUnits**](TimeUnits.md) |  | [optional] 
**id** | **str** |  | 

## Example

```python
from planship_openapi_gen.models.plan_in_db_base import PlanInDbBase

# TODO update the JSON string below
json = "{}"
# create an instance of PlanInDbBase from a JSON string
plan_in_db_base_instance = PlanInDbBase.from_json(json)
# print the JSON string representation of the object
print PlanInDbBase.to_json()

# convert the object into a dict
plan_in_db_base_dict = plan_in_db_base_instance.to_dict()
# create an instance of PlanInDbBase from a dict
plan_in_db_base_form_dict = plan_in_db_base.from_dict(plan_in_db_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


