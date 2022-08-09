#!/usr/bin/python3
"""
TEST OF CLASS STATE
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.state import State


class test_State(unittest.TestCase):
    """test to class State"""
    def test_procedure(self):
        """checking procedure"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_class(self):
        """checking class"""
        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr_type(self):
        """checking attr(type, value)"""
        obj = State()
        self.assertEqual(type(obj.name), str)

    def tests_instances_attr(self):
        """Testing attr(type, value), subclass"""
        self.assertTrue('name' in State.__dict__)

    def test_str(self):
        """Testing str"""
        obj = State()
        string = f"[State] ({obj.id}) {obj.__dict__}"
        self.assertEqual(string, str(obj))

    def test_save(self):
        """Testing save"""
        obj = State()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_documentation(self):
        """
        Testing documentation
        """
        self.assertIsNotNone(State.__doc__)


if __name__ == '__main__':
    unittest.main()