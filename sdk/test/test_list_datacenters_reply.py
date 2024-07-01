# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.list_datacenters_reply import ListDatacentersReply

class TestListDatacentersReply(unittest.TestCase):
    """ListDatacentersReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDatacentersReply:
        """Test ListDatacentersReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDatacentersReply`
        """
        model = ListDatacentersReply()
        if include_optional:
            return ListDatacentersReply(
                datacenters = [
                    openapi_client.models.datacenter_list_item.DatacenterListItem(
                        id = '', 
                        region_id = '', 
                        domain = '', 
                        coordinates = [
                            ''
                            ], 
                        use_kata = True, 
                        use_gpu = True, 
                        use_kuma = True, )
                    ]
            )
        else:
            return ListDatacentersReply(
        )
        """

    def testListDatacentersReply(self):
        """Test ListDatacentersReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
