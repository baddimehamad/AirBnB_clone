#!/usr/bin/python3
import unittest
import json
import pep8
import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def document_mod_test(self):
        thedocument = BaseModel.__doc__
        self.assertGreater(len(thedocument), 1)
    def task1_test(self):
        the_a_model = BaseModel()
        self.assertIs(type(the_a_model), BaseModel)
        the_a_model.name = "baddi"
        the_a_model.my_number = 13
        self.assertEqual(the_a_model.name, "baddi")
        self.assertEqual(the_a_model.my_number, 13)
        model_types_json = {
            "number": int,
            "name": str,
            "__class__": str,
            "time_update": str,
            "id": str,
            "time_create": str
        }
        the_a_model_json = the_a_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, the_a_model_json)
                self.assertIs(type(the_a_model_json[key]), value)

    def pep8_test(self):
        a_styles = pep8.StyleGuide(quiet=True).check_files(['models/base_model.py'])
        self.assertEqual(a_styles.total_errors, 0,"error or warning found.")

    def document_constract_test(self):
        thedocuement = BaseModel.__init__.__doc__
        self.assertGreater(len(thedocuement), 1)

    def pep8_basem_test(self):
        a_styles = pep8.StyleGuide(quiet=True).check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(a_styles.total_errors, 0,"error or warning found.")


    def types_test(self):
        model22 = BaseModel()
        self.assertIs(type(model22), BaseModel)
        model22.name = "baddi"
        model22.my_number = 23
        self.assertEqual(model22.name, "baddi")
        self.assertEqual(model22.my_number, 23)
        model_types = {
            "number": int,
            "name": str,
            "time_update": datetime.datetime,
            "id": str,
            "time_create": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, model22.__dict__)
                self.assertIs(type(model22.__dict__[key]), value)

    def test_datetime_model(self):
        model33 = BaseModel()
        model43 = BaseModel()
        self.assertNotEqual(model33.time_create, model33.time_update)
        self.assertNotEqual(model33.time_create, model43.time_create)

    def test_uuid(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_constructor_kwargs(self):
        x= BaseModel()
        x.my_number = 13
        x.name = "baddi"
        json_attributes = x.to_dict()

        y = BaseModel(**json_attributes)

        self.assertIsInstance(y, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        
    def test_string_representation(self):
        the_a_model = BaseModel()
        the_a_model.my_number = 23
        the_a_model.name = "baddi"

        id_model = the_a_model.id

        expected = '[BaseModel] ({}) {}'\
                   .format(id_model, the_a_model.__dict__)
        self.assertEqual(str(the_a_model), expected)

        self.assertIsNot(x, y)

    def test_file_save(self):
        b3 = BaseModel()
        b3.save()
        with open("f.json", 'r') as f:
            self.assertIn(b3.id, f.read())


if __name__ == '__main__':
    unittest.main()
