# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.deployment_scaling_target import DeploymentScalingTarget

class TestDeploymentScalingTarget(unittest.TestCase):
    """DeploymentScalingTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentScalingTarget:
        """Test DeploymentScalingTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentScalingTarget`
        """
        model = DeploymentScalingTarget()
        if include_optional:
            return DeploymentScalingTarget(
                average_cpu = openapi_client.models.deployment_scaling_target_average_cpu.DeploymentScalingTargetAverageCPU(
                    value = 56, ),
                average_mem = openapi_client.models.deployment_scaling_target_average_mem.DeploymentScalingTargetAverageMem(
                    value = 56, ),
                requests_per_second = openapi_client.models.deployment_scaling_target_requests_per_second.DeploymentScalingTargetRequestsPerSecond(
                    value = 56, ),
                concurrent_requests = openapi_client.models.deployment_scaling_target_concurrent_requests.DeploymentScalingTargetConcurrentRequests(
                    value = 56, ),
                requests_response_time = openapi_client.models.deployment_scaling_target_requests_response_time.DeploymentScalingTargetRequestsResponseTime(
                    value = 56, 
                    quantile = 56, )
            )
        else:
            return DeploymentScalingTarget(
        )
        """

    def testDeploymentScalingTarget(self):
        """Test DeploymentScalingTarget"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
