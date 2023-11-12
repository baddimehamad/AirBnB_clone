#!/usr/bin/python3
"""Module for test Place class"""
import unittest
import json
import pep8
import datetime

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    
    def document_constract_test(self):
        the_document = Place.__init__.__doc__
        self.assertGreater(len(the_document), 1)
        
    def doc_m_test(self):
        the_document = Place.__doc__
        self.assertGreater(len(the_document), 1)

    def pep8_test(self):
        the_styles = pep8.StyleGuide(quiet=True).check_files(['models/place.py'])
        self.assertEqual(the_styles.total_errors, 0,"error or warning found.")

    def c_test(self):
        with self.subTest(msg='Att'):
            self.assertIsInstance(Place.city_id, str)
            self.assertIsInstance(Place.user_id, str)
            self.assertIsInstance(Place.latitude, float)
            self.assertIsInstance(Place.name, str)
            self.assertIsInstance(Place.description, str)
            self.assertIsInstance(Place.longitude, float)
            self.assertIsInstance(Place.number_rooms, int)
            self.assertIsInstance(Place.number_bathrooms, int)
            self.assertIsInstance(Place.max_guest, int)
            self.assertIsInstance(Place.price_by_night, int)
            self.assertIsInstance(Place.amenity_ids, list)
            
        with self.subTest(msg='Inh'):
            self.assertTrue(issubclass(Place, BaseModel))

    def pep8_place_test(self):
        the_styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_place.py'])
        self.assertEqual(the_styles.total_errors, 0,"error or warning found.")




if __name__ == '__main__':
    unittest.main()
