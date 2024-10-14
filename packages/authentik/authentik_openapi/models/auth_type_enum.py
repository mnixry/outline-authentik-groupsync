# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class AuthTypeEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BASIC = 'basic'
    BEARER = 'bearer'

    def __init__(self):
        """AuthTypeEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuthTypeEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuthTypeEnum of this AuthTypeEnum.
        """
        return util.deserialize_model(dikt, cls)
