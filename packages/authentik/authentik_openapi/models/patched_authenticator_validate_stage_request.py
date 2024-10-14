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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.device_classes_enum import DeviceClassesEnum
from authentik_openapi.models.flow_set_request import FlowSetRequest
from authentik_openapi.models.not_configured_action_enum import NotConfiguredActionEnum
from authentik_openapi.models.user_verification_enum import UserVerificationEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedAuthenticatorValidateStageRequest(BaseModel):
    """
    AuthenticatorValidateStage Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    flow_set: Optional[List[FlowSetRequest]] = None
    not_configured_action: Optional[NotConfiguredActionEnum] = None
    device_classes: Optional[List[DeviceClassesEnum]] = Field(default=None, description="Device classes which can be used to authenticate")
    configuration_stages: Optional[List[StrictStr]] = Field(default=None, description="Stages used to configure Authenticator when user doesn't have any compatible devices. After this configuration Stage passes, the user is not prompted again.")
    last_auth_threshold: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="If any of the user's device has been used within this threshold, this stage will be skipped")
    webauthn_user_verification: Optional[UserVerificationEnum] = Field(default=None, description="Enforce user verification for WebAuthn devices.")
    webauthn_allowed_device_types: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["name", "flow_set", "not_configured_action", "device_classes", "configuration_stages", "last_auth_threshold", "webauthn_user_verification", "webauthn_allowed_device_types"]

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
        """Create an instance of PatchedAuthenticatorValidateStageRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item_flow_set in self.flow_set:
                if _item_flow_set:
                    _items.append(_item_flow_set.to_dict())
            _dict['flow_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedAuthenticatorValidateStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj["flow_set"]] if obj.get("flow_set") is not None else None,
            "not_configured_action": obj.get("not_configured_action"),
            "device_classes": obj.get("device_classes"),
            "configuration_stages": obj.get("configuration_stages"),
            "last_auth_threshold": obj.get("last_auth_threshold"),
            "webauthn_user_verification": obj.get("webauthn_user_verification"),
            "webauthn_allowed_device_types": obj.get("webauthn_allowed_device_types")
        })
        return _obj


