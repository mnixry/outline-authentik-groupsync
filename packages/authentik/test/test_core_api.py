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

from authentik_openapi.api.core_api import CoreApi


class TestCoreApi(unittest.IsolatedAsyncioTestCase):
    """CoreApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = CoreApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_core_applications_check_access_retrieve(self) -> None:
        """Test case for core_applications_check_access_retrieve

        """
        pass

    async def test_core_applications_create(self) -> None:
        """Test case for core_applications_create

        """
        pass

    async def test_core_applications_destroy(self) -> None:
        """Test case for core_applications_destroy

        """
        pass

    async def test_core_applications_list(self) -> None:
        """Test case for core_applications_list

        """
        pass

    async def test_core_applications_metrics_list(self) -> None:
        """Test case for core_applications_metrics_list

        """
        pass

    async def test_core_applications_partial_update(self) -> None:
        """Test case for core_applications_partial_update

        """
        pass

    async def test_core_applications_retrieve(self) -> None:
        """Test case for core_applications_retrieve

        """
        pass

    async def test_core_applications_set_icon_create(self) -> None:
        """Test case for core_applications_set_icon_create

        """
        pass

    async def test_core_applications_set_icon_url_create(self) -> None:
        """Test case for core_applications_set_icon_url_create

        """
        pass

    async def test_core_applications_update(self) -> None:
        """Test case for core_applications_update

        """
        pass

    async def test_core_applications_used_by_list(self) -> None:
        """Test case for core_applications_used_by_list

        """
        pass

    async def test_core_authenticated_sessions_destroy(self) -> None:
        """Test case for core_authenticated_sessions_destroy

        """
        pass

    async def test_core_authenticated_sessions_list(self) -> None:
        """Test case for core_authenticated_sessions_list

        """
        pass

    async def test_core_authenticated_sessions_retrieve(self) -> None:
        """Test case for core_authenticated_sessions_retrieve

        """
        pass

    async def test_core_authenticated_sessions_used_by_list(self) -> None:
        """Test case for core_authenticated_sessions_used_by_list

        """
        pass

    async def test_core_brands_create(self) -> None:
        """Test case for core_brands_create

        """
        pass

    async def test_core_brands_current_retrieve(self) -> None:
        """Test case for core_brands_current_retrieve

        """
        pass

    async def test_core_brands_destroy(self) -> None:
        """Test case for core_brands_destroy

        """
        pass

    async def test_core_brands_list(self) -> None:
        """Test case for core_brands_list

        """
        pass

    async def test_core_brands_partial_update(self) -> None:
        """Test case for core_brands_partial_update

        """
        pass

    async def test_core_brands_retrieve(self) -> None:
        """Test case for core_brands_retrieve

        """
        pass

    async def test_core_brands_update(self) -> None:
        """Test case for core_brands_update

        """
        pass

    async def test_core_brands_used_by_list(self) -> None:
        """Test case for core_brands_used_by_list

        """
        pass

    async def test_core_groups_add_user_create(self) -> None:
        """Test case for core_groups_add_user_create

        """
        pass

    async def test_core_groups_create(self) -> None:
        """Test case for core_groups_create

        """
        pass

    async def test_core_groups_destroy(self) -> None:
        """Test case for core_groups_destroy

        """
        pass

    async def test_core_groups_list(self) -> None:
        """Test case for core_groups_list

        """
        pass

    async def test_core_groups_partial_update(self) -> None:
        """Test case for core_groups_partial_update

        """
        pass

    async def test_core_groups_remove_user_create(self) -> None:
        """Test case for core_groups_remove_user_create

        """
        pass

    async def test_core_groups_retrieve(self) -> None:
        """Test case for core_groups_retrieve

        """
        pass

    async def test_core_groups_update(self) -> None:
        """Test case for core_groups_update

        """
        pass

    async def test_core_groups_used_by_list(self) -> None:
        """Test case for core_groups_used_by_list

        """
        pass

    async def test_core_tokens_create(self) -> None:
        """Test case for core_tokens_create

        """
        pass

    async def test_core_tokens_destroy(self) -> None:
        """Test case for core_tokens_destroy

        """
        pass

    async def test_core_tokens_list(self) -> None:
        """Test case for core_tokens_list

        """
        pass

    async def test_core_tokens_partial_update(self) -> None:
        """Test case for core_tokens_partial_update

        """
        pass

    async def test_core_tokens_retrieve(self) -> None:
        """Test case for core_tokens_retrieve

        """
        pass

    async def test_core_tokens_set_key_create(self) -> None:
        """Test case for core_tokens_set_key_create

        """
        pass

    async def test_core_tokens_update(self) -> None:
        """Test case for core_tokens_update

        """
        pass

    async def test_core_tokens_used_by_list(self) -> None:
        """Test case for core_tokens_used_by_list

        """
        pass

    async def test_core_tokens_view_key_retrieve(self) -> None:
        """Test case for core_tokens_view_key_retrieve

        """
        pass

    async def test_core_transactional_applications_update(self) -> None:
        """Test case for core_transactional_applications_update

        """
        pass

    async def test_core_user_consent_destroy(self) -> None:
        """Test case for core_user_consent_destroy

        """
        pass

    async def test_core_user_consent_list(self) -> None:
        """Test case for core_user_consent_list

        """
        pass

    async def test_core_user_consent_retrieve(self) -> None:
        """Test case for core_user_consent_retrieve

        """
        pass

    async def test_core_user_consent_used_by_list(self) -> None:
        """Test case for core_user_consent_used_by_list

        """
        pass

    async def test_core_users_create(self) -> None:
        """Test case for core_users_create

        """
        pass

    async def test_core_users_destroy(self) -> None:
        """Test case for core_users_destroy

        """
        pass

    async def test_core_users_impersonate_create(self) -> None:
        """Test case for core_users_impersonate_create

        """
        pass

    async def test_core_users_impersonate_end_retrieve(self) -> None:
        """Test case for core_users_impersonate_end_retrieve

        """
        pass

    async def test_core_users_list(self) -> None:
        """Test case for core_users_list

        """
        pass

    async def test_core_users_me_retrieve(self) -> None:
        """Test case for core_users_me_retrieve

        """
        pass

    async def test_core_users_metrics_retrieve(self) -> None:
        """Test case for core_users_metrics_retrieve

        """
        pass

    async def test_core_users_partial_update(self) -> None:
        """Test case for core_users_partial_update

        """
        pass

    async def test_core_users_paths_retrieve(self) -> None:
        """Test case for core_users_paths_retrieve

        """
        pass

    async def test_core_users_recovery_create(self) -> None:
        """Test case for core_users_recovery_create

        """
        pass

    async def test_core_users_recovery_email_create(self) -> None:
        """Test case for core_users_recovery_email_create

        """
        pass

    async def test_core_users_retrieve(self) -> None:
        """Test case for core_users_retrieve

        """
        pass

    async def test_core_users_service_account_create(self) -> None:
        """Test case for core_users_service_account_create

        """
        pass

    async def test_core_users_set_password_create(self) -> None:
        """Test case for core_users_set_password_create

        """
        pass

    async def test_core_users_update(self) -> None:
        """Test case for core_users_update

        """
        pass

    async def test_core_users_used_by_list(self) -> None:
        """Test case for core_users_used_by_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
