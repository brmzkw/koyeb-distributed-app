# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.list_organization_members_reply import ListOrganizationMembersReply

class TestListOrganizationMembersReply(unittest.TestCase):
    """ListOrganizationMembersReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListOrganizationMembersReply:
        """Test ListOrganizationMembersReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListOrganizationMembersReply`
        """
        model = ListOrganizationMembersReply()
        if include_optional:
            return ListOrganizationMembersReply(
                members = [
                    openapi_client.models.organization_member.OrganizationMember(
                        id = '', 
                        organization_id = '', 
                        user_id = '', 
                        joined_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        role = 'INVALID', 
                        status = 'INVALID', 
                        user = openapi_client.models.public_user.PublicUser(
                            id = '', 
                            email = '', 
                            name = '', 
                            avatar_url = '', 
                            github_id = '', 
                            github_user = '', ), 
                        organization = openapi_client.models.public_organization.PublicOrganization(
                            id = '', 
                            name = '', 
                            plan = 'hobby', ), )
                    ],
                limit = 56,
                offset = 56,
                count = 56
            )
        else:
            return ListOrganizationMembersReply(
        )
        """

    def testListOrganizationMembersReply(self):
        """Test ListOrganizationMembersReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
