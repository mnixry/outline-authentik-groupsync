# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.contextual_flow_info import ContextualFlowInfo
from authentik_openapi.models.error_detail import ErrorDetail
from authentik_openapi import util


class AuthenticatorSMSChallenge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, flow_info: ContextualFlowInfo=None, component: str='ak-stage-authenticator-sms', response_errors: Dict[str, List[ErrorDetail]]=None, pending_user: str=None, pending_user_avatar: str=None, phone_number_required: bool=True):
        """AuthenticatorSMSChallenge - a model defined in OpenAPI

        :param flow_info: The flow_info of this AuthenticatorSMSChallenge.
        :param component: The component of this AuthenticatorSMSChallenge.
        :param response_errors: The response_errors of this AuthenticatorSMSChallenge.
        :param pending_user: The pending_user of this AuthenticatorSMSChallenge.
        :param pending_user_avatar: The pending_user_avatar of this AuthenticatorSMSChallenge.
        :param phone_number_required: The phone_number_required of this AuthenticatorSMSChallenge.
        """
        self.openapi_types = {
            'flow_info': ContextualFlowInfo,
            'component': str,
            'response_errors': Dict[str, List[ErrorDetail]],
            'pending_user': str,
            'pending_user_avatar': str,
            'phone_number_required': bool
        }

        self.attribute_map = {
            'flow_info': 'flow_info',
            'component': 'component',
            'response_errors': 'response_errors',
            'pending_user': 'pending_user',
            'pending_user_avatar': 'pending_user_avatar',
            'phone_number_required': 'phone_number_required'
        }

        self._flow_info = flow_info
        self._component = component
        self._response_errors = response_errors
        self._pending_user = pending_user
        self._pending_user_avatar = pending_user_avatar
        self._phone_number_required = phone_number_required

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuthenticatorSMSChallenge':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuthenticatorSMSChallenge of this AuthenticatorSMSChallenge.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def flow_info(self):
        """Gets the flow_info of this AuthenticatorSMSChallenge.


        :return: The flow_info of this AuthenticatorSMSChallenge.
        :rtype: ContextualFlowInfo
        """
        return self._flow_info

    @flow_info.setter
    def flow_info(self, flow_info):
        """Sets the flow_info of this AuthenticatorSMSChallenge.


        :param flow_info: The flow_info of this AuthenticatorSMSChallenge.
        :type flow_info: ContextualFlowInfo
        """

        self._flow_info = flow_info

    @property
    def component(self):
        """Gets the component of this AuthenticatorSMSChallenge.


        :return: The component of this AuthenticatorSMSChallenge.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this AuthenticatorSMSChallenge.


        :param component: The component of this AuthenticatorSMSChallenge.
        :type component: str
        """

        self._component = component

    @property
    def response_errors(self):
        """Gets the response_errors of this AuthenticatorSMSChallenge.


        :return: The response_errors of this AuthenticatorSMSChallenge.
        :rtype: Dict[str, List[ErrorDetail]]
        """
        return self._response_errors

    @response_errors.setter
    def response_errors(self, response_errors):
        """Sets the response_errors of this AuthenticatorSMSChallenge.


        :param response_errors: The response_errors of this AuthenticatorSMSChallenge.
        :type response_errors: Dict[str, List[ErrorDetail]]
        """

        self._response_errors = response_errors

    @property
    def pending_user(self):
        """Gets the pending_user of this AuthenticatorSMSChallenge.


        :return: The pending_user of this AuthenticatorSMSChallenge.
        :rtype: str
        """
        return self._pending_user

    @pending_user.setter
    def pending_user(self, pending_user):
        """Sets the pending_user of this AuthenticatorSMSChallenge.


        :param pending_user: The pending_user of this AuthenticatorSMSChallenge.
        :type pending_user: str
        """
        if pending_user is None:
            raise ValueError("Invalid value for `pending_user`, must not be `None`")

        self._pending_user = pending_user

    @property
    def pending_user_avatar(self):
        """Gets the pending_user_avatar of this AuthenticatorSMSChallenge.


        :return: The pending_user_avatar of this AuthenticatorSMSChallenge.
        :rtype: str
        """
        return self._pending_user_avatar

    @pending_user_avatar.setter
    def pending_user_avatar(self, pending_user_avatar):
        """Sets the pending_user_avatar of this AuthenticatorSMSChallenge.


        :param pending_user_avatar: The pending_user_avatar of this AuthenticatorSMSChallenge.
        :type pending_user_avatar: str
        """
        if pending_user_avatar is None:
            raise ValueError("Invalid value for `pending_user_avatar`, must not be `None`")

        self._pending_user_avatar = pending_user_avatar

    @property
    def phone_number_required(self):
        """Gets the phone_number_required of this AuthenticatorSMSChallenge.


        :return: The phone_number_required of this AuthenticatorSMSChallenge.
        :rtype: bool
        """
        return self._phone_number_required

    @phone_number_required.setter
    def phone_number_required(self, phone_number_required):
        """Sets the phone_number_required of this AuthenticatorSMSChallenge.


        :param phone_number_required: The phone_number_required of this AuthenticatorSMSChallenge.
        :type phone_number_required: bool
        """

        self._phone_number_required = phone_number_required
