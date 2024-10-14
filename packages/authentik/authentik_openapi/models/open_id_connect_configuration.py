# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class OpenIDConnectConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issuer: str=None, authorization_endpoint: str=None, token_endpoint: str=None, userinfo_endpoint: str=None, end_session_endpoint: str=None, introspection_endpoint: str=None, jwks_uri: str=None, response_types_supported: List[str]=None, id_token_signing_alg_values_supported: List[str]=None, subject_types_supported: List[str]=None, token_endpoint_auth_methods_supported: List[str]=None):
        """OpenIDConnectConfiguration - a model defined in OpenAPI

        :param issuer: The issuer of this OpenIDConnectConfiguration.
        :param authorization_endpoint: The authorization_endpoint of this OpenIDConnectConfiguration.
        :param token_endpoint: The token_endpoint of this OpenIDConnectConfiguration.
        :param userinfo_endpoint: The userinfo_endpoint of this OpenIDConnectConfiguration.
        :param end_session_endpoint: The end_session_endpoint of this OpenIDConnectConfiguration.
        :param introspection_endpoint: The introspection_endpoint of this OpenIDConnectConfiguration.
        :param jwks_uri: The jwks_uri of this OpenIDConnectConfiguration.
        :param response_types_supported: The response_types_supported of this OpenIDConnectConfiguration.
        :param id_token_signing_alg_values_supported: The id_token_signing_alg_values_supported of this OpenIDConnectConfiguration.
        :param subject_types_supported: The subject_types_supported of this OpenIDConnectConfiguration.
        :param token_endpoint_auth_methods_supported: The token_endpoint_auth_methods_supported of this OpenIDConnectConfiguration.
        """
        self.openapi_types = {
            'issuer': str,
            'authorization_endpoint': str,
            'token_endpoint': str,
            'userinfo_endpoint': str,
            'end_session_endpoint': str,
            'introspection_endpoint': str,
            'jwks_uri': str,
            'response_types_supported': List[str],
            'id_token_signing_alg_values_supported': List[str],
            'subject_types_supported': List[str],
            'token_endpoint_auth_methods_supported': List[str]
        }

        self.attribute_map = {
            'issuer': 'issuer',
            'authorization_endpoint': 'authorization_endpoint',
            'token_endpoint': 'token_endpoint',
            'userinfo_endpoint': 'userinfo_endpoint',
            'end_session_endpoint': 'end_session_endpoint',
            'introspection_endpoint': 'introspection_endpoint',
            'jwks_uri': 'jwks_uri',
            'response_types_supported': 'response_types_supported',
            'id_token_signing_alg_values_supported': 'id_token_signing_alg_values_supported',
            'subject_types_supported': 'subject_types_supported',
            'token_endpoint_auth_methods_supported': 'token_endpoint_auth_methods_supported'
        }

        self._issuer = issuer
        self._authorization_endpoint = authorization_endpoint
        self._token_endpoint = token_endpoint
        self._userinfo_endpoint = userinfo_endpoint
        self._end_session_endpoint = end_session_endpoint
        self._introspection_endpoint = introspection_endpoint
        self._jwks_uri = jwks_uri
        self._response_types_supported = response_types_supported
        self._id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self._subject_types_supported = subject_types_supported
        self._token_endpoint_auth_methods_supported = token_endpoint_auth_methods_supported

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OpenIDConnectConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OpenIDConnectConfiguration of this OpenIDConnectConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issuer(self):
        """Gets the issuer of this OpenIDConnectConfiguration.


        :return: The issuer of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OpenIDConnectConfiguration.


        :param issuer: The issuer of this OpenIDConnectConfiguration.
        :type issuer: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")

        self._issuer = issuer

    @property
    def authorization_endpoint(self):
        """Gets the authorization_endpoint of this OpenIDConnectConfiguration.


        :return: The authorization_endpoint of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        """Sets the authorization_endpoint of this OpenIDConnectConfiguration.


        :param authorization_endpoint: The authorization_endpoint of this OpenIDConnectConfiguration.
        :type authorization_endpoint: str
        """
        if authorization_endpoint is None:
            raise ValueError("Invalid value for `authorization_endpoint`, must not be `None`")

        self._authorization_endpoint = authorization_endpoint

    @property
    def token_endpoint(self):
        """Gets the token_endpoint of this OpenIDConnectConfiguration.


        :return: The token_endpoint of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        """Sets the token_endpoint of this OpenIDConnectConfiguration.


        :param token_endpoint: The token_endpoint of this OpenIDConnectConfiguration.
        :type token_endpoint: str
        """
        if token_endpoint is None:
            raise ValueError("Invalid value for `token_endpoint`, must not be `None`")

        self._token_endpoint = token_endpoint

    @property
    def userinfo_endpoint(self):
        """Gets the userinfo_endpoint of this OpenIDConnectConfiguration.


        :return: The userinfo_endpoint of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._userinfo_endpoint

    @userinfo_endpoint.setter
    def userinfo_endpoint(self, userinfo_endpoint):
        """Sets the userinfo_endpoint of this OpenIDConnectConfiguration.


        :param userinfo_endpoint: The userinfo_endpoint of this OpenIDConnectConfiguration.
        :type userinfo_endpoint: str
        """
        if userinfo_endpoint is None:
            raise ValueError("Invalid value for `userinfo_endpoint`, must not be `None`")

        self._userinfo_endpoint = userinfo_endpoint

    @property
    def end_session_endpoint(self):
        """Gets the end_session_endpoint of this OpenIDConnectConfiguration.


        :return: The end_session_endpoint of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._end_session_endpoint

    @end_session_endpoint.setter
    def end_session_endpoint(self, end_session_endpoint):
        """Sets the end_session_endpoint of this OpenIDConnectConfiguration.


        :param end_session_endpoint: The end_session_endpoint of this OpenIDConnectConfiguration.
        :type end_session_endpoint: str
        """
        if end_session_endpoint is None:
            raise ValueError("Invalid value for `end_session_endpoint`, must not be `None`")

        self._end_session_endpoint = end_session_endpoint

    @property
    def introspection_endpoint(self):
        """Gets the introspection_endpoint of this OpenIDConnectConfiguration.


        :return: The introspection_endpoint of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._introspection_endpoint

    @introspection_endpoint.setter
    def introspection_endpoint(self, introspection_endpoint):
        """Sets the introspection_endpoint of this OpenIDConnectConfiguration.


        :param introspection_endpoint: The introspection_endpoint of this OpenIDConnectConfiguration.
        :type introspection_endpoint: str
        """
        if introspection_endpoint is None:
            raise ValueError("Invalid value for `introspection_endpoint`, must not be `None`")

        self._introspection_endpoint = introspection_endpoint

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this OpenIDConnectConfiguration.


        :return: The jwks_uri of this OpenIDConnectConfiguration.
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this OpenIDConnectConfiguration.


        :param jwks_uri: The jwks_uri of this OpenIDConnectConfiguration.
        :type jwks_uri: str
        """
        if jwks_uri is None:
            raise ValueError("Invalid value for `jwks_uri`, must not be `None`")

        self._jwks_uri = jwks_uri

    @property
    def response_types_supported(self):
        """Gets the response_types_supported of this OpenIDConnectConfiguration.


        :return: The response_types_supported of this OpenIDConnectConfiguration.
        :rtype: List[str]
        """
        return self._response_types_supported

    @response_types_supported.setter
    def response_types_supported(self, response_types_supported):
        """Sets the response_types_supported of this OpenIDConnectConfiguration.


        :param response_types_supported: The response_types_supported of this OpenIDConnectConfiguration.
        :type response_types_supported: List[str]
        """
        if response_types_supported is None:
            raise ValueError("Invalid value for `response_types_supported`, must not be `None`")

        self._response_types_supported = response_types_supported

    @property
    def id_token_signing_alg_values_supported(self):
        """Gets the id_token_signing_alg_values_supported of this OpenIDConnectConfiguration.


        :return: The id_token_signing_alg_values_supported of this OpenIDConnectConfiguration.
        :rtype: List[str]
        """
        return self._id_token_signing_alg_values_supported

    @id_token_signing_alg_values_supported.setter
    def id_token_signing_alg_values_supported(self, id_token_signing_alg_values_supported):
        """Sets the id_token_signing_alg_values_supported of this OpenIDConnectConfiguration.


        :param id_token_signing_alg_values_supported: The id_token_signing_alg_values_supported of this OpenIDConnectConfiguration.
        :type id_token_signing_alg_values_supported: List[str]
        """
        if id_token_signing_alg_values_supported is None:
            raise ValueError("Invalid value for `id_token_signing_alg_values_supported`, must not be `None`")

        self._id_token_signing_alg_values_supported = id_token_signing_alg_values_supported

    @property
    def subject_types_supported(self):
        """Gets the subject_types_supported of this OpenIDConnectConfiguration.


        :return: The subject_types_supported of this OpenIDConnectConfiguration.
        :rtype: List[str]
        """
        return self._subject_types_supported

    @subject_types_supported.setter
    def subject_types_supported(self, subject_types_supported):
        """Sets the subject_types_supported of this OpenIDConnectConfiguration.


        :param subject_types_supported: The subject_types_supported of this OpenIDConnectConfiguration.
        :type subject_types_supported: List[str]
        """
        if subject_types_supported is None:
            raise ValueError("Invalid value for `subject_types_supported`, must not be `None`")

        self._subject_types_supported = subject_types_supported

    @property
    def token_endpoint_auth_methods_supported(self):
        """Gets the token_endpoint_auth_methods_supported of this OpenIDConnectConfiguration.


        :return: The token_endpoint_auth_methods_supported of this OpenIDConnectConfiguration.
        :rtype: List[str]
        """
        return self._token_endpoint_auth_methods_supported

    @token_endpoint_auth_methods_supported.setter
    def token_endpoint_auth_methods_supported(self, token_endpoint_auth_methods_supported):
        """Sets the token_endpoint_auth_methods_supported of this OpenIDConnectConfiguration.


        :param token_endpoint_auth_methods_supported: The token_endpoint_auth_methods_supported of this OpenIDConnectConfiguration.
        :type token_endpoint_auth_methods_supported: List[str]
        """
        if token_endpoint_auth_methods_supported is None:
            raise ValueError("Invalid value for `token_endpoint_auth_methods_supported`, must not be `None`")

        self._token_endpoint_auth_methods_supported = token_endpoint_auth_methods_supported
