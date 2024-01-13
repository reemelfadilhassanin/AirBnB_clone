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

    # BaseModel with default attributes

    def test_base_model_default_attributes(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    # BaseModel to dictionary using to_dict()
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

    # updates_at attribute is updated
    def test_base_model_save(self):
        base_model = BaseModel()
        initial_updates_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updates_at, base_model.updated_at)

    # BaseModel with custom attributes
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

    # to_dict() method
    def test_base_model_to_dict_datetime_edge_cases(self):
        base_model = BaseModel()
        base_model.created_at = datetime(2022, 1, 1)
        base_model.updates_at = datetime(2022, 1, 2)
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['created_at'], '2022-01-01T00:00:00')
        self.assertEqual(base_model_dict['updates_at'], '2022-01-02T00:00:00')

    # save() method
    def test_save_updates_updated_at_to_current_datetime(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        assert base_model.updated_at > initial_updated_at
        assert isinstance(base_model.updated_at, datetime)
    # __str__() method

    def test_base_model_str_method(self):
        base_model = BaseModel()
        self.assertIsInstance(str(base_model), str)

    # uuid attribute
    def test_base_model_unique_id(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    # __str__() method for non-string
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

    def test_init_of_base(self):
        """Check __init__ of BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_of_base(self):
        """this to check __str__ method of BaseModel work in correct"""
        model = BaseModel()
        string_representation = str(model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn(str(model.id), string_representation)

    def test_save_of_base(self):
        """Test the save"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model_json = my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_json["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model_json["name"], "Test Model")

    def test_instance_from_dict(self):
        """check creating an instance from a dictionary"""
        model = BaseModel()
        model.name = "Test Model"
        model_json = model.to_dict()

        new_model = BaseModel(**model_json)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertEqual(new_model.name, "Test Model")

    def test_empty_kwargs(self):
        """test initialize instance of base with empty dic
        """
        base_model = BaseModel(**{})
        assert isinstance(base_model.id, str)
        assert isinstance(base_model.created_at, datetime)
        assert isinstance(base_model.updated_at, datetime)

    def test_updated_after_save(self):
        """Test update changes after calling save"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_attributes_not_included(self):

        data = {
            'id': '123',
            'created_at': '2022-01-13T12:34:56.789012',
            'updated_at': '2022-01-13T12:34:56.789012',
            'name': 'Test Name'
        }
        my_model = BaseModel(**data)
        self.assertFalse(hasattr(my_model, 'nonexistent_attribute'))


if __name__ == '__main__':
    unittest.main()
