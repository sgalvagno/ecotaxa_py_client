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


class UserModel(object):
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
        'id': 'int',
        'email': 'str',
        'name': 'str',
        'organisation': 'str',
        'active': 'bool',
        'country': 'str',
        'usercreationdate': 'datetime',
        'usercreationreason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'name': 'name',
        'organisation': 'organisation',
        'active': 'active',
        'country': 'country',
        'usercreationdate': 'usercreationdate',
        'usercreationreason': 'usercreationreason'
    }

    def __init__(self, id=None, email=None, name=None, organisation=None, active=None, country=None, usercreationdate=None, usercreationreason=None, local_vars_configuration=None):  # noqa: E501
        """UserModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._name = None
        self._organisation = None
        self._active = None
        self._country = None
        self._usercreationdate = None
        self._usercreationreason = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.name = name
        if organisation is not None:
            self.organisation = organisation
        if active is not None:
            self.active = active
        if country is not None:
            self.country = country
        if usercreationdate is not None:
            self.usercreationdate = usercreationdate
        if usercreationreason is not None:
            self.usercreationreason = usercreationreason

    @property
    def id(self):
        """Gets the id of this UserModel.  # noqa: E501

        Unique user identifier  # noqa: E501

        :return: The id of this UserModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserModel.

        Unique user identifier  # noqa: E501

        :param id: The id of this UserModel.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this UserModel.  # noqa: E501

        User's email used during registration  # noqa: E501

        :return: The email of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserModel.

        User's email used during registration  # noqa: E501

        :param email: The email of this UserModel.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this UserModel.  # noqa: E501

        User's full name  # noqa: E501

        :return: The name of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserModel.

        User's full name  # noqa: E501

        :param name: The name of this UserModel.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organisation(self):
        """Gets the organisation of this UserModel.  # noqa: E501

        User's organisation  # noqa: E501

        :return: The organisation of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this UserModel.

        User's organisation  # noqa: E501

        :param organisation: The organisation of this UserModel.  # noqa: E501
        :type organisation: str
        """

        self._organisation = organisation

    @property
    def active(self):
        """Gets the active of this UserModel.  # noqa: E501

        User's Account status  # noqa: E501

        :return: The active of this UserModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserModel.

        User's Account status  # noqa: E501

        :param active: The active of this UserModel.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def country(self):
        """Gets the country of this UserModel.  # noqa: E501

        User's country  # noqa: E501

        :return: The country of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserModel.

        User's country  # noqa: E501

        :param country: The country of this UserModel.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def usercreationdate(self):
        """Gets the usercreationdate of this UserModel.  # noqa: E501

        User account creation date  # noqa: E501

        :return: The usercreationdate of this UserModel.  # noqa: E501
        :rtype: datetime
        """
        return self._usercreationdate

    @usercreationdate.setter
    def usercreationdate(self, usercreationdate):
        """Sets the usercreationdate of this UserModel.

        User account creation date  # noqa: E501

        :param usercreationdate: The usercreationdate of this UserModel.  # noqa: E501
        :type usercreationdate: datetime
        """

        self._usercreationdate = usercreationdate

    @property
    def usercreationreason(self):
        """Gets the usercreationreason of this UserModel.  # noqa: E501

        The reason of creation of this user account  # noqa: E501

        :return: The usercreationreason of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._usercreationreason

    @usercreationreason.setter
    def usercreationreason(self, usercreationreason):
        """Sets the usercreationreason of this UserModel.

        The reason of creation of this user account  # noqa: E501

        :param usercreationreason: The usercreationreason of this UserModel.  # noqa: E501
        :type usercreationreason: str
        """

        self._usercreationreason = usercreationreason

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
        if not isinstance(other, UserModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserModel):
            return True

        return self.to_dict() != other.to_dict()
