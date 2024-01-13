#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os
from datetime import datetime
import json
from models.user import User


class test_fileStorage(unittest.TestCase):
    """ Define test class for file storgae with base model"""

    def setUp(self):
        """ Set up the defualt value"""
        del_list = []
        for k in storage._FileStorage__objects.keys():
            del_list.append(k)
        for k in del_list:
            del storage._FileStorage__objects[k]

    def tearDown(self):
        """ tear down the storage file at the end of test """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_init_empty(self):
        self.assertEqual(len(storage.all()), 0)

    def test_all_return_objects(self):
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_with_storage_fle(self):
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty_save_to_file(self):
        new = BaseModel()
        copy = new.to_dict()
        new.save()
        new_cop = BaseModel(**copy)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save_module(self):
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_from_empty(self):
        with open('file.json', 'w') as empty:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent_file(self):
        self.assertEqual(storage.reload(), None)

    def test_base_model_with_module_save(self):
        copy = BaseModel()
        copy.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_file_path_is_str(self):
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_sict_type_of_objects(self):
        self.assertEqual(type(storage.all()), dict)

    def test_storage_obj_created(self):
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_reload_from_nonexistent_file(self):
        storage_new = FileStorage()
        storage_new.reload()

    def test_saving_reload_multiple_models(self):
        modl1 = BaseModel()
        modl1.name = "Model1"
        modl1.save()

        modl2 = BaseModel()
        modl2.name = "Model2"
        modl2.save()

        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        key1 = f"{type(modl1).__name__}.{modl1.id}"
        key2 = f"{type(modl2).__name__}.{modl2.id}"

        self.assertIn(key1, all_objects)
        self.assertIn(key2, all_objects)

        reloaded_model1 = all_objects[key1]
        reloaded_model2 = all_objects[key2]

        self.assertEqual(reloaded_model1.name, modl1.name)
        self.assertEqual(reloaded_model2.name, modl2.name)

    def test_loads_valid_data_and_populates_objects_dictionary(self):
        # Initialize the class object
        file_storage = FileStorage()

        # Create a JSON file with valid data
        valid_data = {
            "User.1": {
                "__class__": "User",
                "id": "1",
                "name": "John Doe",
                        "age": 25
            },
            "User.2": {
                "__class__": "User",
                "id": "2",
                "name": "Jane Smith",
                        "age": 30
            }
        }
        with open(file_storage._FileStorage__file_path, 'w') as f:
            json.dump(valid_data, f)

        # Call the reload method
        file_storage.reload()

        # Check if the __objects dictionary is populated correctly
        assert len(file_storage._FileStorage__objects) == 2
        assert isinstance(file_storage._FileStorage__objects["User.1"], User)
        assert isinstance(file_storage._FileStorage__objects["User.2"], User)
        assert file_storage._FileStorage__objects["User.1"].name == "John Doe"
        assert file_storage._FileStorage__objects["User.1"].age == 25
        assert file_storage._FileStorage__objects["User.2"].name == "Jane Smith"
        assert file_storage._FileStorage__objects["User.2"].age == 30

    def test_does_not_load_nonexistent_file_and_does_not_raise_exception(self):
        # Initialize the class object
        file_storage = FileStorage()

        # Call the reload method
        file_storage.reload()

        # Check if the __objects dictionary is empty
        assert len(file_storage._FileStorage__objects) == 0
