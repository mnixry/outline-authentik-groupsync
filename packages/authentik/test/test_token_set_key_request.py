# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.8.3
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.token_set_key_request import TokenSetKeyRequest

class TestTokenSetKeyRequest(unittest.TestCase):
    """TokenSetKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenSetKeyRequest:
        """Test TokenSetKeyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenSetKeyRequest`
        """
        model = TokenSetKeyRequest()
        if include_optional:
            return TokenSetKeyRequest(
                key = '0'
            )
        else:
            return TokenSetKeyRequest(
                key = '0',
        )
        """

    def testTokenSetKeyRequest(self):
        """Test TokenSetKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
