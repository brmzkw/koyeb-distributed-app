# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.billing_api import BillingApi


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingApi()

    def tearDown(self) -> None:
        pass

    def test_has_unpaid_invoices(self) -> None:
        """Test case for has_unpaid_invoices

        Experimental: Has unpaid invoices
        """
        pass

    def test_manage(self) -> None:
        """Test case for manage

        """
        pass

    def test_next_invoice(self) -> None:
        """Test case for next_invoice

        Experimental: Fetch next invoice
        """
        pass


if __name__ == '__main__':
    unittest.main()