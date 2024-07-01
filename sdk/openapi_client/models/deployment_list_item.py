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
from openapi_client.models.deployment_database_info import DeploymentDatabaseInfo
from openapi_client.models.deployment_definition import DeploymentDefinition
from openapi_client.models.deployment_metadata import DeploymentMetadata
from openapi_client.models.deployment_provisioning_info import DeploymentProvisioningInfo
from openapi_client.models.deployment_status import DeploymentStatus
from typing import Optional, Set
from typing_extensions import Self

class DeploymentListItem(BaseModel):
    """
    DeploymentListItem
    """ # noqa: E501
    id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    allocated_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    succeeded_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    organization_id: Optional[StrictStr] = None
    app_id: Optional[StrictStr] = None
    service_id: Optional[StrictStr] = None
    parent_id: Optional[StrictStr] = None
    child_id: Optional[StrictStr] = None
    status: Optional[DeploymentStatus] = None
    metadata: Optional[DeploymentMetadata] = None
    definition: Optional[DeploymentDefinition] = None
    messages: Optional[List[StrictStr]] = None
    provisioning_info: Optional[DeploymentProvisioningInfo] = None
    database_info: Optional[DeploymentDatabaseInfo] = None
    version: Optional[StrictStr] = None
    deployment_group: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "allocated_at", "started_at", "succeeded_at", "terminated_at", "organization_id", "app_id", "service_id", "parent_id", "child_id", "status", "metadata", "definition", "messages", "provisioning_info", "database_info", "version", "deployment_group"]

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
        """Create an instance of DeploymentListItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provisioning_info
        if self.provisioning_info:
            _dict['provisioning_info'] = self.provisioning_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of database_info
        if self.database_info:
            _dict['database_info'] = self.database_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentListItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "allocated_at": obj.get("allocated_at"),
            "started_at": obj.get("started_at"),
            "succeeded_at": obj.get("succeeded_at"),
            "terminated_at": obj.get("terminated_at"),
            "organization_id": obj.get("organization_id"),
            "app_id": obj.get("app_id"),
            "service_id": obj.get("service_id"),
            "parent_id": obj.get("parent_id"),
            "child_id": obj.get("child_id"),
            "status": obj.get("status"),
            "metadata": DeploymentMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "definition": DeploymentDefinition.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "messages": obj.get("messages"),
            "provisioning_info": DeploymentProvisioningInfo.from_dict(obj["provisioning_info"]) if obj.get("provisioning_info") is not None else None,
            "database_info": DeploymentDatabaseInfo.from_dict(obj["database_info"]) if obj.get("database_info") is not None else None,
            "version": obj.get("version"),
            "deployment_group": obj.get("deployment_group")
        })
        return _obj

