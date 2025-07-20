#!/usr/bin/env python3
"""Utils module with helper functions"""
import requests
from functools import wraps


def access_nested_map(nested_map, path):
    """Access a nested dictionary with a given path"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """GET JSON content from a URL"""
    response = requests.get(url)
    return response.json()


def memoize(method):
    """Decorator to memoize method output"""
    attr_name = "_{}".format(method.__name__)

    @property
    @wraps(method)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)
    return wrapper
