# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class DummyPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, name: str=None, execution_logging: bool=None, component: str=None, verbose_name: str=None, verbose_name_plural: str=None, meta_model_name: str=None, bound_to: int=None, result: bool=None, wait_min: int=None, wait_max: int=None):
        """DummyPolicy - a model defined in OpenAPI

        :param pk: The pk of this DummyPolicy.
        :param name: The name of this DummyPolicy.
        :param execution_logging: The execution_logging of this DummyPolicy.
        :param component: The component of this DummyPolicy.
        :param verbose_name: The verbose_name of this DummyPolicy.
        :param verbose_name_plural: The verbose_name_plural of this DummyPolicy.
        :param meta_model_name: The meta_model_name of this DummyPolicy.
        :param bound_to: The bound_to of this DummyPolicy.
        :param result: The result of this DummyPolicy.
        :param wait_min: The wait_min of this DummyPolicy.
        :param wait_max: The wait_max of this DummyPolicy.
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
            'result': bool,
            'wait_min': int,
            'wait_max': int
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
            'result': 'result',
            'wait_min': 'wait_min',
            'wait_max': 'wait_max'
        }

        self._pk = pk
        self._name = name
        self._execution_logging = execution_logging
        self._component = component
        self._verbose_name = verbose_name
        self._verbose_name_plural = verbose_name_plural
        self._meta_model_name = meta_model_name
        self._bound_to = bound_to
        self._result = result
        self._wait_min = wait_min
        self._wait_max = wait_max

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DummyPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DummyPolicy of this DummyPolicy.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this DummyPolicy.


        :return: The pk of this DummyPolicy.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this DummyPolicy.


        :param pk: The pk of this DummyPolicy.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this DummyPolicy.


        :return: The name of this DummyPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DummyPolicy.


        :param name: The name of this DummyPolicy.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def execution_logging(self):
        """Gets the execution_logging of this DummyPolicy.

        When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.

        :return: The execution_logging of this DummyPolicy.
        :rtype: bool
        """
        return self._execution_logging

    @execution_logging.setter
    def execution_logging(self, execution_logging):
        """Sets the execution_logging of this DummyPolicy.

        When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.

        :param execution_logging: The execution_logging of this DummyPolicy.
        :type execution_logging: bool
        """

        self._execution_logging = execution_logging

    @property
    def component(self):
        """Gets the component of this DummyPolicy.

        Get object component so that we know how to edit the object

        :return: The component of this DummyPolicy.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this DummyPolicy.

        Get object component so that we know how to edit the object

        :param component: The component of this DummyPolicy.
        :type component: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")

        self._component = component

    @property
    def verbose_name(self):
        """Gets the verbose_name of this DummyPolicy.

        Return object's verbose_name

        :return: The verbose_name of this DummyPolicy.
        :rtype: str
        """
        return self._verbose_name

    @verbose_name.setter
    def verbose_name(self, verbose_name):
        """Sets the verbose_name of this DummyPolicy.

        Return object's verbose_name

        :param verbose_name: The verbose_name of this DummyPolicy.
        :type verbose_name: str
        """
        if verbose_name is None:
            raise ValueError("Invalid value for `verbose_name`, must not be `None`")

        self._verbose_name = verbose_name

    @property
    def verbose_name_plural(self):
        """Gets the verbose_name_plural of this DummyPolicy.

        Return object's plural verbose_name

        :return: The verbose_name_plural of this DummyPolicy.
        :rtype: str
        """
        return self._verbose_name_plural

    @verbose_name_plural.setter
    def verbose_name_plural(self, verbose_name_plural):
        """Sets the verbose_name_plural of this DummyPolicy.

        Return object's plural verbose_name

        :param verbose_name_plural: The verbose_name_plural of this DummyPolicy.
        :type verbose_name_plural: str
        """
        if verbose_name_plural is None:
            raise ValueError("Invalid value for `verbose_name_plural`, must not be `None`")

        self._verbose_name_plural = verbose_name_plural

    @property
    def meta_model_name(self):
        """Gets the meta_model_name of this DummyPolicy.

        Return internal model name

        :return: The meta_model_name of this DummyPolicy.
        :rtype: str
        """
        return self._meta_model_name

    @meta_model_name.setter
    def meta_model_name(self, meta_model_name):
        """Sets the meta_model_name of this DummyPolicy.

        Return internal model name

        :param meta_model_name: The meta_model_name of this DummyPolicy.
        :type meta_model_name: str
        """
        if meta_model_name is None:
            raise ValueError("Invalid value for `meta_model_name`, must not be `None`")

        self._meta_model_name = meta_model_name

    @property
    def bound_to(self):
        """Gets the bound_to of this DummyPolicy.

        Return objects policy is bound to

        :return: The bound_to of this DummyPolicy.
        :rtype: int
        """
        return self._bound_to

    @bound_to.setter
    def bound_to(self, bound_to):
        """Sets the bound_to of this DummyPolicy.

        Return objects policy is bound to

        :param bound_to: The bound_to of this DummyPolicy.
        :type bound_to: int
        """
        if bound_to is None:
            raise ValueError("Invalid value for `bound_to`, must not be `None`")

        self._bound_to = bound_to

    @property
    def result(self):
        """Gets the result of this DummyPolicy.


        :return: The result of this DummyPolicy.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DummyPolicy.


        :param result: The result of this DummyPolicy.
        :type result: bool
        """

        self._result = result

    @property
    def wait_min(self):
        """Gets the wait_min of this DummyPolicy.


        :return: The wait_min of this DummyPolicy.
        :rtype: int
        """
        return self._wait_min

    @wait_min.setter
    def wait_min(self, wait_min):
        """Sets the wait_min of this DummyPolicy.


        :param wait_min: The wait_min of this DummyPolicy.
        :type wait_min: int
        """
        if wait_min is not None and wait_min > 2147483647:
            raise ValueError("Invalid value for `wait_min`, must be a value less than or equal to `2147483647`")
        if wait_min is not None and wait_min < -2147483648:
            raise ValueError("Invalid value for `wait_min`, must be a value greater than or equal to `-2147483648`")

        self._wait_min = wait_min

    @property
    def wait_max(self):
        """Gets the wait_max of this DummyPolicy.


        :return: The wait_max of this DummyPolicy.
        :rtype: int
        """
        return self._wait_max

    @wait_max.setter
    def wait_max(self, wait_max):
        """Sets the wait_max of this DummyPolicy.


        :param wait_max: The wait_max of this DummyPolicy.
        :type wait_max: int
        """
        if wait_max is not None and wait_max > 2147483647:
            raise ValueError("Invalid value for `wait_max`, must be a value less than or equal to `2147483647`")
        if wait_max is not None and wait_max < -2147483648:
            raise ValueError("Invalid value for `wait_max`, must be a value greater than or equal to `-2147483648`")

        self._wait_max = wait_max
