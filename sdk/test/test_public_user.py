# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.public_user import PublicUser

class TestPublicUser(unittest.TestCase):
    """PublicUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublicUser:
        """Test PublicUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublicUser`
        """
        model = PublicUser()
        if include_optional:
            return PublicUser(
                id = '',
                email = '',
                name = '',
                avatar_url = '',
                github_id = '',
                github_user = ''
            )
        else:
            return PublicUser(
        )
        """

    def testPublicUser(self):
        """Test PublicUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
