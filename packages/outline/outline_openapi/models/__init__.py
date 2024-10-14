# coding: utf-8

# flake8: noqa
"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST` methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token` parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Most API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible. 

    The version of the OpenAPI document: 0.1.0
    Contact: hello@getoutline.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from outline_openapi.models.attachment import Attachment
from outline_openapi.models.attachments_create_post200_response import AttachmentsCreatePost200Response
from outline_openapi.models.attachments_create_post200_response_data import AttachmentsCreatePost200ResponseData
from outline_openapi.models.attachments_create_post_request import AttachmentsCreatePostRequest
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.attachments_redirect_post_request import AttachmentsRedirectPostRequest
from outline_openapi.models.auth import Auth
from outline_openapi.models.auth_config_post200_response import AuthConfigPost200Response
from outline_openapi.models.auth_config_post200_response_data import AuthConfigPost200ResponseData
from outline_openapi.models.auth_config_post200_response_data_services_inner import AuthConfigPost200ResponseDataServicesInner
from outline_openapi.models.auth_info_post200_response import AuthInfoPost200Response
from outline_openapi.models.collection import Collection
from outline_openapi.models.collection_group_membership import CollectionGroupMembership
from outline_openapi.models.collection_sort import CollectionSort
from outline_openapi.models.collections_add_group_post200_response import CollectionsAddGroupPost200Response
from outline_openapi.models.collections_add_group_post200_response_data import CollectionsAddGroupPost200ResponseData
from outline_openapi.models.collections_add_group_post_request import CollectionsAddGroupPostRequest
from outline_openapi.models.collections_add_user_post200_response import CollectionsAddUserPost200Response
from outline_openapi.models.collections_add_user_post200_response_data import CollectionsAddUserPost200ResponseData
from outline_openapi.models.collections_add_user_post_request import CollectionsAddUserPostRequest
from outline_openapi.models.collections_create_post200_response import CollectionsCreatePost200Response
from outline_openapi.models.collections_create_post_request import CollectionsCreatePostRequest
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.collections_documents_post200_response import CollectionsDocumentsPost200Response
from outline_openapi.models.collections_export_all_post_request import CollectionsExportAllPostRequest
from outline_openapi.models.collections_export_post200_response import CollectionsExportPost200Response
from outline_openapi.models.collections_export_post200_response_data import CollectionsExportPost200ResponseData
from outline_openapi.models.collections_export_post_request import CollectionsExportPostRequest
from outline_openapi.models.collections_group_memberships_post200_response import CollectionsGroupMembershipsPost200Response
from outline_openapi.models.collections_group_memberships_post200_response_data import CollectionsGroupMembershipsPost200ResponseData
from outline_openapi.models.collections_group_memberships_post_request import CollectionsGroupMembershipsPostRequest
from outline_openapi.models.collections_info_post200_response import CollectionsInfoPost200Response
from outline_openapi.models.collections_info_post_request import CollectionsInfoPostRequest
from outline_openapi.models.collections_list_post200_response import CollectionsListPost200Response
from outline_openapi.models.collections_memberships_post200_response import CollectionsMembershipsPost200Response
from outline_openapi.models.collections_memberships_post_request import CollectionsMembershipsPostRequest
from outline_openapi.models.collections_remove_group_post_request import CollectionsRemoveGroupPostRequest
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
from outline_openapi.models.collections_update_post_request import CollectionsUpdatePostRequest
from outline_openapi.models.comment import Comment
from outline_openapi.models.comments_create_post200_response import CommentsCreatePost200Response
from outline_openapi.models.comments_create_post_request import CommentsCreatePostRequest
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
from outline_openapi.models.comments_list_post_request import CommentsListPostRequest
from outline_openapi.models.comments_update_post_request import CommentsUpdatePostRequest
from outline_openapi.models.document import Document
from outline_openapi.models.documents_add_user_post_request import DocumentsAddUserPostRequest
from outline_openapi.models.documents_answer_question_post200_response import DocumentsAnswerQuestionPost200Response
from outline_openapi.models.documents_answer_question_post_request import DocumentsAnswerQuestionPostRequest
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
from outline_openapi.models.documents_create_post_request import DocumentsCreatePostRequest
from outline_openapi.models.documents_delete_post_request import DocumentsDeletePostRequest
from outline_openapi.models.documents_drafts_post_request import DocumentsDraftsPostRequest
from outline_openapi.models.documents_export_post200_response import DocumentsExportPost200Response
from outline_openapi.models.documents_export_post_request import DocumentsExportPostRequest
from outline_openapi.models.documents_info_post200_response import DocumentsInfoPost200Response
from outline_openapi.models.documents_info_post_request import DocumentsInfoPostRequest
from outline_openapi.models.documents_list_post_request import DocumentsListPostRequest
from outline_openapi.models.documents_memberships_post_request import DocumentsMembershipsPostRequest
from outline_openapi.models.documents_move_post200_response import DocumentsMovePost200Response
from outline_openapi.models.documents_move_post200_response_data import DocumentsMovePost200ResponseData
from outline_openapi.models.documents_move_post_request import DocumentsMovePostRequest
from outline_openapi.models.documents_remove_user_post_request import DocumentsRemoveUserPostRequest
from outline_openapi.models.documents_restore_post_request import DocumentsRestorePostRequest
from outline_openapi.models.documents_search_post200_response import DocumentsSearchPost200Response
from outline_openapi.models.documents_search_post200_response_data_inner import DocumentsSearchPost200ResponseDataInner
from outline_openapi.models.documents_search_post_request import DocumentsSearchPostRequest
from outline_openapi.models.documents_star_post200_response import DocumentsStarPost200Response
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest
from outline_openapi.models.documents_update_post_request import DocumentsUpdatePostRequest
from outline_openapi.models.documents_users_post200_response import DocumentsUsersPost200Response
from outline_openapi.models.documents_users_post_request import DocumentsUsersPostRequest
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.event import Event
from outline_openapi.models.events_list_post200_response import EventsListPost200Response
from outline_openapi.models.events_list_post_request import EventsListPostRequest
from outline_openapi.models.file_operation import FileOperation
from outline_openapi.models.file_operation_collection import FileOperationCollection
from outline_openapi.models.file_operations_info_post200_response import FileOperationsInfoPost200Response
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest
from outline_openapi.models.file_operations_list_post200_response import FileOperationsListPost200Response
from outline_openapi.models.file_operations_list_post_request import FileOperationsListPostRequest
from outline_openapi.models.group import Group
from outline_openapi.models.group_membership import GroupMembership
from outline_openapi.models.groups_add_user_post200_response import GroupsAddUserPost200Response
from outline_openapi.models.groups_add_user_post200_response_data import GroupsAddUserPost200ResponseData
from outline_openapi.models.groups_add_user_post_request import GroupsAddUserPostRequest
from outline_openapi.models.groups_create_post200_response import GroupsCreatePost200Response
from outline_openapi.models.groups_create_post_request import GroupsCreatePostRequest
from outline_openapi.models.groups_info_post200_response import GroupsInfoPost200Response
from outline_openapi.models.groups_info_post_request import GroupsInfoPostRequest
from outline_openapi.models.groups_list_post200_response import GroupsListPost200Response
from outline_openapi.models.groups_list_post200_response_data import GroupsListPost200ResponseData
from outline_openapi.models.groups_memberships_post200_response import GroupsMembershipsPost200Response
from outline_openapi.models.groups_memberships_post200_response_data import GroupsMembershipsPost200ResponseData
from outline_openapi.models.groups_memberships_post_request import GroupsMembershipsPostRequest
from outline_openapi.models.groups_remove_user_post200_response import GroupsRemoveUserPost200Response
from outline_openapi.models.groups_remove_user_post200_response_data import GroupsRemoveUserPost200ResponseData
from outline_openapi.models.groups_update_post_request import GroupsUpdatePostRequest
from outline_openapi.models.invite import Invite
from outline_openapi.models.membership import Membership
from outline_openapi.models.navigation_node import NavigationNode
from outline_openapi.models.pagination import Pagination
from outline_openapi.models.permission import Permission
from outline_openapi.models.policy import Policy
from outline_openapi.models.policy_abilities import PolicyAbilities
from outline_openapi.models.revision import Revision
from outline_openapi.models.revisions_info_post200_response import RevisionsInfoPost200Response
from outline_openapi.models.revisions_info_post_request import RevisionsInfoPostRequest
from outline_openapi.models.revisions_list_post200_response import RevisionsListPost200Response
from outline_openapi.models.search_result import SearchResult
from outline_openapi.models.share import Share
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.shares_info_post200_response import SharesInfoPost200Response
from outline_openapi.models.shares_info_post_request import SharesInfoPostRequest
from outline_openapi.models.shares_list_post200_response import SharesListPost200Response
from outline_openapi.models.shares_update_post_request import SharesUpdatePostRequest
from outline_openapi.models.sorting import Sorting
from outline_openapi.models.team import Team
from outline_openapi.models.user import User
from outline_openapi.models.user_role import UserRole
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
from outline_openapi.models.users_invite_post200_response import UsersInvitePost200Response
from outline_openapi.models.users_invite_post200_response_data import UsersInvitePost200ResponseData
from outline_openapi.models.users_invite_post_request import UsersInvitePostRequest
from outline_openapi.models.users_list_post200_response import UsersListPost200Response
from outline_openapi.models.users_list_post_request import UsersListPostRequest
from outline_openapi.models.users_update_post_request import UsersUpdatePostRequest
from outline_openapi.models.users_update_role_post_request import UsersUpdateRolePostRequest
from outline_openapi.models.view import View
from outline_openapi.models.views_create_post200_response import ViewsCreatePost200Response
from outline_openapi.models.views_list_post200_response import ViewsListPost200Response
