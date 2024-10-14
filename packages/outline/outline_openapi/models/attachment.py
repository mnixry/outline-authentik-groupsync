# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi import util


class Attachment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content_type: str=None, size: float=None, name: str=None, url: str=None, document_id: str=None):
        """Attachment - a model defined in OpenAPI

        :param content_type: The content_type of this Attachment.
        :param size: The size of this Attachment.
        :param name: The name of this Attachment.
        :param url: The url of this Attachment.
        :param document_id: The document_id of this Attachment.
        """
        self.openapi_types = {
            'content_type': str,
            'size': float,
            'name': str,
            'url': str,
            'document_id': str
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'size': 'size',
            'name': 'name',
            'url': 'url',
            'document_id': 'documentId'
        }

        self._content_type = content_type
        self._size = size
        self._name = name
        self._url = url
        self._document_id = document_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Attachment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Attachment of this Attachment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_type(self):
        """Gets the content_type of this Attachment.


        :return: The content_type of this Attachment.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Attachment.


        :param content_type: The content_type of this Attachment.
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def size(self):
        """Gets the size of this Attachment.


        :return: The size of this Attachment.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Attachment.


        :param size: The size of this Attachment.
        :type size: float
        """

        self._size = size

    @property
    def name(self):
        """Gets the name of this Attachment.


        :return: The name of this Attachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attachment.


        :param name: The name of this Attachment.
        :type name: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Attachment.


        :return: The url of this Attachment.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Attachment.


        :param url: The url of this Attachment.
        :type url: str
        """

        self._url = url

    @property
    def document_id(self):
        """Gets the document_id of this Attachment.

        Identifier for the associated document, if any.

        :return: The document_id of this Attachment.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Attachment.

        Identifier for the associated document, if any.

        :param document_id: The document_id of this Attachment.
        :type document_id: str
        """

        self._document_id = document_id
