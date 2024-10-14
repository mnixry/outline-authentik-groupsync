# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class Permission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    READ = 'read'
    READ_WRITE = 'read_write'

    def __init__(self):
        """Permission - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Permission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Permission of this Permission.
        """
        return util.deserialize_model(dikt, cls)
