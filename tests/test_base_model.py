#!/usr/bin/python3

import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    # BaseModel instance is created with default attributes
    def test_base_model_default_attributes(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    # BaseModel instance can be converted to dictionary using to_dict() method
    def test_base_model_to_dict(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(
            base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(
            base_model_dict['updated_at'], base_model.updated_at.isoformat())

    # BaseModel instance can be saved and updates_at attribute is updated
    def test_base_model_save(self):
        base_model = BaseModel()
        initial_updates_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updates_at, base_model.updated_at)

    # BaseModel instance is created with custom attributes
    def test_base_model_custom_attributes(self):
        custom_id = 'custom_id'
        custom_created_at = datetime(2022, 1, 1)
        custom_updates_at = datetime(2022, 1, 2)
        base_model = BaseModel()
        base_model.id = custom_id
        base_model.created_at = custom_created_at
        base_model.updates_at = custom_updates_at
        self.assertEqual(base_model.id, custom_id)
        self.assertEqual(base_model.created_at, custom_created_at)
        self.assertEqual(base_model.updates_at, custom_updates_at)

    # to_dict() method handles edge cases for datetime objects
    def test_base_model_to_dict_datetime_edge_cases(self):
        base_model = BaseModel()
        base_model.created_at = datetime(2022, 1, 1)
        base_model.updates_at = datetime(2022, 1, 2)
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['created_at'], '2022-01-01T00:00:00')
        self.assertEqual(base_model_dict['updates_at'], '2022-01-02T00:00:00')

    # save() method handles edge cases for datetime objects
    def test_save_updates_updated_at_to_current_datetime(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        assert base_model.updated_at != initial_updated_at
        assert isinstance(base_model.updated_at, datetime)
    # BaseModel instance can be printed as a string using __str__() method

    def test_base_model_str_method(self):
        base_model = BaseModel()
        self.assertIsInstance(str(base_model), str)

    # BaseModel instance has unique id attribute
    def test_base_model_unique_id(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    # __str__() method handles edge cases for non-string attributes
    def test_base_model_str_method_edge_cases(self):
        base_model = BaseModel()
        base_model.some_attribute = 123
        self.assertIn("some_attribute", str(base_model))
