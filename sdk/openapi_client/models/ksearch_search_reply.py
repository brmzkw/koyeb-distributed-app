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
from openapi_client.models.ksearch_app import KsearchApp
from openapi_client.models.ksearch_global_deployment import KsearchGlobalDeployment
from openapi_client.models.ksearch_instance import KsearchInstance
from openapi_client.models.ksearch_organization import KsearchOrganization
from openapi_client.models.ksearch_regional_deployment import KsearchRegionalDeployment
from openapi_client.models.ksearch_service import KsearchService
from openapi_client.models.ksearch_user import KsearchUser
from typing import Optional, Set
from typing_extensions import Self

class KsearchSearchReply(BaseModel):
    """
    KsearchSearchReply
    """ # noqa: E501
    organizations: Optional[List[KsearchOrganization]] = None
    users: Optional[List[KsearchUser]] = None
    apps: Optional[List[KsearchApp]] = None
    services: Optional[List[KsearchService]] = None
    global_deployments: Optional[List[KsearchGlobalDeployment]] = None
    regional_deployments: Optional[List[KsearchRegionalDeployment]] = None
    instances: Optional[List[KsearchInstance]] = None
    __properties: ClassVar[List[str]] = ["organizations", "users", "apps", "services", "global_deployments", "regional_deployments", "instances"]

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
        """Create an instance of KsearchSearchReply from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in organizations (list)
        _items = []
        if self.organizations:
            for _item in self.organizations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['organizations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in apps (list)
        _items = []
        if self.apps:
            for _item in self.apps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['apps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in services (list)
        _items = []
        if self.services:
            for _item in self.services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['services'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in global_deployments (list)
        _items = []
        if self.global_deployments:
            for _item in self.global_deployments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['global_deployments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in regional_deployments (list)
        _items = []
        if self.regional_deployments:
            for _item in self.regional_deployments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['regional_deployments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in instances (list)
        _items = []
        if self.instances:
            for _item in self.instances:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instances'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KsearchSearchReply from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "organizations": [KsearchOrganization.from_dict(_item) for _item in obj["organizations"]] if obj.get("organizations") is not None else None,
            "users": [KsearchUser.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "apps": [KsearchApp.from_dict(_item) for _item in obj["apps"]] if obj.get("apps") is not None else None,
            "services": [KsearchService.from_dict(_item) for _item in obj["services"]] if obj.get("services") is not None else None,
            "global_deployments": [KsearchGlobalDeployment.from_dict(_item) for _item in obj["global_deployments"]] if obj.get("global_deployments") is not None else None,
            "regional_deployments": [KsearchRegionalDeployment.from_dict(_item) for _item in obj["regional_deployments"]] if obj.get("regional_deployments") is not None else None,
            "instances": [KsearchInstance.from_dict(_item) for _item in obj["instances"]] if obj.get("instances") is not None else None
        })
        return _obj


