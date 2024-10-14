# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class SelectableStage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, name: str=None, verbose_name: str=None, meta_model_name: str=None):
        """SelectableStage - a model defined in OpenAPI

        :param pk: The pk of this SelectableStage.
        :param name: The name of this SelectableStage.
        :param verbose_name: The verbose_name of this SelectableStage.
        :param meta_model_name: The meta_model_name of this SelectableStage.
        """
        self.openapi_types = {
            'pk': str,
            'name': str,
            'verbose_name': str,
            'meta_model_name': str
        }

        self.attribute_map = {
            'pk': 'pk',
            'name': 'name',
            'verbose_name': 'verbose_name',
            'meta_model_name': 'meta_model_name'
        }

        self._pk = pk
        self._name = name
        self._verbose_name = verbose_name
        self._meta_model_name = meta_model_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SelectableStage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SelectableStage of this SelectableStage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this SelectableStage.


        :return: The pk of this SelectableStage.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this SelectableStage.


        :param pk: The pk of this SelectableStage.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this SelectableStage.


        :return: The name of this SelectableStage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SelectableStage.


        :param name: The name of this SelectableStage.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def verbose_name(self):
        """Gets the verbose_name of this SelectableStage.


        :return: The verbose_name of this SelectableStage.
        :rtype: str
        """
        return self._verbose_name

    @verbose_name.setter
    def verbose_name(self, verbose_name):
        """Sets the verbose_name of this SelectableStage.


        :param verbose_name: The verbose_name of this SelectableStage.
        :type verbose_name: str
        """
        if verbose_name is None:
            raise ValueError("Invalid value for `verbose_name`, must not be `None`")

        self._verbose_name = verbose_name

    @property
    def meta_model_name(self):
        """Gets the meta_model_name of this SelectableStage.


        :return: The meta_model_name of this SelectableStage.
        :rtype: str
        """
        return self._meta_model_name

    @meta_model_name.setter
    def meta_model_name(self, meta_model_name):
        """Sets the meta_model_name of this SelectableStage.


        :param meta_model_name: The meta_model_name of this SelectableStage.
        :type meta_model_name: str
        """
        if meta_model_name is None:
            raise ValueError("Invalid value for `meta_model_name`, must not be `None`")

        self._meta_model_name = meta_model_name
