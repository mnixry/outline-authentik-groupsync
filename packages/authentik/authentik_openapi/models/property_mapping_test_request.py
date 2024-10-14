# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class PropertyMappingTestRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user: int=None, context: Dict[str, object]=None, group: str=None):
        """PropertyMappingTestRequest - a model defined in OpenAPI

        :param user: The user of this PropertyMappingTestRequest.
        :param context: The context of this PropertyMappingTestRequest.
        :param group: The group of this PropertyMappingTestRequest.
        """
        self.openapi_types = {
            'user': int,
            'context': Dict[str, object],
            'group': str
        }

        self.attribute_map = {
            'user': 'user',
            'context': 'context',
            'group': 'group'
        }

        self._user = user
        self._context = context
        self._group = group

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PropertyMappingTestRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PropertyMappingTestRequest of this PropertyMappingTestRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user(self):
        """Gets the user of this PropertyMappingTestRequest.


        :return: The user of this PropertyMappingTestRequest.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PropertyMappingTestRequest.


        :param user: The user of this PropertyMappingTestRequest.
        :type user: int
        """

        self._user = user

    @property
    def context(self):
        """Gets the context of this PropertyMappingTestRequest.


        :return: The context of this PropertyMappingTestRequest.
        :rtype: Dict[str, object]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PropertyMappingTestRequest.


        :param context: The context of this PropertyMappingTestRequest.
        :type context: Dict[str, object]
        """

        self._context = context

    @property
    def group(self):
        """Gets the group of this PropertyMappingTestRequest.


        :return: The group of this PropertyMappingTestRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PropertyMappingTestRequest.


        :param group: The group of this PropertyMappingTestRequest.
        :type group: str
        """

        self._group = group
