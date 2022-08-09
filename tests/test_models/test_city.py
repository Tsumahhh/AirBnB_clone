#!/usr/bin/python3
"""
TEST OF CLASS CITY
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.city import City


class test_City(unittest.TestCase):
    """test to class City"""
    def test_procedure(self):
        """checking procedure"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_class(self):
        """checking class"""
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr_type(self):
        """checking attr(type, value)"""
        obj = City()
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.state_id), str)

    def tests_instances_attr(self):
        """Testing attr(type, value), subclass"""
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)

    def test_str(self):
        """Testing str"""
        obj = City()
        string = f"[City] ({obj.id}) {obj.__dict__}"
        self.assertEqual(string, str(obj))

    def test_save(self):
        """Testing save"""
        obj = City()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_documentation(self):
        """
        Testing documentation
        """
        self.assertIsNotNone(City.__doc__)


if __name__ == '__main__':
    unittest.main()