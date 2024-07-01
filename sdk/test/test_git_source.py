# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.git_source import GitSource

class TestGitSource(unittest.TestCase):
    """GitSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GitSource:
        """Test GitSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GitSource`
        """
        model = GitSource()
        if include_optional:
            return GitSource(
                repository = '',
                branch = '',
                tag = '',
                sha = '',
                build_command = '',
                run_command = '',
                no_deploy_on_push = True,
                workdir = '',
                buildpack = openapi_client.models.buildpack_builder.BuildpackBuilder(
                    build_command = '', 
                    run_command = '', 
                    privileged = True, ),
                docker = openapi_client.models.docker_builder.DockerBuilder(
                    dockerfile = '', 
                    entrypoint = [
                        ''
                        ], 
                    command = '', 
                    args = [
                        ''
                        ], 
                    target = '', 
                    privileged = True, )
            )
        else:
            return GitSource(
        )
        """

    def testGitSource(self):
        """Test GitSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()