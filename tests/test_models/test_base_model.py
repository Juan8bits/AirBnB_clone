#!/usr/bin/python3
"""Unittest for BaseModel class.
    16/02/2021
"""

import pep8
import unittest
import datetime
from models import storage
from models import base_model
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
        __init__ method.
    """
    def test_object(self):
        """ Create an object."""
        obj = BaseModel()
        self.assertEqual(BaseModel, type(obj))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "id"))

    def test_unique_id(self):
        """Check unique id per object."""
        ob = BaseModel()
        ob2 = BaseModel()
        self.assertNotEqual(ob.id, ob2.id)

    def test_type_id(self):
        """Check type for attribute id."""
        ob = BaseModel()
        self.assertEqual(str, type(ob.id))

    def test_type_created_at(self):
        """Check type for attribute created_at."""
        ob = BaseModel()
        self.assertEqual(datetime.datetime, type(ob.created_at))

    def test_type_update_at(self):
        """Check type for attribute update_at."""
        ob = BaseModel()
        self.assertEqual(datetime.datetime, type(ob.updated_at))

    def test_type_to_dict(self):
        """Check type of return value method."""
        ob = BaseModel()
        dic = ob.to_dict()
        self.assertEqual(dict, type(dic))


class TestBaseModel_to_dict(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
       to_dict method.
    """
    def test_to_dict_return(self):
        """Check serialization and deserialization."""
        args = {"updated_at": "2021-02-17T20:13:30.925617",
                "id": "44367831-eb30-415e-b395-3aeefab79f12",
                "created_at": "2021-02-17T20:13:30.925458",
                "__class__": "BaseModel"
                }
        dic = {'updated_at': '2021-02-17T20:13:30.925617',
               'id': '44367831-eb30-415e-b395-3aeefab79f12',
               'created_at': '2021-02-17T20:13:30.925458',
               '__class__': 'BaseModel'
               }
        self.bm1 = BaseModel(**args)
        self.assertEqual(self.bm1.to_dict(), dic)


class TestBaseModel__str__(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
       __str__ method.
    """
    def test_str_format(self):
        """Check str format."""
        args = {"updated_at": "2021-02-17T20:13:30.925617",
                "id": "44367831-eb30-415e-b395-3aeefab79f12",
                "created_at": "2021-02-17T20:13:30.925458",
                "__class__": "BaseModel"
                }
        self.bm1 = BaseModel(**args)
        rep = str(self.bm1)
        my_str = "[{}] ({}) {}".format(self.bm1.__class__.__name__,
                                       self.bm1.id, self.bm1.__dict__)
        self.assertIsInstance(rep, str)
        self.assertEqual(rep, my_str)


class TestBaseModel_save(unittest.TestCase):
    """Class to add Unittest for a BaseModel class.
       save method.
    """
    def test_save(self):
        """Check the save method"""
        ob = BaseModel()
        upd1 = ob.updated_at
        ob.save()
        upd2 = ob.updated_at
        self.assertNotEqual(upd1, upd2)


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to probe pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")


class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)
