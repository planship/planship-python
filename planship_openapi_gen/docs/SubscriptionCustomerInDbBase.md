# SubscriptionCustomerInDbBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_** | **object** |  | [optional] 
**is_administrator** | **bool** |  | [optional] [default to False]
**is_subscriber** | **bool** |  | [optional] [default to True]
**customer_id** | **str** |  | 
**subscription_id** | **str** |  | 

## Example

```python
from planship_openapi_gen.models.subscription_customer_in_db_base import SubscriptionCustomerInDbBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCustomerInDbBase from a JSON string
subscription_customer_in_db_base_instance = SubscriptionCustomerInDbBase.from_json(json)
# print the JSON string representation of the object
print SubscriptionCustomerInDbBase.to_json()

# convert the object into a dict
subscription_customer_in_db_base_dict = subscription_customer_in_db_base_instance.to_dict()
# create an instance of SubscriptionCustomerInDbBase from a dict
subscription_customer_in_db_base_form_dict = subscription_customer_in_db_base.from_dict(subscription_customer_in_db_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


