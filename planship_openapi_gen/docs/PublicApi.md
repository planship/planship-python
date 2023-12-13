# planship_openapi_gen.PublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_plan**](PublicApi.md#get_public_plan) | **GET** /api/v1/public/{organization_slug}/{product_slug}/plans/{plan_slug} | Get Public Plan
[**list_public_plans**](PublicApi.md#list_public_plans) | **GET** /api/v1/public/{organization_slug}/{product_slug}/plans | List Public Plans


# **get_public_plan**
> Plan get_public_plan(organization_slug, product_slug, plan_slug)

Get Public Plan

### Example

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


# Enter a context with an instance of the API client
with planship_openapi_gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = planship_openapi_gen.PublicApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    product_slug = 'product_slug_example' # str | 
    plan_slug = 'plan_slug_example' # str | 

    try:
        # Get Public Plan
        api_response = api_instance.get_public_plan(organization_slug, product_slug, plan_slug)
        print("The response of PublicApi->get_public_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_public_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **product_slug** | **str**|  | 
 **plan_slug** | **str**|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_plans**
> List[PlanInList] list_public_plans(organization_slug, product_slug)

List Public Plans

### Example

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


# Enter a context with an instance of the API client
with planship_openapi_gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = planship_openapi_gen.PublicApi(api_client)
    organization_slug = 'organization_slug_example' # str | 
    product_slug = 'product_slug_example' # str | 

    try:
        # List Public Plans
        api_response = api_instance.list_public_plans(organization_slug, product_slug)
        print("The response of PublicApi->list_public_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->list_public_plans: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_slug** | **str**|  | 
 **product_slug** | **str**|  | 

### Return type

[**List[PlanInList]**](PlanInList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

