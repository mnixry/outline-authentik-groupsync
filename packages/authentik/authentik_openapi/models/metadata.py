# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class Metadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, labels: Dict[str, object]=None):
        """Metadata - a model defined in OpenAPI

        :param name: The name of this Metadata.
        :param labels: The labels of this Metadata.
        """
        self.openapi_types = {
            'name': str,
            'labels': Dict[str, object]
        }

        self.attribute_map = {
            'name': 'name',
            'labels': 'labels'
        }

        self._name = name
        self._labels = labels

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Metadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Metadata of this Metadata.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Metadata.


        :return: The name of this Metadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metadata.


        :param name: The name of this Metadata.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def labels(self):
        """Gets the labels of this Metadata.


        :return: The labels of this Metadata.
        :rtype: Dict[str, object]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Metadata.


        :param labels: The labels of this Metadata.
        :type labels: Dict[str, object]
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")

        self._labels = labels
