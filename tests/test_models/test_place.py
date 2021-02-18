#!/usr/bin/python3
"""Unnittest for Place class"""
import pep8
import unittest
from models import place
from models.place import Place


class TestPlace(unittest.TestCase):
    """Place class unit testing"""
    def test_type(self):
        """Method to create and object attribute.
        """
        place1 = Place()
        self.assertEqual(Place, type(place1))
        self.assertIsInstance(place1, Place)

    def test_data_type(self):
        """Method that check if all attributes are in object
        and check their types.
        """
        place1 = Place()
        self.assertTrue(hasattr(place1, "city_id"))
        self.assertEqual(type(place1.city_id), str)
        self.assertTrue(hasattr(place1, "user_id"))
        self.assertEqual(type(place1.user_id), str)
        self.assertTrue(hasattr(place1, "name"))
        self.assertEqual(type(place1.name), str)
        self.assertTrue(hasattr(place1, "description"))
        self.assertEqual(type(place1.description), str)
        self.assertTrue(hasattr(place1, "number_rooms"))
        self.assertEqual(type(place1.number_rooms), int)
        self.assertTrue(hasattr(place1, "number_bathrooms"))
        self.assertEqual(type(place1.number_bathrooms), int)
        self.assertTrue(hasattr(place1, "max_guest"))
        self.assertEqual(type(place1.max_guest), int)
        self.assertTrue(hasattr(place1, "price_by_night"))
        self.assertEqual(type(place1.price_by_night), int)
        self.assertTrue(hasattr(place1, "latitude"))
        self.assertEqual(type(place1.latitude), float)
        self.assertTrue(hasattr(place1, "longitude"))
        self.assertEqual(type(place1.longitude), float)
        self.assertTrue(hasattr(place1, "amenity_ids"))
        self.assertEqual(type(place1.amenity_ids), list)


class TestPep8B(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Method to probe pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(place.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)
