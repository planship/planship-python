# SubscriptionCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_** | **object** |  | [optional] 
**is_administrator** | **bool** |  | [optional] [default to False]
**is_subscriber** | **bool** |  | [optional] [default to True]
**customer_id** | **str** |  | 
**subscription_id** | **str** |  | 
**plan** | [**PlanInDbBase**](PlanInDbBase.md) |  | 

## Example

```python
from planship_openapi_gen.models.subscription_customer import SubscriptionCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCustomer from a JSON string
subscription_customer_instance = SubscriptionCustomer.from_json(json)
# print the JSON string representation of the object
print SubscriptionCustomer.to_json()

# convert the object into a dict
subscription_customer_dict = subscription_customer_instance.to_dict()
# create an instance of SubscriptionCustomer from a dict
subscription_customer_form_dict = subscription_customer.from_dict(subscription_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


