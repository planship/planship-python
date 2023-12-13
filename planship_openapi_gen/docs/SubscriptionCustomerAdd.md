# SubscriptionCustomerAdd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**is_administrator** | **bool** |  | [optional] [default to False]
**is_subscriber** | **bool** |  | [optional] [default to True]
**customer_id** | **str** |  | 

## Example

```python
from planship_openapi_gen.models.subscription_customer_add import SubscriptionCustomerAdd

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCustomerAdd from a JSON string
subscription_customer_add_instance = SubscriptionCustomerAdd.from_json(json)
# print the JSON string representation of the object
print SubscriptionCustomerAdd.to_json()

# convert the object into a dict
subscription_customer_add_dict = subscription_customer_add_instance.to_dict()
# create an instance of SubscriptionCustomerAdd from a dict
subscription_customer_add_form_dict = subscription_customer_add.from_dict(subscription_customer_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


