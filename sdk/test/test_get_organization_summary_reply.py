# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_organization_summary_reply import GetOrganizationSummaryReply

class TestGetOrganizationSummaryReply(unittest.TestCase):
    """GetOrganizationSummaryReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOrganizationSummaryReply:
        """Test GetOrganizationSummaryReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrganizationSummaryReply`
        """
        model = GetOrganizationSummaryReply()
        if include_optional:
            return GetOrganizationSummaryReply(
                summary = openapi_client.models.organization_summary.OrganizationSummary(
                    organization_id = '', 
                    instances = openapi_client.models.instances_summary.InstancesSummary(
                        total = '', 
                        by_type = {
                            'key' : ''
                            }, ), 
                    apps = openapi_client.models.apps_summary.AppsSummary(
                        total = '', 
                        by_status = {
                            'key' : ''
                            }, ), 
                    services = {
                        'key' : openapi_client.models.service_summary.ServiceSummary(
                            total = '', 
                            by_status = {
                                'key' : ''
                                }, )
                        }, 
                    domains = openapi_client.models.domains_summary.DomainsSummary(
                        total = '', 
                        by_status = {
                            'key' : ''
                            }, ), 
                    secrets = openapi_client.models.secrets_summary.SecretsSummary(
                        total = '', 
                        by_type = {
                            'key' : ''
                            }, ), 
                    neon_postgres = openapi_client.models.neon_postgres_summary.NeonPostgresSummary(
                        total = '', 
                        by_instance_type = {
                            'key' : ''
                            }, ), 
                    members = openapi_client.models.members_summary.MembersSummary(
                        total = '', 
                        invitations_by_status = {
                            'key' : ''
                            }, ), )
            )
        else:
            return GetOrganizationSummaryReply(
        )
        """

    def testGetOrganizationSummaryReply(self):
        """Test GetOrganizationSummaryReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
