#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for access_nested_map function in utils.py"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test correct access to values in nested dictionaries"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), TypeError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test exceptions raised for invalid paths"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
