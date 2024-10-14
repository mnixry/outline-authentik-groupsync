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

from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest

class TestGoogleWorkspaceProviderRequest(unittest.TestCase):
    """GoogleWorkspaceProviderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleWorkspaceProviderRequest:
        """Test GoogleWorkspaceProviderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleWorkspaceProviderRequest`
        """
        model = GoogleWorkspaceProviderRequest()
        if include_optional:
            return GoogleWorkspaceProviderRequest(
                name = '0',
                property_mappings = [
                    ''
                    ],
                property_mappings_group = [
                    ''
                    ],
                delegated_subject = '0',
                credentials = None,
                scopes = '0',
                exclude_users_service_account = True,
                filter_group = '',
                user_delete_action = 'do_nothing',
                group_delete_action = 'do_nothing',
                default_group_email_domain = '0'
            )
        else:
            return GoogleWorkspaceProviderRequest(
                name = '0',
                delegated_subject = '0',
                credentials = None,
                default_group_email_domain = '0',
        )
        """

    def testGoogleWorkspaceProviderRequest(self):
        """Test GoogleWorkspaceProviderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
