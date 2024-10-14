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

from authentik_openapi.models.user_write_stage import UserWriteStage

class TestUserWriteStage(unittest.TestCase):
    """UserWriteStage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserWriteStage:
        """Test UserWriteStage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserWriteStage`
        """
        model = UserWriteStage()
        if include_optional:
            return UserWriteStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                flow_set = [
                    authentik_openapi.models.flow_set.FlowSet(
                        pk = '', 
                        policybindingmodel_ptr_id = '', 
                        name = '', 
                        slug = 'z', 
                        title = '', 
                        designation = null, 
                        background = '', 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        export_url = '', 
                        layout = 'stacked', 
                        denied_action = null, )
                    ],
                user_creation_mode = 'never_create',
                create_users_as_inactive = True,
                create_users_group = '',
                user_type = 'internal',
                user_path_template = ''
            )
        else:
            return UserWriteStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
        )
        """

    def testUserWriteStage(self):
        """Test UserWriteStage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
