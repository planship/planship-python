# planship_openapi_gen.CustomersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /api/v1/customers | Create Customer
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /api/v1/customers/{customer_id} | Delete Customer
[**get_customer**](CustomersApi.md#get_customer) | **GET** /api/v1/customers/{customer_id} | Get Customer


# **create_customer**
> Customer create_customer(organization_customer_create)

Create Customer

Create a new customer in the current organization.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.customer import Customer
from planship_openapi_gen.models.organization_customer_create import OrganizationCustomerCreate
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
    api_instance = planship_openapi_gen.CustomersApi(api_client)
    organization_customer_create = planship_openapi_gen.OrganizationCustomerCreate() # OrganizationCustomerCreate | 

    try:
        # Create Customer
        api_response = api_instance.create_customer(organization_customer_create)
        print("The response of CustomersApi->create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_customer_create** | [**OrganizationCustomerCreate**](OrganizationCustomerCreate.md)|  | 

### Return type

[**Customer**](Customer.md)

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

# **delete_customer**
> CustomerInDbBase delete_customer(customer_id)

Delete Customer

Delete the customer with a given id from the current organization.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.customer_in_db_base import CustomerInDbBase
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
    api_instance = planship_openapi_gen.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | 

    try:
        # Delete Customer
        api_response = api_instance.delete_customer(customer_id)
        print("The response of CustomersApi->delete_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

[**CustomerInDbBase**](CustomerInDbBase.md)

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

# **get_customer**
> CustomerInDbBase get_customer(customer_id)

Get Customer

Get the customer with a given id

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.customer_in_db_base import CustomerInDbBase
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
    api_instance = planship_openapi_gen.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | 

    try:
        # Get Customer
        api_response = api_instance.get_customer(customer_id)
        print("The response of CustomersApi->get_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

[**CustomerInDbBase**](CustomerInDbBase.md)

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

