#!/usr/bin/python3
"""Unnittest for Review class"""
import pep8
import unittest
from models import review
from models.review import Review


class TestReview(unittest.TestCase):
    """Review class unit testing"""
    def test_type(self):
        """Method to create and object attribute.
        """
        rev1 = Review()
        self.assertEqual(Review, type(rev1))
        self.assertIsInstance(rev1, Review)

    def test_data_type(self):
        """Method that check if all attributes are in object
        and check their types.
        """
        rev1 = Review()
        self.assertTrue(hasattr(rev1, "place_id"))
        self.assertEqual(type(rev1.place_id), str)
        self.assertTrue(hasattr(rev1, "user_id"))
        self.assertEqual(type(rev1.user_id), str)
        self.assertTrue(hasattr(rev1, "text"))
        self.assertEqual(type(rev1.text), str)


class TestPep8B(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Method to probe pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(review.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)
