# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.log_event import LogEvent
from authentik_openapi import util


class PolicyTestResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, passing: bool=None, messages: List[str]=None, log_messages: List[LogEvent]=None):
        """PolicyTestResult - a model defined in OpenAPI

        :param passing: The passing of this PolicyTestResult.
        :param messages: The messages of this PolicyTestResult.
        :param log_messages: The log_messages of this PolicyTestResult.
        """
        self.openapi_types = {
            'passing': bool,
            'messages': List[str],
            'log_messages': List[LogEvent]
        }

        self.attribute_map = {
            'passing': 'passing',
            'messages': 'messages',
            'log_messages': 'log_messages'
        }

        self._passing = passing
        self._messages = messages
        self._log_messages = log_messages

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PolicyTestResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PolicyTestResult of this PolicyTestResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def passing(self):
        """Gets the passing of this PolicyTestResult.


        :return: The passing of this PolicyTestResult.
        :rtype: bool
        """
        return self._passing

    @passing.setter
    def passing(self, passing):
        """Sets the passing of this PolicyTestResult.


        :param passing: The passing of this PolicyTestResult.
        :type passing: bool
        """
        if passing is None:
            raise ValueError("Invalid value for `passing`, must not be `None`")

        self._passing = passing

    @property
    def messages(self):
        """Gets the messages of this PolicyTestResult.


        :return: The messages of this PolicyTestResult.
        :rtype: List[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this PolicyTestResult.


        :param messages: The messages of this PolicyTestResult.
        :type messages: List[str]
        """
        if messages is None:
            raise ValueError("Invalid value for `messages`, must not be `None`")

        self._messages = messages

    @property
    def log_messages(self):
        """Gets the log_messages of this PolicyTestResult.


        :return: The log_messages of this PolicyTestResult.
        :rtype: List[LogEvent]
        """
        return self._log_messages

    @log_messages.setter
    def log_messages(self, log_messages):
        """Sets the log_messages of this PolicyTestResult.


        :param log_messages: The log_messages of this PolicyTestResult.
        :type log_messages: List[LogEvent]
        """
        if log_messages is None:
            raise ValueError("Invalid value for `log_messages`, must not be `None`")

        self._log_messages = log_messages
