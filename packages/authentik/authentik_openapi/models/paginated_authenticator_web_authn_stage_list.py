# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.authenticator_web_authn_stage import AuthenticatorWebAuthnStage
from authentik_openapi.models.pagination import Pagination
from authentik_openapi import util


class PaginatedAuthenticatorWebAuthnStageList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[AuthenticatorWebAuthnStage]=None):
        """PaginatedAuthenticatorWebAuthnStageList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedAuthenticatorWebAuthnStageList.
        :param results: The results of this PaginatedAuthenticatorWebAuthnStageList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[AuthenticatorWebAuthnStage]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedAuthenticatorWebAuthnStageList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedAuthenticatorWebAuthnStageList of this PaginatedAuthenticatorWebAuthnStageList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedAuthenticatorWebAuthnStageList.


        :return: The pagination of this PaginatedAuthenticatorWebAuthnStageList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedAuthenticatorWebAuthnStageList.


        :param pagination: The pagination of this PaginatedAuthenticatorWebAuthnStageList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedAuthenticatorWebAuthnStageList.


        :return: The results of this PaginatedAuthenticatorWebAuthnStageList.
        :rtype: List[AuthenticatorWebAuthnStage]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedAuthenticatorWebAuthnStageList.


        :param results: The results of this PaginatedAuthenticatorWebAuthnStageList.
        :type results: List[AuthenticatorWebAuthnStage]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
