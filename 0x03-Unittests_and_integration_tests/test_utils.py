#!/usr/bin/env python3
"""Unit tests for utils"""

import unittest
from utils import memoize
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize

# --------------------------
# TestAccessNestedMap
# --------------------------
class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected results"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))

# --------------------------
# TestGetJson
# --------------------------
class TestGetJson(unittest.TestCase):
    """TestCase for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected payload"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

# --------------------------
# TestMemoize
# --------------------------
class TestMemoize(unittest.TestCase):
    """TestCase for memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches a method result"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()
        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            # Call the memoized method twice
            result1 = obj.a_property()  # <-- must call
            result2 = obj.a_property()  # <-- must call

            # Assert both results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure the original method was called only once
            mocked.assert_called_once()
