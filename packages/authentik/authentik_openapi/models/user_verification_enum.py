# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class UserVerificationEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    REQUIRED = 'required'
    PREFERRED = 'preferred'
    DISCOURAGED = 'discouraged'

    def __init__(self):
        """UserVerificationEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserVerificationEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserVerificationEnum of this UserVerificationEnum.
        """
        return util.deserialize_model(dikt, cls)
