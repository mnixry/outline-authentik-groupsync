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

from authentik_openapi.models.paginated_saml_source_property_mapping_list import PaginatedSAMLSourcePropertyMappingList

class TestPaginatedSAMLSourcePropertyMappingList(unittest.TestCase):
    """PaginatedSAMLSourcePropertyMappingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedSAMLSourcePropertyMappingList:
        """Test PaginatedSAMLSourcePropertyMappingList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedSAMLSourcePropertyMappingList`
        """
        model = PaginatedSAMLSourcePropertyMappingList()
        if include_optional:
            return PaginatedSAMLSourcePropertyMappingList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.saml_source_property_mapping.SAMLSourcePropertyMapping(
                        pk = '', 
                        managed = '', 
                        name = '', 
                        expression = '', 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', )
                    ]
            )
        else:
            return PaginatedSAMLSourcePropertyMappingList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.saml_source_property_mapping.SAMLSourcePropertyMapping(
                        pk = '', 
                        managed = '', 
                        name = '', 
                        expression = '', 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', )
                    ],
        )
        """

    def testPaginatedSAMLSourcePropertyMappingList(self):
        """Test PaginatedSAMLSourcePropertyMappingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
