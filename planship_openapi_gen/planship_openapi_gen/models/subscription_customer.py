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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from planship_openapi_gen.models.plan_in_db_base import PlanInDbBase

class SubscriptionCustomer(BaseModel):
    """
    SubscriptionCustomer
    """
    metadata_: Optional[Dict[str, Any]] = None
    is_administrator: Optional[StrictBool] = False
    is_subscriber: Optional[StrictBool] = True
    customer_id: StrictStr = Field(...)
    subscription_id: StrictStr = Field(...)
    plan: PlanInDbBase = Field(...)
    __properties = ["metadata_", "is_administrator", "is_subscriber", "customer_id", "subscription_id", "plan"]

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
    def from_json(cls, json_str: str) -> SubscriptionCustomer:
        """Create an instance of SubscriptionCustomer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionCustomer:
        """Create an instance of SubscriptionCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionCustomer.parse_obj(obj)

        _obj = SubscriptionCustomer.parse_obj({
            "metadata_": obj.get("metadata_"),
            "is_administrator": obj.get("is_administrator") if obj.get("is_administrator") is not None else False,
            "is_subscriber": obj.get("is_subscriber") if obj.get("is_subscriber") is not None else True,
            "customer_id": obj.get("customer_id"),
            "subscription_id": obj.get("subscription_id"),
            "plan": PlanInDbBase.from_dict(obj.get("plan")) if obj.get("plan") is not None else None
        })
        return _obj

