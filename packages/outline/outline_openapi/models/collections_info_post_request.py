# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class CollectionsInfoPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None):
        """CollectionsInfoPostRequest - a model defined in OpenAPI

        :param id: The id of this CollectionsInfoPostRequest.
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionsInfoPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _collections_info_post_request of this CollectionsInfoPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CollectionsInfoPostRequest.

        Unique identifier for the collection.

        :return: The id of this CollectionsInfoPostRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionsInfoPostRequest.

        Unique identifier for the collection.

        :param id: The id of this CollectionsInfoPostRequest.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
