# planship_openapi_gen.CustomerSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_subscription_for_customer**](CustomerSubscriptionsApi.md#create_plan_subscription_for_customer) | **POST** /api/v1/customers/{customer_id}/subscriptions | Create Plan Subscription For Customer
[**get_customer_plan_subscription**](CustomerSubscriptionsApi.md#get_customer_plan_subscription) | **GET** /api/v1/customers/{customer_id}/subscriptions/{subscription_id} | Get Customer Plan Subscription
[**list_customer_plan_subscriptions**](CustomerSubscriptionsApi.md#list_customer_plan_subscriptions) | **GET** /api/v1/customers/{customer_id}/subscriptions | List Customer Plan Subscriptions
[**modify_customer_plan_subscription**](CustomerSubscriptionsApi.md#modify_customer_plan_subscription) | **PATCH** /api/v1/customers/{customer_id}/subscriptions/{subscription_id} | Modify Customer Plan Subscription


# **create_plan_subscription_for_customer**
> SubscriptionWithPlan create_plan_subscription_for_customer(customer_id, subscription_create)

Create Plan Subscription For Customer

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.subscription_create import SubscriptionCreate
from planship_openapi_gen.models.subscription_with_plan import SubscriptionWithPlan
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
    api_instance = planship_openapi_gen.CustomerSubscriptionsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    subscription_create = planship_openapi_gen.SubscriptionCreate() # SubscriptionCreate | 

    try:
        # Create Plan Subscription For Customer
        api_response = api_instance.create_plan_subscription_for_customer(customer_id, subscription_create)
        print("The response of CustomerSubscriptionsApi->create_plan_subscription_for_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerSubscriptionsApi->create_plan_subscription_for_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **subscription_create** | [**SubscriptionCreate**](SubscriptionCreate.md)|  | 

### Return type

[**SubscriptionWithPlan**](SubscriptionWithPlan.md)

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

# **get_customer_plan_subscription**
> CustomerSubscriptionWithPlan get_customer_plan_subscription(customer_id, subscription_id)

Get Customer Plan Subscription

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.customer_subscription_with_plan import CustomerSubscriptionWithPlan
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
    api_instance = planship_openapi_gen.CustomerSubscriptionsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get Customer Plan Subscription
        api_response = api_instance.get_customer_plan_subscription(customer_id, subscription_id)
        print("The response of CustomerSubscriptionsApi->get_customer_plan_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerSubscriptionsApi->get_customer_plan_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **subscription_id** | **str**|  | 

### Return type

[**CustomerSubscriptionWithPlan**](CustomerSubscriptionWithPlan.md)

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

# **list_customer_plan_subscriptions**
> List[CustomerSubscriptionWithPlan] list_customer_plan_subscriptions(customer_id)

List Customer Plan Subscriptions

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.customer_subscription_with_plan import CustomerSubscriptionWithPlan
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
    api_instance = planship_openapi_gen.CustomerSubscriptionsApi(api_client)
    customer_id = 'customer_id_example' # str | 

    try:
        # List Customer Plan Subscriptions
        api_response = api_instance.list_customer_plan_subscriptions(customer_id)
        print("The response of CustomerSubscriptionsApi->list_customer_plan_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerSubscriptionsApi->list_customer_plan_subscriptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

[**List[CustomerSubscriptionWithPlan]**](CustomerSubscriptionWithPlan.md)

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

# **modify_customer_plan_subscription**
> CustomerSubscriptionWithPlan modify_customer_plan_subscription(customer_id, subscription_id, subscription_update_with_slugs)

Modify Customer Plan Subscription

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.customer_subscription_with_plan import CustomerSubscriptionWithPlan
from planship_openapi_gen.models.subscription_update_with_slugs import SubscriptionUpdateWithSlugs
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
    api_instance = planship_openapi_gen.CustomerSubscriptionsApi(api_client)
    customer_id = 'customer_id_example' # str | 
    subscription_id = 'subscription_id_example' # str | 
    subscription_update_with_slugs = planship_openapi_gen.SubscriptionUpdateWithSlugs() # SubscriptionUpdateWithSlugs | 

    try:
        # Modify Customer Plan Subscription
        api_response = api_instance.modify_customer_plan_subscription(customer_id, subscription_id, subscription_update_with_slugs)
        print("The response of CustomerSubscriptionsApi->modify_customer_plan_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerSubscriptionsApi->modify_customer_plan_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **subscription_update_with_slugs** | [**SubscriptionUpdateWithSlugs**](SubscriptionUpdateWithSlugs.md)|  | 

### Return type

[**CustomerSubscriptionWithPlan**](CustomerSubscriptionWithPlan.md)

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

