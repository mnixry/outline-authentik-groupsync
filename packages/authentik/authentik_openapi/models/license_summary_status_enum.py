# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class LicenseSummaryStatusEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNLICENSED = 'unlicensed'
    VALID = 'valid'
    EXPIRED = 'expired'
    EXPIRY_SOON = 'expiry_soon'
    LIMIT_EXCEEDED_ADMIN = 'limit_exceeded_admin'
    LIMIT_EXCEEDED_USER = 'limit_exceeded_user'
    READ_ONLY = 'read_only'

    def __init__(self):
        """LicenseSummaryStatusEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LicenseSummaryStatusEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LicenseSummaryStatusEnum of this LicenseSummaryStatusEnum.
        """
        return util.deserialize_model(dikt, cls)
