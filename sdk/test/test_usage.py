# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.usage import Usage

class TestUsage(unittest.TestCase):
    """Usage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Usage:
        """Test Usage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Usage`
        """
        model = Usage()
        if include_optional:
            return Usage(
                organization_id = '',
                periods = {
                    'key' : openapi_client.models.period_usage.PeriodUsage(
                        starting_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        ending_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        apps = [
                            openapi_client.models.app_usage.AppUsage(
                                app_id = '', 
                                app_name = '', 
                                services = [
                                    openapi_client.models.service_usage.ServiceUsage(
                                        service_id = '', 
                                        service_name = '', 
                                        regions = {
                                            'key' : openapi_client.models.region_usage.RegionUsage(
                                                instances = {
                                                    'key' : openapi_client.models.instance_usage.InstanceUsage(
                                                        duration_seconds = 56, )
                                                    }, )
                                            }, )
                                    ], )
                            ], )
                    }
            )
        else:
            return Usage(
        )
        """

    def testUsage(self):
        """Test Usage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
