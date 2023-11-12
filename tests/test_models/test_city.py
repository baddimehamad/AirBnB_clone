#!/usr/bin/python3
import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def doc_m_test(self):
        thedocument = City.__doc__
        self.assertGreater(len(thedocument), 1)

    def pep8_test(self):
        the_styles = pep8.StyleGuide(quiet=True).check_files(['models/city.py'])
        self.assertEqual(the_styles.total_errors, 0,"error or warning found.")

    def document_constract_test(self):
        thedocument = City.__init__.__doc__
        self.assertGreater(len(thedocument), 1)

    def pep8_city_test(self):
        the_styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_city.py'])
        self.assertEqual(the_styles.total_errors, 0,"error or warning found.")

    def c_test(self):
        with self.subTest(msg='Att'):
            self.assertIsInstance(City.state_id, str)
            self.assertIsInstance(City.name, str)

            
        with self.subTest(msg='Inh'):
            self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
