# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deployment_provisioning_info import DeploymentProvisioningInfo

class TestDeploymentProvisioningInfo(unittest.TestCase):
    """DeploymentProvisioningInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentProvisioningInfo:
        """Test DeploymentProvisioningInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentProvisioningInfo`
        """
        model = DeploymentProvisioningInfo()
        if include_optional:
            return DeploymentProvisioningInfo(
                sha = '',
                image = '',
                stages = [
                    openapi_client.models.deployment_provisioning_info/stage.DeploymentProvisioningInfo.Stage(
                        name = '', 
                        status = 'UNKNOWN', 
                        messages = [
                            ''
                            ], 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        build_attempts = [
                            openapi_client.models.deployment_provisioning_info/stage/build_attempt.DeploymentProvisioningInfo.Stage.BuildAttempt(
                                id = 56, 
                                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ]
            )
        else:
            return DeploymentProvisioningInfo(
        )
        """

    def testDeploymentProvisioningInfo(self):
        """Test DeploymentProvisioningInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
