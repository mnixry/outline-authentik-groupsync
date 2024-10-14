# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi.models.collections_group_memberships_post200_response_data import CollectionsGroupMembershipsPost200ResponseData
from outline_openapi.models.pagination import Pagination
from outline_openapi import util


class CollectionsGroupMembershipsPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: CollectionsGroupMembershipsPost200ResponseData=None, pagination: Pagination=None):
        """CollectionsGroupMembershipsPost200Response - a model defined in OpenAPI

        :param data: The data of this CollectionsGroupMembershipsPost200Response.
        :param pagination: The pagination of this CollectionsGroupMembershipsPost200Response.
        """
        self.openapi_types = {
            'data': CollectionsGroupMembershipsPost200ResponseData,
            'pagination': Pagination
        }

        self.attribute_map = {
            'data': 'data',
            'pagination': 'pagination'
        }

        self._data = data
        self._pagination = pagination

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionsGroupMembershipsPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _collections_group_memberships_post_200_response of this CollectionsGroupMembershipsPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CollectionsGroupMembershipsPost200Response.


        :return: The data of this CollectionsGroupMembershipsPost200Response.
        :rtype: CollectionsGroupMembershipsPost200ResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CollectionsGroupMembershipsPost200Response.


        :param data: The data of this CollectionsGroupMembershipsPost200Response.
        :type data: CollectionsGroupMembershipsPost200ResponseData
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this CollectionsGroupMembershipsPost200Response.


        :return: The pagination of this CollectionsGroupMembershipsPost200Response.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CollectionsGroupMembershipsPost200Response.


        :param pagination: The pagination of this CollectionsGroupMembershipsPost200Response.
        :type pagination: Pagination
        """

        self._pagination = pagination
