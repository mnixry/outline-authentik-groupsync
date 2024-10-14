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

from authentik_openapi.models.event_matcher_policy_request import EventMatcherPolicyRequest

class TestEventMatcherPolicyRequest(unittest.TestCase):
    """EventMatcherPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventMatcherPolicyRequest:
        """Test EventMatcherPolicyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventMatcherPolicyRequest`
        """
        model = EventMatcherPolicyRequest()
        if include_optional:
            return EventMatcherPolicyRequest(
                name = '0',
                execution_logging = True,
                action = 'login',
                client_ip = '0',
                app = 'authentik.tenants',
                model = 'authentik_tenants.domain'
            )
        else:
            return EventMatcherPolicyRequest(
                name = '0',
        )
        """

    def testEventMatcherPolicyRequest(self):
        """Test EventMatcherPolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
