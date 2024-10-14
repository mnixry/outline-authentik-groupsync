# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class UserPlexSourceConnectionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identifier: str=None, plex_token: str=None):
        """UserPlexSourceConnectionRequest - a model defined in OpenAPI

        :param identifier: The identifier of this UserPlexSourceConnectionRequest.
        :param plex_token: The plex_token of this UserPlexSourceConnectionRequest.
        """
        self.openapi_types = {
            'identifier': str,
            'plex_token': str
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'plex_token': 'plex_token'
        }

        self._identifier = identifier
        self._plex_token = plex_token

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserPlexSourceConnectionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserPlexSourceConnectionRequest of this UserPlexSourceConnectionRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self):
        """Gets the identifier of this UserPlexSourceConnectionRequest.


        :return: The identifier of this UserPlexSourceConnectionRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserPlexSourceConnectionRequest.


        :param identifier: The identifier of this UserPlexSourceConnectionRequest.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")
        if identifier is not None and len(identifier) < 1:
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")

        self._identifier = identifier

    @property
    def plex_token(self):
        """Gets the plex_token of this UserPlexSourceConnectionRequest.


        :return: The plex_token of this UserPlexSourceConnectionRequest.
        :rtype: str
        """
        return self._plex_token

    @plex_token.setter
    def plex_token(self, plex_token):
        """Sets the plex_token of this UserPlexSourceConnectionRequest.


        :param plex_token: The plex_token of this UserPlexSourceConnectionRequest.
        :type plex_token: str
        """
        if plex_token is None:
            raise ValueError("Invalid value for `plex_token`, must not be `None`")
        if plex_token is not None and len(plex_token) < 1:
            raise ValueError("Invalid value for `plex_token`, length must be greater than or equal to `1`")

        self._plex_token = plex_token
