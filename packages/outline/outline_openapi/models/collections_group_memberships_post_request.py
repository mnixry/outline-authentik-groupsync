# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi.models.permission import Permission
from outline_openapi import util


class CollectionsGroupMembershipsPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset: float=None, limit: float=None, id: str=None, query: str=None, permission: Permission=None):
        """CollectionsGroupMembershipsPostRequest - a model defined in OpenAPI

        :param offset: The offset of this CollectionsGroupMembershipsPostRequest.
        :param limit: The limit of this CollectionsGroupMembershipsPostRequest.
        :param id: The id of this CollectionsGroupMembershipsPostRequest.
        :param query: The query of this CollectionsGroupMembershipsPostRequest.
        :param permission: The permission of this CollectionsGroupMembershipsPostRequest.
        """
        self.openapi_types = {
            'offset': float,
            'limit': float,
            'id': str,
            'query': str,
            'permission': Permission
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'id': 'id',
            'query': 'query',
            'permission': 'permission'
        }

        self._offset = offset
        self._limit = limit
        self._id = id
        self._query = query
        self._permission = permission

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionsGroupMembershipsPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _collections_group_memberships_post_request of this CollectionsGroupMembershipsPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this CollectionsGroupMembershipsPostRequest.


        :return: The offset of this CollectionsGroupMembershipsPostRequest.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CollectionsGroupMembershipsPostRequest.


        :param offset: The offset of this CollectionsGroupMembershipsPostRequest.
        :type offset: float
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this CollectionsGroupMembershipsPostRequest.


        :return: The limit of this CollectionsGroupMembershipsPostRequest.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CollectionsGroupMembershipsPostRequest.


        :param limit: The limit of this CollectionsGroupMembershipsPostRequest.
        :type limit: float
        """

        self._limit = limit

    @property
    def id(self):
        """Gets the id of this CollectionsGroupMembershipsPostRequest.

        Identifier for the collection

        :return: The id of this CollectionsGroupMembershipsPostRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionsGroupMembershipsPostRequest.

        Identifier for the collection

        :param id: The id of this CollectionsGroupMembershipsPostRequest.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def query(self):
        """Gets the query of this CollectionsGroupMembershipsPostRequest.

        Filter memberships by group names

        :return: The query of this CollectionsGroupMembershipsPostRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CollectionsGroupMembershipsPostRequest.

        Filter memberships by group names

        :param query: The query of this CollectionsGroupMembershipsPostRequest.
        :type query: str
        """

        self._query = query

    @property
    def permission(self):
        """Gets the permission of this CollectionsGroupMembershipsPostRequest.


        :return: The permission of this CollectionsGroupMembershipsPostRequest.
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this CollectionsGroupMembershipsPostRequest.


        :param permission: The permission of this CollectionsGroupMembershipsPostRequest.
        :type permission: Permission
        """

        self._permission = permission
