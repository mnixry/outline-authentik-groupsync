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

from authentik_openapi.models.deny_stage_request import DenyStageRequest

class TestDenyStageRequest(unittest.TestCase):
    """DenyStageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DenyStageRequest:
        """Test DenyStageRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DenyStageRequest`
        """
        model = DenyStageRequest()
        if include_optional:
            return DenyStageRequest(
                name = '0',
                flow_set = [
                    authentik_openapi.models.flow_set_request.FlowSetRequest(
                        name = '0', 
                        slug = 'z0', 
                        title = '0', 
                        designation = null, 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        layout = 'stacked', 
                        denied_action = null, )
                    ],
                deny_message = ''
            )
        else:
            return DenyStageRequest(
                name = '0',
        )
        """

    def testDenyStageRequest(self):
        """Test DenyStageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
