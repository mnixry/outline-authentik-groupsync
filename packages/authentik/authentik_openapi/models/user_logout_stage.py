# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.flow_set import FlowSet
from authentik_openapi import util


class UserLogoutStage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, name: str=None, component: str=None, verbose_name: str=None, verbose_name_plural: str=None, meta_model_name: str=None, flow_set: List[FlowSet]=None):
        """UserLogoutStage - a model defined in OpenAPI

        :param pk: The pk of this UserLogoutStage.
        :param name: The name of this UserLogoutStage.
        :param component: The component of this UserLogoutStage.
        :param verbose_name: The verbose_name of this UserLogoutStage.
        :param verbose_name_plural: The verbose_name_plural of this UserLogoutStage.
        :param meta_model_name: The meta_model_name of this UserLogoutStage.
        :param flow_set: The flow_set of this UserLogoutStage.
        """
        self.openapi_types = {
            'pk': str,
            'name': str,
            'component': str,
            'verbose_name': str,
            'verbose_name_plural': str,
            'meta_model_name': str,
            'flow_set': List[FlowSet]
        }

        self.attribute_map = {
            'pk': 'pk',
            'name': 'name',
            'component': 'component',
            'verbose_name': 'verbose_name',
            'verbose_name_plural': 'verbose_name_plural',
            'meta_model_name': 'meta_model_name',
            'flow_set': 'flow_set'
        }

        self._pk = pk
        self._name = name
        self._component = component
        self._verbose_name = verbose_name
        self._verbose_name_plural = verbose_name_plural
        self._meta_model_name = meta_model_name
        self._flow_set = flow_set

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserLogoutStage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserLogoutStage of this UserLogoutStage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this UserLogoutStage.


        :return: The pk of this UserLogoutStage.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this UserLogoutStage.


        :param pk: The pk of this UserLogoutStage.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this UserLogoutStage.


        :return: The name of this UserLogoutStage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserLogoutStage.


        :param name: The name of this UserLogoutStage.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def component(self):
        """Gets the component of this UserLogoutStage.

        Get object type so that we know how to edit the object

        :return: The component of this UserLogoutStage.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this UserLogoutStage.

        Get object type so that we know how to edit the object

        :param component: The component of this UserLogoutStage.
        :type component: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")

        self._component = component

    @property
    def verbose_name(self):
        """Gets the verbose_name of this UserLogoutStage.

        Return object's verbose_name

        :return: The verbose_name of this UserLogoutStage.
        :rtype: str
        """
        return self._verbose_name

    @verbose_name.setter
    def verbose_name(self, verbose_name):
        """Sets the verbose_name of this UserLogoutStage.

        Return object's verbose_name

        :param verbose_name: The verbose_name of this UserLogoutStage.
        :type verbose_name: str
        """
        if verbose_name is None:
            raise ValueError("Invalid value for `verbose_name`, must not be `None`")

        self._verbose_name = verbose_name

    @property
    def verbose_name_plural(self):
        """Gets the verbose_name_plural of this UserLogoutStage.

        Return object's plural verbose_name

        :return: The verbose_name_plural of this UserLogoutStage.
        :rtype: str
        """
        return self._verbose_name_plural

    @verbose_name_plural.setter
    def verbose_name_plural(self, verbose_name_plural):
        """Sets the verbose_name_plural of this UserLogoutStage.

        Return object's plural verbose_name

        :param verbose_name_plural: The verbose_name_plural of this UserLogoutStage.
        :type verbose_name_plural: str
        """
        if verbose_name_plural is None:
            raise ValueError("Invalid value for `verbose_name_plural`, must not be `None`")

        self._verbose_name_plural = verbose_name_plural

    @property
    def meta_model_name(self):
        """Gets the meta_model_name of this UserLogoutStage.

        Return internal model name

        :return: The meta_model_name of this UserLogoutStage.
        :rtype: str
        """
        return self._meta_model_name

    @meta_model_name.setter
    def meta_model_name(self, meta_model_name):
        """Sets the meta_model_name of this UserLogoutStage.

        Return internal model name

        :param meta_model_name: The meta_model_name of this UserLogoutStage.
        :type meta_model_name: str
        """
        if meta_model_name is None:
            raise ValueError("Invalid value for `meta_model_name`, must not be `None`")

        self._meta_model_name = meta_model_name

    @property
    def flow_set(self):
        """Gets the flow_set of this UserLogoutStage.


        :return: The flow_set of this UserLogoutStage.
        :rtype: List[FlowSet]
        """
        return self._flow_set

    @flow_set.setter
    def flow_set(self, flow_set):
        """Sets the flow_set of this UserLogoutStage.


        :param flow_set: The flow_set of this UserLogoutStage.
        :type flow_set: List[FlowSet]
        """

        self._flow_set = flow_set
