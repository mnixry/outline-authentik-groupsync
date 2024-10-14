# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.role_object_permission import RoleObjectPermission
from authentik_openapi import util


class RoleAssignedObjectPermission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, role_pk: str=None, name: str=None, permissions: List[RoleObjectPermission]=None):
        """RoleAssignedObjectPermission - a model defined in OpenAPI

        :param role_pk: The role_pk of this RoleAssignedObjectPermission.
        :param name: The name of this RoleAssignedObjectPermission.
        :param permissions: The permissions of this RoleAssignedObjectPermission.
        """
        self.openapi_types = {
            'role_pk': str,
            'name': str,
            'permissions': List[RoleObjectPermission]
        }

        self.attribute_map = {
            'role_pk': 'role_pk',
            'name': 'name',
            'permissions': 'permissions'
        }

        self._role_pk = role_pk
        self._name = name
        self._permissions = permissions

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RoleAssignedObjectPermission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RoleAssignedObjectPermission of this RoleAssignedObjectPermission.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def role_pk(self):
        """Gets the role_pk of this RoleAssignedObjectPermission.


        :return: The role_pk of this RoleAssignedObjectPermission.
        :rtype: str
        """
        return self._role_pk

    @role_pk.setter
    def role_pk(self, role_pk):
        """Sets the role_pk of this RoleAssignedObjectPermission.


        :param role_pk: The role_pk of this RoleAssignedObjectPermission.
        :type role_pk: str
        """
        if role_pk is None:
            raise ValueError("Invalid value for `role_pk`, must not be `None`")

        self._role_pk = role_pk

    @property
    def name(self):
        """Gets the name of this RoleAssignedObjectPermission.


        :return: The name of this RoleAssignedObjectPermission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleAssignedObjectPermission.


        :param name: The name of this RoleAssignedObjectPermission.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this RoleAssignedObjectPermission.


        :return: The permissions of this RoleAssignedObjectPermission.
        :rtype: List[RoleObjectPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoleAssignedObjectPermission.


        :param permissions: The permissions of this RoleAssignedObjectPermission.
        :type permissions: List[RoleObjectPermission]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions
