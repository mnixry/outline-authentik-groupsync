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

from authentik_openapi.models.user_group import UserGroup

class TestUserGroup(unittest.TestCase):
    """UserGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroup:
        """Test UserGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroup`
        """
        model = UserGroup()
        if include_optional:
            return UserGroup(
                pk = '',
                num_pk = 56,
                name = '',
                is_superuser = True,
                parent = '',
                parent_name = '',
                attributes = {
                    'key' : null
                    }
            )
        else:
            return UserGroup(
                pk = '',
                num_pk = 56,
                name = '',
                parent_name = '',
        )
        """

    def testUserGroup(self):
        """Test UserGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
