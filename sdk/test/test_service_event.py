# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.service_event import ServiceEvent

class TestServiceEvent(unittest.TestCase):
    """ServiceEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceEvent:
        """Test ServiceEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceEvent`
        """
        model = ServiceEvent()
        if include_optional:
            return ServiceEvent(
                id = '',
                when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization_id = '',
                service_id = '',
                type = '',
                message = '',
                metadata = openapi_client.models.metadata.metadata()
            )
        else:
            return ServiceEvent(
        )
        """

    def testServiceEvent(self):
        """Test ServiceEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()