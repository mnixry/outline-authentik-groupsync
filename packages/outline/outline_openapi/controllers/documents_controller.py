from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_add_user_post200_response import CollectionsAddUserPost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.collections_memberships_post200_response import CollectionsMembershipsPost200Response
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
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
from outline_openapi.models.documents_move_post_request import DocumentsMovePostRequest
from outline_openapi.models.documents_remove_user_post_request import DocumentsRemoveUserPostRequest
from outline_openapi.models.documents_restore_post_request import DocumentsRestorePostRequest
from outline_openapi.models.documents_search_post200_response import DocumentsSearchPost200Response
from outline_openapi.models.documents_search_post_request import DocumentsSearchPostRequest
from outline_openapi.models.documents_star_post200_response import DocumentsStarPost200Response
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest
from outline_openapi.models.documents_update_post_request import DocumentsUpdatePostRequest
from outline_openapi.models.documents_users_post200_response import DocumentsUsersPost200Response
from outline_openapi.models.documents_users_post_request import DocumentsUsersPostRequest
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi import util


async def documents_add_user_post(request: web.Request, body=None) -> web.Response:
    """Add a document user

    This method allows you to add a user membership to the specified document.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsAddUserPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_answer_question_post(request: web.Request, body=None) -> web.Response:
    """Query documents with natural language

    This method allows asking direct questions of your documents – where possible an answer will be provided. Search results will be restricted to those accessible by the current access token. Note that \&quot;AI answers\&quot; must be enabled for the workspace.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsAnswerQuestionPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_archive_post(request: web.Request, body=None) -> web.Response:
    """Archive a document

    Archiving a document allows outdated information to be moved out of sight whilst retaining the ability to optionally search and restore it later.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsStarPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_create_post(request: web.Request, body=None) -> web.Response:
    """Create a document

    This method allows you to create or publish a new document. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete a document

    Deleting a document moves it to the trash. If not restored within 30 days it is permenantly deleted.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsDeletePostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_drafts_post(request: web.Request, body=None) -> web.Response:
    """List all draft documents

    This method will list all draft documents belonging to the current user.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsDraftsPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_export_post(request: web.Request, body=None) -> web.Response:
    """Export a document as markdown

    

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsExportPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_import_post(request: web.Request, file=None, collection_id=None, parent_document_id=None, template=None, publish=None) -> web.Response:
    """Import a file as a document

    This method allows you to create a new document by importing an existing file. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

    :param file: Only plain text, markdown, docx, and html format are supported.
    :type file: dict | bytes
    :param collection_id: 
    :type collection_id: str
    :type collection_id: str
    :param parent_document_id: 
    :type parent_document_id: str
    :type parent_document_id: str
    :param template: 
    :type template: bool
    :param publish: 
    :type publish: bool

    """
    file = object.from_dict(file)
    return web.Response(status=200)


async def documents_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a document

    

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_list_post(request: web.Request, body=None) -> web.Response:
    """List all documents

    This method will list all published documents and draft documents belonging to the current user.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsListPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_memberships_post(request: web.Request, body=None) -> web.Response:
    """List document memberships

    Users with direct membership to a document. To list all users with access to a document use &#x60;documents.users&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsMembershipsPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_move_post(request: web.Request, body=None) -> web.Response:
    """Move a document

    Move a document to a new location or collection. If no parent document is provided, the document will be moved to the collection root.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsMovePostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_remove_user_post(request: web.Request, body=None) -> web.Response:
    """Remove a document user

    This method allows you to remove a user membership from the specified document.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsRemoveUserPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_restore_post(request: web.Request, body=None) -> web.Response:
    """Restore a document

    If a document has been archived or deleted, it can be restored. Optionally a revision can be passed to restore the document to a previous point in time.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsRestorePostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_search_post(request: web.Request, body=None) -> web.Response:
    """Search all documents

    This methods allows you to search your teams documents with keywords. Note that search results will be restricted to those accessible by the current access token.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsSearchPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_star_post(request: web.Request, body=None) -> web.Response:
    """Star a document

    Starring a document gives it extra priority in the UI and makes it easier to find important information later.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsStarPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_templatize_post(request: web.Request, body=None) -> web.Response:
    """Create a template from a document

    This method allows you to createa new template using an existing document as the basis

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsDeletePostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_unpublish_post(request: web.Request, body=None) -> web.Response:
    """Unpublish a document

    Unpublishing a document moves it back to a draft status and out of the collection.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsStarPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_unstar_post(request: web.Request, body=None) -> web.Response:
    """Unstar a document

    Starring a document gives it extra priority in the UI and makes it easier to find important information later.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsStarPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_update_post(request: web.Request, body=None) -> web.Response:
    """Update a document

    This method allows you to modify an already created document

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsUpdatePostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_users_post(request: web.Request, body=None) -> web.Response:
    """List document users

    All users with access to a document. To list only users with direct membership to the document use &#x60;documents.memberships&#x60;

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsUsersPostRequest.from_dict(body)
    return web.Response(status=200)


async def documents_viewed_post(request: web.Request, body=None) -> web.Response:
    """List all recently viewed documents

    This method will list all documents recently viewed by the current user.

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsViewedPostRequest.from_dict(body)
    return web.Response(status=200)
