# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.geo_ip_policy import GeoIPPolicy
from authentik_openapi.models.pagination import Pagination
from authentik_openapi import util


class PaginatedGeoIPPolicyList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[GeoIPPolicy]=None):
        """PaginatedGeoIPPolicyList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedGeoIPPolicyList.
        :param results: The results of this PaginatedGeoIPPolicyList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[GeoIPPolicy]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedGeoIPPolicyList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedGeoIPPolicyList of this PaginatedGeoIPPolicyList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedGeoIPPolicyList.


        :return: The pagination of this PaginatedGeoIPPolicyList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedGeoIPPolicyList.


        :param pagination: The pagination of this PaginatedGeoIPPolicyList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedGeoIPPolicyList.


        :return: The results of this PaginatedGeoIPPolicyList.
        :rtype: List[GeoIPPolicy]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedGeoIPPolicyList.


        :param results: The results of this PaginatedGeoIPPolicyList.
        :type results: List[GeoIPPolicy]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
