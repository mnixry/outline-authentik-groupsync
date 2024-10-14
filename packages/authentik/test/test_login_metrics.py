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

from authentik_openapi.models.login_metrics import LoginMetrics

class TestLoginMetrics(unittest.TestCase):
    """LoginMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginMetrics:
        """Test LoginMetrics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginMetrics`
        """
        model = LoginMetrics()
        if include_optional:
            return LoginMetrics(
                logins = [
                    authentik_openapi.models.coordinate.Coordinate(
                        x_cord = 56, 
                        y_cord = 56, )
                    ],
                logins_failed = [
                    authentik_openapi.models.coordinate.Coordinate(
                        x_cord = 56, 
                        y_cord = 56, )
                    ],
                authorizations = [
                    authentik_openapi.models.coordinate.Coordinate(
                        x_cord = 56, 
                        y_cord = 56, )
                    ]
            )
        else:
            return LoginMetrics(
                logins = [
                    authentik_openapi.models.coordinate.Coordinate(
                        x_cord = 56, 
                        y_cord = 56, )
                    ],
                logins_failed = [
                    authentik_openapi.models.coordinate.Coordinate(
                        x_cord = 56, 
                        y_cord = 56, )
                    ],
                authorizations = [
                    authentik_openapi.models.coordinate.Coordinate(
                        x_cord = 56, 
                        y_cord = 56, )
                    ],
        )
        """

    def testLoginMetrics(self):
        """Test LoginMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
