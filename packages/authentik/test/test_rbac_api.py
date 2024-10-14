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

from authentik_openapi.api.rbac_api import RbacApi


class TestRbacApi(unittest.IsolatedAsyncioTestCase):
    """RbacApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = RbacApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_rbac_permissions_assigned_by_roles_assign(self) -> None:
        """Test case for rbac_permissions_assigned_by_roles_assign

        """
        pass

    async def test_rbac_permissions_assigned_by_roles_list(self) -> None:
        """Test case for rbac_permissions_assigned_by_roles_list

        """
        pass

    async def test_rbac_permissions_assigned_by_roles_unassign_partial_update(self) -> None:
        """Test case for rbac_permissions_assigned_by_roles_unassign_partial_update

        """
        pass

    async def test_rbac_permissions_assigned_by_users_assign(self) -> None:
        """Test case for rbac_permissions_assigned_by_users_assign

        """
        pass

    async def test_rbac_permissions_assigned_by_users_list(self) -> None:
        """Test case for rbac_permissions_assigned_by_users_list

        """
        pass

    async def test_rbac_permissions_assigned_by_users_unassign_partial_update(self) -> None:
        """Test case for rbac_permissions_assigned_by_users_unassign_partial_update

        """
        pass

    async def test_rbac_permissions_list(self) -> None:
        """Test case for rbac_permissions_list

        """
        pass

    async def test_rbac_permissions_retrieve(self) -> None:
        """Test case for rbac_permissions_retrieve

        """
        pass

    async def test_rbac_permissions_roles_destroy(self) -> None:
        """Test case for rbac_permissions_roles_destroy

        """
        pass

    async def test_rbac_permissions_roles_list(self) -> None:
        """Test case for rbac_permissions_roles_list

        """
        pass

    async def test_rbac_permissions_roles_partial_update(self) -> None:
        """Test case for rbac_permissions_roles_partial_update

        """
        pass

    async def test_rbac_permissions_roles_retrieve(self) -> None:
        """Test case for rbac_permissions_roles_retrieve

        """
        pass

    async def test_rbac_permissions_roles_update(self) -> None:
        """Test case for rbac_permissions_roles_update

        """
        pass

    async def test_rbac_permissions_users_destroy(self) -> None:
        """Test case for rbac_permissions_users_destroy

        """
        pass

    async def test_rbac_permissions_users_list(self) -> None:
        """Test case for rbac_permissions_users_list

        """
        pass

    async def test_rbac_permissions_users_partial_update(self) -> None:
        """Test case for rbac_permissions_users_partial_update

        """
        pass

    async def test_rbac_permissions_users_retrieve(self) -> None:
        """Test case for rbac_permissions_users_retrieve

        """
        pass

    async def test_rbac_permissions_users_update(self) -> None:
        """Test case for rbac_permissions_users_update

        """
        pass

    async def test_rbac_roles_create(self) -> None:
        """Test case for rbac_roles_create

        """
        pass

    async def test_rbac_roles_destroy(self) -> None:
        """Test case for rbac_roles_destroy

        """
        pass

    async def test_rbac_roles_list(self) -> None:
        """Test case for rbac_roles_list

        """
        pass

    async def test_rbac_roles_partial_update(self) -> None:
        """Test case for rbac_roles_partial_update

        """
        pass

    async def test_rbac_roles_retrieve(self) -> None:
        """Test case for rbac_roles_retrieve

        """
        pass

    async def test_rbac_roles_update(self) -> None:
        """Test case for rbac_roles_update

        """
        pass

    async def test_rbac_roles_used_by_list(self) -> None:
        """Test case for rbac_roles_used_by_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
