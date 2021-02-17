#!/usr/bin/python3
""" Unittest for FileStorage class.
"""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)
