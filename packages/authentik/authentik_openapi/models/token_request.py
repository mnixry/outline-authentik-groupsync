# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.intent_enum import IntentEnum
import re
from authentik_openapi import util


class TokenRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, managed: str=None, identifier: str=None, intent: IntentEnum=None, user: int=None, description: str=None, expires: datetime=None, expiring: bool=None):
        """TokenRequest - a model defined in OpenAPI

        :param managed: The managed of this TokenRequest.
        :param identifier: The identifier of this TokenRequest.
        :param intent: The intent of this TokenRequest.
        :param user: The user of this TokenRequest.
        :param description: The description of this TokenRequest.
        :param expires: The expires of this TokenRequest.
        :param expiring: The expiring of this TokenRequest.
        """
        self.openapi_types = {
            'managed': str,
            'identifier': str,
            'intent': IntentEnum,
            'user': int,
            'description': str,
            'expires': datetime,
            'expiring': bool
        }

        self.attribute_map = {
            'managed': 'managed',
            'identifier': 'identifier',
            'intent': 'intent',
            'user': 'user',
            'description': 'description',
            'expires': 'expires',
            'expiring': 'expiring'
        }

        self._managed = managed
        self._identifier = identifier
        self._intent = intent
        self._user = user
        self._description = description
        self._expires = expires
        self._expiring = expiring

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TokenRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TokenRequest of this TokenRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def managed(self):
        """Gets the managed of this TokenRequest.

        Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.

        :return: The managed of this TokenRequest.
        :rtype: str
        """
        return self._managed

    @managed.setter
    def managed(self, managed):
        """Sets the managed of this TokenRequest.

        Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.

        :param managed: The managed of this TokenRequest.
        :type managed: str
        """
        if managed is not None and len(managed) < 1:
            raise ValueError("Invalid value for `managed`, length must be greater than or equal to `1`")

        self._managed = managed

    @property
    def identifier(self):
        """Gets the identifier of this TokenRequest.


        :return: The identifier of this TokenRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TokenRequest.


        :param identifier: The identifier of this TokenRequest.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")
        if identifier is not None and len(identifier) > 255:
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `255`")
        if identifier is not None and len(identifier) < 1:
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")
        if identifier is not None and not re.search(r'^[-a-zA-Z0-9_]+$', identifier):
            raise ValueError("Invalid value for `identifier`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")

        self._identifier = identifier

    @property
    def intent(self):
        """Gets the intent of this TokenRequest.


        :return: The intent of this TokenRequest.
        :rtype: IntentEnum
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this TokenRequest.


        :param intent: The intent of this TokenRequest.
        :type intent: IntentEnum
        """

        self._intent = intent

    @property
    def user(self):
        """Gets the user of this TokenRequest.


        :return: The user of this TokenRequest.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TokenRequest.


        :param user: The user of this TokenRequest.
        :type user: int
        """

        self._user = user

    @property
    def description(self):
        """Gets the description of this TokenRequest.


        :return: The description of this TokenRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TokenRequest.


        :param description: The description of this TokenRequest.
        :type description: str
        """

        self._description = description

    @property
    def expires(self):
        """Gets the expires of this TokenRequest.


        :return: The expires of this TokenRequest.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this TokenRequest.


        :param expires: The expires of this TokenRequest.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def expiring(self):
        """Gets the expiring of this TokenRequest.


        :return: The expiring of this TokenRequest.
        :rtype: bool
        """
        return self._expiring

    @expiring.setter
    def expiring(self, expiring):
        """Sets the expiring of this TokenRequest.


        :param expiring: The expiring of this TokenRequest.
        :type expiring: bool
        """

        self._expiring = expiring
