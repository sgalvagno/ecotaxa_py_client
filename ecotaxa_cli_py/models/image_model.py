# coding: utf-8

"""
    EcoTaxa

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.17
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from ecotaxa_cli_py.configuration import Configuration


class ImageModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'imgid': 'int',
        'objid': 'int',
        'imgrank': 'int',
        'file_name': 'str',
        'orig_file_name': 'str',
        'width': 'int',
        'height': 'int',
        'thumb_file_name': 'str',
        'thumb_width': 'int',
        'thumb_height': 'int'
    }

    attribute_map = {
        'imgid': 'imgid',
        'objid': 'objid',
        'imgrank': 'imgrank',
        'file_name': 'file_name',
        'orig_file_name': 'orig_file_name',
        'width': 'width',
        'height': 'height',
        'thumb_file_name': 'thumb_file_name',
        'thumb_width': 'thumb_width',
        'thumb_height': 'thumb_height'
    }

    def __init__(self, imgid=None, objid=None, imgrank=None, file_name=None, orig_file_name=None, width=None, height=None, thumb_file_name=None, thumb_width=None, thumb_height=None, local_vars_configuration=None):  # noqa: E501
        """ImageModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._imgid = None
        self._objid = None
        self._imgrank = None
        self._file_name = None
        self._orig_file_name = None
        self._width = None
        self._height = None
        self._thumb_file_name = None
        self._thumb_width = None
        self._thumb_height = None
        self.discriminator = None

        self.imgid = imgid
        if objid is not None:
            self.objid = objid
        self.imgrank = imgrank
        self.file_name = file_name
        self.orig_file_name = orig_file_name
        self.width = width
        self.height = height
        if thumb_file_name is not None:
            self.thumb_file_name = thumb_file_name
        if thumb_width is not None:
            self.thumb_width = thumb_width
        if thumb_height is not None:
            self.thumb_height = thumb_height

    @property
    def imgid(self):
        """Gets the imgid of this ImageModel.  # noqa: E501


        :return: The imgid of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._imgid

    @imgid.setter
    def imgid(self, imgid):
        """Sets the imgid of this ImageModel.


        :param imgid: The imgid of this ImageModel.  # noqa: E501
        :type imgid: int
        """
        if self.local_vars_configuration.client_side_validation and imgid is None:  # noqa: E501
            raise ValueError("Invalid value for `imgid`, must not be `None`")  # noqa: E501

        self._imgid = imgid

    @property
    def objid(self):
        """Gets the objid of this ImageModel.  # noqa: E501


        :return: The objid of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._objid

    @objid.setter
    def objid(self, objid):
        """Sets the objid of this ImageModel.


        :param objid: The objid of this ImageModel.  # noqa: E501
        :type objid: int
        """

        self._objid = objid

    @property
    def imgrank(self):
        """Gets the imgrank of this ImageModel.  # noqa: E501


        :return: The imgrank of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._imgrank

    @imgrank.setter
    def imgrank(self, imgrank):
        """Sets the imgrank of this ImageModel.


        :param imgrank: The imgrank of this ImageModel.  # noqa: E501
        :type imgrank: int
        """
        if self.local_vars_configuration.client_side_validation and imgrank is None:  # noqa: E501
            raise ValueError("Invalid value for `imgrank`, must not be `None`")  # noqa: E501

        self._imgrank = imgrank

    @property
    def file_name(self):
        """Gets the file_name of this ImageModel.  # noqa: E501


        :return: The file_name of this ImageModel.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ImageModel.


        :param file_name: The file_name of this ImageModel.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def orig_file_name(self):
        """Gets the orig_file_name of this ImageModel.  # noqa: E501


        :return: The orig_file_name of this ImageModel.  # noqa: E501
        :rtype: str
        """
        return self._orig_file_name

    @orig_file_name.setter
    def orig_file_name(self, orig_file_name):
        """Sets the orig_file_name of this ImageModel.


        :param orig_file_name: The orig_file_name of this ImageModel.  # noqa: E501
        :type orig_file_name: str
        """
        if self.local_vars_configuration.client_side_validation and orig_file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `orig_file_name`, must not be `None`")  # noqa: E501

        self._orig_file_name = orig_file_name

    @property
    def width(self):
        """Gets the width of this ImageModel.  # noqa: E501


        :return: The width of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ImageModel.


        :param width: The width of this ImageModel.  # noqa: E501
        :type width: int
        """
        if self.local_vars_configuration.client_side_validation and width is None:  # noqa: E501
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this ImageModel.  # noqa: E501


        :return: The height of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ImageModel.


        :param height: The height of this ImageModel.  # noqa: E501
        :type height: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def thumb_file_name(self):
        """Gets the thumb_file_name of this ImageModel.  # noqa: E501


        :return: The thumb_file_name of this ImageModel.  # noqa: E501
        :rtype: str
        """
        return self._thumb_file_name

    @thumb_file_name.setter
    def thumb_file_name(self, thumb_file_name):
        """Sets the thumb_file_name of this ImageModel.


        :param thumb_file_name: The thumb_file_name of this ImageModel.  # noqa: E501
        :type thumb_file_name: str
        """

        self._thumb_file_name = thumb_file_name

    @property
    def thumb_width(self):
        """Gets the thumb_width of this ImageModel.  # noqa: E501


        :return: The thumb_width of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._thumb_width

    @thumb_width.setter
    def thumb_width(self, thumb_width):
        """Sets the thumb_width of this ImageModel.


        :param thumb_width: The thumb_width of this ImageModel.  # noqa: E501
        :type thumb_width: int
        """

        self._thumb_width = thumb_width

    @property
    def thumb_height(self):
        """Gets the thumb_height of this ImageModel.  # noqa: E501


        :return: The thumb_height of this ImageModel.  # noqa: E501
        :rtype: int
        """
        return self._thumb_height

    @thumb_height.setter
    def thumb_height(self, thumb_height):
        """Sets the thumb_height of this ImageModel.


        :param thumb_height: The thumb_height of this ImageModel.  # noqa: E501
        :type thumb_height: int
        """

        self._thumb_height = thumb_height

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageModel):
            return True

        return self.to_dict() != other.to_dict()