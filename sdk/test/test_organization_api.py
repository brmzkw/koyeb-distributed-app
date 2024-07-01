# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.organization_api import OrganizationApi


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization(self) -> None:
        """Test case for create_organization

        Create organization
        """
        pass

    def test_deactivate_organization(self) -> None:
        """Test case for deactivate_organization

        Deactivate an organization
        """
        pass

    def test_delete_organization(self) -> None:
        """Test case for delete_organization

        Delete an organization
        """
        pass

    def test_get_github_installation(self) -> None:
        """Test case for get_github_installation

        Fetch github installation configuration
        """
        pass

    def test_get_organization(self) -> None:
        """Test case for get_organization

        Get organization
        """
        pass

    def test_github_installation(self) -> None:
        """Test case for github_installation

        Start github installation
        """
        pass

    def test_github_installation_callback(self) -> None:
        """Test case for github_installation_callback

        Github callback for app installation
        """
        pass

    def test_reactivate_organization(self) -> None:
        """Test case for reactivate_organization

        Reactivate an organization
        """
        pass

    def test_switch_organization(self) -> None:
        """Test case for switch_organization

        Switch organization context
        """
        pass

    def test_update_organization(self) -> None:
        """Test case for update_organization

        Update organization
        """
        pass

    def test_update_organization2(self) -> None:
        """Test case for update_organization2

        Update organization
        """
        pass

    def test_update_organization_plan(self) -> None:
        """Test case for update_organization_plan

        Update organization plan
        """
        pass

    def test_upsert_signup_qualification(self) -> None:
        """Test case for upsert_signup_qualification

        Upsert organization's signup qualification
        """
        pass


if __name__ == '__main__':
    unittest.main()