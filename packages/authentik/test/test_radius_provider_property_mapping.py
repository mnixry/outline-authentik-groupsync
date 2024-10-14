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

from authentik_openapi.models.radius_provider_property_mapping import RadiusProviderPropertyMapping

class TestRadiusProviderPropertyMapping(unittest.TestCase):
    """RadiusProviderPropertyMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RadiusProviderPropertyMapping:
        """Test RadiusProviderPropertyMapping
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RadiusProviderPropertyMapping`
        """
        model = RadiusProviderPropertyMapping()
        if include_optional:
            return RadiusProviderPropertyMapping(
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
            return RadiusProviderPropertyMapping(
                pk = '',
                name = '',
                expression = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
        )
        """

    def testRadiusProviderPropertyMapping(self):
        """Test RadiusProviderPropertyMapping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
