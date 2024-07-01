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
from openapi_client.models.trigger_git_deployment_metadata_provider import TriggerGitDeploymentMetadataProvider
from typing import Optional, Set
from typing_extensions import Self

class TriggerGitDeploymentMetadata(BaseModel):
    """
    TriggerGitDeploymentMetadata
    """ # noqa: E501
    provider: Optional[TriggerGitDeploymentMetadataProvider] = TriggerGitDeploymentMetadataProvider.UNKNOWN
    repository: Optional[StrictStr] = None
    branch: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    sender_username: Optional[StrictStr] = None
    sender_avatar_url: Optional[StrictStr] = None
    sender_profile_url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["provider", "repository", "branch", "sha", "message", "sender_username", "sender_avatar_url", "sender_profile_url"]

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
        """Create an instance of TriggerGitDeploymentMetadata from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TriggerGitDeploymentMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provider": obj.get("provider") if obj.get("provider") is not None else TriggerGitDeploymentMetadataProvider.UNKNOWN,
            "repository": obj.get("repository"),
            "branch": obj.get("branch"),
            "sha": obj.get("sha"),
            "message": obj.get("message"),
            "sender_username": obj.get("sender_username"),
            "sender_avatar_url": obj.get("sender_avatar_url"),
            "sender_profile_url": obj.get("sender_profile_url")
        })
        return _obj


