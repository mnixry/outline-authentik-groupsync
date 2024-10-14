# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class DocumentsInfoPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, share_id: str=None):
        """DocumentsInfoPostRequest - a model defined in OpenAPI

        :param id: The id of this DocumentsInfoPostRequest.
        :param share_id: The share_id of this DocumentsInfoPostRequest.
        """
        self.openapi_types = {
            'id': str,
            'share_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'share_id': 'shareId'
        }

        self._id = id
        self._share_id = share_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DocumentsInfoPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _documents_info_post_request of this DocumentsInfoPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DocumentsInfoPostRequest.

        Unique identifier for the document. Either the UUID or the urlId is acceptable.

        :return: The id of this DocumentsInfoPostRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsInfoPostRequest.

        Unique identifier for the document. Either the UUID or the urlId is acceptable.

        :param id: The id of this DocumentsInfoPostRequest.
        :type id: str
        """

        self._id = id

    @property
    def share_id(self):
        """Gets the share_id of this DocumentsInfoPostRequest.

        Unique identifier for a document share, a shareId may be used in place of a document UUID

        :return: The share_id of this DocumentsInfoPostRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this DocumentsInfoPostRequest.

        Unique identifier for a document share, a shareId may be used in place of a document UUID

        :param share_id: The share_id of this DocumentsInfoPostRequest.
        :type share_id: str
        """

        self._share_id = share_id
