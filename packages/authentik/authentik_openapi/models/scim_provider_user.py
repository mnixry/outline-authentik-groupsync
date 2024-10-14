# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.group_member import GroupMember
from authentik_openapi import util


class SCIMProviderUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, scim_id: str=None, user: int=None, user_obj: GroupMember=None, provider: int=None):
        """SCIMProviderUser - a model defined in OpenAPI

        :param id: The id of this SCIMProviderUser.
        :param scim_id: The scim_id of this SCIMProviderUser.
        :param user: The user of this SCIMProviderUser.
        :param user_obj: The user_obj of this SCIMProviderUser.
        :param provider: The provider of this SCIMProviderUser.
        """
        self.openapi_types = {
            'id': str,
            'scim_id': str,
            'user': int,
            'user_obj': GroupMember,
            'provider': int
        }

        self.attribute_map = {
            'id': 'id',
            'scim_id': 'scim_id',
            'user': 'user',
            'user_obj': 'user_obj',
            'provider': 'provider'
        }

        self._id = id
        self._scim_id = scim_id
        self._user = user
        self._user_obj = user_obj
        self._provider = provider

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SCIMProviderUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SCIMProviderUser of this SCIMProviderUser.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SCIMProviderUser.


        :return: The id of this SCIMProviderUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SCIMProviderUser.


        :param id: The id of this SCIMProviderUser.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def scim_id(self):
        """Gets the scim_id of this SCIMProviderUser.


        :return: The scim_id of this SCIMProviderUser.
        :rtype: str
        """
        return self._scim_id

    @scim_id.setter
    def scim_id(self, scim_id):
        """Sets the scim_id of this SCIMProviderUser.


        :param scim_id: The scim_id of this SCIMProviderUser.
        :type scim_id: str
        """
        if scim_id is None:
            raise ValueError("Invalid value for `scim_id`, must not be `None`")

        self._scim_id = scim_id

    @property
    def user(self):
        """Gets the user of this SCIMProviderUser.


        :return: The user of this SCIMProviderUser.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SCIMProviderUser.


        :param user: The user of this SCIMProviderUser.
        :type user: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def user_obj(self):
        """Gets the user_obj of this SCIMProviderUser.


        :return: The user_obj of this SCIMProviderUser.
        :rtype: GroupMember
        """
        return self._user_obj

    @user_obj.setter
    def user_obj(self, user_obj):
        """Sets the user_obj of this SCIMProviderUser.


        :param user_obj: The user_obj of this SCIMProviderUser.
        :type user_obj: GroupMember
        """
        if user_obj is None:
            raise ValueError("Invalid value for `user_obj`, must not be `None`")

        self._user_obj = user_obj

    @property
    def provider(self):
        """Gets the provider of this SCIMProviderUser.


        :return: The provider of this SCIMProviderUser.
        :rtype: int
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this SCIMProviderUser.


        :param provider: The provider of this SCIMProviderUser.
        :type provider: int
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider
