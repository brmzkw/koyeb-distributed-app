# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.organization_invitation import OrganizationInvitation

class TestOrganizationInvitation(unittest.TestCase):
    """OrganizationInvitation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationInvitation:
        """Test OrganizationInvitation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationInvitation`
        """
        model = OrganizationInvitation()
        if include_optional:
            return OrganizationInvitation(
                id = '',
                email = '',
                role = 'INVALID',
                status = 'INVALID',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization_id = '',
                organization = openapi_client.models.public_organization.PublicOrganization(
                    id = '', 
                    name = '', 
                    plan = 'hobby', 
                    status = 'WARNING', ),
                invitee_id = '',
                invitee = openapi_client.models.public_user.PublicUser(
                    id = '', 
                    email = '', 
                    name = '', 
                    avatar_url = '', 
                    github_id = '', 
                    github_user = '', ),
                inviter_id = '',
                inviter = openapi_client.models.public_user.PublicUser(
                    id = '', 
                    email = '', 
                    name = '', 
                    avatar_url = '', 
                    github_id = '', 
                    github_user = '', )
            )
        else:
            return OrganizationInvitation(
        )
        """

    def testOrganizationInvitation(self):
        """Test OrganizationInvitation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
