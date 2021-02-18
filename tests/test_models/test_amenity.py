#!/usr/bin/python3
"""Unnittest for User class"""
import pep8
import unittest
from models import amenity
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity class unit testing"""
    def Test_type(self):
        """Method to create and object attribute.
        """
        ameni = Amenity()
        self.assertEqual(Amenity, type(ameni))
        self.assertIsInstance(self.amenity1, Amenity)

    def test_data_type(self):
        """Method that check if all attributes are in object
        and check their types.
        """
        ameni = Amenity()
        self.assertTrue(hasattr(ameni, "name"))
        self.assertEqual(type(ameni.name), str)


class TestPep8B(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Method to probe pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)
