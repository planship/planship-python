# planship_openapi_gen.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](AuthApi.md#get_access_token) | **POST** /api/v1/auth/token | Get Access Token


# **get_access_token**
> TokenResponse get_access_token()

Get Access Token

Obtain an access token for client credentials

### Example

```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.token_response import TokenResponse
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

# Enter a context with an instance of the API client
with planship_openapi_gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = planship_openapi_gen.AuthApi(api_client)

    try:
        # Get Access Token
        api_response = api_instance.get_access_token()
        print("The response of AuthApi->get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_access_token: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

