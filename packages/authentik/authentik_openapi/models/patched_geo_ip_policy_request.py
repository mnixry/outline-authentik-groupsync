# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.country_code_enum import CountryCodeEnum
from authentik_openapi import util


class PatchedGeoIPPolicyRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, execution_logging: bool=None, asns: List[int]=None, countries: List[CountryCodeEnum]=None):
        """PatchedGeoIPPolicyRequest - a model defined in OpenAPI

        :param name: The name of this PatchedGeoIPPolicyRequest.
        :param execution_logging: The execution_logging of this PatchedGeoIPPolicyRequest.
        :param asns: The asns of this PatchedGeoIPPolicyRequest.
        :param countries: The countries of this PatchedGeoIPPolicyRequest.
        """
        self.openapi_types = {
            'name': str,
            'execution_logging': bool,
            'asns': List[int],
            'countries': List[CountryCodeEnum]
        }

        self.attribute_map = {
            'name': 'name',
            'execution_logging': 'execution_logging',
            'asns': 'asns',
            'countries': 'countries'
        }

        self._name = name
        self._execution_logging = execution_logging
        self._asns = asns
        self._countries = countries

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatchedGeoIPPolicyRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatchedGeoIPPolicyRequest of this PatchedGeoIPPolicyRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this PatchedGeoIPPolicyRequest.


        :return: The name of this PatchedGeoIPPolicyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedGeoIPPolicyRequest.


        :param name: The name of this PatchedGeoIPPolicyRequest.
        :type name: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def execution_logging(self):
        """Gets the execution_logging of this PatchedGeoIPPolicyRequest.

        When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.

        :return: The execution_logging of this PatchedGeoIPPolicyRequest.
        :rtype: bool
        """
        return self._execution_logging

    @execution_logging.setter
    def execution_logging(self, execution_logging):
        """Sets the execution_logging of this PatchedGeoIPPolicyRequest.

        When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.

        :param execution_logging: The execution_logging of this PatchedGeoIPPolicyRequest.
        :type execution_logging: bool
        """

        self._execution_logging = execution_logging

    @property
    def asns(self):
        """Gets the asns of this PatchedGeoIPPolicyRequest.


        :return: The asns of this PatchedGeoIPPolicyRequest.
        :rtype: List[int]
        """
        return self._asns

    @asns.setter
    def asns(self, asns):
        """Sets the asns of this PatchedGeoIPPolicyRequest.


        :param asns: The asns of this PatchedGeoIPPolicyRequest.
        :type asns: List[int]
        """

        self._asns = asns

    @property
    def countries(self):
        """Gets the countries of this PatchedGeoIPPolicyRequest.


        :return: The countries of this PatchedGeoIPPolicyRequest.
        :rtype: List[CountryCodeEnum]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this PatchedGeoIPPolicyRequest.


        :param countries: The countries of this PatchedGeoIPPolicyRequest.
        :type countries: List[CountryCodeEnum]
        """
        if countries is not None and len(countries) > 249:
            raise ValueError("Invalid value for `countries`, number of items must be less than or equal to `249`")

        self._countries = countries
