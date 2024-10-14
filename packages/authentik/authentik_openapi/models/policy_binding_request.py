# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class PolicyBindingRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, policy: str=None, group: str=None, user: int=None, target: str=None, negate: bool=None, enabled: bool=None, order: int=None, timeout: int=None, failure_result: bool=None):
        """PolicyBindingRequest - a model defined in OpenAPI

        :param policy: The policy of this PolicyBindingRequest.
        :param group: The group of this PolicyBindingRequest.
        :param user: The user of this PolicyBindingRequest.
        :param target: The target of this PolicyBindingRequest.
        :param negate: The negate of this PolicyBindingRequest.
        :param enabled: The enabled of this PolicyBindingRequest.
        :param order: The order of this PolicyBindingRequest.
        :param timeout: The timeout of this PolicyBindingRequest.
        :param failure_result: The failure_result of this PolicyBindingRequest.
        """
        self.openapi_types = {
            'policy': str,
            'group': str,
            'user': int,
            'target': str,
            'negate': bool,
            'enabled': bool,
            'order': int,
            'timeout': int,
            'failure_result': bool
        }

        self.attribute_map = {
            'policy': 'policy',
            'group': 'group',
            'user': 'user',
            'target': 'target',
            'negate': 'negate',
            'enabled': 'enabled',
            'order': 'order',
            'timeout': 'timeout',
            'failure_result': 'failure_result'
        }

        self._policy = policy
        self._group = group
        self._user = user
        self._target = target
        self._negate = negate
        self._enabled = enabled
        self._order = order
        self._timeout = timeout
        self._failure_result = failure_result

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PolicyBindingRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PolicyBindingRequest of this PolicyBindingRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def policy(self):
        """Gets the policy of this PolicyBindingRequest.


        :return: The policy of this PolicyBindingRequest.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyBindingRequest.


        :param policy: The policy of this PolicyBindingRequest.
        :type policy: str
        """

        self._policy = policy

    @property
    def group(self):
        """Gets the group of this PolicyBindingRequest.


        :return: The group of this PolicyBindingRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PolicyBindingRequest.


        :param group: The group of this PolicyBindingRequest.
        :type group: str
        """

        self._group = group

    @property
    def user(self):
        """Gets the user of this PolicyBindingRequest.


        :return: The user of this PolicyBindingRequest.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PolicyBindingRequest.


        :param user: The user of this PolicyBindingRequest.
        :type user: int
        """

        self._user = user

    @property
    def target(self):
        """Gets the target of this PolicyBindingRequest.


        :return: The target of this PolicyBindingRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this PolicyBindingRequest.


        :param target: The target of this PolicyBindingRequest.
        :type target: str
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

    @property
    def negate(self):
        """Gets the negate of this PolicyBindingRequest.

        Negates the outcome of the policy. Messages are unaffected.

        :return: The negate of this PolicyBindingRequest.
        :rtype: bool
        """
        return self._negate

    @negate.setter
    def negate(self, negate):
        """Sets the negate of this PolicyBindingRequest.

        Negates the outcome of the policy. Messages are unaffected.

        :param negate: The negate of this PolicyBindingRequest.
        :type negate: bool
        """

        self._negate = negate

    @property
    def enabled(self):
        """Gets the enabled of this PolicyBindingRequest.


        :return: The enabled of this PolicyBindingRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PolicyBindingRequest.


        :param enabled: The enabled of this PolicyBindingRequest.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def order(self):
        """Gets the order of this PolicyBindingRequest.


        :return: The order of this PolicyBindingRequest.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PolicyBindingRequest.


        :param order: The order of this PolicyBindingRequest.
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
    def timeout(self):
        """Gets the timeout of this PolicyBindingRequest.

        Timeout after which Policy execution is terminated.

        :return: The timeout of this PolicyBindingRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this PolicyBindingRequest.

        Timeout after which Policy execution is terminated.

        :param timeout: The timeout of this PolicyBindingRequest.
        :type timeout: int
        """
        if timeout is not None and timeout > 2147483647:
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `2147483647`")
        if timeout is not None and timeout < 0:
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `0`")

        self._timeout = timeout

    @property
    def failure_result(self):
        """Gets the failure_result of this PolicyBindingRequest.

        Result if the Policy execution fails.

        :return: The failure_result of this PolicyBindingRequest.
        :rtype: bool
        """
        return self._failure_result

    @failure_result.setter
    def failure_result(self, failure_result):
        """Sets the failure_result of this PolicyBindingRequest.

        Result if the Policy execution fails.

        :param failure_result: The failure_result of this PolicyBindingRequest.
        :type failure_result: bool
        """

        self._failure_result = failure_result
