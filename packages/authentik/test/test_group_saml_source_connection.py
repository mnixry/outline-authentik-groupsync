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

from authentik_openapi.models.group_saml_source_connection import GroupSAMLSourceConnection

class TestGroupSAMLSourceConnection(unittest.TestCase):
    """GroupSAMLSourceConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupSAMLSourceConnection:
        """Test GroupSAMLSourceConnection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupSAMLSourceConnection`
        """
        model = GroupSAMLSourceConnection()
        if include_optional:
            return GroupSAMLSourceConnection(
                pk = 56,
                group = '',
                source = authentik_openapi.models.source.Source(
                    pk = '', 
                    name = '', 
                    slug = 'z', 
                    enabled = True, 
                    authentication_flow = '', 
                    enrollment_flow = '', 
                    user_property_mappings = [
                        ''
                        ], 
                    group_property_mappings = [
                        ''
                        ], 
                    component = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    policy_engine_mode = 'all', 
                    user_matching_mode = null, 
                    managed = '', 
                    user_path_template = '', 
                    icon = '', ),
                identifier = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GroupSAMLSourceConnection(
                pk = 56,
                group = '',
                source = authentik_openapi.models.source.Source(
                    pk = '', 
                    name = '', 
                    slug = 'z', 
                    enabled = True, 
                    authentication_flow = '', 
                    enrollment_flow = '', 
                    user_property_mappings = [
                        ''
                        ], 
                    group_property_mappings = [
                        ''
                        ], 
                    component = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    policy_engine_mode = 'all', 
                    user_matching_mode = null, 
                    managed = '', 
                    user_path_template = '', 
                    icon = '', ),
                identifier = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testGroupSAMLSourceConnection(self):
        """Test GroupSAMLSourceConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
