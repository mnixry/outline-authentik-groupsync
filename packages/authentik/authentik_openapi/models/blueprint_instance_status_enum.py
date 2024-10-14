# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class BlueprintInstanceStatusEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SUCCESSFUL = 'successful'
    WARNING = 'warning'
    ERROR = 'error'
    ORPHANED = 'orphaned'
    UNKNOWN = 'unknown'

    def __init__(self):
        """BlueprintInstanceStatusEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BlueprintInstanceStatusEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BlueprintInstanceStatusEnum of this BlueprintInstanceStatusEnum.
        """
        return util.deserialize_model(dikt, cls)
