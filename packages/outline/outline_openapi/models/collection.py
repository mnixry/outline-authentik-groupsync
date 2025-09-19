# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a `POST` method on `https://app.getoutline.com/api/:method`. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  ## API key  You can create new API keys under **Settings => API & Apps**. Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you should supply the API key as the `Authorization` header (`Authorization: Bearer YOUR_API_KEY`).  ## OAuth 2.0  OAuth 2.0 is a widely used protocol for authorization and authentication. It allows users to grant third-party _or_ internal applications access to their resources without sharing their credentials. To use OAuth 2.0 you need to follow these steps:  1. Register your application under **Settings => Applications** 2. Obtain an access token by exchanging the client credentials for an access token 3. Use the access token to authenticate requests to the API  Some API endpoints allow unauthenticated requests for public resources and they can be called without authentication  # Scopes  Scopes are used to limit the access of an API key or application to specific resources. For example, an application may only need access to read documents, but not write them. Scopes can be global in the case of `read` and `write` scopes, scoped to a namespace, scoped to an API endpoint, or use wildcard scopes like `documents.*`. Some examples of scopes that can be used are:  ## Global  - `read`: Allows all read actions - `write`: Allows all read and write actions  ## Namespaced  - `documents:read`: Allows all document read actions - `collections:write`: Allows all collection write actions  ## Endpoints  - `documents.info`: Allows only one specific API method - `documents.*`: Allows all document API methods - `users.*`: Allows all user API methods  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Rate limits  Like most APIs, Outline has rate limits in place to prevent abuse. Endpoints that mutate data are more restrictive than read-only endpoints. If you exceed the rate limit for a given endpoint, you will receive a `429 Too Many Requests` status code.  The response will include a `Retry-After` header that indicates how many seconds you should wait before making another request.  # Policies  Most API resources have associated \"policies\", these objects describe the current authentications authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible. 

    The version of the OpenAPI document: 0.1.0
    Contact: hello@getoutline.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from outline_openapi.models.collection_sort import CollectionSort
from outline_openapi.models.permission import Permission
from outline_openapi.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class Collection(BaseModel):
    """
    Collection
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the object.")
    url_id: Optional[StrictStr] = Field(default=None, description="A short unique identifier that can be used to identify the collection instead of the UUID.", alias="urlId")
    name: Optional[StrictStr] = Field(default=None, description="The name of the collection.")
    description: Optional[StrictStr] = Field(default=None, description="A description of the collection, may contain markdown formatting")
    sort: Optional[CollectionSort] = None
    index: Optional[StrictStr] = Field(default=None, description="The position of the collection in the sidebar")
    color: Optional[StrictStr] = Field(default=None, description="A color representing the collection, this is used to help make collections more identifiable in the UI. It should be in HEX format including the #")
    icon: Optional[StrictStr] = Field(default=None, description="A string that represents an icon in the outline-icons package or an emoji")
    permission: Optional[Permission] = None
    sharing: Optional[StrictBool] = Field(default=False, description="Whether public document sharing is enabled in this collection")
    created_at: Optional[datetime] = Field(default=None, description="The date and time that this object was created", alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, description="The date and time that this object was last changed", alias="updatedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="The date and time that this object was deleted", alias="deletedAt")
    archived_at: Optional[datetime] = Field(default=None, description="The date and time that this object was archived", alias="archivedAt")
    archived_by: Optional[User] = Field(default=None, alias="archivedBy")
    __properties: ClassVar[List[str]] = ["id", "urlId", "name", "description", "sort", "index", "color", "icon", "permission", "sharing", "createdAt", "updatedAt", "deletedAt", "archivedAt", "archivedBy"]

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
        """Create an instance of Collection from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "url_id",
            "created_at",
            "updated_at",
            "deleted_at",
            "archived_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of archived_by
        if self.archived_by:
            _dict['archivedBy'] = self.archived_by.to_dict()
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deletedAt'] = None

        # set to None if archived_at (nullable) is None
        # and model_fields_set contains the field
        if self.archived_at is None and "archived_at" in self.model_fields_set:
            _dict['archivedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Collection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "urlId": obj.get("urlId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "sort": CollectionSort.from_dict(obj["sort"]) if obj.get("sort") is not None else None,
            "index": obj.get("index"),
            "color": obj.get("color"),
            "icon": obj.get("icon"),
            "permission": obj.get("permission"),
            "sharing": obj.get("sharing") if obj.get("sharing") is not None else False,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "deletedAt": obj.get("deletedAt"),
            "archivedAt": obj.get("archivedAt"),
            "archivedBy": User.from_dict(obj["archivedBy"]) if obj.get("archivedBy") is not None else None
        })
        return _obj


