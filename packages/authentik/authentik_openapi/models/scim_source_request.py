# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
import re
from authentik_openapi import util


class SCIMSourceRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, slug: str=None, enabled: bool=None, user_property_mappings: List[str]=None, group_property_mappings: List[str]=None, user_path_template: str=None):
        """SCIMSourceRequest - a model defined in OpenAPI

        :param name: The name of this SCIMSourceRequest.
        :param slug: The slug of this SCIMSourceRequest.
        :param enabled: The enabled of this SCIMSourceRequest.
        :param user_property_mappings: The user_property_mappings of this SCIMSourceRequest.
        :param group_property_mappings: The group_property_mappings of this SCIMSourceRequest.
        :param user_path_template: The user_path_template of this SCIMSourceRequest.
        """
        self.openapi_types = {
            'name': str,
            'slug': str,
            'enabled': bool,
            'user_property_mappings': List[str],
            'group_property_mappings': List[str],
            'user_path_template': str
        }

        self.attribute_map = {
            'name': 'name',
            'slug': 'slug',
            'enabled': 'enabled',
            'user_property_mappings': 'user_property_mappings',
            'group_property_mappings': 'group_property_mappings',
            'user_path_template': 'user_path_template'
        }

        self._name = name
        self._slug = slug
        self._enabled = enabled
        self._user_property_mappings = user_property_mappings
        self._group_property_mappings = group_property_mappings
        self._user_path_template = user_path_template

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SCIMSourceRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SCIMSourceRequest of this SCIMSourceRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this SCIMSourceRequest.

        Source's display Name.

        :return: The name of this SCIMSourceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SCIMSourceRequest.

        Source's display Name.

        :param name: The name of this SCIMSourceRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this SCIMSourceRequest.

        Internal source name, used in URLs.

        :return: The slug of this SCIMSourceRequest.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this SCIMSourceRequest.

        Internal source name, used in URLs.

        :param slug: The slug of this SCIMSourceRequest.
        :type slug: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")
        if slug is not None and len(slug) > 50:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `50`")
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):
            raise ValueError("Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")

        self._slug = slug

    @property
    def enabled(self):
        """Gets the enabled of this SCIMSourceRequest.


        :return: The enabled of this SCIMSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SCIMSourceRequest.


        :param enabled: The enabled of this SCIMSourceRequest.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def user_property_mappings(self):
        """Gets the user_property_mappings of this SCIMSourceRequest.


        :return: The user_property_mappings of this SCIMSourceRequest.
        :rtype: List[str]
        """
        return self._user_property_mappings

    @user_property_mappings.setter
    def user_property_mappings(self, user_property_mappings):
        """Sets the user_property_mappings of this SCIMSourceRequest.


        :param user_property_mappings: The user_property_mappings of this SCIMSourceRequest.
        :type user_property_mappings: List[str]
        """

        self._user_property_mappings = user_property_mappings

    @property
    def group_property_mappings(self):
        """Gets the group_property_mappings of this SCIMSourceRequest.


        :return: The group_property_mappings of this SCIMSourceRequest.
        :rtype: List[str]
        """
        return self._group_property_mappings

    @group_property_mappings.setter
    def group_property_mappings(self, group_property_mappings):
        """Sets the group_property_mappings of this SCIMSourceRequest.


        :param group_property_mappings: The group_property_mappings of this SCIMSourceRequest.
        :type group_property_mappings: List[str]
        """

        self._group_property_mappings = group_property_mappings

    @property
    def user_path_template(self):
        """Gets the user_path_template of this SCIMSourceRequest.


        :return: The user_path_template of this SCIMSourceRequest.
        :rtype: str
        """
        return self._user_path_template

    @user_path_template.setter
    def user_path_template(self, user_path_template):
        """Sets the user_path_template of this SCIMSourceRequest.


        :param user_path_template: The user_path_template of this SCIMSourceRequest.
        :type user_path_template: str
        """
        if user_path_template is not None and len(user_path_template) < 1:
            raise ValueError("Invalid value for `user_path_template`, length must be greater than or equal to `1`")

        self._user_path_template = user_path_template
