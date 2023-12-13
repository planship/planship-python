# MeteringRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_allocated** | **bool** |  | [optional] [default to False]
**usage** | **int** |  | 
**metering_id** | **str** |  | 
**customer_id** | **str** |  | 
**product_id** | **str** |  | 
**subscription_id** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 

## Example

```python
from planship_openapi_gen.models.metering_record import MeteringRecord

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringRecord from a JSON string
metering_record_instance = MeteringRecord.from_json(json)
# print the JSON string representation of the object
print MeteringRecord.to_json()

# convert the object into a dict
metering_record_dict = metering_record_instance.to_dict()
# create an instance of MeteringRecord from a dict
metering_record_form_dict = metering_record.from_dict(metering_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


