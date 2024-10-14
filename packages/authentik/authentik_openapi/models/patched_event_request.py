# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.event_actions import EventActions
from authentik_openapi import util


class PatchedEventRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user: object=None, action: EventActions=None, app: str=None, context: object=None, client_ip: str=None, expires: datetime=None, brand: object=None):
        """PatchedEventRequest - a model defined in OpenAPI

        :param user: The user of this PatchedEventRequest.
        :param action: The action of this PatchedEventRequest.
        :param app: The app of this PatchedEventRequest.
        :param context: The context of this PatchedEventRequest.
        :param client_ip: The client_ip of this PatchedEventRequest.
        :param expires: The expires of this PatchedEventRequest.
        :param brand: The brand of this PatchedEventRequest.
        """
        self.openapi_types = {
            'user': object,
            'action': EventActions,
            'app': str,
            'context': object,
            'client_ip': str,
            'expires': datetime,
            'brand': object
        }

        self.attribute_map = {
            'user': 'user',
            'action': 'action',
            'app': 'app',
            'context': 'context',
            'client_ip': 'client_ip',
            'expires': 'expires',
            'brand': 'brand'
        }

        self._user = user
        self._action = action
        self._app = app
        self._context = context
        self._client_ip = client_ip
        self._expires = expires
        self._brand = brand

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PatchedEventRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PatchedEventRequest of this PatchedEventRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user(self):
        """Gets the user of this PatchedEventRequest.


        :return: The user of this PatchedEventRequest.
        :rtype: object
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PatchedEventRequest.


        :param user: The user of this PatchedEventRequest.
        :type user: object
        """

        self._user = user

    @property
    def action(self):
        """Gets the action of this PatchedEventRequest.


        :return: The action of this PatchedEventRequest.
        :rtype: EventActions
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PatchedEventRequest.


        :param action: The action of this PatchedEventRequest.
        :type action: EventActions
        """

        self._action = action

    @property
    def app(self):
        """Gets the app of this PatchedEventRequest.


        :return: The app of this PatchedEventRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this PatchedEventRequest.


        :param app: The app of this PatchedEventRequest.
        :type app: str
        """
        if app is not None and len(app) < 1:
            raise ValueError("Invalid value for `app`, length must be greater than or equal to `1`")

        self._app = app

    @property
    def context(self):
        """Gets the context of this PatchedEventRequest.


        :return: The context of this PatchedEventRequest.
        :rtype: object
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PatchedEventRequest.


        :param context: The context of this PatchedEventRequest.
        :type context: object
        """

        self._context = context

    @property
    def client_ip(self):
        """Gets the client_ip of this PatchedEventRequest.


        :return: The client_ip of this PatchedEventRequest.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this PatchedEventRequest.


        :param client_ip: The client_ip of this PatchedEventRequest.
        :type client_ip: str
        """
        if client_ip is not None and len(client_ip) < 1:
            raise ValueError("Invalid value for `client_ip`, length must be greater than or equal to `1`")

        self._client_ip = client_ip

    @property
    def expires(self):
        """Gets the expires of this PatchedEventRequest.


        :return: The expires of this PatchedEventRequest.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this PatchedEventRequest.


        :param expires: The expires of this PatchedEventRequest.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def brand(self):
        """Gets the brand of this PatchedEventRequest.


        :return: The brand of this PatchedEventRequest.
        :rtype: object
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PatchedEventRequest.


        :param brand: The brand of this PatchedEventRequest.
        :type brand: object
        """

        self._brand = brand
