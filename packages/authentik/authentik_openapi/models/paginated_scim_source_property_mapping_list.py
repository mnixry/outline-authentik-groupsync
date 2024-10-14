# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.pagination import Pagination
from authentik_openapi.models.scim_source_property_mapping import SCIMSourcePropertyMapping
from authentik_openapi import util


class PaginatedSCIMSourcePropertyMappingList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[SCIMSourcePropertyMapping]=None):
        """PaginatedSCIMSourcePropertyMappingList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedSCIMSourcePropertyMappingList.
        :param results: The results of this PaginatedSCIMSourcePropertyMappingList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[SCIMSourcePropertyMapping]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedSCIMSourcePropertyMappingList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedSCIMSourcePropertyMappingList of this PaginatedSCIMSourcePropertyMappingList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedSCIMSourcePropertyMappingList.


        :return: The pagination of this PaginatedSCIMSourcePropertyMappingList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedSCIMSourcePropertyMappingList.


        :param pagination: The pagination of this PaginatedSCIMSourcePropertyMappingList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedSCIMSourcePropertyMappingList.


        :return: The results of this PaginatedSCIMSourcePropertyMappingList.
        :rtype: List[SCIMSourcePropertyMapping]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedSCIMSourcePropertyMappingList.


        :param results: The results of this PaginatedSCIMSourcePropertyMappingList.
        :type results: List[SCIMSourcePropertyMapping]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
