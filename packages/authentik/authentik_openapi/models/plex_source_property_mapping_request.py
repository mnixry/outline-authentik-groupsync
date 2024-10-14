# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class PlexSourcePropertyMappingRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, managed: str=None, name: str=None, expression: str=None):
        """PlexSourcePropertyMappingRequest - a model defined in OpenAPI

        :param managed: The managed of this PlexSourcePropertyMappingRequest.
        :param name: The name of this PlexSourcePropertyMappingRequest.
        :param expression: The expression of this PlexSourcePropertyMappingRequest.
        """
        self.openapi_types = {
            'managed': str,
            'name': str,
            'expression': str
        }

        self.attribute_map = {
            'managed': 'managed',
            'name': 'name',
            'expression': 'expression'
        }

        self._managed = managed
        self._name = name
        self._expression = expression

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PlexSourcePropertyMappingRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PlexSourcePropertyMappingRequest of this PlexSourcePropertyMappingRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def managed(self):
        """Gets the managed of this PlexSourcePropertyMappingRequest.

        Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.

        :return: The managed of this PlexSourcePropertyMappingRequest.
        :rtype: str
        """
        return self._managed

    @managed.setter
    def managed(self, managed):
        """Sets the managed of this PlexSourcePropertyMappingRequest.

        Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.

        :param managed: The managed of this PlexSourcePropertyMappingRequest.
        :type managed: str
        """
        if managed is not None and len(managed) < 1:
            raise ValueError("Invalid value for `managed`, length must be greater than or equal to `1`")

        self._managed = managed

    @property
    def name(self):
        """Gets the name of this PlexSourcePropertyMappingRequest.


        :return: The name of this PlexSourcePropertyMappingRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlexSourcePropertyMappingRequest.


        :param name: The name of this PlexSourcePropertyMappingRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def expression(self):
        """Gets the expression of this PlexSourcePropertyMappingRequest.


        :return: The expression of this PlexSourcePropertyMappingRequest.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this PlexSourcePropertyMappingRequest.


        :param expression: The expression of this PlexSourcePropertyMappingRequest.
        :type expression: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")
        if expression is not None and len(expression) < 1:
            raise ValueError("Invalid value for `expression`, length must be greater than or equal to `1`")

        self._expression = expression
