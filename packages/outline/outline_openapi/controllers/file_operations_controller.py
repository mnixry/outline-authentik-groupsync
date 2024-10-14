from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.error import Error
from outline_openapi.models.file_operations_info_post200_response import FileOperationsInfoPost200Response
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest
from outline_openapi.models.file_operations_list_post200_response import FileOperationsListPost200Response
from outline_openapi.models.file_operations_list_post_request import FileOperationsListPostRequest
from outline_openapi import util


async def file_operations_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete a file operation

    

    :param body: 
    :type body: dict | bytes

    """
    body = FileOperationsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def file_operations_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a file operation

    

    :param body: 
    :type body: dict | bytes

    """
    body = FileOperationsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def file_operations_list_post(request: web.Request, body=None) -> web.Response:
    """List all file operations

    

    :param body: 
    :type body: dict | bytes

    """
    body = FileOperationsListPostRequest.from_dict(body)
    return web.Response(status=200)


async def file_operations_redirect_post(request: web.Request, body=None) -> web.Response:
    """Retrieve the file

    Load the resulting file from where it is stored based on the id. A temporary, signed url with embedded credentials is generated on demand.

    :param body: 
    :type body: dict | bytes

    """
    body = FileOperationsInfoPostRequest.from_dict(body)
    return web.Response(status=200)
