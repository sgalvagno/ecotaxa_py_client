# ecotaxa_cli_py.InstrumentsApi

All URIs are relative to *https://raw.githubusercontent.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instrument_query_instruments_get**](InstrumentsApi.md#instrument_query_instruments_get) | **GET** /instruments/ | Instrument Query


# **instrument_query_instruments_get**
> [str] instrument_query_instruments_get(project_ids)

Instrument Query

Returns the list of instruments, inside specific project(s).

### Example


```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import instruments_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = instruments_api.InstrumentsApi(api_client)
    project_ids = "1,2,3" # str | String containing the list of one or more project id separated by non-num char.

    # example passing only required values which don't have defaults set
    try:
        # Instrument Query
        api_response = api_instance.instrument_query_instruments_get(project_ids)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling InstrumentsApi->instrument_query_instruments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| String containing the list of one or more project id separated by non-num char. |

### Return type

**[str]**

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
