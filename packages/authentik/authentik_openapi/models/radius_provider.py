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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RadiusProvider(BaseModel):
    """
    RadiusProvider Serializer
    """ # noqa: E501
    pk: StrictInt
    name: StrictStr
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: StrictStr = Field(description="Flow used when authorizing this provider.")
    invalidation_flow: StrictStr = Field(description="Flow used ending the session from a provider.")
    property_mappings: Optional[List[StrictStr]] = None
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    assigned_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_application_name: StrictStr = Field(description="Application's display Name.")
    assigned_backchannel_application_slug: StrictStr = Field(description="Internal application name, used in URLs.")
    assigned_backchannel_application_name: StrictStr = Field(description="Application's display Name.")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    client_networks: Optional[StrictStr] = Field(default=None, description="List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped.")
    shared_secret: Optional[StrictStr] = Field(default=None, description="Shared secret between clients and server to hash packets.")
    outpost_set: List[StrictStr]
    mfa_support: Optional[StrictBool] = Field(default=None, description="When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon.")
    __properties: ClassVar[List[str]] = ["pk", "name", "authentication_flow", "authorization_flow", "invalidation_flow", "property_mappings", "component", "assigned_application_slug", "assigned_application_name", "assigned_backchannel_application_slug", "assigned_backchannel_application_name", "verbose_name", "verbose_name_plural", "meta_model_name", "client_networks", "shared_secret", "outpost_set", "mfa_support"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RadiusProvider from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "pk",
            "component",
            "assigned_application_slug",
            "assigned_application_name",
            "assigned_backchannel_application_slug",
            "assigned_backchannel_application_name",
            "verbose_name",
            "verbose_name_plural",
            "meta_model_name",
            "outpost_set",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if authentication_flow (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_flow is None and "authentication_flow" in self.model_fields_set:
            _dict['authentication_flow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RadiusProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "invalidation_flow": obj.get("invalidation_flow"),
            "property_mappings": obj.get("property_mappings"),
            "component": obj.get("component"),
            "assigned_application_slug": obj.get("assigned_application_slug"),
            "assigned_application_name": obj.get("assigned_application_name"),
            "assigned_backchannel_application_slug": obj.get("assigned_backchannel_application_slug"),
            "assigned_backchannel_application_name": obj.get("assigned_backchannel_application_name"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "client_networks": obj.get("client_networks"),
            "shared_secret": obj.get("shared_secret"),
            "outpost_set": obj.get("outpost_set"),
            "mfa_support": obj.get("mfa_support")
        })
        return _obj


