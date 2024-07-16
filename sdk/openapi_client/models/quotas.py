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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.persistent_volume_quotas import PersistentVolumeQuotas
from typing import Optional, Set
from typing_extensions import Self

class Quotas(BaseModel):
    """
    Quotas
    """ # noqa: E501
    apps: Optional[StrictStr] = None
    services: Optional[StrictStr] = None
    domains: Optional[StrictStr] = None
    services_by_app: Optional[StrictStr] = None
    service_provisioning_concurrency: Optional[StrictStr] = None
    memory_mb: Optional[StrictStr] = None
    instance_types: Optional[List[StrictStr]] = None
    regions: Optional[List[StrictStr]] = None
    max_organization_members: Optional[StrictStr] = None
    max_instances_by_type: Optional[Dict[str, StrictStr]] = None
    persistent_volumes_by_region: Optional[Dict[str, PersistentVolumeQuotas]] = None
    __properties: ClassVar[List[str]] = ["apps", "services", "domains", "services_by_app", "service_provisioning_concurrency", "memory_mb", "instance_types", "regions", "max_organization_members", "max_instances_by_type", "persistent_volumes_by_region"]

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
        """Create an instance of Quotas from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in persistent_volumes_by_region (dict)
        _field_dict = {}
        if self.persistent_volumes_by_region:
            for _key in self.persistent_volumes_by_region:
                if self.persistent_volumes_by_region[_key]:
                    _field_dict[_key] = self.persistent_volumes_by_region[_key].to_dict()
            _dict['persistent_volumes_by_region'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Quotas from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apps": obj.get("apps"),
            "services": obj.get("services"),
            "domains": obj.get("domains"),
            "services_by_app": obj.get("services_by_app"),
            "service_provisioning_concurrency": obj.get("service_provisioning_concurrency"),
            "memory_mb": obj.get("memory_mb"),
            "instance_types": obj.get("instance_types"),
            "regions": obj.get("regions"),
            "max_organization_members": obj.get("max_organization_members"),
            "max_instances_by_type": obj.get("max_instances_by_type"),
            "persistent_volumes_by_region": dict(
                (_k, PersistentVolumeQuotas.from_dict(_v))
                for _k, _v in obj["persistent_volumes_by_region"].items()
            )
            if obj.get("persistent_volumes_by_region") is not None
            else None
        })
        return _obj


