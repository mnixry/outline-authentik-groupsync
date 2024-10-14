# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi.models.permission import Permission
from outline_openapi import util


class CollectionsUpdatePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, permission: Permission=None, description: str=None, color: str=None):
        """CollectionsUpdatePostRequest - a model defined in OpenAPI

        :param id: The id of this CollectionsUpdatePostRequest.
        :param name: The name of this CollectionsUpdatePostRequest.
        :param permission: The permission of this CollectionsUpdatePostRequest.
        :param description: The description of this CollectionsUpdatePostRequest.
        :param color: The color of this CollectionsUpdatePostRequest.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'permission': Permission,
            'description': str,
            'color': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'permission': 'permission',
            'description': 'description',
            'color': 'color'
        }

        self._id = id
        self._name = name
        self._permission = permission
        self._description = description
        self._color = color

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionsUpdatePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _collections_update_post_request of this CollectionsUpdatePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CollectionsUpdatePostRequest.


        :return: The id of this CollectionsUpdatePostRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionsUpdatePostRequest.


        :param id: The id of this CollectionsUpdatePostRequest.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this CollectionsUpdatePostRequest.


        :return: The name of this CollectionsUpdatePostRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CollectionsUpdatePostRequest.


        :param name: The name of this CollectionsUpdatePostRequest.
        :type name: str
        """

        self._name = name

    @property
    def permission(self):
        """Gets the permission of this CollectionsUpdatePostRequest.


        :return: The permission of this CollectionsUpdatePostRequest.
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this CollectionsUpdatePostRequest.


        :param permission: The permission of this CollectionsUpdatePostRequest.
        :type permission: Permission
        """

        self._permission = permission

    @property
    def description(self):
        """Gets the description of this CollectionsUpdatePostRequest.


        :return: The description of this CollectionsUpdatePostRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CollectionsUpdatePostRequest.


        :param description: The description of this CollectionsUpdatePostRequest.
        :type description: str
        """

        self._description = description

    @property
    def color(self):
        """Gets the color of this CollectionsUpdatePostRequest.


        :return: The color of this CollectionsUpdatePostRequest.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CollectionsUpdatePostRequest.


        :param color: The color of this CollectionsUpdatePostRequest.
        :type color: str
        """

        self._color = color
