# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.models.user import User
from authentik_openapi import util


class TokenModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: int=None, provider: OAuth2Provider=None, user: User=None, is_expired: bool=None, expires: datetime=None, scope: List[str]=None, id_token: str=None, revoked: bool=None):
        """TokenModel - a model defined in OpenAPI

        :param pk: The pk of this TokenModel.
        :param provider: The provider of this TokenModel.
        :param user: The user of this TokenModel.
        :param is_expired: The is_expired of this TokenModel.
        :param expires: The expires of this TokenModel.
        :param scope: The scope of this TokenModel.
        :param id_token: The id_token of this TokenModel.
        :param revoked: The revoked of this TokenModel.
        """
        self.openapi_types = {
            'pk': int,
            'provider': OAuth2Provider,
            'user': User,
            'is_expired': bool,
            'expires': datetime,
            'scope': List[str],
            'id_token': str,
            'revoked': bool
        }

        self.attribute_map = {
            'pk': 'pk',
            'provider': 'provider',
            'user': 'user',
            'is_expired': 'is_expired',
            'expires': 'expires',
            'scope': 'scope',
            'id_token': 'id_token',
            'revoked': 'revoked'
        }

        self._pk = pk
        self._provider = provider
        self._user = user
        self._is_expired = is_expired
        self._expires = expires
        self._scope = scope
        self._id_token = id_token
        self._revoked = revoked

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TokenModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TokenModel of this TokenModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this TokenModel.


        :return: The pk of this TokenModel.
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this TokenModel.


        :param pk: The pk of this TokenModel.
        :type pk: int
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def provider(self):
        """Gets the provider of this TokenModel.


        :return: The provider of this TokenModel.
        :rtype: OAuth2Provider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this TokenModel.


        :param provider: The provider of this TokenModel.
        :type provider: OAuth2Provider
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider

    @property
    def user(self):
        """Gets the user of this TokenModel.


        :return: The user of this TokenModel.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TokenModel.


        :param user: The user of this TokenModel.
        :type user: User
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def is_expired(self):
        """Gets the is_expired of this TokenModel.

        Check if token is expired yet.

        :return: The is_expired of this TokenModel.
        :rtype: bool
        """
        return self._is_expired

    @is_expired.setter
    def is_expired(self, is_expired):
        """Sets the is_expired of this TokenModel.

        Check if token is expired yet.

        :param is_expired: The is_expired of this TokenModel.
        :type is_expired: bool
        """
        if is_expired is None:
            raise ValueError("Invalid value for `is_expired`, must not be `None`")

        self._is_expired = is_expired

    @property
    def expires(self):
        """Gets the expires of this TokenModel.


        :return: The expires of this TokenModel.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this TokenModel.


        :param expires: The expires of this TokenModel.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def scope(self):
        """Gets the scope of this TokenModel.


        :return: The scope of this TokenModel.
        :rtype: List[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this TokenModel.


        :param scope: The scope of this TokenModel.
        :type scope: List[str]
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")

        self._scope = scope

    @property
    def id_token(self):
        """Gets the id_token of this TokenModel.

        Get the token's id_token as JSON String

        :return: The id_token of this TokenModel.
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this TokenModel.

        Get the token's id_token as JSON String

        :param id_token: The id_token of this TokenModel.
        :type id_token: str
        """
        if id_token is None:
            raise ValueError("Invalid value for `id_token`, must not be `None`")

        self._id_token = id_token

    @property
    def revoked(self):
        """Gets the revoked of this TokenModel.


        :return: The revoked of this TokenModel.
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this TokenModel.


        :param revoked: The revoked of this TokenModel.
        :type revoked: bool
        """

        self._revoked = revoked
