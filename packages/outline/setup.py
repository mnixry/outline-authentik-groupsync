# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "outline_openapi"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Outline API",
    author_email="hello@getoutline.com",
    url="",
    keywords=["OpenAPI", "Outline API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['outline_openapi=outline_openapi.__main__:main']},
    long_description="""\
    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on &#x60;https://app.getoutline.com/api/method&#x60;. Both &#x60;GET&#x60; and &#x60;POST&#x60; methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making &#x60;POST&#x60; requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  &#x60;&#x60;&#x60; curl https://app.getoutline.com/api/documents.info \\ -X &#39;POST&#39; \\ -H &#39;authorization: Bearer MY_API_KEY&#39; \\ -H &#39;content-type: application/json&#39; \\ -H &#39;accept: application/json&#39; \\ -d &#39;{\&quot;id\&quot;: \&quot;outline-api-NTpezNwhUP\&quot;}&#39; &#x60;&#x60;&#x60;  Or, with JavaScript:  &#x60;&#x60;&#x60;javascript const response &#x3D; await fetch(\&quot;https://app.getoutline.com/api/documents.info\&quot;, {   method: \&quot;POST\&quot;,   headers: {     Accept: \&quot;application/json\&quot;,     \&quot;Content-Type\&quot;: \&quot;application/json\&quot;,     Authorization: \&quot;Bearer MY_API_KEY\&quot;   } })  const body &#x3D; await response.json(); const document &#x3D; body.data; &#x60;&#x60;&#x60;  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (&#x60;Authorization: Bearer YOUR_API_KEY&#x60;) or as part of the payload using &#x60;token&#x60; parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and &#x60;ok: true&#x60; in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  &#x60;&#x60;&#x60; {   \&quot;ok\&quot;: false,   \&quot;error\&quot;: \&quot;Not Found\&quot; } &#x60;&#x60;&#x60;  # Pagination  Most top-level API resources have support for \&quot;list\&quot; API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both &#x60;limit&#x60; and &#x60;offset&#x60;.  Responses will echo these parameters in the root &#x60;pagination&#x60; key, and also include a &#x60;nextPath&#x60; key which can be used as a handy shortcut to fetch the next page of results. For example:  &#x60;&#x60;&#x60; {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \&quot;/api/documents.list?limit&#x3D;25&amp;offset&#x3D;25\&quot;   } } &#x60;&#x60;&#x60;  # Policies  Most API resources have associated \&quot;policies\&quot;, these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \&quot;id\&quot; is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible. 
    """
)

