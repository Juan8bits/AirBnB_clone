#!/usr/bin/python3
"""Unittest for BaseModel class.
    16/02/2021
"""
import os
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
        b = BaseModel()
        self.assertEqual(datetime.datetime, type(b.created_at))
        b.created_at = datetime.datetime(2021, 2, 17, 21, 5, 54, 119427)
        b_dict = b.to_dict()
        real = b_dict["created_at"]
        exp = "2021-02-17T21:05:54.119427"
        self.assertEqual(exp, real)

    def test_type_update_at(self):
        """Check type for attribute update_at."""
        b = BaseModel()
        self.assertEqual(datetime.datetime, type(b.updated_at))
        b.updated_at = datetime.datetime(2021, 2, 17, 21, 5, 54, 119572)
        b_dict = b.to_dict()
        real = b_dict["updated_at"]
        exp = "2021-02-17T21:05:54.119572"
        self.assertEqual(exp, real)

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

    def test_str_add_attr(self):
        """Check new attribute in the object."""
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 89
        b_str = str(b)

        part1 = "[BaseModel] ("
        len_part1 = len(part1) + len(b.id) + 2
        real1 = b_str[: len_part1]
        exp1 = part1 + b.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(b_str[len_part1:])
        exp2 = b.__dict__
        self.assertEqual(exp2, real2)


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
        self.assertLess(upd1, upd2)

    def test_save_jsonfile(self):
        """Check json file."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        b = BaseModel()
        b.save()
        b_key = "BaseModel." + b.id
        with open("file.json", "r") as file:
            json_text = file.read()
        self.assertTrue(b_key in json_text)


class TestBaseModel_kwargs(unittest.TestCase):
    """"Class to add Unittest for a BaseModel class.
       kwargs input.
    """
    def test_correct_dict_input(self):
        """Check for correct dic inputs."""
        b1 = BaseModel()
        b1.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        b1.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        b1.name = "Holberton"
        b1.my_number = "89"
        b1_dict = b1.to_dict()

        b2 = BaseModel(**b1_dict)
        b2_dict = b2.to_dict()

        self.assertEqual(b1_dict, b2_dict)
        self.assertEqual(datetime.datetime, type(b2.created_at))
        self.assertFalse(b1 is b2)

    def test_kwargs_all_inputs(self):
        """Check an input with all attributes with kwargs."""
        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        b = BaseModel(
            id=id_val,
            created_at=c_date,
            updated_at=u_date,
            name="Holberton")
        real = b.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427',
            'name': 'Holberton'}
        self.assertEqual(exp, real)

    def test_kwargs_id_create_at(self):
        """Check id create with kwars attribute method."""
        c_date = '2017-09-28T21:05:54.119427'
        id_val = "hola"
        b = BaseModel(id=id_val, created_at=c_date)
        b.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119573)
        real = b.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '2017-09-28T21:05:54.119573',
            'id': 'hola',
            'created_at': '2017-09-28T21:05:54.119427'}
        self.assertEqual(exp, real)

    def test_args_input_unused(self):
        """Chekc for unused attribute unused args."""
        b = BaseModel("element")
        self.assertNotIn("element", b.__dict__.values())

    def test_args_kwargs_input(self):
        """check kwargs input."""
        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        b = BaseModel(34, id=id_val, created_at=c_date, updated_at=u_date)
        real = b.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '2017-09-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2017-09-28T21:05:54.119427'}
        self.assertEqual(exp, real)


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
