# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class SCIMMapping(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, managed: str=None, name: str=None, expression: str=None, component: str=None, verbose_name: str=None, verbose_name_plural: str=None, meta_model_name: str=None):
        """SCIMMapping - a model defined in OpenAPI

        :param pk: The pk of this SCIMMapping.
        :param managed: The managed of this SCIMMapping.
        :param name: The name of this SCIMMapping.
        :param expression: The expression of this SCIMMapping.
        :param component: The component of this SCIMMapping.
        :param verbose_name: The verbose_name of this SCIMMapping.
        :param verbose_name_plural: The verbose_name_plural of this SCIMMapping.
        :param meta_model_name: The meta_model_name of this SCIMMapping.
        """
        self.openapi_types = {
            'pk': str,
            'managed': str,
            'name': str,
            'expression': str,
            'component': str,
            'verbose_name': str,
            'verbose_name_plural': str,
            'meta_model_name': str
        }

        self.attribute_map = {
            'pk': 'pk',
            'managed': 'managed',
            'name': 'name',
            'expression': 'expression',
            'component': 'component',
            'verbose_name': 'verbose_name',
            'verbose_name_plural': 'verbose_name_plural',
            'meta_model_name': 'meta_model_name'
        }

        self._pk = pk
        self._managed = managed
        self._name = name
        self._expression = expression
        self._component = component
        self._verbose_name = verbose_name
        self._verbose_name_plural = verbose_name_plural
        self._meta_model_name = meta_model_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SCIMMapping':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SCIMMapping of this SCIMMapping.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this SCIMMapping.


        :return: The pk of this SCIMMapping.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this SCIMMapping.


        :param pk: The pk of this SCIMMapping.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def managed(self):
        """Gets the managed of this SCIMMapping.

        Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.

        :return: The managed of this SCIMMapping.
        :rtype: str
        """
        return self._managed

    @managed.setter
    def managed(self, managed):
        """Sets the managed of this SCIMMapping.

        Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.

        :param managed: The managed of this SCIMMapping.
        :type managed: str
        """

        self._managed = managed

    @property
    def name(self):
        """Gets the name of this SCIMMapping.


        :return: The name of this SCIMMapping.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SCIMMapping.


        :param name: The name of this SCIMMapping.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def expression(self):
        """Gets the expression of this SCIMMapping.


        :return: The expression of this SCIMMapping.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this SCIMMapping.


        :param expression: The expression of this SCIMMapping.
        :type expression: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")

        self._expression = expression

    @property
    def component(self):
        """Gets the component of this SCIMMapping.

        Get object's component so that we know how to edit the object

        :return: The component of this SCIMMapping.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this SCIMMapping.

        Get object's component so that we know how to edit the object

        :param component: The component of this SCIMMapping.
        :type component: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")

        self._component = component

    @property
    def verbose_name(self):
        """Gets the verbose_name of this SCIMMapping.

        Return object's verbose_name

        :return: The verbose_name of this SCIMMapping.
        :rtype: str
        """
        return self._verbose_name

    @verbose_name.setter
    def verbose_name(self, verbose_name):
        """Sets the verbose_name of this SCIMMapping.

        Return object's verbose_name

        :param verbose_name: The verbose_name of this SCIMMapping.
        :type verbose_name: str
        """
        if verbose_name is None:
            raise ValueError("Invalid value for `verbose_name`, must not be `None`")

        self._verbose_name = verbose_name

    @property
    def verbose_name_plural(self):
        """Gets the verbose_name_plural of this SCIMMapping.

        Return object's plural verbose_name

        :return: The verbose_name_plural of this SCIMMapping.
        :rtype: str
        """
        return self._verbose_name_plural

    @verbose_name_plural.setter
    def verbose_name_plural(self, verbose_name_plural):
        """Sets the verbose_name_plural of this SCIMMapping.

        Return object's plural verbose_name

        :param verbose_name_plural: The verbose_name_plural of this SCIMMapping.
        :type verbose_name_plural: str
        """
        if verbose_name_plural is None:
            raise ValueError("Invalid value for `verbose_name_plural`, must not be `None`")

        self._verbose_name_plural = verbose_name_plural

    @property
    def meta_model_name(self):
        """Gets the meta_model_name of this SCIMMapping.

        Return internal model name

        :return: The meta_model_name of this SCIMMapping.
        :rtype: str
        """
        return self._meta_model_name

    @meta_model_name.setter
    def meta_model_name(self, meta_model_name):
        """Sets the meta_model_name of this SCIMMapping.

        Return internal model name

        :param meta_model_name: The meta_model_name of this SCIMMapping.
        :type meta_model_name: str
        """
        if meta_model_name is None:
            raise ValueError("Invalid value for `meta_model_name`, must not be `None`")

        self._meta_model_name = meta_model_name
