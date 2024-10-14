# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class CommentsCreatePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, document_id: str=None, parent_comment_id: str=None, data: object=None):
        """CommentsCreatePostRequest - a model defined in OpenAPI

        :param id: The id of this CommentsCreatePostRequest.
        :param document_id: The document_id of this CommentsCreatePostRequest.
        :param parent_comment_id: The parent_comment_id of this CommentsCreatePostRequest.
        :param data: The data of this CommentsCreatePostRequest.
        """
        self.openapi_types = {
            'id': str,
            'document_id': str,
            'parent_comment_id': str,
            'data': object
        }

        self.attribute_map = {
            'id': 'id',
            'document_id': 'documentId',
            'parent_comment_id': 'parentCommentId',
            'data': 'data'
        }

        self._id = id
        self._document_id = document_id
        self._parent_comment_id = parent_comment_id
        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CommentsCreatePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _comments_create_post_request of this CommentsCreatePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CommentsCreatePostRequest.


        :return: The id of this CommentsCreatePostRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommentsCreatePostRequest.


        :param id: The id of this CommentsCreatePostRequest.
        :type id: str
        """

        self._id = id

    @property
    def document_id(self):
        """Gets the document_id of this CommentsCreatePostRequest.


        :return: The document_id of this CommentsCreatePostRequest.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this CommentsCreatePostRequest.


        :param document_id: The document_id of this CommentsCreatePostRequest.
        :type document_id: str
        """
        if document_id is None:
            raise ValueError("Invalid value for `document_id`, must not be `None`")

        self._document_id = document_id

    @property
    def parent_comment_id(self):
        """Gets the parent_comment_id of this CommentsCreatePostRequest.


        :return: The parent_comment_id of this CommentsCreatePostRequest.
        :rtype: str
        """
        return self._parent_comment_id

    @parent_comment_id.setter
    def parent_comment_id(self, parent_comment_id):
        """Sets the parent_comment_id of this CommentsCreatePostRequest.


        :param parent_comment_id: The parent_comment_id of this CommentsCreatePostRequest.
        :type parent_comment_id: str
        """

        self._parent_comment_id = parent_comment_id

    @property
    def data(self):
        """Gets the data of this CommentsCreatePostRequest.


        :return: The data of this CommentsCreatePostRequest.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CommentsCreatePostRequest.


        :param data: The data of this CommentsCreatePostRequest.
        :type data: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data
