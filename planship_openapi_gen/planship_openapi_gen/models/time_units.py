# coding: utf-8

"""
    Planship API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TimeUnits(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    MINUTE = 'minute'
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'
    PERPETUAL = 'perpetual'

    @classmethod
    def from_json(cls, json_str: str) -> TimeUnits:
        """Create an instance of TimeUnits from a JSON string"""
        return TimeUnits(json.loads(json_str))


