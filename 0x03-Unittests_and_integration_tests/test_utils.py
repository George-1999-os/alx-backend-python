#!/usr/bin/env python3
"""Unit tests for utils module"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""

    @parameterized.expand([
        ("simple_map", {"a": 1}, ("a",), 1),
        ("nested_map", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("deep_nested_map", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("missing_key", {}, ("a",)),
        ("partial_path", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, name, nested_map, path):
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, url, expected, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_get.return_value = mock_response

        result = get_json(url)
        self.assertEqual(result, expected)


class TestMemoize(unittest.TestCase):
    """Tests for memoize"""

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, "a_method") as mock_method:
            mock_method.return_value = 42
            result1 = test_obj.a_property
            result2 = test_obj.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
