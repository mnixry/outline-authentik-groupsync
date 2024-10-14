# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.capabilities_enum import CapabilitiesEnum
from authentik_openapi.models.error_reporting_config import ErrorReportingConfig
from authentik_openapi import util


class Config(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error_reporting: ErrorReportingConfig=None, capabilities: List[CapabilitiesEnum]=None, cache_timeout: int=None, cache_timeout_flows: int=None, cache_timeout_policies: int=None, cache_timeout_reputation: int=None):
        """Config - a model defined in OpenAPI

        :param error_reporting: The error_reporting of this Config.
        :param capabilities: The capabilities of this Config.
        :param cache_timeout: The cache_timeout of this Config.
        :param cache_timeout_flows: The cache_timeout_flows of this Config.
        :param cache_timeout_policies: The cache_timeout_policies of this Config.
        :param cache_timeout_reputation: The cache_timeout_reputation of this Config.
        """
        self.openapi_types = {
            'error_reporting': ErrorReportingConfig,
            'capabilities': List[CapabilitiesEnum],
            'cache_timeout': int,
            'cache_timeout_flows': int,
            'cache_timeout_policies': int,
            'cache_timeout_reputation': int
        }

        self.attribute_map = {
            'error_reporting': 'error_reporting',
            'capabilities': 'capabilities',
            'cache_timeout': 'cache_timeout',
            'cache_timeout_flows': 'cache_timeout_flows',
            'cache_timeout_policies': 'cache_timeout_policies',
            'cache_timeout_reputation': 'cache_timeout_reputation'
        }

        self._error_reporting = error_reporting
        self._capabilities = capabilities
        self._cache_timeout = cache_timeout
        self._cache_timeout_flows = cache_timeout_flows
        self._cache_timeout_policies = cache_timeout_policies
        self._cache_timeout_reputation = cache_timeout_reputation

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Config':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Config of this Config.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_reporting(self):
        """Gets the error_reporting of this Config.


        :return: The error_reporting of this Config.
        :rtype: ErrorReportingConfig
        """
        return self._error_reporting

    @error_reporting.setter
    def error_reporting(self, error_reporting):
        """Sets the error_reporting of this Config.


        :param error_reporting: The error_reporting of this Config.
        :type error_reporting: ErrorReportingConfig
        """
        if error_reporting is None:
            raise ValueError("Invalid value for `error_reporting`, must not be `None`")

        self._error_reporting = error_reporting

    @property
    def capabilities(self):
        """Gets the capabilities of this Config.


        :return: The capabilities of this Config.
        :rtype: List[CapabilitiesEnum]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this Config.


        :param capabilities: The capabilities of this Config.
        :type capabilities: List[CapabilitiesEnum]
        """
        if capabilities is None:
            raise ValueError("Invalid value for `capabilities`, must not be `None`")

        self._capabilities = capabilities

    @property
    def cache_timeout(self):
        """Gets the cache_timeout of this Config.


        :return: The cache_timeout of this Config.
        :rtype: int
        """
        return self._cache_timeout

    @cache_timeout.setter
    def cache_timeout(self, cache_timeout):
        """Sets the cache_timeout of this Config.


        :param cache_timeout: The cache_timeout of this Config.
        :type cache_timeout: int
        """
        if cache_timeout is None:
            raise ValueError("Invalid value for `cache_timeout`, must not be `None`")

        self._cache_timeout = cache_timeout

    @property
    def cache_timeout_flows(self):
        """Gets the cache_timeout_flows of this Config.


        :return: The cache_timeout_flows of this Config.
        :rtype: int
        """
        return self._cache_timeout_flows

    @cache_timeout_flows.setter
    def cache_timeout_flows(self, cache_timeout_flows):
        """Sets the cache_timeout_flows of this Config.


        :param cache_timeout_flows: The cache_timeout_flows of this Config.
        :type cache_timeout_flows: int
        """
        if cache_timeout_flows is None:
            raise ValueError("Invalid value for `cache_timeout_flows`, must not be `None`")

        self._cache_timeout_flows = cache_timeout_flows

    @property
    def cache_timeout_policies(self):
        """Gets the cache_timeout_policies of this Config.


        :return: The cache_timeout_policies of this Config.
        :rtype: int
        """
        return self._cache_timeout_policies

    @cache_timeout_policies.setter
    def cache_timeout_policies(self, cache_timeout_policies):
        """Sets the cache_timeout_policies of this Config.


        :param cache_timeout_policies: The cache_timeout_policies of this Config.
        :type cache_timeout_policies: int
        """
        if cache_timeout_policies is None:
            raise ValueError("Invalid value for `cache_timeout_policies`, must not be `None`")

        self._cache_timeout_policies = cache_timeout_policies

    @property
    def cache_timeout_reputation(self):
        """Gets the cache_timeout_reputation of this Config.


        :return: The cache_timeout_reputation of this Config.
        :rtype: int
        """
        return self._cache_timeout_reputation

    @cache_timeout_reputation.setter
    def cache_timeout_reputation(self, cache_timeout_reputation):
        """Sets the cache_timeout_reputation of this Config.


        :param cache_timeout_reputation: The cache_timeout_reputation of this Config.
        :type cache_timeout_reputation: int
        """
        if cache_timeout_reputation is None:
            raise ValueError("Invalid value for `cache_timeout_reputation`, must not be `None`")

        self._cache_timeout_reputation = cache_timeout_reputation
