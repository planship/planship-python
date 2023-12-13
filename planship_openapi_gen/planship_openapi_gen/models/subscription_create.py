# coding: utf-8

"""
    Planship API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class SubscriptionCreate(BaseModel):
    """
    SubscriptionCreate
    """
    auto_renew: StrictBool = Field(...)
    is_active: StrictBool = Field(...)
    plan_id: StrictStr = Field(...)
    renew_plan_id: StrictStr = Field(...)
    renew_at: datetime = Field(...)
    last_renewed_at: datetime = Field(...)
    max_subscribers: Optional[StrictInt] = 1
    start_at: datetime = Field(...)
    __properties = ["auto_renew", "is_active", "plan_id", "renew_plan_id", "renew_at", "last_renewed_at", "max_subscribers", "start_at"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SubscriptionCreate:
        """Create an instance of SubscriptionCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionCreate:
        """Create an instance of SubscriptionCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionCreate.parse_obj(obj)

        _obj = SubscriptionCreate.parse_obj({
            "auto_renew": obj.get("auto_renew"),
            "is_active": obj.get("is_active"),
            "plan_id": obj.get("plan_id"),
            "renew_plan_id": obj.get("renew_plan_id"),
            "renew_at": obj.get("renew_at"),
            "last_renewed_at": obj.get("last_renewed_at"),
            "max_subscribers": obj.get("max_subscribers") if obj.get("max_subscribers") is not None else 1,
            "start_at": obj.get("start_at")
        })
        return _obj


