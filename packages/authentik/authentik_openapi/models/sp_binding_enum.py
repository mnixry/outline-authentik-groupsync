# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class SpBindingEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    REDIRECT = 'redirect'
    POST = 'post'

    def __init__(self):
        """SpBindingEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SpBindingEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SpBindingEnum of this SpBindingEnum.
        """
        return util.deserialize_model(dikt, cls)
