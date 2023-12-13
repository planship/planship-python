# CustomerInDbBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata_** | **object** |  | [optional] 
**name** | **str** |  | [optional] [default to '']
**email** | **str** |  | [optional] [default to '']
**alternative_id** | **str** |  | [optional] 
**organization_id** | **str** |  | 

## Example

```python
from planship_openapi_gen.models.customer_in_db_base import CustomerInDbBase

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInDbBase from a JSON string
customer_in_db_base_instance = CustomerInDbBase.from_json(json)
# print the JSON string representation of the object
print CustomerInDbBase.to_json()

# convert the object into a dict
customer_in_db_base_dict = customer_in_db_base_instance.to_dict()
# create an instance of CustomerInDbBase from a dict
customer_in_db_base_form_dict = customer_in_db_base.from_dict(customer_in_db_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


