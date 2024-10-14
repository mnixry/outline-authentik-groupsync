# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class CollectionsRemoveUserPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, user_id: str=None):
        """CollectionsRemoveUserPostRequest - a model defined in OpenAPI

        :param id: The id of this CollectionsRemoveUserPostRequest.
        :param user_id: The user_id of this CollectionsRemoveUserPostRequest.
        """
        self.openapi_types = {
            'id': str,
            'user_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId'
        }

        self._id = id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CollectionsRemoveUserPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _collections_remove_user_post_request of this CollectionsRemoveUserPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CollectionsRemoveUserPostRequest.

        Identifier for the collection

        :return: The id of this CollectionsRemoveUserPostRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionsRemoveUserPostRequest.

        Identifier for the collection

        :param id: The id of this CollectionsRemoveUserPostRequest.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this CollectionsRemoveUserPostRequest.


        :return: The user_id of this CollectionsRemoveUserPostRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CollectionsRemoveUserPostRequest.


        :param user_id: The user_id of this CollectionsRemoveUserPostRequest.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id
