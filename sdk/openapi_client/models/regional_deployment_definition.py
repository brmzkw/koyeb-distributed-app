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
from openapi_client.models.deployment_health_check import DeploymentHealthCheck
from openapi_client.models.docker_source import DockerSource
from openapi_client.models.env import Env
from openapi_client.models.git_source import GitSource
from openapi_client.models.port import Port
from openapi_client.models.regional_deployment_definition_type import RegionalDeploymentDefinitionType
from openapi_client.models.regional_deployment_volume import RegionalDeploymentVolume
from openapi_client.models.route import Route
from openapi_client.models.scaling import Scaling
from typing import Optional, Set
from typing_extensions import Self

class RegionalDeploymentDefinition(BaseModel):
    """
    RegionalDeploymentDefinition
    """ # noqa: E501
    name: Optional[StrictStr] = None
    type: Optional[RegionalDeploymentDefinitionType] = None
    routes: Optional[List[Route]] = None
    ports: Optional[List[Port]] = None
    env: Optional[List[Env]] = None
    region: Optional[StrictStr] = None
    scaling: Optional[Scaling] = None
    instance_type: Optional[StrictStr] = None
    deployment_group: Optional[StrictStr] = None
    health_checks: Optional[List[DeploymentHealthCheck]] = None
    volumes: Optional[List[RegionalDeploymentVolume]] = None
    skip_cache: Optional[StrictBool] = None
    use_kuma_v2: Optional[StrictBool] = None
    docker: Optional[DockerSource] = None
    git: Optional[GitSource] = None
    archive: Optional[ArchiveSource] = None
    __properties: ClassVar[List[str]] = ["name", "type", "routes", "ports", "env", "region", "scaling", "instance_type", "deployment_group", "health_checks", "volumes", "skip_cache", "use_kuma_v2", "docker", "git", "archive"]

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
        """Create an instance of RegionalDeploymentDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scaling
        if self.scaling:
            _dict['scaling'] = self.scaling.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of archive
        if self.archive:
            _dict['archive'] = self.archive.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegionalDeploymentDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "routes": [Route.from_dict(_item) for _item in obj["routes"]] if obj.get("routes") is not None else None,
            "ports": [Port.from_dict(_item) for _item in obj["ports"]] if obj.get("ports") is not None else None,
            "env": [Env.from_dict(_item) for _item in obj["env"]] if obj.get("env") is not None else None,
            "region": obj.get("region"),
            "scaling": Scaling.from_dict(obj["scaling"]) if obj.get("scaling") is not None else None,
            "instance_type": obj.get("instance_type"),
            "deployment_group": obj.get("deployment_group"),
            "health_checks": [DeploymentHealthCheck.from_dict(_item) for _item in obj["health_checks"]] if obj.get("health_checks") is not None else None,
            "volumes": [RegionalDeploymentVolume.from_dict(_item) for _item in obj["volumes"]] if obj.get("volumes") is not None else None,
            "skip_cache": obj.get("skip_cache"),
            "use_kuma_v2": obj.get("use_kuma_v2"),
            "docker": DockerSource.from_dict(obj["docker"]) if obj.get("docker") is not None else None,
            "git": GitSource.from_dict(obj["git"]) if obj.get("git") is not None else None,
            "archive": ArchiveSource.from_dict(obj["archive"]) if obj.get("archive") is not None else None
        })
        return _obj


