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

from authentik_openapi.models.ldap_source_property_mapping import LDAPSourcePropertyMapping

class TestLDAPSourcePropertyMapping(unittest.TestCase):
    """LDAPSourcePropertyMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LDAPSourcePropertyMapping:
        """Test LDAPSourcePropertyMapping
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LDAPSourcePropertyMapping`
        """
        model = LDAPSourcePropertyMapping()
        if include_optional:
            return LDAPSourcePropertyMapping(
                pk = '',
                managed = '',
                name = '',
                expression = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = ''
            )
        else:
            return LDAPSourcePropertyMapping(
                pk = '',
                name = '',
                expression = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
        )
        """

    def testLDAPSourcePropertyMapping(self):
        """Test LDAPSourcePropertyMapping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
