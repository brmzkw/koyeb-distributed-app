# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.docker_helper_api import DockerHelperApi


class TestDockerHelperApi(unittest.TestCase):
    """DockerHelperApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DockerHelperApi()

    def tearDown(self) -> None:
        pass

    def test_verify_docker_image(self) -> None:
        """Test case for verify_docker_image

        Verify if a docker image is reachable
        """
        pass


if __name__ == '__main__':
    unittest.main()