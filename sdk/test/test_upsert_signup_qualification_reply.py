# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.upsert_signup_qualification_reply import UpsertSignupQualificationReply

class TestUpsertSignupQualificationReply(unittest.TestCase):
    """UpsertSignupQualificationReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpsertSignupQualificationReply:
        """Test UpsertSignupQualificationReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpsertSignupQualificationReply`
        """
        model = UpsertSignupQualificationReply()
        if include_optional:
            return UpsertSignupQualificationReply(
                organization = openapi_client.models.represent_an_organization.Represent an Organization(
                    id = '', 
                    address1 = '', 
                    address2 = '', 
                    city = '', 
                    postal_code = '', 
                    state = '', 
                    country = '', 
                    company = True, 
                    vat_number = '', 
                    billing_name = '', 
                    billing_email = '', 
                    name = '', 
                    plan = 'hobby', 
                    plan_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    has_payment_method = True, 
                    subscription_id = '', 
                    current_subscription_id = '', 
                    latest_subscription_id = '', 
                    signup_qualification = openapi_client.models.signup_qualification.signup_qualification(), 
                    status = 'WARNING', 
                    status_message = 'NEW', 
                    deactivation_reason = 'INVALID', 
                    verified = True, 
                    qualifies_for_hobby23 = True, 
                    reprocess_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return UpsertSignupQualificationReply(
        )
        """

    def testUpsertSignupQualificationReply(self):
        """Test UpsertSignupQualificationReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
