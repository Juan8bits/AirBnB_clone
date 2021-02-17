#!/usr/bin/python3
"""Unittest for BaseModel class.
    16/02/2021
"""
import os
import unittest
from models import storage
from models.base_model import BaseModel

class TestBaseModelinit(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
        __init__ method.
    """
    def test_object(self):
        obj = BaseModel()
        self.assertEqual(BaseModel, type(obj))

class TestBaseModelid(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
        id attribute.
    """
    def test_unique_id(self):
        ob = BaseModel()
        ob2 = BaseModel()
        self.assertNotEqual(ob.id,ob2.id)

if __name__ == '__main__':
    unittest.main()
