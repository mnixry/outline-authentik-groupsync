# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi.models.user import User
from outline_openapi import util


class View(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, document_id: str=None, first_viewed_at: datetime=None, last_viewed_at: datetime=None, count: float=None, user: User=None):
        """View - a model defined in OpenAPI

        :param id: The id of this View.
        :param document_id: The document_id of this View.
        :param first_viewed_at: The first_viewed_at of this View.
        :param last_viewed_at: The last_viewed_at of this View.
        :param count: The count of this View.
        :param user: The user of this View.
        """
        self.openapi_types = {
            'id': str,
            'document_id': str,
            'first_viewed_at': datetime,
            'last_viewed_at': datetime,
            'count': float,
            'user': User
        }

        self.attribute_map = {
            'id': 'id',
            'document_id': 'documentId',
            'first_viewed_at': 'firstViewedAt',
            'last_viewed_at': 'lastViewedAt',
            'count': 'count',
            'user': 'user'
        }

        self._id = id
        self._document_id = document_id
        self._first_viewed_at = first_viewed_at
        self._last_viewed_at = last_viewed_at
        self._count = count
        self._user = user

    @classmethod
    def from_dict(cls, dikt: dict) -> 'View':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The View of this View.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this View.

        Unique identifier for the object.

        :return: The id of this View.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this View.

        Unique identifier for the object.

        :param id: The id of this View.
        :type id: str
        """

        self._id = id

    @property
    def document_id(self):
        """Gets the document_id of this View.

        Identifier for the associated document.

        :return: The document_id of this View.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this View.

        Identifier for the associated document.

        :param document_id: The document_id of this View.
        :type document_id: str
        """

        self._document_id = document_id

    @property
    def first_viewed_at(self):
        """Gets the first_viewed_at of this View.

        When the document was first viewed by the user

        :return: The first_viewed_at of this View.
        :rtype: datetime
        """
        return self._first_viewed_at

    @first_viewed_at.setter
    def first_viewed_at(self, first_viewed_at):
        """Sets the first_viewed_at of this View.

        When the document was first viewed by the user

        :param first_viewed_at: The first_viewed_at of this View.
        :type first_viewed_at: datetime
        """

        self._first_viewed_at = first_viewed_at

    @property
    def last_viewed_at(self):
        """Gets the last_viewed_at of this View.

        When the document was last viewed by the user

        :return: The last_viewed_at of this View.
        :rtype: datetime
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(self, last_viewed_at):
        """Sets the last_viewed_at of this View.

        When the document was last viewed by the user

        :param last_viewed_at: The last_viewed_at of this View.
        :type last_viewed_at: datetime
        """

        self._last_viewed_at = last_viewed_at

    @property
    def count(self):
        """Gets the count of this View.

        The number of times the user has viewed the document.

        :return: The count of this View.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this View.

        The number of times the user has viewed the document.

        :param count: The count of this View.
        :type count: float
        """

        self._count = count

    @property
    def user(self):
        """Gets the user of this View.


        :return: The user of this View.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this View.


        :param user: The user of this View.
        :type user: User
        """

        self._user = user
