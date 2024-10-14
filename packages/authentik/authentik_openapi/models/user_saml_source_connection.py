# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.source import Source
from authentik_openapi import util


class UserSAMLSourceConnection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: int=None, user: int=None, source: Source=None, created: datetime=None, identifier: str=None):
        """UserSAMLSourceConnection - a model defined in OpenAPI

        :param pk: The pk of this UserSAMLSourceConnection.
        :param user: The user of this UserSAMLSourceConnection.
        :param source: The source of this UserSAMLSourceConnection.
        :param created: The created of this UserSAMLSourceConnection.
        :param identifier: The identifier of this UserSAMLSourceConnection.
        """
        self.openapi_types = {
            'pk': int,
            'user': int,
            'source': Source,
            'created': datetime,
            'identifier': str
        }

        self.attribute_map = {
            'pk': 'pk',
            'user': 'user',
            'source': 'source',
            'created': 'created',
            'identifier': 'identifier'
        }

        self._pk = pk
        self._user = user
        self._source = source
        self._created = created
        self._identifier = identifier

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserSAMLSourceConnection':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserSAMLSourceConnection of this UserSAMLSourceConnection.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this UserSAMLSourceConnection.


        :return: The pk of this UserSAMLSourceConnection.
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this UserSAMLSourceConnection.


        :param pk: The pk of this UserSAMLSourceConnection.
        :type pk: int
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def user(self):
        """Gets the user of this UserSAMLSourceConnection.


        :return: The user of this UserSAMLSourceConnection.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserSAMLSourceConnection.


        :param user: The user of this UserSAMLSourceConnection.
        :type user: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def source(self):
        """Gets the source of this UserSAMLSourceConnection.


        :return: The source of this UserSAMLSourceConnection.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UserSAMLSourceConnection.


        :param source: The source of this UserSAMLSourceConnection.
        :type source: Source
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def created(self):
        """Gets the created of this UserSAMLSourceConnection.


        :return: The created of this UserSAMLSourceConnection.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserSAMLSourceConnection.


        :param created: The created of this UserSAMLSourceConnection.
        :type created: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def identifier(self):
        """Gets the identifier of this UserSAMLSourceConnection.


        :return: The identifier of this UserSAMLSourceConnection.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserSAMLSourceConnection.


        :param identifier: The identifier of this UserSAMLSourceConnection.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")

        self._identifier = identifier
