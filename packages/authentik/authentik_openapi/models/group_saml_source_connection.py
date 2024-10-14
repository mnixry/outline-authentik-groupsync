# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.source import Source
from authentik_openapi import util


class GroupSAMLSourceConnection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: int=None, group: str=None, source: Source=None, identifier: str=None, created: datetime=None):
        """GroupSAMLSourceConnection - a model defined in OpenAPI

        :param pk: The pk of this GroupSAMLSourceConnection.
        :param group: The group of this GroupSAMLSourceConnection.
        :param source: The source of this GroupSAMLSourceConnection.
        :param identifier: The identifier of this GroupSAMLSourceConnection.
        :param created: The created of this GroupSAMLSourceConnection.
        """
        self.openapi_types = {
            'pk': int,
            'group': str,
            'source': Source,
            'identifier': str,
            'created': datetime
        }

        self.attribute_map = {
            'pk': 'pk',
            'group': 'group',
            'source': 'source',
            'identifier': 'identifier',
            'created': 'created'
        }

        self._pk = pk
        self._group = group
        self._source = source
        self._identifier = identifier
        self._created = created

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GroupSAMLSourceConnection':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GroupSAMLSourceConnection of this GroupSAMLSourceConnection.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this GroupSAMLSourceConnection.


        :return: The pk of this GroupSAMLSourceConnection.
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this GroupSAMLSourceConnection.


        :param pk: The pk of this GroupSAMLSourceConnection.
        :type pk: int
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def group(self):
        """Gets the group of this GroupSAMLSourceConnection.


        :return: The group of this GroupSAMLSourceConnection.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupSAMLSourceConnection.


        :param group: The group of this GroupSAMLSourceConnection.
        :type group: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")

        self._group = group

    @property
    def source(self):
        """Gets the source of this GroupSAMLSourceConnection.


        :return: The source of this GroupSAMLSourceConnection.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this GroupSAMLSourceConnection.


        :param source: The source of this GroupSAMLSourceConnection.
        :type source: Source
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def identifier(self):
        """Gets the identifier of this GroupSAMLSourceConnection.


        :return: The identifier of this GroupSAMLSourceConnection.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this GroupSAMLSourceConnection.


        :param identifier: The identifier of this GroupSAMLSourceConnection.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")

        self._identifier = identifier

    @property
    def created(self):
        """Gets the created of this GroupSAMLSourceConnection.


        :return: The created of this GroupSAMLSourceConnection.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GroupSAMLSourceConnection.


        :param created: The created of this GroupSAMLSourceConnection.
        :type created: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created
