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
from openapi_client.models.apps_summary import AppsSummary
from openapi_client.models.domains_summary import DomainsSummary
from openapi_client.models.instances_summary import InstancesSummary
from openapi_client.models.members_summary import MembersSummary
from openapi_client.models.neon_postgres_summary import NeonPostgresSummary
from openapi_client.models.secrets_summary import SecretsSummary
from openapi_client.models.service_summary import ServiceSummary
from typing import Optional, Set
from typing_extensions import Self

class OrganizationSummary(BaseModel):
    """
    OrganizationSummary
    """ # noqa: E501
    organization_id: Optional[StrictStr] = None
    instances: Optional[InstancesSummary] = None
    apps: Optional[AppsSummary] = None
    services: Optional[Dict[str, ServiceSummary]] = None
    domains: Optional[DomainsSummary] = None
    secrets: Optional[SecretsSummary] = None
    neon_postgres: Optional[NeonPostgresSummary] = None
    members: Optional[MembersSummary] = None
    __properties: ClassVar[List[str]] = ["organization_id", "instances", "apps", "services", "domains", "secrets", "neon_postgres", "members"]

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
        """Create an instance of OrganizationSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of instances
        if self.instances:
            _dict['instances'] = self.instances.to_dict()
        # override the default output from pydantic by calling `to_dict()` of apps
        if self.apps:
            _dict['apps'] = self.apps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in services (dict)
        _field_dict = {}
        if self.services:
            for _key in self.services:
                if self.services[_key]:
                    _field_dict[_key] = self.services[_key].to_dict()
            _dict['services'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of domains
        if self.domains:
            _dict['domains'] = self.domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secrets
        if self.secrets:
            _dict['secrets'] = self.secrets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neon_postgres
        if self.neon_postgres:
            _dict['neon_postgres'] = self.neon_postgres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of members
        if self.members:
            _dict['members'] = self.members.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "organization_id": obj.get("organization_id"),
            "instances": InstancesSummary.from_dict(obj["instances"]) if obj.get("instances") is not None else None,
            "apps": AppsSummary.from_dict(obj["apps"]) if obj.get("apps") is not None else None,
            "services": dict(
                (_k, ServiceSummary.from_dict(_v))
                for _k, _v in obj["services"].items()
            )
            if obj.get("services") is not None
            else None,
            "domains": DomainsSummary.from_dict(obj["domains"]) if obj.get("domains") is not None else None,
            "secrets": SecretsSummary.from_dict(obj["secrets"]) if obj.get("secrets") is not None else None,
            "neon_postgres": NeonPostgresSummary.from_dict(obj["neon_postgres"]) if obj.get("neon_postgres") is not None else None,
            "members": MembersSummary.from_dict(obj["members"]) if obj.get("members") is not None else None
        })
        return _obj

