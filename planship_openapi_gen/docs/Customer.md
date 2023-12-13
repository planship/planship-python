# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata_** | **object** |  | [optional] 
**name** | **str** |  | [optional] [default to '']
**email** | **str** |  | [optional] [default to '']
**alternative_id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**subscriptions** | [**List[SubscriptionCustomer]**](SubscriptionCustomer.md) |  | 

## Example

```python
from planship_openapi_gen.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print Customer.to_json()

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_form_dict = customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


