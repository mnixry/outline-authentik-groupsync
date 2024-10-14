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

from authentik_openapi.models.paginated_password_policy_list import PaginatedPasswordPolicyList

class TestPaginatedPasswordPolicyList(unittest.TestCase):
    """PaginatedPasswordPolicyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPasswordPolicyList:
        """Test PaginatedPasswordPolicyList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPasswordPolicyList`
        """
        model = PaginatedPasswordPolicyList()
        if include_optional:
            return PaginatedPasswordPolicyList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.password_policy.PasswordPolicy(
                        pk = '', 
                        name = '', 
                        execution_logging = True, 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        bound_to = 56, 
                        password_field = '', 
                        amount_digits = 0, 
                        amount_uppercase = 0, 
                        amount_lowercase = 0, 
                        amount_symbols = 0, 
                        length_min = 0, 
                        symbol_charset = '', 
                        error_message = '', 
                        check_static_rules = True, 
                        check_have_i_been_pwned = True, 
                        check_zxcvbn = True, 
                        hibp_allowed_count = 0, 
                        zxcvbn_score_threshold = 0, )
                    ]
            )
        else:
            return PaginatedPasswordPolicyList(
                pagination = authentik_openapi.models.pagination.Pagination(
                    next = 1.337, 
                    previous = 1.337, 
                    count = 1.337, 
                    current = 1.337, 
                    total_pages = 1.337, 
                    start_index = 1.337, 
                    end_index = 1.337, ),
                results = [
                    authentik_openapi.models.password_policy.PasswordPolicy(
                        pk = '', 
                        name = '', 
                        execution_logging = True, 
                        component = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', 
                        bound_to = 56, 
                        password_field = '', 
                        amount_digits = 0, 
                        amount_uppercase = 0, 
                        amount_lowercase = 0, 
                        amount_symbols = 0, 
                        length_min = 0, 
                        symbol_charset = '', 
                        error_message = '', 
                        check_static_rules = True, 
                        check_have_i_been_pwned = True, 
                        check_zxcvbn = True, 
                        hibp_allowed_count = 0, 
                        zxcvbn_score_threshold = 0, )
                    ],
        )
        """

    def testPaginatedPasswordPolicyList(self):
        """Test PaginatedPasswordPolicyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
