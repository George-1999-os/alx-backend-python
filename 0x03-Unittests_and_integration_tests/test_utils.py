#!/usr/bin/env python3
"""Unit tests for utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test nested dictionary access"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test exceptions raised for invalid paths"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestCase for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected_payload):
        """Test get_json returns expected payload"""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = expected_payload
            mock_get.return_value = mock_response

            self.assertEqual(get_json(url), expected_payload)


class TestMemoize(unittest.TestCase):
    """TestCase for memoize decorator"""

    def test_memoize(self):
        """Test memoize caches method result"""
        class TestClass:
            def a_method(self):
                return 42

            def a_property(self):
                return self.a_method()

        obj = TestClass()
        obj.a_property = memoize(obj.a_property)

        with patch.object(obj, "a_method", return_value=42) as mock_method:
            result1 = obj.a_property()
            result2 = obj.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
    
#!/usr/bin/env python3
"""Unit tests for utils.get_json"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns expected payload with mock"""
        with patch("utils.requests.get") as mock_get:
            # Mock the response
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            # Check that requests.get was called once with test_url
            mock_get.assert_called_once_with(test_url)

            # Check that result equals test_payload
            self.assertEqual(result, test_payload)
