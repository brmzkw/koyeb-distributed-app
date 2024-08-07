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
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.service_state import ServiceState
from openapi_client.models.service_status import ServiceStatus
from openapi_client.models.service_type import ServiceType
from typing import Optional, Set
from typing_extensions import Self

class Service(BaseModel):
    """
    Service
    """ # noqa: E501
    id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    succeeded_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    resumed_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    name: Optional[StrictStr] = None
    type: Optional[ServiceType] = None
    organization_id: Optional[StrictStr] = None
    app_id: Optional[StrictStr] = None
    status: Optional[ServiceStatus] = None
    messages: Optional[List[StrictStr]] = None
    version: Optional[StrictStr] = None
    active_deployment_id: Optional[StrictStr] = None
    latest_deployment_id: Optional[StrictStr] = None
    last_provisioned_deployment_id: Optional[StrictStr] = None
    state: Optional[ServiceState] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "started_at", "succeeded_at", "paused_at", "resumed_at", "terminated_at", "name", "type", "organization_id", "app_id", "status", "messages", "version", "active_deployment_id", "latest_deployment_id", "last_provisioned_deployment_id", "state"]

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
        """Create an instance of Service from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "started_at": obj.get("started_at"),
            "succeeded_at": obj.get("succeeded_at"),
            "paused_at": obj.get("paused_at"),
            "resumed_at": obj.get("resumed_at"),
            "terminated_at": obj.get("terminated_at"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "organization_id": obj.get("organization_id"),
            "app_id": obj.get("app_id"),
            "status": obj.get("status"),
            "messages": obj.get("messages"),
            "version": obj.get("version"),
            "active_deployment_id": obj.get("active_deployment_id"),
            "latest_deployment_id": obj.get("latest_deployment_id"),
            "last_provisioned_deployment_id": obj.get("last_provisioned_deployment_id"),
            "state": ServiceState.from_dict(obj["state"]) if obj.get("state") is not None else None
        })
        return _obj


