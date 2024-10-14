# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class DuoDevice(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: int=None, name: str=None):
        """DuoDevice - a model defined in OpenAPI

        :param pk: The pk of this DuoDevice.
        :param name: The name of this DuoDevice.
        """
        self.openapi_types = {
            'pk': int,
            'name': str
        }

        self.attribute_map = {
            'pk': 'pk',
            'name': 'name'
        }

        self._pk = pk
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DuoDevice':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DuoDevice of this DuoDevice.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this DuoDevice.


        :return: The pk of this DuoDevice.
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this DuoDevice.


        :param pk: The pk of this DuoDevice.
        :type pk: int
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this DuoDevice.

        The human-readable name of this device.

        :return: The name of this DuoDevice.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DuoDevice.

        The human-readable name of this device.

        :param name: The name of this DuoDevice.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")

        self._name = name
