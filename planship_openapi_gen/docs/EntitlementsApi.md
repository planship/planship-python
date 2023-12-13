# planship_openapi_gen.EntitlementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_entitlements_for_customer**](EntitlementsApi.md#get_product_entitlements_for_customer) | **GET** /api/v1/customers/{customer_id}/products/{product_slug}/entitlements | Get Product Entitlements For Customer


# **get_product_entitlements_for_customer**
> object get_product_entitlements_for_customer(product_slug, customer_id)

Get Product Entitlements For Customer

List all entitlements for the customer with a given id and the product with a given slug. Entitlements are returned as a dictionary keyed by lever slugs.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
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
    api_instance = planship_openapi_gen.EntitlementsApi(api_client)
    product_slug = 'product_slug_example' # str | 
    customer_id = 'customer_id_example' # str | 

    try:
        # Get Product Entitlements For Customer
        api_response = api_instance.get_product_entitlements_for_customer(product_slug, customer_id)
        print("The response of EntitlementsApi->get_product_entitlements_for_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_product_entitlements_for_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_slug** | **str**|  | 
 **customer_id** | **str**|  | 

### Return type

**object**

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

