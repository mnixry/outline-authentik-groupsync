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

from authentik_openapi.models.permission import Permission

class TestPermission(unittest.TestCase):
    """Permission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Permission:
        """Test Permission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Permission`
        """
        model = Permission()
        if include_optional:
            return Permission(
                id = 56,
                name = '',
                codename = '',
                model = '',
                app_label = '',
                app_label_verbose = '',
                model_verbose = ''
            )
        else:
            return Permission(
                id = 56,
                name = '',
                codename = '',
                model = '',
                app_label = '',
                app_label_verbose = '',
                model_verbose = '',
        )
        """

    def testPermission(self):
        """Test Permission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
