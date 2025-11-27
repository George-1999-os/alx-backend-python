#!/usr/bin/env python3
"""
Utility functions and decorators for the ALX Backend Python project.
"""

import requests
from typing import Mapping, Any, Sequence
from functools import wraps


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map using a sequence of keys.

    Args:
        nested_map (Mapping): The dictionary to access.
        path (Sequence): A sequence of keys representing the path.

    Returns:
        Any: The value located at the end of the path.

    Raises:
        KeyError: If a key in the path does not exist.
    """
    value = nested_map
    for key in path:
        value = value[key]
    return value


def get_json(url: str) -> dict:
    """
    Fetch JSON data from a URL.

    Args:
        url (str): URL to request.

    Returns:
        dict: The JSON payload from the response.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn):
    """
    Decorator that caches the result of a method.

    When the method is first called, its result is stored.
    Subsequent calls return the cached result instead of recalculating.
    """
    attr_name = "_" + fn.__name__

    @wraps(fn)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return wrapper
