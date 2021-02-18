#!/usr/bin/python3
"""Unnittest for User class"""
import pep8
import unittest
from models import state
from models.state import State


class TestState(unittest.TestCase):
    """State class unit testing"""
    def test_type(self):
        """check the instance of the object"""
        state_ = State()
        self.assertEqual(State, type(state_))
        self.assertIsInstance(state_, State)

    def test_attributes_all(self):
        """Check types an existances of all attributes"""
        state1 = State()
        self.assertTrue(hasattr(state1, "name"))
        self.assertEqual(type(state1.name), str)
        self.assertEqual(str, type(state1.id))


class TestPep8B(unittest.TestCase):
    """Class to do pep8 validation."""
    def test_pep8(self):
        """Method to probe pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/state.py'
        file2 = 'tests/test_models/test_state.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """ Method to check for module documentation."""
        self.assertTrue(len(state.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)
