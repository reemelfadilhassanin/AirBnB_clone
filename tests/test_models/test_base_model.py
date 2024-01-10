#!/usr/bin/python3

import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

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
        assert base_model.updated_at > initial_updated_at
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

    def test_no_arguments(self):
        model = BaseModel()
        assert isinstance(model.id, str)
        assert isinstance(model.created_at, datetime)
        assert isinstance(model.updated_at, datetime)

    def test_from_dict_empty(self):
        my_new_model = BaseModel()

        self.assertIsNotNone(my_new_model.id)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)

    def test_kwargs(self):
        attributes = {
            'id': 'test_id',
            'created_at': '2022-01-11T12:34:56.789012',
            'updated_at': '2022-01-11T12:45:00.123456',
            'name': 'Test_Model',
            'my_number': 42,
            'additional_attr': 'test_value'
        }

        m_model = BaseModel(**attributes)

        self.assertEqual(m_model.id, attributes['id'])
        self.assertEqual(m_model.name, attributes['name'])
        self.assertEqual(m_model.my_number, attributes['my_number'])
        self.assertEqual(m_model.additional_attr,
                         attributes['additional_attr'])
        self.assertIsInstance(m_model.created_at, datetime)
        self.assertIsInstance(m_model.updated_at, datetime)

    def test_not_equal_base(self):
        """this to check if two base are not equale in attribute
        """
        m1 = BaseModel(name="Model1", my_number=42)
        m2 = BaseModel(name="Model2", my_number=42)

        self.assertNotEqual(m1, m2)

    def test_instance_diff(self):
        m1 = BaseModel(name="Model1", my_number=42)
        diff_in = "not_a_BaseModel_instance"

        self.assertNotEqual(m1, diff_in)


if __name__ == '__main__':
    unittest.main()
