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

from authentik_openapi.models.captcha_challenge_response_request import CaptchaChallengeResponseRequest

class TestCaptchaChallengeResponseRequest(unittest.TestCase):
    """CaptchaChallengeResponseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaptchaChallengeResponseRequest:
        """Test CaptchaChallengeResponseRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaptchaChallengeResponseRequest`
        """
        model = CaptchaChallengeResponseRequest()
        if include_optional:
            return CaptchaChallengeResponseRequest(
                component = 'ak-stage-captcha',
                token = '0'
            )
        else:
            return CaptchaChallengeResponseRequest(
                token = '0',
        )
        """

    def testCaptchaChallengeResponseRequest(self):
        """Test CaptchaChallengeResponseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
