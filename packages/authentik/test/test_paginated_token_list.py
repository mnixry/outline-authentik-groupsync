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

from authentik_openapi.models.paginated_token_list import PaginatedTokenList

class TestPaginatedTokenList(unittest.TestCase):
    """PaginatedTokenList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedTokenList:
        """Test PaginatedTokenList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedTokenList`
        """
        model = PaginatedTokenList()
        if include_optional:
            return PaginatedTokenList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.token.Token(
                        pk = '', 
                        managed = '', 
                        identifier = 'z', 
                        intent = 'verification', 
                        user = 56, 
                        user_obj = null, 
                        description = '', 
                        expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiring = True, )
                    ]
            )
        else:
            return PaginatedTokenList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.token.Token(
                        pk = '', 
                        managed = '', 
                        identifier = 'z', 
                        intent = 'verification', 
                        user = 56, 
                        user_obj = null, 
                        description = '', 
                        expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expiring = True, )
                    ],
        )
        """

    def testPaginatedTokenList(self):
        """Test PaginatedTokenList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
