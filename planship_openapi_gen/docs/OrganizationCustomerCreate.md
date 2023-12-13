# OrganizationCustomerCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**name** | **str** |  | [optional] [default to '']
**email** | **str** |  | [optional] [default to '']
**alternative_id** | **str** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.organization_customer_create import OrganizationCustomerCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomerCreate from a JSON string
organization_customer_create_instance = OrganizationCustomerCreate.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomerCreate.to_json()

# convert the object into a dict
organization_customer_create_dict = organization_customer_create_instance.to_dict()
# create an instance of OrganizationCustomerCreate from a dict
organization_customer_create_form_dict = organization_customer_create.from_dict(organization_customer_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


