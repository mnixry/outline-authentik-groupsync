# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.models.pagination import Pagination
from authentik_openapi import util


class PaginatedLDAPProviderList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[LDAPProvider]=None):
        """PaginatedLDAPProviderList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedLDAPProviderList.
        :param results: The results of this PaginatedLDAPProviderList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[LDAPProvider]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedLDAPProviderList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedLDAPProviderList of this PaginatedLDAPProviderList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedLDAPProviderList.


        :return: The pagination of this PaginatedLDAPProviderList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedLDAPProviderList.


        :param pagination: The pagination of this PaginatedLDAPProviderList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedLDAPProviderList.


        :return: The results of this PaginatedLDAPProviderList.
        :rtype: List[LDAPProvider]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedLDAPProviderList.


        :param results: The results of this PaginatedLDAPProviderList.
        :type results: List[LDAPProvider]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
