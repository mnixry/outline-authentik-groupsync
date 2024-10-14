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

from authentik_openapi.models.plex_source_property_mapping_request import PlexSourcePropertyMappingRequest

class TestPlexSourcePropertyMappingRequest(unittest.TestCase):
    """PlexSourcePropertyMappingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlexSourcePropertyMappingRequest:
        """Test PlexSourcePropertyMappingRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlexSourcePropertyMappingRequest`
        """
        model = PlexSourcePropertyMappingRequest()
        if include_optional:
            return PlexSourcePropertyMappingRequest(
                managed = '0',
                name = '0',
                expression = '0'
            )
        else:
            return PlexSourcePropertyMappingRequest(
                name = '0',
                expression = '0',
        )
        """

    def testPlexSourcePropertyMappingRequest(self):
        """Test PlexSourcePropertyMappingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
