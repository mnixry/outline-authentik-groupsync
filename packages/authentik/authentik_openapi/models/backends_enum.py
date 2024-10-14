# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.8.3
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class BackendsEnum(str, Enum):
    """
    BackendsEnum
    """

    """
    allowed enum values
    """
    AUTHENTIK_DOT_CORE_DOT_AUTH_DOT_INBUILT_BACKEND = 'authentik.core.auth.InbuiltBackend'
    AUTHENTIK_DOT_CORE_DOT_AUTH_DOT_TOKEN_BACKEND = 'authentik.core.auth.TokenBackend'
    AUTHENTIK_DOT_SOURCES_DOT_LDAP_DOT_AUTH_DOT_LDAP_BACKEND = 'authentik.sources.ldap.auth.LDAPBackend'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BackendsEnum from a JSON string"""
        return cls(json.loads(json_str))


