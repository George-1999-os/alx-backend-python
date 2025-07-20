#!/usr/bin/env python3
"""Unit test module for utils.py"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns correct value from nested path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """Test access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit tests for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected_payload):
        """Test get_json returns expected payload from mocked response"""
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected_payload
            result = get_json(url)
            self.assertEqual(result, expected_payload)


class TestMemoize(unittest.TestCase):
    """Unit tests for memoize decorator"""

    def test_memoize(self):
        """Test memoize caches method result and avoids repeated calls"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test = TestClass()

        with patch.object(test, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test.a_property
            result2 = test.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
