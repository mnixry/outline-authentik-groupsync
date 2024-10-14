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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.flow_set_request import FlowSetRequest
from authentik_openapi.models.user_fields_enum import UserFieldsEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedIdentificationStageRequest(BaseModel):
    """
    IdentificationStage Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    flow_set: Optional[List[FlowSetRequest]] = None
    user_fields: Optional[List[UserFieldsEnum]] = Field(default=None, description="Fields of the user object to match against. (Hold shift to select multiple options)")
    password_stage: Optional[StrictStr] = Field(default=None, description="When set, shows a password field, instead of showing the password field as separate step.")
    case_insensitive_matching: Optional[StrictBool] = Field(default=None, description="When enabled, user fields are matched regardless of their casing.")
    show_matched_user: Optional[StrictBool] = Field(default=None, description="When a valid username/email has been entered, and this option is enabled, the user's username and avatar will be shown. Otherwise, the text that the user entered will be shown")
    enrollment_flow: Optional[StrictStr] = Field(default=None, description="Optional enrollment flow, which is linked at the bottom of the page.")
    recovery_flow: Optional[StrictStr] = Field(default=None, description="Optional recovery flow, which is linked at the bottom of the page.")
    passwordless_flow: Optional[StrictStr] = Field(default=None, description="Optional passwordless flow, which is linked at the bottom of the page.")
    sources: Optional[List[StrictStr]] = Field(default=None, description="Specify which sources should be shown.")
    show_source_labels: Optional[StrictBool] = None
    pretend_user_exists: Optional[StrictBool] = Field(default=None, description="When enabled, the stage will succeed and continue even when incorrect user info is entered.")
    __properties: ClassVar[List[str]] = ["name", "flow_set", "user_fields", "password_stage", "case_insensitive_matching", "show_matched_user", "enrollment_flow", "recovery_flow", "passwordless_flow", "sources", "show_source_labels", "pretend_user_exists"]

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
        """Create an instance of PatchedIdentificationStageRequest from a JSON string"""
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
        # set to None if password_stage (nullable) is None
        # and model_fields_set contains the field
        if self.password_stage is None and "password_stage" in self.model_fields_set:
            _dict['password_stage'] = None

        # set to None if enrollment_flow (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_flow is None and "enrollment_flow" in self.model_fields_set:
            _dict['enrollment_flow'] = None

        # set to None if recovery_flow (nullable) is None
        # and model_fields_set contains the field
        if self.recovery_flow is None and "recovery_flow" in self.model_fields_set:
            _dict['recovery_flow'] = None

        # set to None if passwordless_flow (nullable) is None
        # and model_fields_set contains the field
        if self.passwordless_flow is None and "passwordless_flow" in self.model_fields_set:
            _dict['passwordless_flow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedIdentificationStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj["flow_set"]] if obj.get("flow_set") is not None else None,
            "user_fields": obj.get("user_fields"),
            "password_stage": obj.get("password_stage"),
            "case_insensitive_matching": obj.get("case_insensitive_matching"),
            "show_matched_user": obj.get("show_matched_user"),
            "enrollment_flow": obj.get("enrollment_flow"),
            "recovery_flow": obj.get("recovery_flow"),
            "passwordless_flow": obj.get("passwordless_flow"),
            "sources": obj.get("sources"),
            "show_source_labels": obj.get("show_source_labels"),
            "pretend_user_exists": obj.get("pretend_user_exists")
        })
        return _obj


