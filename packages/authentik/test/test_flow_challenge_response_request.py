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

from authentik_openapi.models.flow_challenge_response_request import FlowChallengeResponseRequest

class TestFlowChallengeResponseRequest(unittest.TestCase):
    """FlowChallengeResponseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowChallengeResponseRequest:
        """Test FlowChallengeResponseRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowChallengeResponseRequest`
        """
        model = FlowChallengeResponseRequest()
        if include_optional:
            return FlowChallengeResponseRequest(
                component = 'ak-stage-user-login',
                code = 56,
                phone_number = '0',
                selected_challenge = authentik_openapi.models.device_challenge_request.DeviceChallengeRequest(
                    device_class = '0', 
                    device_uid = '0', 
                    challenge = {
                        'key' : null
                        }, ),
                selected_stage = '0',
                webauthn = {
                    'key' : None
                    },
                duo = 56,
                response = {
                    'key' : None
                    },
                token = '0',
                uid_field = '0',
                password = '0',
                remember_me = True
            )
        else:
            return FlowChallengeResponseRequest(
                code = 56,
                response = {
                    'key' : None
                    },
                token = '0',
                uid_field = '0',
                password = '0',
                remember_me = True,
        )
        """

    def testFlowChallengeResponseRequest(self):
        """Test FlowChallengeResponseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
