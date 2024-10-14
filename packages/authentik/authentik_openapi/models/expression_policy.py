# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class ExpressionPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, name: str=None, execution_logging: bool=None, component: str=None, verbose_name: str=None, verbose_name_plural: str=None, meta_model_name: str=None, bound_to: int=None, expression: str=None):
        """ExpressionPolicy - a model defined in OpenAPI

        :param pk: The pk of this ExpressionPolicy.
        :param name: The name of this ExpressionPolicy.
        :param execution_logging: The execution_logging of this ExpressionPolicy.
        :param component: The component of this ExpressionPolicy.
        :param verbose_name: The verbose_name of this ExpressionPolicy.
        :param verbose_name_plural: The verbose_name_plural of this ExpressionPolicy.
        :param meta_model_name: The meta_model_name of this ExpressionPolicy.
        :param bound_to: The bound_to of this ExpressionPolicy.
        :param expression: The expression of this ExpressionPolicy.
        """
        self.openapi_types = {
            'pk': str,
            'name': str,
            'execution_logging': bool,
            'component': str,
            'verbose_name': str,
            'verbose_name_plural': str,
            'meta_model_name': str,
            'bound_to': int,
            'expression': str
        }

        self.attribute_map = {
            'pk': 'pk',
            'name': 'name',
            'execution_logging': 'execution_logging',
            'component': 'component',
            'verbose_name': 'verbose_name',
            'verbose_name_plural': 'verbose_name_plural',
            'meta_model_name': 'meta_model_name',
            'bound_to': 'bound_to',
            'expression': 'expression'
        }

        self._pk = pk
        self._name = name
        self._execution_logging = execution_logging
        self._component = component
        self._verbose_name = verbose_name
        self._verbose_name_plural = verbose_name_plural
        self._meta_model_name = meta_model_name
        self._bound_to = bound_to
        self._expression = expression

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExpressionPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExpressionPolicy of this ExpressionPolicy.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this ExpressionPolicy.


        :return: The pk of this ExpressionPolicy.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this ExpressionPolicy.


        :param pk: The pk of this ExpressionPolicy.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this ExpressionPolicy.


        :return: The name of this ExpressionPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExpressionPolicy.


        :param name: The name of this ExpressionPolicy.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def execution_logging(self):
        """Gets the execution_logging of this ExpressionPolicy.

        When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.

        :return: The execution_logging of this ExpressionPolicy.
        :rtype: bool
        """
        return self._execution_logging

    @execution_logging.setter
    def execution_logging(self, execution_logging):
        """Sets the execution_logging of this ExpressionPolicy.

        When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.

        :param execution_logging: The execution_logging of this ExpressionPolicy.
        :type execution_logging: bool
        """

        self._execution_logging = execution_logging

    @property
    def component(self):
        """Gets the component of this ExpressionPolicy.

        Get object component so that we know how to edit the object

        :return: The component of this ExpressionPolicy.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ExpressionPolicy.

        Get object component so that we know how to edit the object

        :param component: The component of this ExpressionPolicy.
        :type component: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")

        self._component = component

    @property
    def verbose_name(self):
        """Gets the verbose_name of this ExpressionPolicy.

        Return object's verbose_name

        :return: The verbose_name of this ExpressionPolicy.
        :rtype: str
        """
        return self._verbose_name

    @verbose_name.setter
    def verbose_name(self, verbose_name):
        """Sets the verbose_name of this ExpressionPolicy.

        Return object's verbose_name

        :param verbose_name: The verbose_name of this ExpressionPolicy.
        :type verbose_name: str
        """
        if verbose_name is None:
            raise ValueError("Invalid value for `verbose_name`, must not be `None`")

        self._verbose_name = verbose_name

    @property
    def verbose_name_plural(self):
        """Gets the verbose_name_plural of this ExpressionPolicy.

        Return object's plural verbose_name

        :return: The verbose_name_plural of this ExpressionPolicy.
        :rtype: str
        """
        return self._verbose_name_plural

    @verbose_name_plural.setter
    def verbose_name_plural(self, verbose_name_plural):
        """Sets the verbose_name_plural of this ExpressionPolicy.

        Return object's plural verbose_name

        :param verbose_name_plural: The verbose_name_plural of this ExpressionPolicy.
        :type verbose_name_plural: str
        """
        if verbose_name_plural is None:
            raise ValueError("Invalid value for `verbose_name_plural`, must not be `None`")

        self._verbose_name_plural = verbose_name_plural

    @property
    def meta_model_name(self):
        """Gets the meta_model_name of this ExpressionPolicy.

        Return internal model name

        :return: The meta_model_name of this ExpressionPolicy.
        :rtype: str
        """
        return self._meta_model_name

    @meta_model_name.setter
    def meta_model_name(self, meta_model_name):
        """Sets the meta_model_name of this ExpressionPolicy.

        Return internal model name

        :param meta_model_name: The meta_model_name of this ExpressionPolicy.
        :type meta_model_name: str
        """
        if meta_model_name is None:
            raise ValueError("Invalid value for `meta_model_name`, must not be `None`")

        self._meta_model_name = meta_model_name

    @property
    def bound_to(self):
        """Gets the bound_to of this ExpressionPolicy.

        Return objects policy is bound to

        :return: The bound_to of this ExpressionPolicy.
        :rtype: int
        """
        return self._bound_to

    @bound_to.setter
    def bound_to(self, bound_to):
        """Sets the bound_to of this ExpressionPolicy.

        Return objects policy is bound to

        :param bound_to: The bound_to of this ExpressionPolicy.
        :type bound_to: int
        """
        if bound_to is None:
            raise ValueError("Invalid value for `bound_to`, must not be `None`")

        self._bound_to = bound_to

    @property
    def expression(self):
        """Gets the expression of this ExpressionPolicy.


        :return: The expression of this ExpressionPolicy.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ExpressionPolicy.


        :param expression: The expression of this ExpressionPolicy.
        :type expression: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")

        self._expression = expression
