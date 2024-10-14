# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.outgoing_sync_delete_action import OutgoingSyncDeleteAction
from authentik_openapi import util


class GoogleWorkspaceProvider(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: int=None, name: str=None, property_mappings: List[str]=None, property_mappings_group: List[str]=None, component: str=None, assigned_backchannel_application_slug: str=None, assigned_backchannel_application_name: str=None, verbose_name: str=None, verbose_name_plural: str=None, meta_model_name: str=None, delegated_subject: str=None, credentials: object=None, scopes: str=None, exclude_users_service_account: bool=None, filter_group: str=None, user_delete_action: OutgoingSyncDeleteAction=None, group_delete_action: OutgoingSyncDeleteAction=None, default_group_email_domain: str=None):
        """GoogleWorkspaceProvider - a model defined in OpenAPI

        :param pk: The pk of this GoogleWorkspaceProvider.
        :param name: The name of this GoogleWorkspaceProvider.
        :param property_mappings: The property_mappings of this GoogleWorkspaceProvider.
        :param property_mappings_group: The property_mappings_group of this GoogleWorkspaceProvider.
        :param component: The component of this GoogleWorkspaceProvider.
        :param assigned_backchannel_application_slug: The assigned_backchannel_application_slug of this GoogleWorkspaceProvider.
        :param assigned_backchannel_application_name: The assigned_backchannel_application_name of this GoogleWorkspaceProvider.
        :param verbose_name: The verbose_name of this GoogleWorkspaceProvider.
        :param verbose_name_plural: The verbose_name_plural of this GoogleWorkspaceProvider.
        :param meta_model_name: The meta_model_name of this GoogleWorkspaceProvider.
        :param delegated_subject: The delegated_subject of this GoogleWorkspaceProvider.
        :param credentials: The credentials of this GoogleWorkspaceProvider.
        :param scopes: The scopes of this GoogleWorkspaceProvider.
        :param exclude_users_service_account: The exclude_users_service_account of this GoogleWorkspaceProvider.
        :param filter_group: The filter_group of this GoogleWorkspaceProvider.
        :param user_delete_action: The user_delete_action of this GoogleWorkspaceProvider.
        :param group_delete_action: The group_delete_action of this GoogleWorkspaceProvider.
        :param default_group_email_domain: The default_group_email_domain of this GoogleWorkspaceProvider.
        """
        self.openapi_types = {
            'pk': int,
            'name': str,
            'property_mappings': List[str],
            'property_mappings_group': List[str],
            'component': str,
            'assigned_backchannel_application_slug': str,
            'assigned_backchannel_application_name': str,
            'verbose_name': str,
            'verbose_name_plural': str,
            'meta_model_name': str,
            'delegated_subject': str,
            'credentials': object,
            'scopes': str,
            'exclude_users_service_account': bool,
            'filter_group': str,
            'user_delete_action': OutgoingSyncDeleteAction,
            'group_delete_action': OutgoingSyncDeleteAction,
            'default_group_email_domain': str
        }

        self.attribute_map = {
            'pk': 'pk',
            'name': 'name',
            'property_mappings': 'property_mappings',
            'property_mappings_group': 'property_mappings_group',
            'component': 'component',
            'assigned_backchannel_application_slug': 'assigned_backchannel_application_slug',
            'assigned_backchannel_application_name': 'assigned_backchannel_application_name',
            'verbose_name': 'verbose_name',
            'verbose_name_plural': 'verbose_name_plural',
            'meta_model_name': 'meta_model_name',
            'delegated_subject': 'delegated_subject',
            'credentials': 'credentials',
            'scopes': 'scopes',
            'exclude_users_service_account': 'exclude_users_service_account',
            'filter_group': 'filter_group',
            'user_delete_action': 'user_delete_action',
            'group_delete_action': 'group_delete_action',
            'default_group_email_domain': 'default_group_email_domain'
        }

        self._pk = pk
        self._name = name
        self._property_mappings = property_mappings
        self._property_mappings_group = property_mappings_group
        self._component = component
        self._assigned_backchannel_application_slug = assigned_backchannel_application_slug
        self._assigned_backchannel_application_name = assigned_backchannel_application_name
        self._verbose_name = verbose_name
        self._verbose_name_plural = verbose_name_plural
        self._meta_model_name = meta_model_name
        self._delegated_subject = delegated_subject
        self._credentials = credentials
        self._scopes = scopes
        self._exclude_users_service_account = exclude_users_service_account
        self._filter_group = filter_group
        self._user_delete_action = user_delete_action
        self._group_delete_action = group_delete_action
        self._default_group_email_domain = default_group_email_domain

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GoogleWorkspaceProvider':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GoogleWorkspaceProvider of this GoogleWorkspaceProvider.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this GoogleWorkspaceProvider.


        :return: The pk of this GoogleWorkspaceProvider.
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this GoogleWorkspaceProvider.


        :param pk: The pk of this GoogleWorkspaceProvider.
        :type pk: int
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def name(self):
        """Gets the name of this GoogleWorkspaceProvider.


        :return: The name of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GoogleWorkspaceProvider.


        :param name: The name of this GoogleWorkspaceProvider.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def property_mappings(self):
        """Gets the property_mappings of this GoogleWorkspaceProvider.


        :return: The property_mappings of this GoogleWorkspaceProvider.
        :rtype: List[str]
        """
        return self._property_mappings

    @property_mappings.setter
    def property_mappings(self, property_mappings):
        """Sets the property_mappings of this GoogleWorkspaceProvider.


        :param property_mappings: The property_mappings of this GoogleWorkspaceProvider.
        :type property_mappings: List[str]
        """

        self._property_mappings = property_mappings

    @property
    def property_mappings_group(self):
        """Gets the property_mappings_group of this GoogleWorkspaceProvider.

        Property mappings used for group creation/updating.

        :return: The property_mappings_group of this GoogleWorkspaceProvider.
        :rtype: List[str]
        """
        return self._property_mappings_group

    @property_mappings_group.setter
    def property_mappings_group(self, property_mappings_group):
        """Sets the property_mappings_group of this GoogleWorkspaceProvider.

        Property mappings used for group creation/updating.

        :param property_mappings_group: The property_mappings_group of this GoogleWorkspaceProvider.
        :type property_mappings_group: List[str]
        """

        self._property_mappings_group = property_mappings_group

    @property
    def component(self):
        """Gets the component of this GoogleWorkspaceProvider.

        Get object component so that we know how to edit the object

        :return: The component of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this GoogleWorkspaceProvider.

        Get object component so that we know how to edit the object

        :param component: The component of this GoogleWorkspaceProvider.
        :type component: str
        """
        if component is None:
            raise ValueError("Invalid value for `component`, must not be `None`")

        self._component = component

    @property
    def assigned_backchannel_application_slug(self):
        """Gets the assigned_backchannel_application_slug of this GoogleWorkspaceProvider.

        Internal application name, used in URLs.

        :return: The assigned_backchannel_application_slug of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._assigned_backchannel_application_slug

    @assigned_backchannel_application_slug.setter
    def assigned_backchannel_application_slug(self, assigned_backchannel_application_slug):
        """Sets the assigned_backchannel_application_slug of this GoogleWorkspaceProvider.

        Internal application name, used in URLs.

        :param assigned_backchannel_application_slug: The assigned_backchannel_application_slug of this GoogleWorkspaceProvider.
        :type assigned_backchannel_application_slug: str
        """
        if assigned_backchannel_application_slug is None:
            raise ValueError("Invalid value for `assigned_backchannel_application_slug`, must not be `None`")

        self._assigned_backchannel_application_slug = assigned_backchannel_application_slug

    @property
    def assigned_backchannel_application_name(self):
        """Gets the assigned_backchannel_application_name of this GoogleWorkspaceProvider.

        Application's display Name.

        :return: The assigned_backchannel_application_name of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._assigned_backchannel_application_name

    @assigned_backchannel_application_name.setter
    def assigned_backchannel_application_name(self, assigned_backchannel_application_name):
        """Sets the assigned_backchannel_application_name of this GoogleWorkspaceProvider.

        Application's display Name.

        :param assigned_backchannel_application_name: The assigned_backchannel_application_name of this GoogleWorkspaceProvider.
        :type assigned_backchannel_application_name: str
        """
        if assigned_backchannel_application_name is None:
            raise ValueError("Invalid value for `assigned_backchannel_application_name`, must not be `None`")

        self._assigned_backchannel_application_name = assigned_backchannel_application_name

    @property
    def verbose_name(self):
        """Gets the verbose_name of this GoogleWorkspaceProvider.

        Return object's verbose_name

        :return: The verbose_name of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._verbose_name

    @verbose_name.setter
    def verbose_name(self, verbose_name):
        """Sets the verbose_name of this GoogleWorkspaceProvider.

        Return object's verbose_name

        :param verbose_name: The verbose_name of this GoogleWorkspaceProvider.
        :type verbose_name: str
        """
        if verbose_name is None:
            raise ValueError("Invalid value for `verbose_name`, must not be `None`")

        self._verbose_name = verbose_name

    @property
    def verbose_name_plural(self):
        """Gets the verbose_name_plural of this GoogleWorkspaceProvider.

        Return object's plural verbose_name

        :return: The verbose_name_plural of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._verbose_name_plural

    @verbose_name_plural.setter
    def verbose_name_plural(self, verbose_name_plural):
        """Sets the verbose_name_plural of this GoogleWorkspaceProvider.

        Return object's plural verbose_name

        :param verbose_name_plural: The verbose_name_plural of this GoogleWorkspaceProvider.
        :type verbose_name_plural: str
        """
        if verbose_name_plural is None:
            raise ValueError("Invalid value for `verbose_name_plural`, must not be `None`")

        self._verbose_name_plural = verbose_name_plural

    @property
    def meta_model_name(self):
        """Gets the meta_model_name of this GoogleWorkspaceProvider.

        Return internal model name

        :return: The meta_model_name of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._meta_model_name

    @meta_model_name.setter
    def meta_model_name(self, meta_model_name):
        """Sets the meta_model_name of this GoogleWorkspaceProvider.

        Return internal model name

        :param meta_model_name: The meta_model_name of this GoogleWorkspaceProvider.
        :type meta_model_name: str
        """
        if meta_model_name is None:
            raise ValueError("Invalid value for `meta_model_name`, must not be `None`")

        self._meta_model_name = meta_model_name

    @property
    def delegated_subject(self):
        """Gets the delegated_subject of this GoogleWorkspaceProvider.


        :return: The delegated_subject of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._delegated_subject

    @delegated_subject.setter
    def delegated_subject(self, delegated_subject):
        """Sets the delegated_subject of this GoogleWorkspaceProvider.


        :param delegated_subject: The delegated_subject of this GoogleWorkspaceProvider.
        :type delegated_subject: str
        """
        if delegated_subject is None:
            raise ValueError("Invalid value for `delegated_subject`, must not be `None`")
        if delegated_subject is not None and len(delegated_subject) > 254:
            raise ValueError("Invalid value for `delegated_subject`, length must be less than or equal to `254`")

        self._delegated_subject = delegated_subject

    @property
    def credentials(self):
        """Gets the credentials of this GoogleWorkspaceProvider.


        :return: The credentials of this GoogleWorkspaceProvider.
        :rtype: object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this GoogleWorkspaceProvider.


        :param credentials: The credentials of this GoogleWorkspaceProvider.
        :type credentials: object
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")

        self._credentials = credentials

    @property
    def scopes(self):
        """Gets the scopes of this GoogleWorkspaceProvider.


        :return: The scopes of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this GoogleWorkspaceProvider.


        :param scopes: The scopes of this GoogleWorkspaceProvider.
        :type scopes: str
        """

        self._scopes = scopes

    @property
    def exclude_users_service_account(self):
        """Gets the exclude_users_service_account of this GoogleWorkspaceProvider.


        :return: The exclude_users_service_account of this GoogleWorkspaceProvider.
        :rtype: bool
        """
        return self._exclude_users_service_account

    @exclude_users_service_account.setter
    def exclude_users_service_account(self, exclude_users_service_account):
        """Sets the exclude_users_service_account of this GoogleWorkspaceProvider.


        :param exclude_users_service_account: The exclude_users_service_account of this GoogleWorkspaceProvider.
        :type exclude_users_service_account: bool
        """

        self._exclude_users_service_account = exclude_users_service_account

    @property
    def filter_group(self):
        """Gets the filter_group of this GoogleWorkspaceProvider.


        :return: The filter_group of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._filter_group

    @filter_group.setter
    def filter_group(self, filter_group):
        """Sets the filter_group of this GoogleWorkspaceProvider.


        :param filter_group: The filter_group of this GoogleWorkspaceProvider.
        :type filter_group: str
        """

        self._filter_group = filter_group

    @property
    def user_delete_action(self):
        """Gets the user_delete_action of this GoogleWorkspaceProvider.


        :return: The user_delete_action of this GoogleWorkspaceProvider.
        :rtype: OutgoingSyncDeleteAction
        """
        return self._user_delete_action

    @user_delete_action.setter
    def user_delete_action(self, user_delete_action):
        """Sets the user_delete_action of this GoogleWorkspaceProvider.


        :param user_delete_action: The user_delete_action of this GoogleWorkspaceProvider.
        :type user_delete_action: OutgoingSyncDeleteAction
        """

        self._user_delete_action = user_delete_action

    @property
    def group_delete_action(self):
        """Gets the group_delete_action of this GoogleWorkspaceProvider.


        :return: The group_delete_action of this GoogleWorkspaceProvider.
        :rtype: OutgoingSyncDeleteAction
        """
        return self._group_delete_action

    @group_delete_action.setter
    def group_delete_action(self, group_delete_action):
        """Sets the group_delete_action of this GoogleWorkspaceProvider.


        :param group_delete_action: The group_delete_action of this GoogleWorkspaceProvider.
        :type group_delete_action: OutgoingSyncDeleteAction
        """

        self._group_delete_action = group_delete_action

    @property
    def default_group_email_domain(self):
        """Gets the default_group_email_domain of this GoogleWorkspaceProvider.


        :return: The default_group_email_domain of this GoogleWorkspaceProvider.
        :rtype: str
        """
        return self._default_group_email_domain

    @default_group_email_domain.setter
    def default_group_email_domain(self, default_group_email_domain):
        """Sets the default_group_email_domain of this GoogleWorkspaceProvider.


        :param default_group_email_domain: The default_group_email_domain of this GoogleWorkspaceProvider.
        :type default_group_email_domain: str
        """
        if default_group_email_domain is None:
            raise ValueError("Invalid value for `default_group_email_domain`, must not be `None`")

        self._default_group_email_domain = default_group_email_domain
