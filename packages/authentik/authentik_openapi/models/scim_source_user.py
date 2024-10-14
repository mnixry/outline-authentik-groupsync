# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.group_member import GroupMember
from authentik_openapi import util


class SCIMSourceUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, user: int=None, user_obj: GroupMember=None, source: str=None, attributes: object=None):
        """SCIMSourceUser - a model defined in OpenAPI

        :param id: The id of this SCIMSourceUser.
        :param user: The user of this SCIMSourceUser.
        :param user_obj: The user_obj of this SCIMSourceUser.
        :param source: The source of this SCIMSourceUser.
        :param attributes: The attributes of this SCIMSourceUser.
        """
        self.openapi_types = {
            'id': str,
            'user': int,
            'user_obj': GroupMember,
            'source': str,
            'attributes': object
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'user_obj': 'user_obj',
            'source': 'source',
            'attributes': 'attributes'
        }

        self._id = id
        self._user = user
        self._user_obj = user_obj
        self._source = source
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SCIMSourceUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SCIMSourceUser of this SCIMSourceUser.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SCIMSourceUser.


        :return: The id of this SCIMSourceUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SCIMSourceUser.


        :param id: The id of this SCIMSourceUser.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def user(self):
        """Gets the user of this SCIMSourceUser.


        :return: The user of this SCIMSourceUser.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SCIMSourceUser.


        :param user: The user of this SCIMSourceUser.
        :type user: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def user_obj(self):
        """Gets the user_obj of this SCIMSourceUser.


        :return: The user_obj of this SCIMSourceUser.
        :rtype: GroupMember
        """
        return self._user_obj

    @user_obj.setter
    def user_obj(self, user_obj):
        """Sets the user_obj of this SCIMSourceUser.


        :param user_obj: The user_obj of this SCIMSourceUser.
        :type user_obj: GroupMember
        """
        if user_obj is None:
            raise ValueError("Invalid value for `user_obj`, must not be `None`")

        self._user_obj = user_obj

    @property
    def source(self):
        """Gets the source of this SCIMSourceUser.


        :return: The source of this SCIMSourceUser.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SCIMSourceUser.


        :param source: The source of this SCIMSourceUser.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def attributes(self):
        """Gets the attributes of this SCIMSourceUser.


        :return: The attributes of this SCIMSourceUser.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SCIMSourceUser.


        :param attributes: The attributes of this SCIMSourceUser.
        :type attributes: object
        """

        self._attributes = attributes
