#!/usr/bin/python3
"""
Test for user class
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.user import User


class test_User(unittest.TestCase):
    """Test to class User"""
    def test_instances(self):
        """ Test instances"""
        obj = User()
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")
        self.assertEqual(obj.email, "")

    def test_attr_type(self):
        """Test type of attributes"""
        obj = User()
        self.assertEqual(type(obj.password), str)
        self.assertEqual(type(obj.first_name), str)
        self.assertEqual(type(obj.last_name), str)
        self.assertEqual(type(obj.email), str)

    def test_attr_existence(self):
        """Test if attributes exist"""
        obj = User()
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))
        self.assertTrue(hasattr(obj, "email"))

    def test_dif_id(self):
        """Test different id"""
        obj = User()
        other = User()
        self.assertNotEqual(obj.id, other.id)

    def test_procedence(self):
        """check if subclass"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_str_representation(self):
        """Testing string representation"""
        obj = User()
        clase = obj.__class__.__name__
        ide = obj.id
        cadena = f"[{clase}] ({ide}) {obj.__dict__}"
        self.assertEqual(str(obj), cadena)

    def test_documentation(self):
        """
        checking documentation
        """
        self.assertIsNotNone(User.__doc__)

if __name__ == '__main__':
    unittest.main()