# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.extra_user_object_permission import ExtraUserObjectPermission
from authentik_openapi.models.pagination import Pagination
from authentik_openapi import util


class PaginatedExtraUserObjectPermissionList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[ExtraUserObjectPermission]=None):
        """PaginatedExtraUserObjectPermissionList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedExtraUserObjectPermissionList.
        :param results: The results of this PaginatedExtraUserObjectPermissionList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[ExtraUserObjectPermission]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedExtraUserObjectPermissionList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedExtraUserObjectPermissionList of this PaginatedExtraUserObjectPermissionList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedExtraUserObjectPermissionList.


        :return: The pagination of this PaginatedExtraUserObjectPermissionList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedExtraUserObjectPermissionList.


        :param pagination: The pagination of this PaginatedExtraUserObjectPermissionList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedExtraUserObjectPermissionList.


        :return: The results of this PaginatedExtraUserObjectPermissionList.
        :rtype: List[ExtraUserObjectPermission]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedExtraUserObjectPermissionList.


        :param results: The results of this PaginatedExtraUserObjectPermissionList.
        :type results: List[ExtraUserObjectPermission]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
