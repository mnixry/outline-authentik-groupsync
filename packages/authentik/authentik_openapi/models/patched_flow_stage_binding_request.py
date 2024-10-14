# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.invalid_response_action_enum import InvalidResponseActionEnum
from authentik_openapi.models.policy_engine_mode import PolicyEngineMode
from authentik_openapi import util


class PatchedFlowStageBindingRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, target: str=None, stage: str=None, evaluate_on_plan: bool=None, re_evaluate_policies: bool=None, order: int=None, policy_engine_mode: PolicyEngineMode=None, invalid_response_action: InvalidResponseActionEnum=None):
        """PatchedFlowStageBindingRequest - a model defined in OpenAPI

        :param target: The target of this PatchedFlowStageBindingRequest.
        :param stage: The stage of this PatchedFlowStageBindingRequest.
        :param evaluate_on_plan: The evaluate_on_plan of this PatchedFlowStageBindingRequest.
        :param re_evaluate_policies: The re_evaluate_policies of this PatchedFlowStageBindingRequest.
        :param order: The order of this PatchedFlowStageBindingRequest.
        :param policy_engine_mode: The policy_engine_mode of this PatchedFlowStageBindingRequest.
        :param invalid_response_action: The invalid_response_action of this PatchedFlowStageBindingRequest.
        """
        self.openapi_types = {
            'target': str,
            'stage': str,
            'evaluate_on_plan': bool,
            're_evaluate_policies': bool,
            'order': int,
            'policy_engine_mode': PolicyEngineMode,
            'invalid_response_action': InvalidResponseActionEnum
        }

        self.attribute_map = {
            'target': 'target',
            'stage': 'stage',
            'evaluate_on_plan': 'evaluate_on_plan',
            're_evaluate_policies': 're_evaluate_policies',
            'order': 'order',
            'policy_engine_mode': 'policy_engine_mode',
            'invalid_response_action': 'invalid_response_action'
        }

        self._target = target
        self._stage = stage
        self._evaluate_on_plan = evaluate_on_plan
        self._re_evaluate_policies = re_evaluate_policies
        self._order = order
        self._policy_engine_mode = policy_engine_mode
        self._invalid_response_action = invalid_response_action

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatchedFlowStageBindingRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatchedFlowStageBindingRequest of this PatchedFlowStageBindingRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target(self):
        """Gets the target of this PatchedFlowStageBindingRequest.


        :return: The target of this PatchedFlowStageBindingRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this PatchedFlowStageBindingRequest.


        :param target: The target of this PatchedFlowStageBindingRequest.
        :type target: str
        """

        self._target = target

    @property
    def stage(self):
        """Gets the stage of this PatchedFlowStageBindingRequest.


        :return: The stage of this PatchedFlowStageBindingRequest.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this PatchedFlowStageBindingRequest.


        :param stage: The stage of this PatchedFlowStageBindingRequest.
        :type stage: str
        """

        self._stage = stage

    @property
    def evaluate_on_plan(self):
        """Gets the evaluate_on_plan of this PatchedFlowStageBindingRequest.

        Evaluate policies during the Flow planning process.

        :return: The evaluate_on_plan of this PatchedFlowStageBindingRequest.
        :rtype: bool
        """
        return self._evaluate_on_plan

    @evaluate_on_plan.setter
    def evaluate_on_plan(self, evaluate_on_plan):
        """Sets the evaluate_on_plan of this PatchedFlowStageBindingRequest.

        Evaluate policies during the Flow planning process.

        :param evaluate_on_plan: The evaluate_on_plan of this PatchedFlowStageBindingRequest.
        :type evaluate_on_plan: bool
        """

        self._evaluate_on_plan = evaluate_on_plan

    @property
    def re_evaluate_policies(self):
        """Gets the re_evaluate_policies of this PatchedFlowStageBindingRequest.

        Evaluate policies when the Stage is present to the user.

        :return: The re_evaluate_policies of this PatchedFlowStageBindingRequest.
        :rtype: bool
        """
        return self._re_evaluate_policies

    @re_evaluate_policies.setter
    def re_evaluate_policies(self, re_evaluate_policies):
        """Sets the re_evaluate_policies of this PatchedFlowStageBindingRequest.

        Evaluate policies when the Stage is present to the user.

        :param re_evaluate_policies: The re_evaluate_policies of this PatchedFlowStageBindingRequest.
        :type re_evaluate_policies: bool
        """

        self._re_evaluate_policies = re_evaluate_policies

    @property
    def order(self):
        """Gets the order of this PatchedFlowStageBindingRequest.


        :return: The order of this PatchedFlowStageBindingRequest.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PatchedFlowStageBindingRequest.


        :param order: The order of this PatchedFlowStageBindingRequest.
        :type order: int
        """
        if order is not None and order > 2147483647:
            raise ValueError("Invalid value for `order`, must be a value less than or equal to `2147483647`")
        if order is not None and order < -2147483648:
            raise ValueError("Invalid value for `order`, must be a value greater than or equal to `-2147483648`")

        self._order = order

    @property
    def policy_engine_mode(self):
        """Gets the policy_engine_mode of this PatchedFlowStageBindingRequest.


        :return: The policy_engine_mode of this PatchedFlowStageBindingRequest.
        :rtype: PolicyEngineMode
        """
        return self._policy_engine_mode

    @policy_engine_mode.setter
    def policy_engine_mode(self, policy_engine_mode):
        """Sets the policy_engine_mode of this PatchedFlowStageBindingRequest.


        :param policy_engine_mode: The policy_engine_mode of this PatchedFlowStageBindingRequest.
        :type policy_engine_mode: PolicyEngineMode
        """

        self._policy_engine_mode = policy_engine_mode

    @property
    def invalid_response_action(self):
        """Gets the invalid_response_action of this PatchedFlowStageBindingRequest.

        Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.

        :return: The invalid_response_action of this PatchedFlowStageBindingRequest.
        :rtype: InvalidResponseActionEnum
        """
        return self._invalid_response_action

    @invalid_response_action.setter
    def invalid_response_action(self, invalid_response_action):
        """Sets the invalid_response_action of this PatchedFlowStageBindingRequest.

        Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.

        :param invalid_response_action: The invalid_response_action of this PatchedFlowStageBindingRequest.
        :type invalid_response_action: InvalidResponseActionEnum
        """

        self._invalid_response_action = invalid_response_action
