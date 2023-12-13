# planship_openapi_gen.MeteredUsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lever_usage_for_customer**](MeteredUsageApi.md#get_lever_usage_for_customer) | **GET** /api/v1/customers/{customer_id}/products/{product_slug}/levers/{lever_slug}/usage | Get Lever Usage For Customer
[**get_metering_id_levers_usage_for_customer**](MeteredUsageApi.md#get_metering_id_levers_usage_for_customer) | **GET** /api/v1/customers/{customer_id}/products/{product_slug}/usage/{metering_id} | Get Metering Id Levers Usage For Customer
[**report_metered_usage_for_customer**](MeteredUsageApi.md#report_metered_usage_for_customer) | **POST** /api/v1/customers/{customer_id}/products/{product_slug}/usage/{metering_id} | Report Metered Usage For Customer


# **get_lever_usage_for_customer**
> LeverUsage get_lever_usage_for_customer(customer_id, product_slug, lever_slug)

Get Lever Usage For Customer

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.lever_usage import LeverUsage
from planship_openapi_gen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = planship_openapi_gen.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with planship_openapi_gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = planship_openapi_gen.MeteredUsageApi(api_client)
    customer_id = 'customer_id_example' # str | 
    product_slug = 'product_slug_example' # str | 
    lever_slug = 'lever_slug_example' # str | 

    try:
        # Get Lever Usage For Customer
        api_response = api_instance.get_lever_usage_for_customer(customer_id, product_slug, lever_slug)
        print("The response of MeteredUsageApi->get_lever_usage_for_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteredUsageApi->get_lever_usage_for_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **product_slug** | **str**|  | 
 **lever_slug** | **str**|  | 

### Return type

[**LeverUsage**](LeverUsage.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metering_id_levers_usage_for_customer**
> Dict[str, LeverUsage] get_metering_id_levers_usage_for_customer(customer_id, product_slug, metering_id)

Get Metering Id Levers Usage For Customer

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.lever_usage import LeverUsage
from planship_openapi_gen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = planship_openapi_gen.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with planship_openapi_gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = planship_openapi_gen.MeteredUsageApi(api_client)
    customer_id = 'customer_id_example' # str | 
    product_slug = 'product_slug_example' # str | 
    metering_id = 'metering_id_example' # str | 

    try:
        # Get Metering Id Levers Usage For Customer
        api_response = api_instance.get_metering_id_levers_usage_for_customer(customer_id, product_slug, metering_id)
        print("The response of MeteredUsageApi->get_metering_id_levers_usage_for_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteredUsageApi->get_metering_id_levers_usage_for_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **product_slug** | **str**|  | 
 **metering_id** | **str**|  | 

### Return type

[**Dict[str, LeverUsage]**](LeverUsage.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_metered_usage_for_customer**
> MeteringRecord report_metered_usage_for_customer(customer_id, product_slug, metering_id, metered_usage_in)

Report Metered Usage For Customer

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.metered_usage_in import MeteredUsageIn
from planship_openapi_gen.models.metering_record import MeteringRecord
from planship_openapi_gen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = planship_openapi_gen.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with planship_openapi_gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = planship_openapi_gen.MeteredUsageApi(api_client)
    customer_id = 'customer_id_example' # str | 
    product_slug = 'product_slug_example' # str | 
    metering_id = 'metering_id_example' # str | 
    metered_usage_in = planship_openapi_gen.MeteredUsageIn() # MeteredUsageIn | 

    try:
        # Report Metered Usage For Customer
        api_response = api_instance.report_metered_usage_for_customer(customer_id, product_slug, metering_id, metered_usage_in)
        print("The response of MeteredUsageApi->report_metered_usage_for_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeteredUsageApi->report_metered_usage_for_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **product_slug** | **str**|  | 
 **metering_id** | **str**|  | 
 **metered_usage_in** | [**MeteredUsageIn**](MeteredUsageIn.md)|  | 

### Return type

[**MeteringRecord**](MeteringRecord.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

