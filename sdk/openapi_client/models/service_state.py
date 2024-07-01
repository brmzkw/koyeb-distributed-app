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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.auto_release import AutoRelease
from openapi_client.models.desired_deployment import DesiredDeployment
from typing import Optional, Set
from typing_extensions import Self

class ServiceState(BaseModel):
    """
    ServiceState
    """ # noqa: E501
    desired_deployment: Optional[DesiredDeployment] = None
    auto_release: Optional[AutoRelease] = None
    __properties: ClassVar[List[str]] = ["desired_deployment", "auto_release"]

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
        """Create an instance of ServiceState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of desired_deployment
        if self.desired_deployment:
            _dict['desired_deployment'] = self.desired_deployment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_release
        if self.auto_release:
            _dict['auto_release'] = self.auto_release.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "desired_deployment": DesiredDeployment.from_dict(obj["desired_deployment"]) if obj.get("desired_deployment") is not None else None,
            "auto_release": AutoRelease.from_dict(obj["auto_release"]) if obj.get("auto_release") is not None else None
        })
        return _obj

