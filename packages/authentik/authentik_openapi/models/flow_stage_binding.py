# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.invalid_response_action_enum import InvalidResponseActionEnum
from authentik_openapi.models.policy_engine_mode import PolicyEngineMode
from authentik_openapi.models.stage import Stage
from authentik_openapi import util


class FlowStageBinding(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, policybindingmodel_ptr_id: str=None, target: str=None, stage: str=None, stage_obj: Stage=None, evaluate_on_plan: bool=None, re_evaluate_policies: bool=None, order: int=None, policy_engine_mode: PolicyEngineMode=None, invalid_response_action: InvalidResponseActionEnum=None):
        """FlowStageBinding - a model defined in OpenAPI

        :param pk: The pk of this FlowStageBinding.
        :param policybindingmodel_ptr_id: The policybindingmodel_ptr_id of this FlowStageBinding.
        :param target: The target of this FlowStageBinding.
        :param stage: The stage of this FlowStageBinding.
        :param stage_obj: The stage_obj of this FlowStageBinding.
        :param evaluate_on_plan: The evaluate_on_plan of this FlowStageBinding.
        :param re_evaluate_policies: The re_evaluate_policies of this FlowStageBinding.
        :param order: The order of this FlowStageBinding.
        :param policy_engine_mode: The policy_engine_mode of this FlowStageBinding.
        :param invalid_response_action: The invalid_response_action of this FlowStageBinding.
        """
        self.openapi_types = {
            'pk': str,
            'policybindingmodel_ptr_id': str,
            'target': str,
            'stage': str,
            'stage_obj': Stage,
            'evaluate_on_plan': bool,
            're_evaluate_policies': bool,
            'order': int,
            'policy_engine_mode': PolicyEngineMode,
            'invalid_response_action': InvalidResponseActionEnum
        }

        self.attribute_map = {
            'pk': 'pk',
            'policybindingmodel_ptr_id': 'policybindingmodel_ptr_id',
            'target': 'target',
            'stage': 'stage',
            'stage_obj': 'stage_obj',
            'evaluate_on_plan': 'evaluate_on_plan',
            're_evaluate_policies': 're_evaluate_policies',
            'order': 'order',
            'policy_engine_mode': 'policy_engine_mode',
            'invalid_response_action': 'invalid_response_action'
        }

        self._pk = pk
        self._policybindingmodel_ptr_id = policybindingmodel_ptr_id
        self._target = target
        self._stage = stage
        self._stage_obj = stage_obj
        self._evaluate_on_plan = evaluate_on_plan
        self._re_evaluate_policies = re_evaluate_policies
        self._order = order
        self._policy_engine_mode = policy_engine_mode
        self._invalid_response_action = invalid_response_action

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FlowStageBinding':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FlowStageBinding of this FlowStageBinding.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this FlowStageBinding.


        :return: The pk of this FlowStageBinding.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this FlowStageBinding.


        :param pk: The pk of this FlowStageBinding.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def policybindingmodel_ptr_id(self):
        """Gets the policybindingmodel_ptr_id of this FlowStageBinding.


        :return: The policybindingmodel_ptr_id of this FlowStageBinding.
        :rtype: str
        """
        return self._policybindingmodel_ptr_id

    @policybindingmodel_ptr_id.setter
    def policybindingmodel_ptr_id(self, policybindingmodel_ptr_id):
        """Sets the policybindingmodel_ptr_id of this FlowStageBinding.


        :param policybindingmodel_ptr_id: The policybindingmodel_ptr_id of this FlowStageBinding.
        :type policybindingmodel_ptr_id: str
        """
        if policybindingmodel_ptr_id is None:
            raise ValueError("Invalid value for `policybindingmodel_ptr_id`, must not be `None`")

        self._policybindingmodel_ptr_id = policybindingmodel_ptr_id

    @property
    def target(self):
        """Gets the target of this FlowStageBinding.


        :return: The target of this FlowStageBinding.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this FlowStageBinding.


        :param target: The target of this FlowStageBinding.
        :type target: str
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

    @property
    def stage(self):
        """Gets the stage of this FlowStageBinding.


        :return: The stage of this FlowStageBinding.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this FlowStageBinding.


        :param stage: The stage of this FlowStageBinding.
        :type stage: str
        """
        if stage is None:
            raise ValueError("Invalid value for `stage`, must not be `None`")

        self._stage = stage

    @property
    def stage_obj(self):
        """Gets the stage_obj of this FlowStageBinding.


        :return: The stage_obj of this FlowStageBinding.
        :rtype: Stage
        """
        return self._stage_obj

    @stage_obj.setter
    def stage_obj(self, stage_obj):
        """Sets the stage_obj of this FlowStageBinding.


        :param stage_obj: The stage_obj of this FlowStageBinding.
        :type stage_obj: Stage
        """
        if stage_obj is None:
            raise ValueError("Invalid value for `stage_obj`, must not be `None`")

        self._stage_obj = stage_obj

    @property
    def evaluate_on_plan(self):
        """Gets the evaluate_on_plan of this FlowStageBinding.

        Evaluate policies during the Flow planning process.

        :return: The evaluate_on_plan of this FlowStageBinding.
        :rtype: bool
        """
        return self._evaluate_on_plan

    @evaluate_on_plan.setter
    def evaluate_on_plan(self, evaluate_on_plan):
        """Sets the evaluate_on_plan of this FlowStageBinding.

        Evaluate policies during the Flow planning process.

        :param evaluate_on_plan: The evaluate_on_plan of this FlowStageBinding.
        :type evaluate_on_plan: bool
        """

        self._evaluate_on_plan = evaluate_on_plan

    @property
    def re_evaluate_policies(self):
        """Gets the re_evaluate_policies of this FlowStageBinding.

        Evaluate policies when the Stage is present to the user.

        :return: The re_evaluate_policies of this FlowStageBinding.
        :rtype: bool
        """
        return self._re_evaluate_policies

    @re_evaluate_policies.setter
    def re_evaluate_policies(self, re_evaluate_policies):
        """Sets the re_evaluate_policies of this FlowStageBinding.

        Evaluate policies when the Stage is present to the user.

        :param re_evaluate_policies: The re_evaluate_policies of this FlowStageBinding.
        :type re_evaluate_policies: bool
        """

        self._re_evaluate_policies = re_evaluate_policies

    @property
    def order(self):
        """Gets the order of this FlowStageBinding.


        :return: The order of this FlowStageBinding.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this FlowStageBinding.


        :param order: The order of this FlowStageBinding.
        :type order: int
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")
        if order is not None and order > 2147483647:
            raise ValueError("Invalid value for `order`, must be a value less than or equal to `2147483647`")
        if order is not None and order < -2147483648:
            raise ValueError("Invalid value for `order`, must be a value greater than or equal to `-2147483648`")

        self._order = order

    @property
    def policy_engine_mode(self):
        """Gets the policy_engine_mode of this FlowStageBinding.


        :return: The policy_engine_mode of this FlowStageBinding.
        :rtype: PolicyEngineMode
        """
        return self._policy_engine_mode

    @policy_engine_mode.setter
    def policy_engine_mode(self, policy_engine_mode):
        """Sets the policy_engine_mode of this FlowStageBinding.


        :param policy_engine_mode: The policy_engine_mode of this FlowStageBinding.
        :type policy_engine_mode: PolicyEngineMode
        """

        self._policy_engine_mode = policy_engine_mode

    @property
    def invalid_response_action(self):
        """Gets the invalid_response_action of this FlowStageBinding.

        Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.

        :return: The invalid_response_action of this FlowStageBinding.
        :rtype: InvalidResponseActionEnum
        """
        return self._invalid_response_action

    @invalid_response_action.setter
    def invalid_response_action(self, invalid_response_action):
        """Sets the invalid_response_action of this FlowStageBinding.

        Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.

        :param invalid_response_action: The invalid_response_action of this FlowStageBinding.
        :type invalid_response_action: InvalidResponseActionEnum
        """

        self._invalid_response_action = invalid_response_action
