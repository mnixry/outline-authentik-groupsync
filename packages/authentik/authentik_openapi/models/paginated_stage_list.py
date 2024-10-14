# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.pagination import Pagination
from authentik_openapi.models.stage import Stage
from authentik_openapi import util


class PaginatedStageList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[Stage]=None):
        """PaginatedStageList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedStageList.
        :param results: The results of this PaginatedStageList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[Stage]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedStageList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedStageList of this PaginatedStageList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedStageList.


        :return: The pagination of this PaginatedStageList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedStageList.


        :param pagination: The pagination of this PaginatedStageList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedStageList.


        :return: The results of this PaginatedStageList.
        :rtype: List[Stage]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedStageList.


        :param results: The results of this PaginatedStageList.
        :type results: List[Stage]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
