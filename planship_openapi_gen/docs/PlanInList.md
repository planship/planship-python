# PlanInList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** | Plan name | 
**description** | **str** | Plan description | 
**order** | **int** | Plan display order | [optional] 

## Example

```python
from planship_openapi_gen.models.plan_in_list import PlanInList

# TODO update the JSON string below
json = "{}"
# create an instance of PlanInList from a JSON string
plan_in_list_instance = PlanInList.from_json(json)
# print the JSON string representation of the object
print PlanInList.to_json()

# convert the object into a dict
plan_in_list_dict = plan_in_list_instance.to_dict()
# create an instance of PlanInList from a dict
plan_in_list_form_dict = plan_in_list.from_dict(plan_in_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


