# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.models.group_member import GroupMember
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi import util


class ConnectionToken(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, provider: int=None, provider_obj: RACProvider=None, endpoint: str=None, endpoint_obj: Endpoint=None, user: GroupMember=None):
        """ConnectionToken - a model defined in OpenAPI

        :param pk: The pk of this ConnectionToken.
        :param provider: The provider of this ConnectionToken.
        :param provider_obj: The provider_obj of this ConnectionToken.
        :param endpoint: The endpoint of this ConnectionToken.
        :param endpoint_obj: The endpoint_obj of this ConnectionToken.
        :param user: The user of this ConnectionToken.
        """
        self.openapi_types = {
            'pk': str,
            'provider': int,
            'provider_obj': RACProvider,
            'endpoint': str,
            'endpoint_obj': Endpoint,
            'user': GroupMember
        }

        self.attribute_map = {
            'pk': 'pk',
            'provider': 'provider',
            'provider_obj': 'provider_obj',
            'endpoint': 'endpoint',
            'endpoint_obj': 'endpoint_obj',
            'user': 'user'
        }

        self._pk = pk
        self._provider = provider
        self._provider_obj = provider_obj
        self._endpoint = endpoint
        self._endpoint_obj = endpoint_obj
        self._user = user

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConnectionToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConnectionToken of this ConnectionToken.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this ConnectionToken.


        :return: The pk of this ConnectionToken.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this ConnectionToken.


        :param pk: The pk of this ConnectionToken.
        :type pk: str
        """

        self._pk = pk

    @property
    def provider(self):
        """Gets the provider of this ConnectionToken.


        :return: The provider of this ConnectionToken.
        :rtype: int
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ConnectionToken.


        :param provider: The provider of this ConnectionToken.
        :type provider: int
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider

    @property
    def provider_obj(self):
        """Gets the provider_obj of this ConnectionToken.


        :return: The provider_obj of this ConnectionToken.
        :rtype: RACProvider
        """
        return self._provider_obj

    @provider_obj.setter
    def provider_obj(self, provider_obj):
        """Sets the provider_obj of this ConnectionToken.


        :param provider_obj: The provider_obj of this ConnectionToken.
        :type provider_obj: RACProvider
        """
        if provider_obj is None:
            raise ValueError("Invalid value for `provider_obj`, must not be `None`")

        self._provider_obj = provider_obj

    @property
    def endpoint(self):
        """Gets the endpoint of this ConnectionToken.


        :return: The endpoint of this ConnectionToken.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ConnectionToken.


        :param endpoint: The endpoint of this ConnectionToken.
        :type endpoint: str
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")

        self._endpoint = endpoint

    @property
    def endpoint_obj(self):
        """Gets the endpoint_obj of this ConnectionToken.


        :return: The endpoint_obj of this ConnectionToken.
        :rtype: Endpoint
        """
        return self._endpoint_obj

    @endpoint_obj.setter
    def endpoint_obj(self, endpoint_obj):
        """Sets the endpoint_obj of this ConnectionToken.


        :param endpoint_obj: The endpoint_obj of this ConnectionToken.
        :type endpoint_obj: Endpoint
        """
        if endpoint_obj is None:
            raise ValueError("Invalid value for `endpoint_obj`, must not be `None`")

        self._endpoint_obj = endpoint_obj

    @property
    def user(self):
        """Gets the user of this ConnectionToken.


        :return: The user of this ConnectionToken.
        :rtype: GroupMember
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ConnectionToken.


        :param user: The user of this ConnectionToken.
        :type user: GroupMember
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user
