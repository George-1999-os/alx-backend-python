#!/usr/bin/env python3
"""Utilities module"""

from typing import Mapping, Any, Sequence
import requests

def access_nested_map(nested_map, path):
    for key in path:
        if isinstance(nested_map, dict) and key in nested_map:
            nested_map = nested_map[key]
        else:
            raise KeyError(key)
    return nested_map


def get_json(url: str) -> dict:
    """Fetch JSON content from a URL."""
    response = requests.get(url)
    return response.json()


def memoize(method):
    """Decorator to cache a method result as a property."""
    attr_name = "_{}".format(method.__name__)

    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return property(wrapper)
