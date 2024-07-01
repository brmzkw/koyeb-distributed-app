# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.kgitproxy_list_repositories_reply import KgitproxyListRepositoriesReply

class TestKgitproxyListRepositoriesReply(unittest.TestCase):
    """KgitproxyListRepositoriesReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KgitproxyListRepositoriesReply:
        """Test KgitproxyListRepositoriesReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KgitproxyListRepositoriesReply`
        """
        model = KgitproxyListRepositoriesReply()
        if include_optional:
            return KgitproxyListRepositoriesReply(
                repositories = [
                    openapi_client.models.kgitproxy/repository.kgitproxy.Repository(
                        id = '', 
                        organization_id = '', 
                        name = '', 
                        url = '', 
                        description = '', 
                        is_private = True, 
                        is_disabled = True, 
                        default_branch = '', 
                        provider = 'INVALID_PROVIDER', 
                        last_push_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        github = openapi_client.models.kgitproxy/git_hub_repository.kgitproxy.GitHubRepository(
                            github_id = '', ), )
                    ],
                limit = 56,
                offset = 56,
                count = 56
            )
        else:
            return KgitproxyListRepositoriesReply(
        )
        """

    def testKgitproxyListRepositoriesReply(self):
        """Test KgitproxyListRepositoriesReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()