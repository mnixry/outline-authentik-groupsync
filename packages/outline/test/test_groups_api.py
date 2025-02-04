# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST` methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token` parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Most API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible. 

    The version of the OpenAPI document: 0.1.0
    Contact: hello@getoutline.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from outline_openapi.api.groups_api import GroupsApi


class TestGroupsApi(unittest.IsolatedAsyncioTestCase):
    """GroupsApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = GroupsApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_groups_add_user_post(self) -> None:
        """Test case for groups_add_user_post

        Add a group member
        """
        pass

    async def test_groups_create_post(self) -> None:
        """Test case for groups_create_post

        Create a group
        """
        pass

    async def test_groups_delete_post(self) -> None:
        """Test case for groups_delete_post

        Delete a group
        """
        pass

    async def test_groups_info_post(self) -> None:
        """Test case for groups_info_post

        Retrieve a group
        """
        pass

    async def test_groups_list_post(self) -> None:
        """Test case for groups_list_post

        List all groups
        """
        pass

    async def test_groups_memberships_post(self) -> None:
        """Test case for groups_memberships_post

        List all group members
        """
        pass

    async def test_groups_remove_user_post(self) -> None:
        """Test case for groups_remove_user_post

        Remove a group member
        """
        pass

    async def test_groups_update_post(self) -> None:
        """Test case for groups_update_post

        Update a group
        """
        pass


if __name__ == '__main__':
    unittest.main()
