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

from authentik_openapi.models.user_self import UserSelf

class TestUserSelf(unittest.TestCase):
    """UserSelf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSelf:
        """Test UserSelf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSelf`
        """
        model = UserSelf()
        if include_optional:
            return UserSelf(
                pk = 56,
                username = 'A',
                name = '',
                is_active = True,
                is_superuser = True,
                groups = [
                    authentik_openapi.models.user_self_groups.UserSelfGroups(
                        name = '', 
                        pk = '', )
                    ],
                email = '',
                avatar = '',
                uid = '',
                settings = {
                    'key' : null
                    },
                type = 'internal',
                system_permissions = [
                    ''
                    ]
            )
        else:
            return UserSelf(
                pk = 56,
                username = 'A',
                name = '',
                is_active = True,
                is_superuser = True,
                groups = [
                    authentik_openapi.models.user_self_groups.UserSelfGroups(
                        name = '', 
                        pk = '', )
                    ],
                avatar = '',
                uid = '',
                settings = {
                    'key' : null
                    },
                system_permissions = [
                    ''
                    ],
        )
        """

    def testUserSelf(self):
        """Test UserSelf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
