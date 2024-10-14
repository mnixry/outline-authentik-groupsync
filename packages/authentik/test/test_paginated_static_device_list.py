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

from authentik_openapi.models.paginated_static_device_list import PaginatedStaticDeviceList

class TestPaginatedStaticDeviceList(unittest.TestCase):
    """PaginatedStaticDeviceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedStaticDeviceList:
        """Test PaginatedStaticDeviceList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedStaticDeviceList`
        """
        model = PaginatedStaticDeviceList()
        if include_optional:
            return PaginatedStaticDeviceList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.static_device.StaticDevice(
                        name = '', 
                        token_set = [
                            authentik_openapi.models.static_device_token.StaticDeviceToken(
                                token = '', )
                            ], 
                        pk = 56, )
                    ]
            )
        else:
            return PaginatedStaticDeviceList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.static_device.StaticDevice(
                        name = '', 
                        token_set = [
                            authentik_openapi.models.static_device_token.StaticDeviceToken(
                                token = '', )
                            ], 
                        pk = 56, )
                    ],
        )
        """

    def testPaginatedStaticDeviceList(self):
        """Test PaginatedStaticDeviceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
