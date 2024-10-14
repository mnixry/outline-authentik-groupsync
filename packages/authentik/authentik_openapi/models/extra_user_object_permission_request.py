# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class ExtraUserObjectPermissionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, object_pk: str=None):
        """ExtraUserObjectPermissionRequest - a model defined in OpenAPI

        :param object_pk: The object_pk of this ExtraUserObjectPermissionRequest.
        """
        self.openapi_types = {
            'object_pk': str
        }

        self.attribute_map = {
            'object_pk': 'object_pk'
        }

        self._object_pk = object_pk

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExtraUserObjectPermissionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExtraUserObjectPermissionRequest of this ExtraUserObjectPermissionRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_pk(self):
        """Gets the object_pk of this ExtraUserObjectPermissionRequest.


        :return: The object_pk of this ExtraUserObjectPermissionRequest.
        :rtype: str
        """
        return self._object_pk

    @object_pk.setter
    def object_pk(self, object_pk):
        """Sets the object_pk of this ExtraUserObjectPermissionRequest.


        :param object_pk: The object_pk of this ExtraUserObjectPermissionRequest.
        :type object_pk: str
        """
        if object_pk is None:
            raise ValueError("Invalid value for `object_pk`, must not be `None`")
        if object_pk is not None and len(object_pk) < 1:
            raise ValueError("Invalid value for `object_pk`, length must be greater than or equal to `1`")

        self._object_pk = object_pk
