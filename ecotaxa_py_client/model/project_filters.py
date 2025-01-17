"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.31
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ecotaxa_py_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from ecotaxa_py_client.exceptions import ApiAttributeError



class ProjectFilters(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('statusfilter',): {
            'max_length': 3,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'taxo': (str,),  # noqa: E501
            'taxochild': (str,),  # noqa: E501
            'statusfilter': (str,),  # noqa: E501
            'map_n': (str,),  # noqa: E501
            'map_w': (str,),  # noqa: E501
            'map_e': (str,),  # noqa: E501
            'map_s': (str,),  # noqa: E501
            'depthmin': (str,),  # noqa: E501
            'depthmax': (str,),  # noqa: E501
            'samples': (str,),  # noqa: E501
            'instrum': (str,),  # noqa: E501
            'daytime': (str,),  # noqa: E501
            'month': (str,),  # noqa: E501
            'fromdate': (str,),  # noqa: E501
            'todate': (str,),  # noqa: E501
            'fromtime': (str,),  # noqa: E501
            'totime': (str,),  # noqa: E501
            'inverttime': (str,),  # noqa: E501
            'validfromdate': (str,),  # noqa: E501
            'validtodate': (str,),  # noqa: E501
            'freenum': (str,),  # noqa: E501
            'freenumst': (str,),  # noqa: E501
            'freenumend': (str,),  # noqa: E501
            'freetxt': (str,),  # noqa: E501
            'freetxtval': (str,),  # noqa: E501
            'filt_annot': (str,),  # noqa: E501
            'filt_last_annot': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'taxo': 'taxo',  # noqa: E501
        'taxochild': 'taxochild',  # noqa: E501
        'statusfilter': 'statusfilter',  # noqa: E501
        'map_n': 'MapN',  # noqa: E501
        'map_w': 'MapW',  # noqa: E501
        'map_e': 'MapE',  # noqa: E501
        'map_s': 'MapS',  # noqa: E501
        'depthmin': 'depthmin',  # noqa: E501
        'depthmax': 'depthmax',  # noqa: E501
        'samples': 'samples',  # noqa: E501
        'instrum': 'instrum',  # noqa: E501
        'daytime': 'daytime',  # noqa: E501
        'month': 'month',  # noqa: E501
        'fromdate': 'fromdate',  # noqa: E501
        'todate': 'todate',  # noqa: E501
        'fromtime': 'fromtime',  # noqa: E501
        'totime': 'totime',  # noqa: E501
        'inverttime': 'inverttime',  # noqa: E501
        'validfromdate': 'validfromdate',  # noqa: E501
        'validtodate': 'validtodate',  # noqa: E501
        'freenum': 'freenum',  # noqa: E501
        'freenumst': 'freenumst',  # noqa: E501
        'freenumend': 'freenumend',  # noqa: E501
        'freetxt': 'freetxt',  # noqa: E501
        'freetxtval': 'freetxtval',  # noqa: E501
        'filt_annot': 'filt_annot',  # noqa: E501
        'filt_last_annot': 'filt_last_annot',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ProjectFilters - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            taxo (str): Coma-separated list of numeric taxonomy/category ids. Only include objects classified with one of them.. [optional]  # noqa: E501
            taxochild (str): If 'Y' and taxo is set, also include children of each member of 'taxo' list in taxonomy tree.. [optional]  # noqa: E501
            statusfilter (str): Include objects with given status:             'NV': Not validated              'PV': Predicted or Validated              'PVD': Predicted or Validated or Dubious             'NVM': Validated, but not by me              'VM': Validated by me              'U': Not classified             other: direct equality comparison with DB value          . [optional]  # noqa: E501
            map_n (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            map_w (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            map_e (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            map_s (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            depthmin (str): Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range.. [optional]  # noqa: E501
            depthmax (str): Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range.. [optional]  # noqa: E501
            samples (str): Coma-separated list of sample IDs, include only objects for these samples.. [optional]  # noqa: E501
            instrum (str): Instrument name, include objects for which sampling was done using this instrument.. [optional]  # noqa: E501
            daytime (str): Coma-separated list of sun position values: D for Day, U for Dusk, N for Night, A for Dawn (Aube in French).. [optional]  # noqa: E501
            month (str): Coma-separated list of month numbers, 1=Jan and so on.. [optional]  # noqa: E501
            fromdate (str): Format is 'YYYY-MM-DD', include objects collected after this date.. [optional]  # noqa: E501
            todate (str): Format is 'YYYY-MM-DD', include objects collected before this date.. [optional]  # noqa: E501
            fromtime (str): Format is 'HH24:MM:SS', include objects collected after this time of day.. [optional]  # noqa: E501
            totime (str): Format is 'HH24:MM:SS', include objects collected before this time of day.. [optional]  # noqa: E501
            inverttime (str): If '1', include objects outside fromtime and totime range.. [optional]  # noqa: E501
            validfromdate (str): Format is 'YYYY-MM-DD HH24:MI', include objects validated/set to dubious after this date+time.. [optional]  # noqa: E501
            validtodate (str): Format is 'YYYY-MM-DD HH24:MI', include objects validated/set to dubious before this date+time.. [optional]  # noqa: E501
            freenum (str): Numerical DB column number in Object as basis for the 2 following criteria (freenumst, freenumend).. [optional]  # noqa: E501
            freenumst (str): Start of included range for the column defined by freenum, in which objects are included.. [optional]  # noqa: E501
            freenumend (str): End of included range for the column defined by freenum, in which objects are included.. [optional]  # noqa: E501
            freetxt (str):  Textual DB column number as basis for following criteria (freetxtval)             If starts with 's' then it's a text column in Sample             If starts with 'a' then it's a text column in Acquisition              If starts with 'p' then it's a text column in Process              If starts with 'o' then it's a text column in Object .         . [optional]  # noqa: E501
            freetxtval (str): Text to match in the column defined by freetxt, for an object to be include.. [optional]  # noqa: E501
            filt_annot (str): Coma-separated list of annotators, i.e. persons who validated the classification at any point in time.. [optional]  # noqa: E501
            filt_last_annot (str): Coma-separated list of annotators, i.e. persons who validated the classification in last.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ProjectFilters - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            taxo (str): Coma-separated list of numeric taxonomy/category ids. Only include objects classified with one of them.. [optional]  # noqa: E501
            taxochild (str): If 'Y' and taxo is set, also include children of each member of 'taxo' list in taxonomy tree.. [optional]  # noqa: E501
            statusfilter (str): Include objects with given status:             'NV': Not validated              'PV': Predicted or Validated              'PVD': Predicted or Validated or Dubious             'NVM': Validated, but not by me              'VM': Validated by me              'U': Not classified             other: direct equality comparison with DB value          . [optional]  # noqa: E501
            map_n (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            map_w (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            map_e (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            map_s (str): If all 4 are set (MapN, MapW, MapE, MapS), include objects inside the defined bounding rectangle.. [optional]  # noqa: E501
            depthmin (str): Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range.. [optional]  # noqa: E501
            depthmax (str): Positive values. If both are set (depthmin, depthmax), include objects for which both depths (min and max) are inside the range.. [optional]  # noqa: E501
            samples (str): Coma-separated list of sample IDs, include only objects for these samples.. [optional]  # noqa: E501
            instrum (str): Instrument name, include objects for which sampling was done using this instrument.. [optional]  # noqa: E501
            daytime (str): Coma-separated list of sun position values: D for Day, U for Dusk, N for Night, A for Dawn (Aube in French).. [optional]  # noqa: E501
            month (str): Coma-separated list of month numbers, 1=Jan and so on.. [optional]  # noqa: E501
            fromdate (str): Format is 'YYYY-MM-DD', include objects collected after this date.. [optional]  # noqa: E501
            todate (str): Format is 'YYYY-MM-DD', include objects collected before this date.. [optional]  # noqa: E501
            fromtime (str): Format is 'HH24:MM:SS', include objects collected after this time of day.. [optional]  # noqa: E501
            totime (str): Format is 'HH24:MM:SS', include objects collected before this time of day.. [optional]  # noqa: E501
            inverttime (str): If '1', include objects outside fromtime and totime range.. [optional]  # noqa: E501
            validfromdate (str): Format is 'YYYY-MM-DD HH24:MI', include objects validated/set to dubious after this date+time.. [optional]  # noqa: E501
            validtodate (str): Format is 'YYYY-MM-DD HH24:MI', include objects validated/set to dubious before this date+time.. [optional]  # noqa: E501
            freenum (str): Numerical DB column number in Object as basis for the 2 following criteria (freenumst, freenumend).. [optional]  # noqa: E501
            freenumst (str): Start of included range for the column defined by freenum, in which objects are included.. [optional]  # noqa: E501
            freenumend (str): End of included range for the column defined by freenum, in which objects are included.. [optional]  # noqa: E501
            freetxt (str):  Textual DB column number as basis for following criteria (freetxtval)             If starts with 's' then it's a text column in Sample             If starts with 'a' then it's a text column in Acquisition              If starts with 'p' then it's a text column in Process              If starts with 'o' then it's a text column in Object .         . [optional]  # noqa: E501
            freetxtval (str): Text to match in the column defined by freetxt, for an object to be include.. [optional]  # noqa: E501
            filt_annot (str): Coma-separated list of annotators, i.e. persons who validated the classification at any point in time.. [optional]  # noqa: E501
            filt_last_annot (str): Coma-separated list of annotators, i.e. persons who validated the classification in last.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
