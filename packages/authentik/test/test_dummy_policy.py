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

from authentik_openapi.models.dummy_policy import DummyPolicy

class TestDummyPolicy(unittest.TestCase):
    """DummyPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DummyPolicy:
        """Test DummyPolicy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DummyPolicy`
        """
        model = DummyPolicy()
        if include_optional:
            return DummyPolicy(
                pk = '',
                name = '',
                execution_logging = True,
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                bound_to = 56,
                result = True,
                wait_min = -2147483648,
                wait_max = -2147483648
            )
        else:
            return DummyPolicy(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                bound_to = 56,
        )
        """

    def testDummyPolicy(self):
        """Test DummyPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
