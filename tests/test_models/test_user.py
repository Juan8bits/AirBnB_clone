#!/usr/bin/python3
"""Unnittest for User class"""
import pep8
import unittest
from models import user
from models.user import User


class TestUser(unittest.TestCase):
    """User class unit testing"""
    def setUp(self):
        """Method to create and object attribute.
        """
        self.user1 = User()

    def test_data_type(self):
        """Method that check if all attributes are in object
        and check their types.
        """
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertEqual(type(self.user1.email), str)

        self.assertTrue(hasattr(self.user1, "password"))
        self.assertEqual(type(self.user1.password), str)

        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertEqual(type(self.user1.first_name), str)

        self.assertTrue(hasattr(self.user1, "last_name"))
        self.assertEqual(type(self.user1.last_name), str)

    def test_instantation(self):
        """Check if the object is instance of User class."""
        self.assertIsInstance(self.user1, User)


class TestPep8B(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Method to probe pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(user.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)
