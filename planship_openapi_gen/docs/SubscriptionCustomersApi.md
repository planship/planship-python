# planship_openapi_gen.SubscriptionCustomersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_to_subscription**](SubscriptionCustomersApi.md#add_customer_to_subscription) | **POST** /api/v1/customers/{customer_id}/subscriptions/{subscription_id}/customers | Add Customer To Subscription
[**list_subscription_customers**](SubscriptionCustomersApi.md#list_subscription_customers) | **GET** /api/v1/customers/{customer_id}/subscriptions/{subscription_id}/customers | List Subscription Customers
[**remove_customer_from_subscription**](SubscriptionCustomersApi.md#remove_customer_from_subscription) | **DELETE** /api/v1/customers/{customer_id}/subscriptions/{subscription_id}/customers/{id} | Remove Customer From Subscription


# **add_customer_to_subscription**
> SubscriptionCustomer add_customer_to_subscription(customer_id, subscription_id, subscription_customer_add)

Add Customer To Subscription

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.subscription_customer import SubscriptionCustomer
from planship_openapi_gen.models.subscription_customer_add import SubscriptionCustomerAdd
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
    api_instance = planship_openapi_gen.SubscriptionCustomersApi(api_client)
    customer_id = 'customer_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 
    subscription_customer_add = planship_openapi_gen.SubscriptionCustomerAdd() # SubscriptionCustomerAdd | 

    try:
        # Add Customer To Subscription
        api_response = api_instance.add_customer_to_subscription(customer_id, subscription_id, subscription_customer_add)
        print("The response of SubscriptionCustomersApi->add_customer_to_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionCustomersApi->add_customer_to_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **subscription_customer_add** | [**SubscriptionCustomerAdd**](SubscriptionCustomerAdd.md)|  | 

### Return type

[**SubscriptionCustomer**](SubscriptionCustomer.md)

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

# **list_subscription_customers**
> List[SubscriptionCustomer] list_subscription_customers(customer_id, subscription_id)

List Subscription Customers

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.subscription_customer import SubscriptionCustomer
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
    api_instance = planship_openapi_gen.SubscriptionCustomersApi(api_client)
    customer_id = 'customer_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 

    try:
        # List Subscription Customers
        api_response = api_instance.list_subscription_customers(customer_id, subscription_id)
        print("The response of SubscriptionCustomersApi->list_subscription_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionCustomersApi->list_subscription_customers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **subscription_id** | **str**|  | 

### Return type

[**List[SubscriptionCustomer]**](SubscriptionCustomer.md)

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

# **remove_customer_from_subscription**
> SubscriptionCustomerInDbBase remove_customer_from_subscription(customer_id, subscription_id, id)

Remove Customer From Subscription

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.subscription_customer_in_db_base import SubscriptionCustomerInDbBase
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
    api_instance = planship_openapi_gen.SubscriptionCustomersApi(api_client)
    customer_id = 'customer_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Remove Customer From Subscription
        api_response = api_instance.remove_customer_from_subscription(customer_id, subscription_id, id)
        print("The response of SubscriptionCustomersApi->remove_customer_from_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionCustomersApi->remove_customer_from_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**SubscriptionCustomerInDbBase**](SubscriptionCustomerInDbBase.md)

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

