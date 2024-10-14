# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from outline_openapi.models.base_model import Model
from outline_openapi.models.user_role import UserRole
from outline_openapi import util


class User(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, avatar_url: str=None, email: str=None, role: UserRole=None, is_suspended: bool=None, last_active_at: datetime=None, created_at: datetime=None):
        """User - a model defined in OpenAPI

        :param id: The id of this User.
        :param name: The name of this User.
        :param avatar_url: The avatar_url of this User.
        :param email: The email of this User.
        :param role: The role of this User.
        :param is_suspended: The is_suspended of this User.
        :param last_active_at: The last_active_at of this User.
        :param created_at: The created_at of this User.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'avatar_url': str,
            'email': str,
            'role': UserRole,
            'is_suspended': bool,
            'last_active_at': datetime,
            'created_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'avatar_url': 'avatarUrl',
            'email': 'email',
            'role': 'role',
            'is_suspended': 'isSuspended',
            'last_active_at': 'lastActiveAt',
            'created_at': 'createdAt'
        }

        self._id = id
        self._name = name
        self._avatar_url = avatar_url
        self._email = email
        self._role = role
        self._is_suspended = is_suspended
        self._last_active_at = last_active_at
        self._created_at = created_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The User of this User.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this User.

        Unique identifier for the object.

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        Unique identifier for the object.

        :param id: The id of this User.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this User.

        The name of this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary.

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        The name of this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary.

        :param name: The name of this User.
        :type name: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this User.

        The URL for the image associated with this user, it will be displayed in the application UI and email notifications.

        :return: The avatar_url of this User.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this User.

        The URL for the image associated with this user, it will be displayed in the application UI and email notifications.

        :param avatar_url: The avatar_url of this User.
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def email(self):
        """Gets the email of this User.

        The email associated with this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary.

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        The email associated with this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary.

        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this User.


        :return: The role of this User.
        :rtype: UserRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.


        :param role: The role of this User.
        :type role: UserRole
        """

        self._role = role

    @property
    def is_suspended(self):
        """Gets the is_suspended of this User.

        Whether this user has been suspended.

        :return: The is_suspended of this User.
        :rtype: bool
        """
        return self._is_suspended

    @is_suspended.setter
    def is_suspended(self, is_suspended):
        """Sets the is_suspended of this User.

        Whether this user has been suspended.

        :param is_suspended: The is_suspended of this User.
        :type is_suspended: bool
        """

        self._is_suspended = is_suspended

    @property
    def last_active_at(self):
        """Gets the last_active_at of this User.

        The last time this user made an API request, this value is updated at most every 5 minutes.

        :return: The last_active_at of this User.
        :rtype: datetime
        """
        return self._last_active_at

    @last_active_at.setter
    def last_active_at(self, last_active_at):
        """Sets the last_active_at of this User.

        The last time this user made an API request, this value is updated at most every 5 minutes.

        :param last_active_at: The last_active_at of this User.
        :type last_active_at: datetime
        """

        self._last_active_at = last_active_at

    @property
    def created_at(self):
        """Gets the created_at of this User.

        The date and time that this user first signed in or was invited as a guest.

        :return: The created_at of this User.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        The date and time that this user first signed in or was invited as a guest.

        :param created_at: The created_at of this User.
        :type created_at: datetime
        """

        self._created_at = created_at
