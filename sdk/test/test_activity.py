# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.activity import Activity

class TestActivity(unittest.TestCase):
    """Activity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Activity:
        """Test Activity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Activity`
        """
        model = Activity()
        if include_optional:
            return Activity(
                id = '',
                actor = openapi_client.models.object.Object(
                    id = '', 
                    name = '', 
                    type = '', 
                    metadata = openapi_client.models.metadata.metadata(), 
                    deleted = True, ),
                object = openapi_client.models.object.Object(
                    id = '', 
                    name = '', 
                    type = '', 
                    metadata = openapi_client.models.metadata.metadata(), 
                    deleted = True, ),
                verb = '',
                metadata = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Activity(
        )
        """

    def testActivity(self):
        """Test Activity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
