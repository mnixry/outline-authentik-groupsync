# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.flow_set_request import FlowSetRequest
from authentik_openapi import util


class PatchedSourceStageRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, flow_set: List[FlowSetRequest]=None, source: str=None, resume_timeout: str=None):
        """PatchedSourceStageRequest - a model defined in OpenAPI

        :param name: The name of this PatchedSourceStageRequest.
        :param flow_set: The flow_set of this PatchedSourceStageRequest.
        :param source: The source of this PatchedSourceStageRequest.
        :param resume_timeout: The resume_timeout of this PatchedSourceStageRequest.
        """
        self.openapi_types = {
            'name': str,
            'flow_set': List[FlowSetRequest],
            'source': str,
            'resume_timeout': str
        }

        self.attribute_map = {
            'name': 'name',
            'flow_set': 'flow_set',
            'source': 'source',
            'resume_timeout': 'resume_timeout'
        }

        self._name = name
        self._flow_set = flow_set
        self._source = source
        self._resume_timeout = resume_timeout

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatchedSourceStageRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatchedSourceStageRequest of this PatchedSourceStageRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this PatchedSourceStageRequest.


        :return: The name of this PatchedSourceStageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedSourceStageRequest.


        :param name: The name of this PatchedSourceStageRequest.
        :type name: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def flow_set(self):
        """Gets the flow_set of this PatchedSourceStageRequest.


        :return: The flow_set of this PatchedSourceStageRequest.
        :rtype: List[FlowSetRequest]
        """
        return self._flow_set

    @flow_set.setter
    def flow_set(self, flow_set):
        """Sets the flow_set of this PatchedSourceStageRequest.


        :param flow_set: The flow_set of this PatchedSourceStageRequest.
        :type flow_set: List[FlowSetRequest]
        """

        self._flow_set = flow_set

    @property
    def source(self):
        """Gets the source of this PatchedSourceStageRequest.


        :return: The source of this PatchedSourceStageRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PatchedSourceStageRequest.


        :param source: The source of this PatchedSourceStageRequest.
        :type source: str
        """

        self._source = source

    @property
    def resume_timeout(self):
        """Gets the resume_timeout of this PatchedSourceStageRequest.

        Amount of time a user can take to return from the source to continue the flow (Format: hours=-1;minutes=-2;seconds=-3)

        :return: The resume_timeout of this PatchedSourceStageRequest.
        :rtype: str
        """
        return self._resume_timeout

    @resume_timeout.setter
    def resume_timeout(self, resume_timeout):
        """Sets the resume_timeout of this PatchedSourceStageRequest.

        Amount of time a user can take to return from the source to continue the flow (Format: hours=-1;minutes=-2;seconds=-3)

        :param resume_timeout: The resume_timeout of this PatchedSourceStageRequest.
        :type resume_timeout: str
        """
        if resume_timeout is not None and len(resume_timeout) < 1:
            raise ValueError("Invalid value for `resume_timeout`, length must be greater than or equal to `1`")

        self._resume_timeout = resume_timeout
