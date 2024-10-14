# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.policy_engine_mode import PolicyEngineMode
from authentik_openapi.models.user_matching_mode_enum import UserMatchingModeEnum
import re
from authentik_openapi import util


class LDAPSourceRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, slug: str=None, enabled: bool=None, authentication_flow: str=None, enrollment_flow: str=None, user_property_mappings: List[str]=None, group_property_mappings: List[str]=None, policy_engine_mode: PolicyEngineMode=None, user_matching_mode: UserMatchingModeEnum=None, user_path_template: str=None, server_uri: str=None, peer_certificate: str=None, client_certificate: str=None, bind_cn: str=None, bind_password: str=None, start_tls: bool=None, sni: bool=None, base_dn: str=None, additional_user_dn: str=None, additional_group_dn: str=None, user_object_filter: str=None, group_object_filter: str=None, group_membership_field: str=None, object_uniqueness_field: str=None, password_login_update_internal_password: bool=None, sync_users: bool=None, sync_users_password: bool=None, sync_groups: bool=None, sync_parent_group: str=None):
        """LDAPSourceRequest - a model defined in OpenAPI

        :param name: The name of this LDAPSourceRequest.
        :param slug: The slug of this LDAPSourceRequest.
        :param enabled: The enabled of this LDAPSourceRequest.
        :param authentication_flow: The authentication_flow of this LDAPSourceRequest.
        :param enrollment_flow: The enrollment_flow of this LDAPSourceRequest.
        :param user_property_mappings: The user_property_mappings of this LDAPSourceRequest.
        :param group_property_mappings: The group_property_mappings of this LDAPSourceRequest.
        :param policy_engine_mode: The policy_engine_mode of this LDAPSourceRequest.
        :param user_matching_mode: The user_matching_mode of this LDAPSourceRequest.
        :param user_path_template: The user_path_template of this LDAPSourceRequest.
        :param server_uri: The server_uri of this LDAPSourceRequest.
        :param peer_certificate: The peer_certificate of this LDAPSourceRequest.
        :param client_certificate: The client_certificate of this LDAPSourceRequest.
        :param bind_cn: The bind_cn of this LDAPSourceRequest.
        :param bind_password: The bind_password of this LDAPSourceRequest.
        :param start_tls: The start_tls of this LDAPSourceRequest.
        :param sni: The sni of this LDAPSourceRequest.
        :param base_dn: The base_dn of this LDAPSourceRequest.
        :param additional_user_dn: The additional_user_dn of this LDAPSourceRequest.
        :param additional_group_dn: The additional_group_dn of this LDAPSourceRequest.
        :param user_object_filter: The user_object_filter of this LDAPSourceRequest.
        :param group_object_filter: The group_object_filter of this LDAPSourceRequest.
        :param group_membership_field: The group_membership_field of this LDAPSourceRequest.
        :param object_uniqueness_field: The object_uniqueness_field of this LDAPSourceRequest.
        :param password_login_update_internal_password: The password_login_update_internal_password of this LDAPSourceRequest.
        :param sync_users: The sync_users of this LDAPSourceRequest.
        :param sync_users_password: The sync_users_password of this LDAPSourceRequest.
        :param sync_groups: The sync_groups of this LDAPSourceRequest.
        :param sync_parent_group: The sync_parent_group of this LDAPSourceRequest.
        """
        self.openapi_types = {
            'name': str,
            'slug': str,
            'enabled': bool,
            'authentication_flow': str,
            'enrollment_flow': str,
            'user_property_mappings': List[str],
            'group_property_mappings': List[str],
            'policy_engine_mode': PolicyEngineMode,
            'user_matching_mode': UserMatchingModeEnum,
            'user_path_template': str,
            'server_uri': str,
            'peer_certificate': str,
            'client_certificate': str,
            'bind_cn': str,
            'bind_password': str,
            'start_tls': bool,
            'sni': bool,
            'base_dn': str,
            'additional_user_dn': str,
            'additional_group_dn': str,
            'user_object_filter': str,
            'group_object_filter': str,
            'group_membership_field': str,
            'object_uniqueness_field': str,
            'password_login_update_internal_password': bool,
            'sync_users': bool,
            'sync_users_password': bool,
            'sync_groups': bool,
            'sync_parent_group': str
        }

        self.attribute_map = {
            'name': 'name',
            'slug': 'slug',
            'enabled': 'enabled',
            'authentication_flow': 'authentication_flow',
            'enrollment_flow': 'enrollment_flow',
            'user_property_mappings': 'user_property_mappings',
            'group_property_mappings': 'group_property_mappings',
            'policy_engine_mode': 'policy_engine_mode',
            'user_matching_mode': 'user_matching_mode',
            'user_path_template': 'user_path_template',
            'server_uri': 'server_uri',
            'peer_certificate': 'peer_certificate',
            'client_certificate': 'client_certificate',
            'bind_cn': 'bind_cn',
            'bind_password': 'bind_password',
            'start_tls': 'start_tls',
            'sni': 'sni',
            'base_dn': 'base_dn',
            'additional_user_dn': 'additional_user_dn',
            'additional_group_dn': 'additional_group_dn',
            'user_object_filter': 'user_object_filter',
            'group_object_filter': 'group_object_filter',
            'group_membership_field': 'group_membership_field',
            'object_uniqueness_field': 'object_uniqueness_field',
            'password_login_update_internal_password': 'password_login_update_internal_password',
            'sync_users': 'sync_users',
            'sync_users_password': 'sync_users_password',
            'sync_groups': 'sync_groups',
            'sync_parent_group': 'sync_parent_group'
        }

        self._name = name
        self._slug = slug
        self._enabled = enabled
        self._authentication_flow = authentication_flow
        self._enrollment_flow = enrollment_flow
        self._user_property_mappings = user_property_mappings
        self._group_property_mappings = group_property_mappings
        self._policy_engine_mode = policy_engine_mode
        self._user_matching_mode = user_matching_mode
        self._user_path_template = user_path_template
        self._server_uri = server_uri
        self._peer_certificate = peer_certificate
        self._client_certificate = client_certificate
        self._bind_cn = bind_cn
        self._bind_password = bind_password
        self._start_tls = start_tls
        self._sni = sni
        self._base_dn = base_dn
        self._additional_user_dn = additional_user_dn
        self._additional_group_dn = additional_group_dn
        self._user_object_filter = user_object_filter
        self._group_object_filter = group_object_filter
        self._group_membership_field = group_membership_field
        self._object_uniqueness_field = object_uniqueness_field
        self._password_login_update_internal_password = password_login_update_internal_password
        self._sync_users = sync_users
        self._sync_users_password = sync_users_password
        self._sync_groups = sync_groups
        self._sync_parent_group = sync_parent_group

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LDAPSourceRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LDAPSourceRequest of this LDAPSourceRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this LDAPSourceRequest.

        Source's display Name.

        :return: The name of this LDAPSourceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LDAPSourceRequest.

        Source's display Name.

        :param name: The name of this LDAPSourceRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this LDAPSourceRequest.

        Internal source name, used in URLs.

        :return: The slug of this LDAPSourceRequest.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this LDAPSourceRequest.

        Internal source name, used in URLs.

        :param slug: The slug of this LDAPSourceRequest.
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
        """Gets the enabled of this LDAPSourceRequest.


        :return: The enabled of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LDAPSourceRequest.


        :param enabled: The enabled of this LDAPSourceRequest.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def authentication_flow(self):
        """Gets the authentication_flow of this LDAPSourceRequest.

        Flow to use when authenticating existing users.

        :return: The authentication_flow of this LDAPSourceRequest.
        :rtype: str
        """
        return self._authentication_flow

    @authentication_flow.setter
    def authentication_flow(self, authentication_flow):
        """Sets the authentication_flow of this LDAPSourceRequest.

        Flow to use when authenticating existing users.

        :param authentication_flow: The authentication_flow of this LDAPSourceRequest.
        :type authentication_flow: str
        """

        self._authentication_flow = authentication_flow

    @property
    def enrollment_flow(self):
        """Gets the enrollment_flow of this LDAPSourceRequest.

        Flow to use when enrolling new users.

        :return: The enrollment_flow of this LDAPSourceRequest.
        :rtype: str
        """
        return self._enrollment_flow

    @enrollment_flow.setter
    def enrollment_flow(self, enrollment_flow):
        """Sets the enrollment_flow of this LDAPSourceRequest.

        Flow to use when enrolling new users.

        :param enrollment_flow: The enrollment_flow of this LDAPSourceRequest.
        :type enrollment_flow: str
        """

        self._enrollment_flow = enrollment_flow

    @property
    def user_property_mappings(self):
        """Gets the user_property_mappings of this LDAPSourceRequest.


        :return: The user_property_mappings of this LDAPSourceRequest.
        :rtype: List[str]
        """
        return self._user_property_mappings

    @user_property_mappings.setter
    def user_property_mappings(self, user_property_mappings):
        """Sets the user_property_mappings of this LDAPSourceRequest.


        :param user_property_mappings: The user_property_mappings of this LDAPSourceRequest.
        :type user_property_mappings: List[str]
        """

        self._user_property_mappings = user_property_mappings

    @property
    def group_property_mappings(self):
        """Gets the group_property_mappings of this LDAPSourceRequest.


        :return: The group_property_mappings of this LDAPSourceRequest.
        :rtype: List[str]
        """
        return self._group_property_mappings

    @group_property_mappings.setter
    def group_property_mappings(self, group_property_mappings):
        """Sets the group_property_mappings of this LDAPSourceRequest.


        :param group_property_mappings: The group_property_mappings of this LDAPSourceRequest.
        :type group_property_mappings: List[str]
        """

        self._group_property_mappings = group_property_mappings

    @property
    def policy_engine_mode(self):
        """Gets the policy_engine_mode of this LDAPSourceRequest.


        :return: The policy_engine_mode of this LDAPSourceRequest.
        :rtype: PolicyEngineMode
        """
        return self._policy_engine_mode

    @policy_engine_mode.setter
    def policy_engine_mode(self, policy_engine_mode):
        """Sets the policy_engine_mode of this LDAPSourceRequest.


        :param policy_engine_mode: The policy_engine_mode of this LDAPSourceRequest.
        :type policy_engine_mode: PolicyEngineMode
        """

        self._policy_engine_mode = policy_engine_mode

    @property
    def user_matching_mode(self):
        """Gets the user_matching_mode of this LDAPSourceRequest.

        How the source determines if an existing user should be authenticated or a new user enrolled.

        :return: The user_matching_mode of this LDAPSourceRequest.
        :rtype: UserMatchingModeEnum
        """
        return self._user_matching_mode

    @user_matching_mode.setter
    def user_matching_mode(self, user_matching_mode):
        """Sets the user_matching_mode of this LDAPSourceRequest.

        How the source determines if an existing user should be authenticated or a new user enrolled.

        :param user_matching_mode: The user_matching_mode of this LDAPSourceRequest.
        :type user_matching_mode: UserMatchingModeEnum
        """

        self._user_matching_mode = user_matching_mode

    @property
    def user_path_template(self):
        """Gets the user_path_template of this LDAPSourceRequest.


        :return: The user_path_template of this LDAPSourceRequest.
        :rtype: str
        """
        return self._user_path_template

    @user_path_template.setter
    def user_path_template(self, user_path_template):
        """Sets the user_path_template of this LDAPSourceRequest.


        :param user_path_template: The user_path_template of this LDAPSourceRequest.
        :type user_path_template: str
        """
        if user_path_template is not None and len(user_path_template) < 1:
            raise ValueError("Invalid value for `user_path_template`, length must be greater than or equal to `1`")

        self._user_path_template = user_path_template

    @property
    def server_uri(self):
        """Gets the server_uri of this LDAPSourceRequest.


        :return: The server_uri of this LDAPSourceRequest.
        :rtype: str
        """
        return self._server_uri

    @server_uri.setter
    def server_uri(self, server_uri):
        """Sets the server_uri of this LDAPSourceRequest.


        :param server_uri: The server_uri of this LDAPSourceRequest.
        :type server_uri: str
        """
        if server_uri is None:
            raise ValueError("Invalid value for `server_uri`, must not be `None`")
        if server_uri is not None and len(server_uri) < 1:
            raise ValueError("Invalid value for `server_uri`, length must be greater than or equal to `1`")

        self._server_uri = server_uri

    @property
    def peer_certificate(self):
        """Gets the peer_certificate of this LDAPSourceRequest.

        Optionally verify the LDAP Server's Certificate against the CA Chain in this keypair.

        :return: The peer_certificate of this LDAPSourceRequest.
        :rtype: str
        """
        return self._peer_certificate

    @peer_certificate.setter
    def peer_certificate(self, peer_certificate):
        """Sets the peer_certificate of this LDAPSourceRequest.

        Optionally verify the LDAP Server's Certificate against the CA Chain in this keypair.

        :param peer_certificate: The peer_certificate of this LDAPSourceRequest.
        :type peer_certificate: str
        """

        self._peer_certificate = peer_certificate

    @property
    def client_certificate(self):
        """Gets the client_certificate of this LDAPSourceRequest.

        Client certificate to authenticate against the LDAP Server's Certificate.

        :return: The client_certificate of this LDAPSourceRequest.
        :rtype: str
        """
        return self._client_certificate

    @client_certificate.setter
    def client_certificate(self, client_certificate):
        """Sets the client_certificate of this LDAPSourceRequest.

        Client certificate to authenticate against the LDAP Server's Certificate.

        :param client_certificate: The client_certificate of this LDAPSourceRequest.
        :type client_certificate: str
        """

        self._client_certificate = client_certificate

    @property
    def bind_cn(self):
        """Gets the bind_cn of this LDAPSourceRequest.


        :return: The bind_cn of this LDAPSourceRequest.
        :rtype: str
        """
        return self._bind_cn

    @bind_cn.setter
    def bind_cn(self, bind_cn):
        """Sets the bind_cn of this LDAPSourceRequest.


        :param bind_cn: The bind_cn of this LDAPSourceRequest.
        :type bind_cn: str
        """

        self._bind_cn = bind_cn

    @property
    def bind_password(self):
        """Gets the bind_password of this LDAPSourceRequest.


        :return: The bind_password of this LDAPSourceRequest.
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """Sets the bind_password of this LDAPSourceRequest.


        :param bind_password: The bind_password of this LDAPSourceRequest.
        :type bind_password: str
        """

        self._bind_password = bind_password

    @property
    def start_tls(self):
        """Gets the start_tls of this LDAPSourceRequest.


        :return: The start_tls of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._start_tls

    @start_tls.setter
    def start_tls(self, start_tls):
        """Sets the start_tls of this LDAPSourceRequest.


        :param start_tls: The start_tls of this LDAPSourceRequest.
        :type start_tls: bool
        """

        self._start_tls = start_tls

    @property
    def sni(self):
        """Gets the sni of this LDAPSourceRequest.


        :return: The sni of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._sni

    @sni.setter
    def sni(self, sni):
        """Sets the sni of this LDAPSourceRequest.


        :param sni: The sni of this LDAPSourceRequest.
        :type sni: bool
        """

        self._sni = sni

    @property
    def base_dn(self):
        """Gets the base_dn of this LDAPSourceRequest.


        :return: The base_dn of this LDAPSourceRequest.
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this LDAPSourceRequest.


        :param base_dn: The base_dn of this LDAPSourceRequest.
        :type base_dn: str
        """
        if base_dn is None:
            raise ValueError("Invalid value for `base_dn`, must not be `None`")
        if base_dn is not None and len(base_dn) < 1:
            raise ValueError("Invalid value for `base_dn`, length must be greater than or equal to `1`")

        self._base_dn = base_dn

    @property
    def additional_user_dn(self):
        """Gets the additional_user_dn of this LDAPSourceRequest.

        Prepended to Base DN for User-queries.

        :return: The additional_user_dn of this LDAPSourceRequest.
        :rtype: str
        """
        return self._additional_user_dn

    @additional_user_dn.setter
    def additional_user_dn(self, additional_user_dn):
        """Sets the additional_user_dn of this LDAPSourceRequest.

        Prepended to Base DN for User-queries.

        :param additional_user_dn: The additional_user_dn of this LDAPSourceRequest.
        :type additional_user_dn: str
        """

        self._additional_user_dn = additional_user_dn

    @property
    def additional_group_dn(self):
        """Gets the additional_group_dn of this LDAPSourceRequest.

        Prepended to Base DN for Group-queries.

        :return: The additional_group_dn of this LDAPSourceRequest.
        :rtype: str
        """
        return self._additional_group_dn

    @additional_group_dn.setter
    def additional_group_dn(self, additional_group_dn):
        """Sets the additional_group_dn of this LDAPSourceRequest.

        Prepended to Base DN for Group-queries.

        :param additional_group_dn: The additional_group_dn of this LDAPSourceRequest.
        :type additional_group_dn: str
        """

        self._additional_group_dn = additional_group_dn

    @property
    def user_object_filter(self):
        """Gets the user_object_filter of this LDAPSourceRequest.

        Consider Objects matching this filter to be Users.

        :return: The user_object_filter of this LDAPSourceRequest.
        :rtype: str
        """
        return self._user_object_filter

    @user_object_filter.setter
    def user_object_filter(self, user_object_filter):
        """Sets the user_object_filter of this LDAPSourceRequest.

        Consider Objects matching this filter to be Users.

        :param user_object_filter: The user_object_filter of this LDAPSourceRequest.
        :type user_object_filter: str
        """
        if user_object_filter is not None and len(user_object_filter) < 1:
            raise ValueError("Invalid value for `user_object_filter`, length must be greater than or equal to `1`")

        self._user_object_filter = user_object_filter

    @property
    def group_object_filter(self):
        """Gets the group_object_filter of this LDAPSourceRequest.

        Consider Objects matching this filter to be Groups.

        :return: The group_object_filter of this LDAPSourceRequest.
        :rtype: str
        """
        return self._group_object_filter

    @group_object_filter.setter
    def group_object_filter(self, group_object_filter):
        """Sets the group_object_filter of this LDAPSourceRequest.

        Consider Objects matching this filter to be Groups.

        :param group_object_filter: The group_object_filter of this LDAPSourceRequest.
        :type group_object_filter: str
        """
        if group_object_filter is not None and len(group_object_filter) < 1:
            raise ValueError("Invalid value for `group_object_filter`, length must be greater than or equal to `1`")

        self._group_object_filter = group_object_filter

    @property
    def group_membership_field(self):
        """Gets the group_membership_field of this LDAPSourceRequest.

        Field which contains members of a group.

        :return: The group_membership_field of this LDAPSourceRequest.
        :rtype: str
        """
        return self._group_membership_field

    @group_membership_field.setter
    def group_membership_field(self, group_membership_field):
        """Sets the group_membership_field of this LDAPSourceRequest.

        Field which contains members of a group.

        :param group_membership_field: The group_membership_field of this LDAPSourceRequest.
        :type group_membership_field: str
        """
        if group_membership_field is not None and len(group_membership_field) < 1:
            raise ValueError("Invalid value for `group_membership_field`, length must be greater than or equal to `1`")

        self._group_membership_field = group_membership_field

    @property
    def object_uniqueness_field(self):
        """Gets the object_uniqueness_field of this LDAPSourceRequest.

        Field which contains a unique Identifier.

        :return: The object_uniqueness_field of this LDAPSourceRequest.
        :rtype: str
        """
        return self._object_uniqueness_field

    @object_uniqueness_field.setter
    def object_uniqueness_field(self, object_uniqueness_field):
        """Sets the object_uniqueness_field of this LDAPSourceRequest.

        Field which contains a unique Identifier.

        :param object_uniqueness_field: The object_uniqueness_field of this LDAPSourceRequest.
        :type object_uniqueness_field: str
        """
        if object_uniqueness_field is not None and len(object_uniqueness_field) < 1:
            raise ValueError("Invalid value for `object_uniqueness_field`, length must be greater than or equal to `1`")

        self._object_uniqueness_field = object_uniqueness_field

    @property
    def password_login_update_internal_password(self):
        """Gets the password_login_update_internal_password of this LDAPSourceRequest.

        Update internal authentik password when login succeeds with LDAP

        :return: The password_login_update_internal_password of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._password_login_update_internal_password

    @password_login_update_internal_password.setter
    def password_login_update_internal_password(self, password_login_update_internal_password):
        """Sets the password_login_update_internal_password of this LDAPSourceRequest.

        Update internal authentik password when login succeeds with LDAP

        :param password_login_update_internal_password: The password_login_update_internal_password of this LDAPSourceRequest.
        :type password_login_update_internal_password: bool
        """

        self._password_login_update_internal_password = password_login_update_internal_password

    @property
    def sync_users(self):
        """Gets the sync_users of this LDAPSourceRequest.


        :return: The sync_users of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._sync_users

    @sync_users.setter
    def sync_users(self, sync_users):
        """Sets the sync_users of this LDAPSourceRequest.


        :param sync_users: The sync_users of this LDAPSourceRequest.
        :type sync_users: bool
        """

        self._sync_users = sync_users

    @property
    def sync_users_password(self):
        """Gets the sync_users_password of this LDAPSourceRequest.

        When a user changes their password, sync it back to LDAP. This can only be enabled on a single LDAP source.

        :return: The sync_users_password of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._sync_users_password

    @sync_users_password.setter
    def sync_users_password(self, sync_users_password):
        """Sets the sync_users_password of this LDAPSourceRequest.

        When a user changes their password, sync it back to LDAP. This can only be enabled on a single LDAP source.

        :param sync_users_password: The sync_users_password of this LDAPSourceRequest.
        :type sync_users_password: bool
        """

        self._sync_users_password = sync_users_password

    @property
    def sync_groups(self):
        """Gets the sync_groups of this LDAPSourceRequest.


        :return: The sync_groups of this LDAPSourceRequest.
        :rtype: bool
        """
        return self._sync_groups

    @sync_groups.setter
    def sync_groups(self, sync_groups):
        """Sets the sync_groups of this LDAPSourceRequest.


        :param sync_groups: The sync_groups of this LDAPSourceRequest.
        :type sync_groups: bool
        """

        self._sync_groups = sync_groups

    @property
    def sync_parent_group(self):
        """Gets the sync_parent_group of this LDAPSourceRequest.


        :return: The sync_parent_group of this LDAPSourceRequest.
        :rtype: str
        """
        return self._sync_parent_group

    @sync_parent_group.setter
    def sync_parent_group(self, sync_parent_group):
        """Sets the sync_parent_group of this LDAPSourceRequest.


        :param sync_parent_group: The sync_parent_group of this LDAPSourceRequest.
        :type sync_parent_group: str
        """

        self._sync_parent_group = sync_parent_group
