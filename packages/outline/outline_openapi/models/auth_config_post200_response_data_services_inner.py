# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class AuthConfigPost200ResponseDataServicesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, auth_url: str=None):
        """AuthConfigPost200ResponseDataServicesInner - a model defined in OpenAPI

        :param id: The id of this AuthConfigPost200ResponseDataServicesInner.
        :param name: The name of this AuthConfigPost200ResponseDataServicesInner.
        :param auth_url: The auth_url of this AuthConfigPost200ResponseDataServicesInner.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'auth_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'auth_url': 'authUrl'
        }

        self._id = id
        self._name = name
        self._auth_url = auth_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuthConfigPost200ResponseDataServicesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _auth_config_post_200_response_data_services_inner of this AuthConfigPost200ResponseDataServicesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AuthConfigPost200ResponseDataServicesInner.


        :return: The id of this AuthConfigPost200ResponseDataServicesInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthConfigPost200ResponseDataServicesInner.


        :param id: The id of this AuthConfigPost200ResponseDataServicesInner.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuthConfigPost200ResponseDataServicesInner.


        :return: The name of this AuthConfigPost200ResponseDataServicesInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthConfigPost200ResponseDataServicesInner.


        :param name: The name of this AuthConfigPost200ResponseDataServicesInner.
        :type name: str
        """

        self._name = name

    @property
    def auth_url(self):
        """Gets the auth_url of this AuthConfigPost200ResponseDataServicesInner.


        :return: The auth_url of this AuthConfigPost200ResponseDataServicesInner.
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this AuthConfigPost200ResponseDataServicesInner.


        :param auth_url: The auth_url of this AuthConfigPost200ResponseDataServicesInner.
        :type auth_url: str
        """

        self._auth_url = auth_url
