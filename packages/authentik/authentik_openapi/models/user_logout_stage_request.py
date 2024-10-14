# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.flow_set_request import FlowSetRequest
from authentik_openapi import util


class UserLogoutStageRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, flow_set: List[FlowSetRequest]=None):
        """UserLogoutStageRequest - a model defined in OpenAPI

        :param name: The name of this UserLogoutStageRequest.
        :param flow_set: The flow_set of this UserLogoutStageRequest.
        """
        self.openapi_types = {
            'name': str,
            'flow_set': List[FlowSetRequest]
        }

        self.attribute_map = {
            'name': 'name',
            'flow_set': 'flow_set'
        }

        self._name = name
        self._flow_set = flow_set

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserLogoutStageRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserLogoutStageRequest of this UserLogoutStageRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this UserLogoutStageRequest.


        :return: The name of this UserLogoutStageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserLogoutStageRequest.


        :param name: The name of this UserLogoutStageRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def flow_set(self):
        """Gets the flow_set of this UserLogoutStageRequest.


        :return: The flow_set of this UserLogoutStageRequest.
        :rtype: List[FlowSetRequest]
        """
        return self._flow_set

    @flow_set.setter
    def flow_set(self, flow_set):
        """Sets the flow_set of this UserLogoutStageRequest.


        :param flow_set: The flow_set of this UserLogoutStageRequest.
        :type flow_set: List[FlowSetRequest]
        """

        self._flow_set = flow_set
