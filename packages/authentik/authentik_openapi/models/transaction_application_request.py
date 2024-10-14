# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.application_request import ApplicationRequest
from authentik_openapi.models.model_request import ModelRequest
from authentik_openapi.models.provider_model_enum import ProviderModelEnum
from authentik_openapi import util


class TransactionApplicationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app: ApplicationRequest=None, provider_model: ProviderModelEnum=None, provider: ModelRequest=None):
        """TransactionApplicationRequest - a model defined in OpenAPI

        :param app: The app of this TransactionApplicationRequest.
        :param provider_model: The provider_model of this TransactionApplicationRequest.
        :param provider: The provider of this TransactionApplicationRequest.
        """
        self.openapi_types = {
            'app': ApplicationRequest,
            'provider_model': ProviderModelEnum,
            'provider': ModelRequest
        }

        self.attribute_map = {
            'app': 'app',
            'provider_model': 'provider_model',
            'provider': 'provider'
        }

        self._app = app
        self._provider_model = provider_model
        self._provider = provider

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransactionApplicationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TransactionApplicationRequest of this TransactionApplicationRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app(self):
        """Gets the app of this TransactionApplicationRequest.


        :return: The app of this TransactionApplicationRequest.
        :rtype: ApplicationRequest
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this TransactionApplicationRequest.


        :param app: The app of this TransactionApplicationRequest.
        :type app: ApplicationRequest
        """
        if app is None:
            raise ValueError("Invalid value for `app`, must not be `None`")

        self._app = app

    @property
    def provider_model(self):
        """Gets the provider_model of this TransactionApplicationRequest.


        :return: The provider_model of this TransactionApplicationRequest.
        :rtype: ProviderModelEnum
        """
        return self._provider_model

    @provider_model.setter
    def provider_model(self, provider_model):
        """Sets the provider_model of this TransactionApplicationRequest.


        :param provider_model: The provider_model of this TransactionApplicationRequest.
        :type provider_model: ProviderModelEnum
        """
        if provider_model is None:
            raise ValueError("Invalid value for `provider_model`, must not be `None`")

        self._provider_model = provider_model

    @property
    def provider(self):
        """Gets the provider of this TransactionApplicationRequest.


        :return: The provider of this TransactionApplicationRequest.
        :rtype: ModelRequest
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this TransactionApplicationRequest.


        :param provider: The provider of this TransactionApplicationRequest.
        :type provider: ModelRequest
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider
