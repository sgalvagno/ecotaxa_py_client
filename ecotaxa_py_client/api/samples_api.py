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
from ecotaxa_py_client.model.sample_model import SampleModel
from ecotaxa_py_client.model.sample_taxo_stats_model import SampleTaxoStatsModel


class SamplesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.sample_query_sample_sample_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (SampleModel,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/sample/{sample_id}',
                'operation_id': 'sample_query_sample_sample_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sample_id',
                ],
                'required': [
                    'sample_id',
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
                    'sample_id':
                        (int,),
                },
                'attribute_map': {
                    'sample_id': 'sample_id',
                },
                'location_map': {
                    'sample_id': 'path',
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
        self.sample_set_get_stats_sample_set_taxo_stats_get_endpoint = _Endpoint(
            settings={
                'response_type': ([SampleTaxoStatsModel],),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/sample_set/taxo_stats',
                'operation_id': 'sample_set_get_stats_sample_set_taxo_stats_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sample_ids',
                ],
                'required': [
                    'sample_ids',
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
                    'sample_ids':
                        (str,),
                },
                'attribute_map': {
                    'sample_ids': 'sample_ids',
                },
                'location_map': {
                    'sample_ids': 'query',
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
        self.samples_search_samples_search_get_endpoint = _Endpoint(
            settings={
                'response_type': ([SampleModel],),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/samples/search',
                'operation_id': 'samples_search_samples_search_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_ids',
                    'id_pattern',
                ],
                'required': [
                    'project_ids',
                    'id_pattern',
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
                    'project_ids':
                        (str,),
                    'id_pattern':
                        (str,),
                },
                'attribute_map': {
                    'project_ids': 'project_ids',
                    'id_pattern': 'id_pattern',
                },
                'location_map': {
                    'project_ids': 'query',
                    'id_pattern': 'query',
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
        self.update_samples_sample_set_update_post_endpoint = _Endpoint(
            settings={
                'response_type': (int,),
                'auth': [
                    'BearerOrCookieAuth'
                ],
                'endpoint_path': '/sample_set/update',
                'operation_id': 'update_samples_sample_set_update_post',
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

    def sample_query_sample_sample_id_get(
        self,
        sample_id,
        **kwargs
    ):
        """Sample Query  # noqa: E501

        Returns **information about the sample** corresponding to the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sample_query_sample_sample_id_get(sample_id, async_req=True)
        >>> result = thread.get()

        Args:
            sample_id (int): Internal, the unique numeric id of this sample.

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
            SampleModel
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
        kwargs['sample_id'] = \
            sample_id
        return self.sample_query_sample_sample_id_get_endpoint.call_with_http_info(**kwargs)

    def sample_set_get_stats_sample_set_taxo_stats_get(
        self,
        sample_ids,
        **kwargs
    ):
        """Sample Set Get Stats  # noqa: E501

        Returns **classification statistics** for the given set of samples.  EXPECT A SLOW RESPONSE : No cache of such information anywhere.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sample_set_get_stats_sample_set_taxo_stats_get(sample_ids, async_req=True)
        >>> result = thread.get()

        Args:
            sample_ids (str): String containing the list of one or more sample ids separated by non-num char.

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
            [SampleTaxoStatsModel]
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
        kwargs['sample_ids'] = \
            sample_ids
        return self.sample_set_get_stats_sample_set_taxo_stats_get_endpoint.call_with_http_info(**kwargs)

    def samples_search_samples_search_get(
        self,
        project_ids,
        id_pattern,
        **kwargs
    ):
        """Samples Search  # noqa: E501

        **Search for samples.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.samples_search_samples_search_get(project_ids, id_pattern, async_req=True)
        >>> result = thread.get()

        Args:
            project_ids (str): String containing the list of one or more project id separated by non-num char.
            id_pattern (str): Sample id textual pattern. Use * or '' for 'any matches'. Match is case-insensitive.

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
            [SampleModel]
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
        kwargs['project_ids'] = \
            project_ids
        kwargs['id_pattern'] = \
            id_pattern
        return self.samples_search_samples_search_get_endpoint.call_with_http_info(**kwargs)

    def update_samples_sample_set_update_post(
        self,
        bulk_update_req,
        **kwargs
    ):
        """Update Samples  # noqa: E501

        Do the required **update for each sample in the set.**   Any non-null field in the model is written to every impacted sample.  **Returns the number of updated entities.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_samples_sample_set_update_post(bulk_update_req, async_req=True)
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
        return self.update_samples_sample_set_update_post_endpoint.call_with_http_info(**kwargs)

