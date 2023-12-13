# PlanEntitlement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Formatted text representation of the entitlement value | 
**name** | **str** | Entitlement name | 
**description** | **str** | Entitlement description | 
**order** | **int** | Entitlement display order | [optional] 
**configuration** | **object** | Entitlement configuration object | [optional] 

## Example

```python
from planship_openapi_gen.models.plan_entitlement import PlanEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of PlanEntitlement from a JSON string
plan_entitlement_instance = PlanEntitlement.from_json(json)
# print the JSON string representation of the object
print PlanEntitlement.to_json()

# convert the object into a dict
plan_entitlement_dict = plan_entitlement_instance.to_dict()
# create an instance of PlanEntitlement from a dict
plan_entitlement_form_dict = plan_entitlement.from_dict(plan_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


