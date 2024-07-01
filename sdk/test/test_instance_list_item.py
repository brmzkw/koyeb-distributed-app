# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.instance_list_item import InstanceListItem

class TestInstanceListItem(unittest.TestCase):
    """InstanceListItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstanceListItem:
        """Test InstanceListItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstanceListItem`
        """
        model = InstanceListItem()
        if include_optional:
            return InstanceListItem(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization_id = '',
                app_id = '',
                service_id = '',
                regional_deployment_id = '',
                allocation_id = '',
                type = '',
                replica_index = 56,
                region = '',
                datacenter = '',
                status = 'ALLOCATING',
                messages = [
                    ''
                    ],
                xyz_deployment_id = ''
            )
        else:
            return InstanceListItem(
        )
        """

    def testInstanceListItem(self):
        """Test InstanceListItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
