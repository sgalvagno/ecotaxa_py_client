# ecotaxa_cli_py.AuthentificationApi

All URIs are relative to *https://raw.githubusercontent.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_login_post**](AuthentificationApi.md#login_login_post) | **POST** /login | Login


# **login_login_post**
> str login_login_post(login_req)

Login

**Login barrier,**   If successful, the login will returns a **JWT** which will have to be used in bearer authentication scheme for subsequent calls.

### Example


```python
import time
import ecotaxa_cli_py
from ecotaxa_cli_py.api import authentification_api
from ecotaxa_cli_py.model.http_validation_error import HTTPValidationError
from ecotaxa_cli_py.model.login_req import LoginReq
from pprint import pprint
# Defining the host is optional and defaults to https://raw.githubusercontent.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://raw.githubusercontent.com/api"
)


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentification_api.AuthentificationApi(api_client)
    login_req = LoginReq(
        password="test!",
        username="ecotaxa.api.user@gmail.com",
    ) # LoginReq | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login_login_post(login_req)
        pprint(api_response)
    except ecotaxa_cli_py.ApiException as e:
        print("Exception when calling AuthentificationApi->login_login_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_req** | [**LoginReq**](LoginReq.md)|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
