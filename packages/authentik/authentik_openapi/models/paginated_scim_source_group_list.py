# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.pagination import Pagination
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
from authentik_openapi import util


class PaginatedSCIMSourceGroupList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[SCIMSourceGroup]=None):
        """PaginatedSCIMSourceGroupList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedSCIMSourceGroupList.
        :param results: The results of this PaginatedSCIMSourceGroupList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[SCIMSourceGroup]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedSCIMSourceGroupList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedSCIMSourceGroupList of this PaginatedSCIMSourceGroupList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedSCIMSourceGroupList.


        :return: The pagination of this PaginatedSCIMSourceGroupList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedSCIMSourceGroupList.


        :param pagination: The pagination of this PaginatedSCIMSourceGroupList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedSCIMSourceGroupList.


        :return: The results of this PaginatedSCIMSourceGroupList.
        :rtype: List[SCIMSourceGroup]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedSCIMSourceGroupList.


        :param results: The results of this PaginatedSCIMSourceGroupList.
        :type results: List[SCIMSourceGroup]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
