# planship_openapi_gen.ProductsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_subscription**](ProductsApi.md#create_plan_subscription) | **POST** /api/v1/products/{product_slug}/plans/{slug}/subscriptions | Create Plan Subscription
[**get_product**](ProductsApi.md#get_product) | **GET** /api/v1/products/{slug} | Get Product
[**get_product_lever**](ProductsApi.md#get_product_lever) | **GET** /api/v1/products/{product_slug}/levers/{slug} | Get Product Lever
[**get_product_plan**](ProductsApi.md#get_product_plan) | **GET** /api/v1/products/{product_slug}/plans/{slug} | Get Product Plan
[**get_product_plan_entitlements**](ProductsApi.md#get_product_plan_entitlements) | **GET** /api/v1/products/{product_slug}/plans/{slug}/entitlements | Get Product Plan Entitlements
[**list_product_levers**](ProductsApi.md#list_product_levers) | **GET** /api/v1/products/{slug}/levers | List Product Levers
[**list_product_plans**](ProductsApi.md#list_product_plans) | **GET** /api/v1/products/{slug}/plans | List Product Plans
[**list_products**](ProductsApi.md#list_products) | **GET** /api/v1/products | List Products


# **create_plan_subscription**
> SubscriptionWithPlan create_plan_subscription(product_slug, slug, plan_subscription_create)

Create Plan Subscription

Create a subscription to the product plan with given product and plan slugs for the customer described in subscription_customer_in. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.plan_subscription_create import PlanSubscriptionCreate
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    product_slug = 'product_slug_example' # str | 
    slug = 'slug_example' # str | 
    plan_subscription_create = planship_openapi_gen.PlanSubscriptionCreate() # PlanSubscriptionCreate | 

    try:
        # Create Plan Subscription
        api_response = api_instance.create_plan_subscription(product_slug, slug, plan_subscription_create)
        print("The response of ProductsApi->create_plan_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->create_plan_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_slug** | **str**|  | 
 **slug** | **str**|  | 
 **plan_subscription_create** | [**PlanSubscriptionCreate**](PlanSubscriptionCreate.md)|  | 

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

# **get_product**
> Product get_product(slug)

Get Product

Get a product with a given slug in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.product import Product
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Get Product
        api_response = api_instance.get_product(slug)
        print("The response of ProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Product**](Product.md)

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

# **get_product_lever**
> Lever get_product_lever(product_slug, slug)

Get Product Lever

Get the product lever for given product and lever slugs in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.lever import Lever
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    product_slug = 'product_slug_example' # str | 
    slug = 'slug_example' # str | 

    try:
        # Get Product Lever
        api_response = api_instance.get_product_lever(product_slug, slug)
        print("The response of ProductsApi->get_product_lever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_lever: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_slug** | **str**|  | 
 **slug** | **str**|  | 

### Return type

[**Lever**](Lever.md)

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

# **get_product_plan**
> Plan get_product_plan(product_slug, slug)

Get Product Plan

Get the product plan for given product and lever slugs in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.plan import Plan
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    product_slug = 'product_slug_example' # str | 
    slug = 'slug_example' # str | 

    try:
        # Get Product Plan
        api_response = api_instance.get_product_plan(product_slug, slug)
        print("The response of ProductsApi->get_product_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_slug** | **str**|  | 
 **slug** | **str**|  | 

### Return type

[**Plan**](Plan.md)

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

# **get_product_plan_entitlements**
> List[IdNameOrmBase] get_product_plan_entitlements(product_slug, slug)

Get Product Plan Entitlements

List all entitlements for the product plan with given product and plan slugs in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.id_name_orm_base import IdNameOrmBase
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    product_slug = 'product_slug_example' # str | 
    slug = 'slug_example' # str | 

    try:
        # Get Product Plan Entitlements
        api_response = api_instance.get_product_plan_entitlements(product_slug, slug)
        print("The response of ProductsApi->get_product_plan_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_plan_entitlements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_slug** | **str**|  | 
 **slug** | **str**|  | 

### Return type

[**List[IdNameOrmBase]**](IdNameOrmBase.md)

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

# **list_product_levers**
> List[IdNameSlugOrmBase] list_product_levers(slug)

List Product Levers

List all levers for the product with a given slug in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.id_name_slug_orm_base import IdNameSlugOrmBase
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # List Product Levers
        api_response = api_instance.list_product_levers(slug)
        print("The response of ProductsApi->list_product_levers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_product_levers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[IdNameSlugOrmBase]**](IdNameSlugOrmBase.md)

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

# **list_product_plans**
> List[PlanInList] list_product_plans(slug, public_only=public_only, order_by=order_by)

List Product Plans

List all plans for the product with a given slug in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.plan_in_list import PlanInList
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    slug = 'slug_example' # str | 
    public_only = False # bool |  (optional) (default to False)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # List Product Plans
        api_response = api_instance.list_product_plans(slug, public_only=public_only, order_by=order_by)
        print("The response of ProductsApi->list_product_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_product_plans: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **public_only** | **bool**|  | [optional] [default to False]
 **order_by** | **str**|  | [optional] 

### Return type

[**List[PlanInList]**](PlanInList.md)

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

# **list_products**
> List[IdNameSlugOrmBase] list_products(skip=skip, limit=limit)

List Products

List all products in the current organization. Organization is determined by the Planship API auth token.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import planship_openapi_gen
from planship_openapi_gen.models.id_name_slug_orm_base import IdNameSlugOrmBase
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
    api_instance = planship_openapi_gen.ProductsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Products
        api_response = api_instance.list_products(skip=skip, limit=limit)
        print("The response of ProductsApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[IdNameSlugOrmBase]**](IdNameSlugOrmBase.md)

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

