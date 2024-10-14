# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class EventTopPerUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: Dict[str, object]=None, counted_events: int=None, unique_users: int=None):
        """EventTopPerUser - a model defined in OpenAPI

        :param application: The application of this EventTopPerUser.
        :param counted_events: The counted_events of this EventTopPerUser.
        :param unique_users: The unique_users of this EventTopPerUser.
        """
        self.openapi_types = {
            'application': Dict[str, object],
            'counted_events': int,
            'unique_users': int
        }

        self.attribute_map = {
            'application': 'application',
            'counted_events': 'counted_events',
            'unique_users': 'unique_users'
        }

        self._application = application
        self._counted_events = counted_events
        self._unique_users = unique_users

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EventTopPerUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EventTopPerUser of this EventTopPerUser.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this EventTopPerUser.


        :return: The application of this EventTopPerUser.
        :rtype: Dict[str, object]
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this EventTopPerUser.


        :param application: The application of this EventTopPerUser.
        :type application: Dict[str, object]
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def counted_events(self):
        """Gets the counted_events of this EventTopPerUser.


        :return: The counted_events of this EventTopPerUser.
        :rtype: int
        """
        return self._counted_events

    @counted_events.setter
    def counted_events(self, counted_events):
        """Sets the counted_events of this EventTopPerUser.


        :param counted_events: The counted_events of this EventTopPerUser.
        :type counted_events: int
        """
        if counted_events is None:
            raise ValueError("Invalid value for `counted_events`, must not be `None`")

        self._counted_events = counted_events

    @property
    def unique_users(self):
        """Gets the unique_users of this EventTopPerUser.


        :return: The unique_users of this EventTopPerUser.
        :rtype: int
        """
        return self._unique_users

    @unique_users.setter
    def unique_users(self, unique_users):
        """Sets the unique_users of this EventTopPerUser.


        :param unique_users: The unique_users of this EventTopPerUser.
        :type unique_users: int
        """
        if unique_users is None:
            raise ValueError("Invalid value for `unique_users`, must not be `None`")

        self._unique_users = unique_users
