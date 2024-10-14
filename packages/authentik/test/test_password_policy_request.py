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

from authentik_openapi.models.password_policy_request import PasswordPolicyRequest

class TestPasswordPolicyRequest(unittest.TestCase):
    """PasswordPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordPolicyRequest:
        """Test PasswordPolicyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordPolicyRequest`
        """
        model = PasswordPolicyRequest()
        if include_optional:
            return PasswordPolicyRequest(
                name = '0',
                execution_logging = True,
                password_field = '0',
                amount_digits = 0,
                amount_uppercase = 0,
                amount_lowercase = 0,
                amount_symbols = 0,
                length_min = 0,
                symbol_charset = '0',
                error_message = '',
                check_static_rules = True,
                check_have_i_been_pwned = True,
                check_zxcvbn = True,
                hibp_allowed_count = 0,
                zxcvbn_score_threshold = 0
            )
        else:
            return PasswordPolicyRequest(
                name = '0',
        )
        """

    def testPasswordPolicyRequest(self):
        """Test PasswordPolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
