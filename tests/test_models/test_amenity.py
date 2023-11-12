#!/usr/bin/python3
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def doc_m_test(self):
        the_doc = Amenity.__doc__
        self.assertGreater(len(the_doc), 1)

    def document_constract_test(self):
        the_document = Amenity.__init__.__doc__
        self.assertGreater(len(the_document), 1)

    def pep8_test(self):
        a_styles = pep8.StyleGuide(quiet=True).check_files(['models/amenity.py'])
        self.assertEqual(a_styles.total_errors, 0,"error or warning found.")

    def pep8_test_amenity_test(self):
        a_styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(a_styles.total_errors, 0,"error or warning found.")

    def c_test(self):
        with self.subTest(msg='Inh'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Att'):
            self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()
