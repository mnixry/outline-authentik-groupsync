# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a `POST` method on `https://app.getoutline.com/api/:method`. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  ## API key  You can create new API keys under **Settings => API & Apps**. Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you should supply the API key as the `Authorization` header (`Authorization: Bearer YOUR_API_KEY`).  ## OAuth 2.0  OAuth 2.0 is a widely used protocol for authorization and authentication. It allows users to grant third-party _or_ internal applications access to their resources without sharing their credentials. To use OAuth 2.0 you need to follow these steps:  1. Register your application under **Settings => Applications** 2. Obtain an access token by exchanging the client credentials for an access token 3. Use the access token to authenticate requests to the API  Some API endpoints allow unauthenticated requests for public resources and they can be called without authentication  # Scopes  Scopes are used to limit the access of an API key or application to specific resources. For example, an application may only need access to read documents, but not write them. Scopes can be global in the case of `read` and `write` scopes, scoped to a namespace, scoped to an API endpoint, or use wildcard scopes like `documents.*`. Some examples of scopes that can be used are:  ## Global  - `read`: Allows all read actions - `write`: Allows all read and write actions  ## Namespaced  - `documents:read`: Allows all document read actions - `collections:write`: Allows all collection write actions  ## Endpoints  - `documents.info`: Allows only one specific API method - `documents.*`: Allows all document API methods - `users.*`: Allows all user API methods  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Rate limits  Like most APIs, Outline has rate limits in place to prevent abuse. Endpoints that mutate data are more restrictive than read-only endpoints. If you exceed the rate limit for a given endpoint, you will receive a `429 Too Many Requests` status code.  The response will include a `Retry-After` header that indicates how many seconds you should wait before making another request.  # Policies  Most API resources have associated \"policies\", these objects describe the current authentications authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible. 

    The version of the OpenAPI document: 0.1.0
    Contact: hello@getoutline.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import json
import re
import ssl
from typing import Optional, Union

import aiohttp
import aiohttp_retry

from outline_openapi.exceptions import ApiException, ApiValueError

RESTResponseType = aiohttp.ClientResponse

ALLOW_RETRY_METHODS = frozenset({'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'TRACE'})

class RESTResponse(io.IOBase):

    def __init__(self, resp) -> None:
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = None

    async def read(self):
        if self.data is None:
            self.data = await self.response.read()
        return self.data

    def getheaders(self):
        """Returns a CIMultiDictProxy of the response headers."""
        return self.response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.response.headers.get(name, default)


class RESTClientObject:

    def __init__(self, configuration) -> None:

        # maxsize is number of requests to host that are allowed in parallel
        self.maxsize = configuration.connection_pool_maxsize

        self.ssl_context = ssl.create_default_context(
            cafile=configuration.ssl_ca_cert,
            cadata=configuration.ca_cert_data,
        )
        if configuration.cert_file:
            self.ssl_context.load_cert_chain(
                configuration.cert_file, keyfile=configuration.key_file
            )

        if not configuration.verify_ssl:
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE

        self.proxy = configuration.proxy
        self.proxy_headers = configuration.proxy_headers

        self.retries = configuration.retries

        self.pool_manager: Optional[aiohttp.ClientSession] = None
        self.retry_client: Optional[aiohttp_retry.RetryClient] = None

    async def close(self) -> None:
        if self.pool_manager:
            await self.pool_manager.close()
        if self.retry_client is not None:
            await self.retry_client.close()

    async def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ):
        """Execute request

        :param method: http request method
        :param url: http request url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in [
            'GET',
            'HEAD',
            'DELETE',
            'POST',
            'PUT',
            'PATCH',
            'OPTIONS'
        ]

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}
        # url already contains the URL query string
        timeout = _request_timeout or 5 * 60

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        args = {
            "method": method,
            "url": url,
            "timeout": timeout,
            "headers": headers
        }

        if self.proxy:
            args["proxy"] = self.proxy
        if self.proxy_headers:
            args["proxy_headers"] = self.proxy_headers

        # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if re.search('json', headers['Content-Type'], re.IGNORECASE):
                if body is not None:
                    body = json.dumps(body)
                args["data"] = body
            elif headers['Content-Type'] == 'application/x-www-form-urlencoded':
                args["data"] = aiohttp.FormData(post_params)
            elif headers['Content-Type'] == 'multipart/form-data':
                # must del headers['Content-Type'], or the correct
                # Content-Type which generated by aiohttp
                del headers['Content-Type']
                data = aiohttp.FormData()
                for param in post_params:
                    k, v = param
                    if isinstance(v, tuple) and len(v) == 3:
                        data.add_field(
                            k,
                            value=v[1],
                            filename=v[0],
                            content_type=v[2]
                        )
                    else:
                        # Ensures that dict objects are serialized
                        if isinstance(v, dict):
                            v = json.dumps(v)
                        elif isinstance(v, int):
                            v = str(v)
                        data.add_field(k, v)
                args["data"] = data

            # Pass a `bytes` or `str` parameter directly in the body to support
            # other content types than Json when `body` argument is provided
            # in serialized form
            elif isinstance(body, str) or isinstance(body, bytes):
                args["data"] = body
            else:
                # Cannot generate the request from given parameters
                msg = """Cannot prepare a request message for provided
                         arguments. Please check that your arguments match
                         declared content type."""
                raise ApiException(status=0, reason=msg)

        pool_manager: Union[aiohttp.ClientSession, aiohttp_retry.RetryClient]

        # https pool manager
        if self.pool_manager is None:
            self.pool_manager = aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(limit=self.maxsize, ssl=self.ssl_context),
                trust_env=True,
            )
        pool_manager = self.pool_manager

        if self.retries is not None and method in ALLOW_RETRY_METHODS:
            if self.retry_client is None:
                self.retry_client = aiohttp_retry.RetryClient(
                    client_session=self.pool_manager,
                    retry_options=aiohttp_retry.ExponentialRetry(
                        attempts=self.retries,
                        factor=2.0,
                        start_timeout=0.1,
                        max_timeout=120.0
                    )
                )
            pool_manager = self.retry_client

        r = await pool_manager.request(**args)

        return RESTResponse(r)
