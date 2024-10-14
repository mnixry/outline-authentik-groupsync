# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.captcha_stage import CaptchaStage
from authentik_openapi.models.pagination import Pagination
from authentik_openapi import util


class PaginatedCaptchaStageList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination: Pagination=None, results: List[CaptchaStage]=None):
        """PaginatedCaptchaStageList - a model defined in OpenAPI

        :param pagination: The pagination of this PaginatedCaptchaStageList.
        :param results: The results of this PaginatedCaptchaStageList.
        """
        self.openapi_types = {
            'pagination': Pagination,
            'results': List[CaptchaStage]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'results': 'results'
        }

        self._pagination = pagination
        self._results = results

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaginatedCaptchaStageList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaginatedCaptchaStageList of this PaginatedCaptchaStageList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this PaginatedCaptchaStageList.


        :return: The pagination of this PaginatedCaptchaStageList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginatedCaptchaStageList.


        :param pagination: The pagination of this PaginatedCaptchaStageList.
        :type pagination: Pagination
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")

        self._pagination = pagination

    @property
    def results(self):
        """Gets the results of this PaginatedCaptchaStageList.


        :return: The results of this PaginatedCaptchaStageList.
        :rtype: List[CaptchaStage]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedCaptchaStageList.


        :param results: The results of this PaginatedCaptchaStageList.
        :type results: List[CaptchaStage]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results
