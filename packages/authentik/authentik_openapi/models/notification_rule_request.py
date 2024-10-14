# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.severity_enum import SeverityEnum
from authentik_openapi import util


class NotificationRuleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, transports: List[str]=None, severity: SeverityEnum=None, group: str=None):
        """NotificationRuleRequest - a model defined in OpenAPI

        :param name: The name of this NotificationRuleRequest.
        :param transports: The transports of this NotificationRuleRequest.
        :param severity: The severity of this NotificationRuleRequest.
        :param group: The group of this NotificationRuleRequest.
        """
        self.openapi_types = {
            'name': str,
            'transports': List[str],
            'severity': SeverityEnum,
            'group': str
        }

        self.attribute_map = {
            'name': 'name',
            'transports': 'transports',
            'severity': 'severity',
            'group': 'group'
        }

        self._name = name
        self._transports = transports
        self._severity = severity
        self._group = group

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationRuleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NotificationRuleRequest of this NotificationRuleRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this NotificationRuleRequest.


        :return: The name of this NotificationRuleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationRuleRequest.


        :param name: The name of this NotificationRuleRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def transports(self):
        """Gets the transports of this NotificationRuleRequest.

        Select which transports should be used to notify the user. If none are selected, the notification will only be shown in the authentik UI.

        :return: The transports of this NotificationRuleRequest.
        :rtype: List[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this NotificationRuleRequest.

        Select which transports should be used to notify the user. If none are selected, the notification will only be shown in the authentik UI.

        :param transports: The transports of this NotificationRuleRequest.
        :type transports: List[str]
        """

        self._transports = transports

    @property
    def severity(self):
        """Gets the severity of this NotificationRuleRequest.

        Controls which severity level the created notifications will have.

        :return: The severity of this NotificationRuleRequest.
        :rtype: SeverityEnum
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this NotificationRuleRequest.

        Controls which severity level the created notifications will have.

        :param severity: The severity of this NotificationRuleRequest.
        :type severity: SeverityEnum
        """

        self._severity = severity

    @property
    def group(self):
        """Gets the group of this NotificationRuleRequest.

        Define which group of users this notification should be sent and shown to. If left empty, Notification won't ben sent.

        :return: The group of this NotificationRuleRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this NotificationRuleRequest.

        Define which group of users this notification should be sent and shown to. If left empty, Notification won't ben sent.

        :param group: The group of this NotificationRuleRequest.
        :type group: str
        """

        self._group = group
