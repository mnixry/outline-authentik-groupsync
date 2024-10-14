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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.group_matching_mode_enum import GroupMatchingModeEnum
from authentik_openapi.models.policy_engine_mode import PolicyEngineMode
from authentik_openapi.models.provider_type_enum import ProviderTypeEnum
from authentik_openapi.models.user_matching_mode_enum import UserMatchingModeEnum
from typing import Optional, Set
from typing_extensions import Self

class OAuthSourceRequest(BaseModel):
    """
    OAuth Source Serializer
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Source's display Name.")
    slug: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="Internal source name, used in URLs.")
    enabled: Optional[StrictBool] = None
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow to use when authenticating existing users.")
    enrollment_flow: Optional[StrictStr] = Field(default=None, description="Flow to use when enrolling new users.")
    user_property_mappings: Optional[List[StrictStr]] = None
    group_property_mappings: Optional[List[StrictStr]] = None
    policy_engine_mode: Optional[PolicyEngineMode] = None
    user_matching_mode: Optional[UserMatchingModeEnum] = Field(default=None, description="How the source determines if an existing user should be authenticated or a new user enrolled.")
    user_path_template: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    group_matching_mode: Optional[GroupMatchingModeEnum] = Field(default=None, description="How the source determines if an existing group should be used or a new group created.")
    provider_type: ProviderTypeEnum
    request_token_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL used to request the initial token. This URL is only required for OAuth 1.")
    authorization_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL the user is redirect to to conest the flow.")
    access_token_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL used by authentik to retrieve tokens.")
    profile_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL used by authentik to get user information.")
    consumer_key: Annotated[str, Field(min_length=1, strict=True)]
    consumer_secret: Annotated[str, Field(min_length=1, strict=True)]
    additional_scopes: Optional[StrictStr] = None
    oidc_well_known_url: Optional[StrictStr] = None
    oidc_jwks_url: Optional[StrictStr] = None
    oidc_jwks: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["name", "slug", "enabled", "authentication_flow", "enrollment_flow", "user_property_mappings", "group_property_mappings", "policy_engine_mode", "user_matching_mode", "user_path_template", "group_matching_mode", "provider_type", "request_token_url", "authorization_url", "access_token_url", "profile_url", "consumer_key", "consumer_secret", "additional_scopes", "oidc_well_known_url", "oidc_jwks_url", "oidc_jwks"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
        return value

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
        """Create an instance of OAuthSourceRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
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

        # set to None if enrollment_flow (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_flow is None and "enrollment_flow" in self.model_fields_set:
            _dict['enrollment_flow'] = None

        # set to None if request_token_url (nullable) is None
        # and model_fields_set contains the field
        if self.request_token_url is None and "request_token_url" in self.model_fields_set:
            _dict['request_token_url'] = None

        # set to None if authorization_url (nullable) is None
        # and model_fields_set contains the field
        if self.authorization_url is None and "authorization_url" in self.model_fields_set:
            _dict['authorization_url'] = None

        # set to None if access_token_url (nullable) is None
        # and model_fields_set contains the field
        if self.access_token_url is None and "access_token_url" in self.model_fields_set:
            _dict['access_token_url'] = None

        # set to None if profile_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_url is None and "profile_url" in self.model_fields_set:
            _dict['profile_url'] = None

        # set to None if oidc_jwks (nullable) is None
        # and model_fields_set contains the field
        if self.oidc_jwks is None and "oidc_jwks" in self.model_fields_set:
            _dict['oidc_jwks'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuthSourceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "enabled": obj.get("enabled"),
            "authentication_flow": obj.get("authentication_flow"),
            "enrollment_flow": obj.get("enrollment_flow"),
            "user_property_mappings": obj.get("user_property_mappings"),
            "group_property_mappings": obj.get("group_property_mappings"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "user_matching_mode": obj.get("user_matching_mode"),
            "user_path_template": obj.get("user_path_template"),
            "group_matching_mode": obj.get("group_matching_mode"),
            "provider_type": obj.get("provider_type"),
            "request_token_url": obj.get("request_token_url"),
            "authorization_url": obj.get("authorization_url"),
            "access_token_url": obj.get("access_token_url"),
            "profile_url": obj.get("profile_url"),
            "consumer_key": obj.get("consumer_key"),
            "consumer_secret": obj.get("consumer_secret"),
            "additional_scopes": obj.get("additional_scopes"),
            "oidc_well_known_url": obj.get("oidc_well_known_url"),
            "oidc_jwks_url": obj.get("oidc_jwks_url"),
            "oidc_jwks": obj.get("oidc_jwks")
        })
        return _obj


