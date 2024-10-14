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

from authentik_openapi.models.notification_rule import NotificationRule

class TestNotificationRule(unittest.TestCase):
    """NotificationRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationRule:
        """Test NotificationRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationRule`
        """
        model = NotificationRule()
        if include_optional:
            return NotificationRule(
                pk = '',
                name = '',
                transports = [
                    ''
                    ],
                severity = 'notice',
                group = '',
                group_obj = authentik_openapi.models.group.Group(
                    pk = '', 
                    num_pk = 56, 
                    name = '', 
                    is_superuser = True, 
                    parent = '', 
                    parent_name = '', 
                    users = [
                        56
                        ], 
                    users_obj = [
                        authentik_openapi.models.group_member.GroupMember(
                            pk = 56, 
                            username = 'A', 
                            name = '', 
                            is_active = True, 
                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            email = '', 
                            attributes = {
                                'key' : null
                                }, 
                            uid = '', )
                        ], 
                    attributes = {
                        'key' : null
                        }, 
                    roles = [
                        ''
                        ], 
                    roles_obj = [
                        authentik_openapi.models.role.Role(
                            pk = '', 
                            name = '', )
                        ], )
            )
        else:
            return NotificationRule(
                pk = '',
                name = '',
                group_obj = authentik_openapi.models.group.Group(
                    pk = '', 
                    num_pk = 56, 
                    name = '', 
                    is_superuser = True, 
                    parent = '', 
                    parent_name = '', 
                    users = [
                        56
                        ], 
                    users_obj = [
                        authentik_openapi.models.group_member.GroupMember(
                            pk = 56, 
                            username = 'A', 
                            name = '', 
                            is_active = True, 
                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            email = '', 
                            attributes = {
                                'key' : null
                                }, 
                            uid = '', )
                        ], 
                    attributes = {
                        'key' : null
                        }, 
                    roles = [
                        ''
                        ], 
                    roles_obj = [
                        authentik_openapi.models.role.Role(
                            pk = '', 
                            name = '', )
                        ], ),
        )
        """

    def testNotificationRule(self):
        """Test NotificationRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
