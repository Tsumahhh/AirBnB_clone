#!/usr/bin/python3
"""
Test for review
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    """Test to Review class"""
    def test_procedure(self):
        """checking procedure"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instances(self):
        """checking instances"""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.text, "")
        self.assertEqual(obj.user_id, "")

    def test_attributes(self):
        """test attributes existence"""
        obj = Review()
        self.assertTrue(hasattr(obj, 'place_id'))
        self.assertTrue(hasattr(obj, 'text'))
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attr_type(self):
        """test type of attributes"""
        obj = Review()
        obj.place_id = "d1"
        obj.user_id = "123"
        obj.text = "my review"

        self.assertEqual(type(obj.place_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.text), str)

    def test_dif_id(self):
        """Test different id"""
        obj = Review()
        other = Review()
        self.assertNotEqual(obj.id, other.id)

    def test_with_args(self):
        """Test with args"""
        obj = Review()
        obj.place_id = "aldea"
        obj.text = "my review"
        obj.user_id = "12df"
        self.assertEqual(obj.place_id, "aldea")
        self.assertEqual(obj.text, "my review")
        self.assertEqual(obj.user_id, "12df")

    def test_documentation(self):
        """
        checking documentation
        """
        self.assertIsNotNone(Review.__doc__)


if __name__ == '__main__':
    unittest.main()