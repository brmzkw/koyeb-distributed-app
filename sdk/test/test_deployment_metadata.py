# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deployment_metadata import DeploymentMetadata

class TestDeploymentMetadata(unittest.TestCase):
    """DeploymentMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentMetadata:
        """Test DeploymentMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentMetadata`
        """
        model = DeploymentMetadata()
        if include_optional:
            return DeploymentMetadata(
                trigger = openapi_client.models.trigger_deployment_metadata.TriggerDeploymentMetadata(
                    type = 'UNKNOWN_TYPE', 
                    actor = 'UNKNOWN_ACTOR', 
                    git = openapi_client.models.trigger_git_deployment_metadata.TriggerGitDeploymentMetadata(
                        provider = 'UNKNOWN', 
                        repository = '', 
                        branch = '', 
                        sha = '', 
                        message = '', 
                        sender_username = '', 
                        sender_avatar_url = '', 
                        sender_profile_url = '', ), ),
                database = openapi_client.models.database_deployment_metadata.DatabaseDeploymentMetadata(
                    neon_postgres = openapi_client.models.neon_postgres_database_deployment_metadata.NeonPostgresDatabaseDeploymentMetadata(
                        reset_role_passwords = [
                            ''
                            ], ), ),
                git = openapi_client.models.git_deployment_metadata.GitDeploymentMetadata(
                    last_provisioned_deployment_id = '', ),
                archive = openapi_client.models.archive_deployment_metadata.ArchiveDeploymentMetadata(
                    last_provisioned_deployment_id = '', )
            )
        else:
            return DeploymentMetadata(
        )
        """

    def testDeploymentMetadata(self):
        """Test DeploymentMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
