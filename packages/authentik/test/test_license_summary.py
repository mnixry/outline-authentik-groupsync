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

from authentik_openapi.models.license_summary import LicenseSummary

class TestLicenseSummary(unittest.TestCase):
    """LicenseSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenseSummary:
        """Test LicenseSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenseSummary`
        """
        model = LicenseSummary()
        if include_optional:
            return LicenseSummary(
                internal_users = 56,
                external_users = 56,
                status = 'unlicensed',
                latest_valid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                license_flags = [
                    'trial'
                    ]
            )
        else:
            return LicenseSummary(
                internal_users = 56,
                external_users = 56,
                status = 'unlicensed',
                latest_valid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                license_flags = [
                    'trial'
                    ],
        )
        """

    def testLicenseSummary(self):
        """Test LicenseSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
