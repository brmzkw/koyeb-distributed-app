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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.archive_source import ArchiveSource
from openapi_client.models.database_source import DatabaseSource
from openapi_client.models.deployment_definition_type import DeploymentDefinitionType
from openapi_client.models.deployment_env import DeploymentEnv
from openapi_client.models.deployment_health_check import DeploymentHealthCheck
from openapi_client.models.deployment_instance_type import DeploymentInstanceType
from openapi_client.models.deployment_port import DeploymentPort
from openapi_client.models.deployment_route import DeploymentRoute
from openapi_client.models.deployment_scaling import DeploymentScaling
from openapi_client.models.deployment_volume import DeploymentVolume
from openapi_client.models.docker_source import DockerSource
from openapi_client.models.git_source import GitSource
from typing import Optional, Set
from typing_extensions import Self

class DeploymentDefinition(BaseModel):
    """
    DeploymentDefinition
    """ # noqa: E501
    name: Optional[StrictStr] = None
    type: Optional[DeploymentDefinitionType] = None
    routes: Optional[List[DeploymentRoute]] = None
    ports: Optional[List[DeploymentPort]] = None
    env: Optional[List[DeploymentEnv]] = None
    regions: Optional[List[StrictStr]] = None
    scalings: Optional[List[DeploymentScaling]] = None
    instance_types: Optional[List[DeploymentInstanceType]] = None
    health_checks: Optional[List[DeploymentHealthCheck]] = None
    volumes: Optional[List[DeploymentVolume]] = None
    skip_cache: Optional[StrictBool] = None
    docker: Optional[DockerSource] = None
    git: Optional[GitSource] = None
    database: Optional[DatabaseSource] = None
    archive: Optional[ArchiveSource] = None
    __properties: ClassVar[List[str]] = ["name", "type", "routes", "ports", "env", "regions", "scalings", "instance_types", "health_checks", "volumes", "skip_cache", "docker", "git", "database", "archive"]

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
        """Create an instance of DeploymentDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in routes (list)
        _items = []
        if self.routes:
            for _item in self.routes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['routes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in env (list)
        _items = []
        if self.env:
            for _item in self.env:
                if _item:
                    _items.append(_item.to_dict())
            _dict['env'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in scalings (list)
        _items = []
        if self.scalings:
            for _item in self.scalings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scalings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in instance_types (list)
        _items = []
        if self.instance_types:
            for _item in self.instance_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instance_types'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in health_checks (list)
        _items = []
        if self.health_checks:
            for _item in self.health_checks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['health_checks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        # override the default output from pydantic by calling `to_dict()` of docker
        if self.docker:
            _dict['docker'] = self.docker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of git
        if self.git:
            _dict['git'] = self.git.to_dict()
        # override the default output from pydantic by calling `to_dict()` of database
        if self.database:
            _dict['database'] = self.database.to_dict()
        # override the default output from pydantic by calling `to_dict()` of archive
        if self.archive:
            _dict['archive'] = self.archive.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "routes": [DeploymentRoute.from_dict(_item) for _item in obj["routes"]] if obj.get("routes") is not None else None,
            "ports": [DeploymentPort.from_dict(_item) for _item in obj["ports"]] if obj.get("ports") is not None else None,
            "env": [DeploymentEnv.from_dict(_item) for _item in obj["env"]] if obj.get("env") is not None else None,
            "regions": obj.get("regions"),
            "scalings": [DeploymentScaling.from_dict(_item) for _item in obj["scalings"]] if obj.get("scalings") is not None else None,
            "instance_types": [DeploymentInstanceType.from_dict(_item) for _item in obj["instance_types"]] if obj.get("instance_types") is not None else None,
            "health_checks": [DeploymentHealthCheck.from_dict(_item) for _item in obj["health_checks"]] if obj.get("health_checks") is not None else None,
            "volumes": [DeploymentVolume.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None,
            "skip_cache": obj.get("skip_cache"),
            "docker": DockerSource.from_dict(obj["docker"]) if obj.get("docker") is not None else None,
            "git": GitSource.from_dict(obj["git"]) if obj.get("git") is not None else None,
            "database": DatabaseSource.from_dict(obj["database"]) if obj.get("database") is not None else None,
            "archive": ArchiveSource.from_dict(obj["archive"]) if obj.get("archive") is not None else None
        })
        return _obj


