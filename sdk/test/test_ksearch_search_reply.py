# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ksearch_search_reply import KsearchSearchReply

class TestKsearchSearchReply(unittest.TestCase):
    """KsearchSearchReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KsearchSearchReply:
        """Test KsearchSearchReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KsearchSearchReply`
        """
        model = KsearchSearchReply()
        if include_optional:
            return KsearchSearchReply(
                organizations = [
                    openapi_client.models.ksearch/organization.ksearch.Organization(
                        id = '', 
                        name = '', )
                    ],
                users = [
                    openapi_client.models.ksearch/user.ksearch.User(
                        id = '', 
                        email = '', 
                        name = '', 
                        github_user = '', )
                    ],
                apps = [
                    openapi_client.models.ksearch/app.ksearch.App(
                        id = '', 
                        organization_id = '', 
                        name = '', )
                    ],
                services = [
                    openapi_client.models.ksearch/service.ksearch.Service(
                        id = '', 
                        organization_id = '', 
                        app_id = '', 
                        name = '', )
                    ],
                global_deployments = [
                    openapi_client.models.ksearch/global_deployment.ksearch.GlobalDeployment(
                        id = '', 
                        organization_id = '', 
                        app_id = '', 
                        service_id = '', )
                    ],
                regional_deployments = [
                    openapi_client.models.ksearch/regional_deployment.ksearch.RegionalDeployment(
                        id = '', 
                        organization_id = '', 
                        app_id = '', 
                        service_id = '', 
                        region = '', )
                    ],
                instances = [
                    openapi_client.models.ksearch/instance.ksearch.Instance(
                        id = '', 
                        organization_id = '', 
                        app_id = '', 
                        service_id = '', 
                        allocation_id = '', )
                    ]
            )
        else:
            return KsearchSearchReply(
        )
        """

    def testKsearchSearchReply(self):
        """Test KsearchSearchReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
