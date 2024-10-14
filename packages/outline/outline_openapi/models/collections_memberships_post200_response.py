# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi.models.collections_add_user_post200_response_data import CollectionsAddUserPost200ResponseData
from outline_openapi.models.pagination import Pagination
from outline_openapi import util


class CollectionsMembershipsPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: CollectionsAddUserPost200ResponseData=None, pagination: Pagination=None):
        """CollectionsMembershipsPost200Response - a model defined in OpenAPI

        :param data: The data of this CollectionsMembershipsPost200Response.
        :param pagination: The pagination of this CollectionsMembershipsPost200Response.
        """
        self.openapi_types = {
            'data': CollectionsAddUserPost200ResponseData,
            'pagination': Pagination
        }

        self.attribute_map = {
            'data': 'data',
            'pagination': 'pagination'
        }

        self._data = data
        self._pagination = pagination

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionsMembershipsPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _collections_memberships_post_200_response of this CollectionsMembershipsPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CollectionsMembershipsPost200Response.


        :return: The data of this CollectionsMembershipsPost200Response.
        :rtype: CollectionsAddUserPost200ResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CollectionsMembershipsPost200Response.


        :param data: The data of this CollectionsMembershipsPost200Response.
        :type data: CollectionsAddUserPost200ResponseData
        """

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this CollectionsMembershipsPost200Response.


        :return: The pagination of this CollectionsMembershipsPost200Response.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CollectionsMembershipsPost200Response.


        :param pagination: The pagination of this CollectionsMembershipsPost200Response.
        :type pagination: Pagination
        """

        self._pagination = pagination
