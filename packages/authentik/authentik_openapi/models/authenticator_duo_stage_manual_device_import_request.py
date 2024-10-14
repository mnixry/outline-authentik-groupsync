# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class AuthenticatorDuoStageManualDeviceImportRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, duo_user_id: str=None, username: str=None):
        """AuthenticatorDuoStageManualDeviceImportRequest - a model defined in OpenAPI

        :param duo_user_id: The duo_user_id of this AuthenticatorDuoStageManualDeviceImportRequest.
        :param username: The username of this AuthenticatorDuoStageManualDeviceImportRequest.
        """
        self.openapi_types = {
            'duo_user_id': str,
            'username': str
        }

        self.attribute_map = {
            'duo_user_id': 'duo_user_id',
            'username': 'username'
        }

        self._duo_user_id = duo_user_id
        self._username = username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuthenticatorDuoStageManualDeviceImportRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuthenticatorDuoStageManualDeviceImportRequest of this AuthenticatorDuoStageManualDeviceImportRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def duo_user_id(self):
        """Gets the duo_user_id of this AuthenticatorDuoStageManualDeviceImportRequest.


        :return: The duo_user_id of this AuthenticatorDuoStageManualDeviceImportRequest.
        :rtype: str
        """
        return self._duo_user_id

    @duo_user_id.setter
    def duo_user_id(self, duo_user_id):
        """Sets the duo_user_id of this AuthenticatorDuoStageManualDeviceImportRequest.


        :param duo_user_id: The duo_user_id of this AuthenticatorDuoStageManualDeviceImportRequest.
        :type duo_user_id: str
        """
        if duo_user_id is None:
            raise ValueError("Invalid value for `duo_user_id`, must not be `None`")
        if duo_user_id is not None and len(duo_user_id) < 1:
            raise ValueError("Invalid value for `duo_user_id`, length must be greater than or equal to `1`")

        self._duo_user_id = duo_user_id

    @property
    def username(self):
        """Gets the username of this AuthenticatorDuoStageManualDeviceImportRequest.


        :return: The username of this AuthenticatorDuoStageManualDeviceImportRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthenticatorDuoStageManualDeviceImportRequest.


        :param username: The username of this AuthenticatorDuoStageManualDeviceImportRequest.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")

        self._username = username
