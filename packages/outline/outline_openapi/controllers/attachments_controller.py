from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_create_post200_response import AttachmentsCreatePost200Response
from outline_openapi.models.attachments_create_post_request import AttachmentsCreatePostRequest
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.attachments_redirect_post_request import AttachmentsRedirectPostRequest
from outline_openapi.models.error import Error
from outline_openapi import util


async def attachments_create_post(request: web.Request, body=None) -> web.Response:
    """Create an attachment

    Creating an attachment object creates a database record and returns the inputs needed to generate a signed url and upload the file from the client to cloud storage.

    :param body: 
    :type body: dict | bytes

    """
    body = AttachmentsCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def attachments_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete an attachment

    Deleting an attachment is permanant. It will not delete references or links to the attachment that may exist in your documents.

    :param body: 
    :type body: dict | bytes

    """
    body = AttachmentsRedirectPostRequest.from_dict(body)
    return web.Response(status=200)


async def attachments_redirect_post(request: web.Request, body=None) -> web.Response:
    """Retrieve an attachment

    Load an attachment from where it is stored based on the id. If the attachment is private then a temporary, signed url with embedded credentials is generated on demand.

    :param body: 
    :type body: dict | bytes

    """
    body = AttachmentsRedirectPostRequest.from_dict(body)
    return web.Response(status=200)
