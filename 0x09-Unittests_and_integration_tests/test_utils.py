#!/usr/bin/env python3
"""test utils module"""

import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """class to test access
    nested map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), {'b': 2},),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test acces nested map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class to test get json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """test get json method"""
        with mock.patch('requests.get') as mock_:
            mock_.return_value.json.return_value = expected
            self.assertEqual(expected, get_json(url))


class TestMemoize(unittest.TestCase):
    """class to test memoized methosd"""

    def test_memoize(self):
        """test memoized method"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_:
            mock_tc = TestClass()
            call_1 = mock_tc.a_property
            call_2 = mock_tc.a_property
            self.assertEqual(call_1, mock_.return_value)
            self.assertEqual(call_2, mock_.return_value)
            mock_.assert_called_once()


if __name__ == '__main__':
    unittest.main()
