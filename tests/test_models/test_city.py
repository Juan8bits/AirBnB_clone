#!/usr/bin/python3
"""Unnittest for City class"""
import pep8
import unittest
from models import city
from models.city import City


class TestCity(unittest.TestCase):
    """City class unit testing"""
    def test_type(self):
        """Method to create and object attribute.
        """
        city1 = City()
        self.assertEqual(City, type(city1))
        self.assertIsInstance(city1, City)
        self.assertEqual(str, type(city1.name))
        self.assertEqual(str, type(city1.state_id))

    def test_attributes(self):
        """Method that check if all attributes are in object.
        """
        city1 = City()
        self.assertTrue(hasattr(city1, "name"))
        self.assertTrue(hasattr(city1, "state_id"))


class TestPep8B(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Method to probe pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(city.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)
