# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class SCIMProviderUserRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, scim_id: str=None, user: int=None, provider: int=None):
        """SCIMProviderUserRequest - a model defined in OpenAPI

        :param scim_id: The scim_id of this SCIMProviderUserRequest.
        :param user: The user of this SCIMProviderUserRequest.
        :param provider: The provider of this SCIMProviderUserRequest.
        """
        self.openapi_types = {
            'scim_id': str,
            'user': int,
            'provider': int
        }

        self.attribute_map = {
            'scim_id': 'scim_id',
            'user': 'user',
            'provider': 'provider'
        }

        self._scim_id = scim_id
        self._user = user
        self._provider = provider

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SCIMProviderUserRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SCIMProviderUserRequest of this SCIMProviderUserRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def scim_id(self):
        """Gets the scim_id of this SCIMProviderUserRequest.


        :return: The scim_id of this SCIMProviderUserRequest.
        :rtype: str
        """
        return self._scim_id

    @scim_id.setter
    def scim_id(self, scim_id):
        """Sets the scim_id of this SCIMProviderUserRequest.


        :param scim_id: The scim_id of this SCIMProviderUserRequest.
        :type scim_id: str
        """
        if scim_id is None:
            raise ValueError("Invalid value for `scim_id`, must not be `None`")
        if scim_id is not None and len(scim_id) < 1:
            raise ValueError("Invalid value for `scim_id`, length must be greater than or equal to `1`")

        self._scim_id = scim_id

    @property
    def user(self):
        """Gets the user of this SCIMProviderUserRequest.


        :return: The user of this SCIMProviderUserRequest.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SCIMProviderUserRequest.


        :param user: The user of this SCIMProviderUserRequest.
        :type user: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def provider(self):
        """Gets the provider of this SCIMProviderUserRequest.


        :return: The provider of this SCIMProviderUserRequest.
        :rtype: int
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this SCIMProviderUserRequest.


        :param provider: The provider of this SCIMProviderUserRequest.
        :type provider: int
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider
