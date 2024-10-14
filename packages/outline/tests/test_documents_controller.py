# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

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


pytestmark = pytest.mark.asyncio

async def test_documents_add_user_post(client):
    """Test case for documents_add_user_post

    Add a document user
    """
    body = outline_openapi.DocumentsAddUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.add_user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_answer_question_post(client):
    """Test case for documents_answer_question_post

    Query documents with natural language
    """
    body = outline_openapi.DocumentsAnswerQuestionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.answerQuestion',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_archive_post(client):
    """Test case for documents_archive_post

    Archive a document
    """
    body = outline_openapi.DocumentsStarPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.archive',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_create_post(client):
    """Test case for documents_create_post

    Create a document
    """
    body = outline_openapi.DocumentsCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_delete_post(client):
    """Test case for documents_delete_post

    Delete a document
    """
    body = outline_openapi.DocumentsDeletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_drafts_post(client):
    """Test case for documents_drafts_post

    List all draft documents
    """
    body = outline_openapi.DocumentsDraftsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.drafts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_export_post(client):
    """Test case for documents_export_post

    Export a document as markdown
    """
    body = outline_openapi.DocumentsExportPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.export',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_documents_import_post(client):
    """Test case for documents_import_post

    Import a file as a document
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', None)
    data.add_field('collection_id', 'collection_id_example')
    data.add_field('parent_document_id', 'parent_document_id_example')
    data.add_field('template', True)
    data.add_field('publish', True)
    response = await client.request(
        method='POST',
        path='/api/documents.import',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_info_post(client):
    """Test case for documents_info_post

    Retrieve a document
    """
    body = outline_openapi.DocumentsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_list_post(client):
    """Test case for documents_list_post

    List all documents
    """
    body = outline_openapi.DocumentsListPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_memberships_post(client):
    """Test case for documents_memberships_post

    List document memberships
    """
    body = outline_openapi.DocumentsMembershipsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.memberships',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_move_post(client):
    """Test case for documents_move_post

    Move a document
    """
    body = outline_openapi.DocumentsMovePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.move',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_remove_user_post(client):
    """Test case for documents_remove_user_post

    Remove a document user
    """
    body = outline_openapi.DocumentsRemoveUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.remove_user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_restore_post(client):
    """Test case for documents_restore_post

    Restore a document
    """
    body = outline_openapi.DocumentsRestorePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.restore',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_search_post(client):
    """Test case for documents_search_post

    Search all documents
    """
    body = outline_openapi.DocumentsSearchPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_star_post(client):
    """Test case for documents_star_post

    Star a document
    """
    body = outline_openapi.DocumentsStarPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.star',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_templatize_post(client):
    """Test case for documents_templatize_post

    Create a template from a document
    """
    body = outline_openapi.CollectionsDeletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.templatize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_unpublish_post(client):
    """Test case for documents_unpublish_post

    Unpublish a document
    """
    body = outline_openapi.DocumentsStarPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.unpublish',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_unstar_post(client):
    """Test case for documents_unstar_post

    Unstar a document
    """
    body = outline_openapi.DocumentsStarPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.unstar',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_update_post(client):
    """Test case for documents_update_post

    Update a document
    """
    body = outline_openapi.DocumentsUpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_users_post(client):
    """Test case for documents_users_post

    List document users
    """
    body = outline_openapi.DocumentsUsersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_viewed_post(client):
    """Test case for documents_viewed_post

    List all recently viewed documents
    """
    body = outline_openapi.DocumentsViewedPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents.viewed',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

