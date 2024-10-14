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

from authentik_openapi.models.microsoft_entra_provider_group_request import MicrosoftEntraProviderGroupRequest

class TestMicrosoftEntraProviderGroupRequest(unittest.TestCase):
    """MicrosoftEntraProviderGroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftEntraProviderGroupRequest:
        """Test MicrosoftEntraProviderGroupRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrosoftEntraProviderGroupRequest`
        """
        model = MicrosoftEntraProviderGroupRequest()
        if include_optional:
            return MicrosoftEntraProviderGroupRequest(
                microsoft_id = '0',
                group = '',
                provider = 56
            )
        else:
            return MicrosoftEntraProviderGroupRequest(
                microsoft_id = '0',
                group = '',
                provider = 56,
        )
        """

    def testMicrosoftEntraProviderGroupRequest(self):
        """Test MicrosoftEntraProviderGroupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
