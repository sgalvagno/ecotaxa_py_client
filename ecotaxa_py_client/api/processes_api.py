"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.23
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ecotaxa_py_client.api_client import ApiClient, Endpoint as _Endpoint
from ecotaxa_py_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ecotaxa_py_client.model.bulk_update_req import BulkUpdateReq
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.process_model import ProcessModel


class ProcessesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.process_query_process_process_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (ProcessModel,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/process/{process_id}',
                'operation_id': 'process_query_process_process_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'process_id',
                ],
                'required': [
                    'process_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'process_id':
                        (int,),
                },
                'attribute_map': {
                    'process_id': 'process_id',
                },
                'location_map': {
                    'process_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_processes_process_set_update_post_endpoint = _Endpoint(
            settings={
                'response_type': (int,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/process_set/update',
                'operation_id': 'update_processes_process_set_update_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'bulk_update_req',
                ],
                'required': [
                    'bulk_update_req',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bulk_update_req':
                        (BulkUpdateReq,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'bulk_update_req': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def process_query_process_process_id_get(
        self,
        process_id,
        **kwargs
    ):
        """Process Query  # noqa: E501

        Returns **information about the process** corresponding to the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.process_query_process_process_id_get(process_id, async_req=True)
        >>> result = thread.get()

        Args:
            process_id (int): Internal, the unique numeric id of this process.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ProcessModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['process_id'] = \
            process_id
        return self.process_query_process_process_id_get_endpoint.call_with_http_info(**kwargs)

    def update_processes_process_set_update_post(
        self,
        bulk_update_req,
        **kwargs
    ):
        """Update Processes  # noqa: E501

        Do the required **update for each process in the set.**  **Returns the number of updated entities.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_processes_process_set_update_post(bulk_update_req, async_req=True)
        >>> result = thread.get()

        Args:
            bulk_update_req (BulkUpdateReq):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            int
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['bulk_update_req'] = \
            bulk_update_req
        return self.update_processes_process_set_update_post_endpoint.call_with_http_info(**kwargs)

