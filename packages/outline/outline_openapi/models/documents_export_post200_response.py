# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class DocumentsExportPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: str=None):
        """DocumentsExportPost200Response - a model defined in OpenAPI

        :param data: The data of this DocumentsExportPost200Response.
        """
        self.openapi_types = {
            'data': str
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DocumentsExportPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _documents_export_post_200_response of this DocumentsExportPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this DocumentsExportPost200Response.

        The document content in Markdown formatting

        :return: The data of this DocumentsExportPost200Response.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DocumentsExportPost200Response.

        The document content in Markdown formatting

        :param data: The data of this DocumentsExportPost200Response.
        :type data: str
        """

        self._data = data
