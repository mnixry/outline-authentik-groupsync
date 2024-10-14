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

from authentik_openapi.models.user import User

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()
        if include_optional:
            return User(
                pk = 56,
                username = '',
                name = '',
                is_active = True,
                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                is_superuser = True,
                groups = [
                    ''
                    ],
                groups_obj = [
                    authentik_openapi.models.user_group.UserGroup(
                        pk = '', 
                        num_pk = 56, 
                        name = '', 
                        is_superuser = True, 
                        parent = '', 
                        parent_name = '', 
                        attributes = {
                            'key' : null
                            }, )
                    ],
                email = '',
                avatar = '',
                attributes = {
                    'key' : null
                    },
                uid = '',
                path = '',
                type = 'internal',
                uuid = ''
            )
        else:
            return User(
                pk = 56,
                username = '',
                name = '',
                is_superuser = True,
                groups_obj = [
                    authentik_openapi.models.user_group.UserGroup(
                        pk = '', 
                        num_pk = 56, 
                        name = '', 
                        is_superuser = True, 
                        parent = '', 
                        parent_name = '', 
                        attributes = {
                            'key' : null
                            }, )
                    ],
                avatar = '',
                uid = '',
                uuid = '',
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
