#!/usr/bin/env python3
"""Unit tests for utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """TestCase for access_nested_map function in utils.py"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests valid key path access in nested dictionaries."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), TypeError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Tests KeyError raised for invalid key path in nested dictionaries."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)



class TestGetJson(unittest.TestCase):
    """TestCase for get_json function in utils.py"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected_payload):
        """Tests get_json returns correct mocked payload."""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = expected_payload
            mock_get.return_value = mock_response

            self.assertEqual(get_json(url), expected_payload)


class TestMemoize(unittest.TestCase):
    """TestCase for memoize decorator in utils.py"""

    def test_memoize(self):
        """Tests that memoize caches method result properly."""
        class TestClass:
            """Dummy class with memoized property."""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()

        with patch.object(obj, "a_method", return_value=42) as mock_method:
            result1 = obj.a_property() #  property access — no ()
            result2 = obj.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
