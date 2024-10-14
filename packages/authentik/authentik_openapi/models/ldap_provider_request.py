# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.ldapapi_access_mode import LDAPAPIAccessMode
from authentik_openapi import util


class LDAPProviderRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, authentication_flow: str=None, authorization_flow: str=None, property_mappings: List[str]=None, base_dn: str=None, certificate: str=None, tls_server_name: str=None, uid_start_number: int=None, gid_start_number: int=None, search_mode: LDAPAPIAccessMode=None, bind_mode: LDAPAPIAccessMode=None, mfa_support: bool=None):
        """LDAPProviderRequest - a model defined in OpenAPI

        :param name: The name of this LDAPProviderRequest.
        :param authentication_flow: The authentication_flow of this LDAPProviderRequest.
        :param authorization_flow: The authorization_flow of this LDAPProviderRequest.
        :param property_mappings: The property_mappings of this LDAPProviderRequest.
        :param base_dn: The base_dn of this LDAPProviderRequest.
        :param certificate: The certificate of this LDAPProviderRequest.
        :param tls_server_name: The tls_server_name of this LDAPProviderRequest.
        :param uid_start_number: The uid_start_number of this LDAPProviderRequest.
        :param gid_start_number: The gid_start_number of this LDAPProviderRequest.
        :param search_mode: The search_mode of this LDAPProviderRequest.
        :param bind_mode: The bind_mode of this LDAPProviderRequest.
        :param mfa_support: The mfa_support of this LDAPProviderRequest.
        """
        self.openapi_types = {
            'name': str,
            'authentication_flow': str,
            'authorization_flow': str,
            'property_mappings': List[str],
            'base_dn': str,
            'certificate': str,
            'tls_server_name': str,
            'uid_start_number': int,
            'gid_start_number': int,
            'search_mode': LDAPAPIAccessMode,
            'bind_mode': LDAPAPIAccessMode,
            'mfa_support': bool
        }

        self.attribute_map = {
            'name': 'name',
            'authentication_flow': 'authentication_flow',
            'authorization_flow': 'authorization_flow',
            'property_mappings': 'property_mappings',
            'base_dn': 'base_dn',
            'certificate': 'certificate',
            'tls_server_name': 'tls_server_name',
            'uid_start_number': 'uid_start_number',
            'gid_start_number': 'gid_start_number',
            'search_mode': 'search_mode',
            'bind_mode': 'bind_mode',
            'mfa_support': 'mfa_support'
        }

        self._name = name
        self._authentication_flow = authentication_flow
        self._authorization_flow = authorization_flow
        self._property_mappings = property_mappings
        self._base_dn = base_dn
        self._certificate = certificate
        self._tls_server_name = tls_server_name
        self._uid_start_number = uid_start_number
        self._gid_start_number = gid_start_number
        self._search_mode = search_mode
        self._bind_mode = bind_mode
        self._mfa_support = mfa_support

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LDAPProviderRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LDAPProviderRequest of this LDAPProviderRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this LDAPProviderRequest.


        :return: The name of this LDAPProviderRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LDAPProviderRequest.


        :param name: The name of this LDAPProviderRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def authentication_flow(self):
        """Gets the authentication_flow of this LDAPProviderRequest.

        Flow used for authentication when the associated application is accessed by an un-authenticated user.

        :return: The authentication_flow of this LDAPProviderRequest.
        :rtype: str
        """
        return self._authentication_flow

    @authentication_flow.setter
    def authentication_flow(self, authentication_flow):
        """Sets the authentication_flow of this LDAPProviderRequest.

        Flow used for authentication when the associated application is accessed by an un-authenticated user.

        :param authentication_flow: The authentication_flow of this LDAPProviderRequest.
        :type authentication_flow: str
        """

        self._authentication_flow = authentication_flow

    @property
    def authorization_flow(self):
        """Gets the authorization_flow of this LDAPProviderRequest.

        Flow used when authorizing this provider.

        :return: The authorization_flow of this LDAPProviderRequest.
        :rtype: str
        """
        return self._authorization_flow

    @authorization_flow.setter
    def authorization_flow(self, authorization_flow):
        """Sets the authorization_flow of this LDAPProviderRequest.

        Flow used when authorizing this provider.

        :param authorization_flow: The authorization_flow of this LDAPProviderRequest.
        :type authorization_flow: str
        """
        if authorization_flow is None:
            raise ValueError("Invalid value for `authorization_flow`, must not be `None`")

        self._authorization_flow = authorization_flow

    @property
    def property_mappings(self):
        """Gets the property_mappings of this LDAPProviderRequest.


        :return: The property_mappings of this LDAPProviderRequest.
        :rtype: List[str]
        """
        return self._property_mappings

    @property_mappings.setter
    def property_mappings(self, property_mappings):
        """Sets the property_mappings of this LDAPProviderRequest.


        :param property_mappings: The property_mappings of this LDAPProviderRequest.
        :type property_mappings: List[str]
        """

        self._property_mappings = property_mappings

    @property
    def base_dn(self):
        """Gets the base_dn of this LDAPProviderRequest.

        DN under which objects are accessible.

        :return: The base_dn of this LDAPProviderRequest.
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this LDAPProviderRequest.

        DN under which objects are accessible.

        :param base_dn: The base_dn of this LDAPProviderRequest.
        :type base_dn: str
        """
        if base_dn is not None and len(base_dn) < 1:
            raise ValueError("Invalid value for `base_dn`, length must be greater than or equal to `1`")

        self._base_dn = base_dn

    @property
    def certificate(self):
        """Gets the certificate of this LDAPProviderRequest.


        :return: The certificate of this LDAPProviderRequest.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this LDAPProviderRequest.


        :param certificate: The certificate of this LDAPProviderRequest.
        :type certificate: str
        """

        self._certificate = certificate

    @property
    def tls_server_name(self):
        """Gets the tls_server_name of this LDAPProviderRequest.


        :return: The tls_server_name of this LDAPProviderRequest.
        :rtype: str
        """
        return self._tls_server_name

    @tls_server_name.setter
    def tls_server_name(self, tls_server_name):
        """Sets the tls_server_name of this LDAPProviderRequest.


        :param tls_server_name: The tls_server_name of this LDAPProviderRequest.
        :type tls_server_name: str
        """

        self._tls_server_name = tls_server_name

    @property
    def uid_start_number(self):
        """Gets the uid_start_number of this LDAPProviderRequest.

        The start for uidNumbers, this number is added to the user.pk to make sure that the numbers aren't too low for POSIX users. Default is 2000 to ensure that we don't collide with local users uidNumber

        :return: The uid_start_number of this LDAPProviderRequest.
        :rtype: int
        """
        return self._uid_start_number

    @uid_start_number.setter
    def uid_start_number(self, uid_start_number):
        """Sets the uid_start_number of this LDAPProviderRequest.

        The start for uidNumbers, this number is added to the user.pk to make sure that the numbers aren't too low for POSIX users. Default is 2000 to ensure that we don't collide with local users uidNumber

        :param uid_start_number: The uid_start_number of this LDAPProviderRequest.
        :type uid_start_number: int
        """
        if uid_start_number is not None and uid_start_number > 2147483647:
            raise ValueError("Invalid value for `uid_start_number`, must be a value less than or equal to `2147483647`")
        if uid_start_number is not None and uid_start_number < -2147483648:
            raise ValueError("Invalid value for `uid_start_number`, must be a value greater than or equal to `-2147483648`")

        self._uid_start_number = uid_start_number

    @property
    def gid_start_number(self):
        """Gets the gid_start_number of this LDAPProviderRequest.

        The start for gidNumbers, this number is added to a number generated from the group.pk to make sure that the numbers aren't too low for POSIX groups. Default is 4000 to ensure that we don't collide with local groups or users primary groups gidNumber

        :return: The gid_start_number of this LDAPProviderRequest.
        :rtype: int
        """
        return self._gid_start_number

    @gid_start_number.setter
    def gid_start_number(self, gid_start_number):
        """Sets the gid_start_number of this LDAPProviderRequest.

        The start for gidNumbers, this number is added to a number generated from the group.pk to make sure that the numbers aren't too low for POSIX groups. Default is 4000 to ensure that we don't collide with local groups or users primary groups gidNumber

        :param gid_start_number: The gid_start_number of this LDAPProviderRequest.
        :type gid_start_number: int
        """
        if gid_start_number is not None and gid_start_number > 2147483647:
            raise ValueError("Invalid value for `gid_start_number`, must be a value less than or equal to `2147483647`")
        if gid_start_number is not None and gid_start_number < -2147483648:
            raise ValueError("Invalid value for `gid_start_number`, must be a value greater than or equal to `-2147483648`")

        self._gid_start_number = gid_start_number

    @property
    def search_mode(self):
        """Gets the search_mode of this LDAPProviderRequest.


        :return: The search_mode of this LDAPProviderRequest.
        :rtype: LDAPAPIAccessMode
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        """Sets the search_mode of this LDAPProviderRequest.


        :param search_mode: The search_mode of this LDAPProviderRequest.
        :type search_mode: LDAPAPIAccessMode
        """

        self._search_mode = search_mode

    @property
    def bind_mode(self):
        """Gets the bind_mode of this LDAPProviderRequest.


        :return: The bind_mode of this LDAPProviderRequest.
        :rtype: LDAPAPIAccessMode
        """
        return self._bind_mode

    @bind_mode.setter
    def bind_mode(self, bind_mode):
        """Sets the bind_mode of this LDAPProviderRequest.


        :param bind_mode: The bind_mode of this LDAPProviderRequest.
        :type bind_mode: LDAPAPIAccessMode
        """

        self._bind_mode = bind_mode

    @property
    def mfa_support(self):
        """Gets the mfa_support of this LDAPProviderRequest.

        When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon.

        :return: The mfa_support of this LDAPProviderRequest.
        :rtype: bool
        """
        return self._mfa_support

    @mfa_support.setter
    def mfa_support(self, mfa_support):
        """Sets the mfa_support of this LDAPProviderRequest.

        When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon.

        :param mfa_support: The mfa_support of this LDAPProviderRequest.
        :type mfa_support: bool
        """

        self._mfa_support = mfa_support
