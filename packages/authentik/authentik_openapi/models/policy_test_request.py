# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class PolicyTestRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user: int=None, context: Dict[str, object]=None):
        """PolicyTestRequest - a model defined in OpenAPI

        :param user: The user of this PolicyTestRequest.
        :param context: The context of this PolicyTestRequest.
        """
        self.openapi_types = {
            'user': int,
            'context': Dict[str, object]
        }

        self.attribute_map = {
            'user': 'user',
            'context': 'context'
        }

        self._user = user
        self._context = context

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PolicyTestRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PolicyTestRequest of this PolicyTestRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user(self):
        """Gets the user of this PolicyTestRequest.


        :return: The user of this PolicyTestRequest.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PolicyTestRequest.


        :param user: The user of this PolicyTestRequest.
        :type user: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def context(self):
        """Gets the context of this PolicyTestRequest.


        :return: The context of this PolicyTestRequest.
        :rtype: Dict[str, object]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PolicyTestRequest.


        :param context: The context of this PolicyTestRequest.
        :type context: Dict[str, object]
        """

        self._context = context
