#!/usr/bin/python3
"""Unittest for BaseModel class.
    16/02/2021
"""
import os
import unittest
import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
        __init__ method.
    """
    def test_object(self):
        obj = BaseModel()
        self.assertEqual(BaseModel, type(obj))

    def test_unique_id(self):
        ob = BaseModel()
        ob2 = BaseModel()
        self.assertNotEqual(ob.id, ob2.id)

    def test_type_id(self):
        ob = BaseModel()
        self.assertEqual(str, type(ob.id))

    def test_type_created_at(self):
        ob = BaseModel()
        self.assertEqual(datetime.datetime, type(ob.created_at))

    def test_type_update_at(self):
        ob = BaseModel()
        self.assertEqual(datetime.datetime, type(ob.updated_at))

    def test_type_to_dict(self):
        ob = BaseModel()
        dic = ob.to_dict()
        self.assertEqual(dict, type(dic))


class TestBaseModel_str_repr(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
        str method.
    """
    def test_unique_id(self):
        ob = BaseModel()
        ob2 = BaseModel()
        self.assertNotEqual(ob.id, ob2.id)
