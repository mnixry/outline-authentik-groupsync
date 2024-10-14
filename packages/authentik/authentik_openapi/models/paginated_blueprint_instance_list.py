# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.models.pagination import Pagination
from authentik_openapi import util


class PaginatedBlueprintInstanceList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[BlueprintInstance]=None):
        """PaginatedBlueprintInstanceList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedBlueprintInstanceList.
        :param results: The results of this PaginatedBlueprintInstanceList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[BlueprintInstance]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedBlueprintInstanceList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedBlueprintInstanceList of this PaginatedBlueprintInstanceList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedBlueprintInstanceList.


        :return: The pagination of this PaginatedBlueprintInstanceList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedBlueprintInstanceList.


        :param pagination: The pagination of this PaginatedBlueprintInstanceList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedBlueprintInstanceList.


        :return: The results of this PaginatedBlueprintInstanceList.
        :rtype: List[BlueprintInstance]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedBlueprintInstanceList.


        :param results: The results of this PaginatedBlueprintInstanceList.
        :type results: List[BlueprintInstance]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
