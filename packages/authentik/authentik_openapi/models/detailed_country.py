# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.country_code_enum import CountryCodeEnum
from authentik_openapi import util


class DetailedCountry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: CountryCodeEnum=None, name: str=None):
        """DetailedCountry - a model defined in OpenAPI

        :param code: The code of this DetailedCountry.
        :param name: The name of this DetailedCountry.
        """
        self.openapi_types = {
            'code': CountryCodeEnum,
            'name': str
        }

        self.attribute_map = {
            'code': 'code',
            'name': 'name'
        }

        self._code = code
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DetailedCountry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DetailedCountry of this DetailedCountry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this DetailedCountry.


        :return: The code of this DetailedCountry.
        :rtype: CountryCodeEnum
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DetailedCountry.


        :param code: The code of this DetailedCountry.
        :type code: CountryCodeEnum
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def name(self):
        """Gets the name of this DetailedCountry.


        :return: The name of this DetailedCountry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetailedCountry.


        :param name: The name of this DetailedCountry.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
