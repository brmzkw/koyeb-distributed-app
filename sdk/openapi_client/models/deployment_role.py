# coding: utf-8

"""
    Koyeb Rest API

    The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DeploymentRole(str, Enum):
    """
    DeploymentRole
    """

    """
    allowed enum values
    """
    INVALID = 'INVALID'
    ACTIVE = 'ACTIVE'
    UPCOMING = 'UPCOMING'
    CURRENT = 'CURRENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeploymentRole from a JSON string"""
        return cls(json.loads(json_str))


