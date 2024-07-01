# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.subscription_payment_failure_stripe_sdk import SubscriptionPaymentFailureStripeSDK
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionPaymentFailure(BaseModel):
    """
    SubscriptionPaymentFailure
    """ # noqa: E501
    failed_at: Optional[datetime] = None
    next_attempt: Optional[datetime] = None
    attempt_count: Optional[StrictStr] = None
    error_code: Optional[StrictStr] = None
    error_reason: Optional[StrictStr] = None
    error_type: Optional[StrictStr] = None
    error_message: Optional[StrictStr] = None
    payment_method_required: Optional[StrictBool] = None
    redirect_url: Optional[StrictStr] = None
    stripe_sdk: Optional[SubscriptionPaymentFailureStripeSDK] = None
    __properties: ClassVar[List[str]] = ["failed_at", "next_attempt", "attempt_count", "error_code", "error_reason", "error_type", "error_message", "payment_method_required", "redirect_url", "stripe_sdk"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SubscriptionPaymentFailure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of stripe_sdk
        if self.stripe_sdk:
            _dict['stripe_sdk'] = self.stripe_sdk.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionPaymentFailure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "failed_at": obj.get("failed_at"),
            "next_attempt": obj.get("next_attempt"),
            "attempt_count": obj.get("attempt_count"),
            "error_code": obj.get("error_code"),
            "error_reason": obj.get("error_reason"),
            "error_type": obj.get("error_type"),
            "error_message": obj.get("error_message"),
            "payment_method_required": obj.get("payment_method_required"),
            "redirect_url": obj.get("redirect_url"),
            "stripe_sdk": SubscriptionPaymentFailureStripeSDK.from_dict(obj["stripe_sdk"]) if obj.get("stripe_sdk") is not None else None
        })
        return _obj

