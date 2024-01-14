#!/usr/bin/python3

"""Tests for FileStorage class."""


import unittest
import uuid
import json
import os
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

import models

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestInstanceInitialization(unittest.TestCase):
    """Test FileStorage instance initialization."""

    def setUp(self):
        """Set up before each test."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialize_instance(self):
        """chk FileStorage instance is initialized and file doesn't exist."""
        self.assertFalse(os.path.exists(self.file_path))
        storage_instance = FileStorage()
        self.assertFalse(os.path.exists(self.file_path))


class TestAllInstanceMethod(unittest.TestCase):
    """Test 'all' instance method on FileStorage instance."""

    def setUp(self):
        """Set up before each test."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_instance_method(self):
        """chk 'all' method returns a dict and updates with new instances."""
        storage_instance = FileStorage()
        all_objects = storage_instance.all()
        self.assertIsInstance(all_objects, dict)
        initial_objects_count = len(all_objects)

        model_instance1 = BaseModel()
        all_objects = storage_instance.all()
        self.assertTrue(len(all_objects) == 1 + initial_objects_count)
        self.assertIn(model_instance1, all_objects.values())

        model_instance2 = BaseModel()
        all_objects = storage_instance.all()
        self.assertTrue(len(all_objects) == 2 + initial_objects_count)
        self.assertIn(model_instance2, all_objects.values())


class TestNewInstanceMethod(unittest.TestCase):
    """Test 'new' instance method on FileStorage instance."""

    def setUp(self):
        """Set up before each test."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_instance_method(self):
        """Verify 'new' method adds new instance to the dictionary."""
        storage_instance = FileStorage()
        all_objects = storage_instance.all()
        self.assertIsInstance(all_objects, dict)
        initial_objects_count = len(all_objects)

        model_instance1 = BaseModel()
        all_objects = storage_instance.all()
        self.assertTrue(len(all_objects) == 1 + initial_objects_count)
        self.assertIn(model_instance1, all_objects.values())

        model_instance2 = BaseModel(**model_instance1.to_dict())
        all_objects = storage_instance.all()
        self.assertNotIn(model_instance2, all_objects.values())
        self.assertTrue(len(all_objects) == 1 + initial_objects_count)
        model_instance2.id = str(uuid.uuid4())
        storage_instance.new(model_instance2)
        all_objects = storage_instance.all()
        self.assertTrue(len(all_objects) == 2 + initial_objects_count)
        self.assertIn(model_instance2, all_objects.values())

        with self.assertRaises(TypeError):
            storage_instance.new()

        with self.assertRaises(TypeError):
            storage_instance.all(model_instance1, model_instance2)

        with self.assertRaises(AttributeError):
            storage_instance.new("string")

        with self.assertRaises(AttributeError):
            storage_instance.new(1)

        with self.assertRaises(AttributeError):
            storage_instance.new({"a": 12})

        with self.assertRaises(AttributeError):
            storage_instance.new((1, 2))

        with self.assertRaises(AttributeError):
            storage_instance.new(1.5)


class TestSaveInstanceMethod(unittest.TestCase):
    """Test 'save' instance method on FileStorage instance."""

    def setUp(self):
        """Set up before each test."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_instance_method(self):
        """Verify 'save' method saves data to file and reloads correctly."""
        storage_instance = FileStorage()
        all_objects = storage_instance.all()
        initial_objects_count = len(all_objects)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            storage_instance.reload()

        self.assertTrue(initial_objects_count == len(storage_instance.all()))
        model_instance1 = BaseModel()
        all_objects = storage_instance.all()
        self.assertTrue(len(all_objects) == 1 + initial_objects_count)
        self.assertIn(model_instance1, all_objects.values())

        self.assertFalse(os.path.exists(self.file_path))
        storage_instance.save()
        self.assertTrue(os.path.exists(self.file_path))

        storage_instance.reload()
        key = model_instance1.__class__.__name__ + "." + model_instance1.id
        self.assertEqual(model_instance1.id, storage_instance.all()[key].id)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            model_instance1 = BaseModel()
            all_objects = storage_instance.all()
            self.assertTrue(len(all_objects) == 2 + initial_objects_count)
            self.assertIn(model_instance1, all_objects.values())

            self.assertFalse(os.path.exists(self.file_path))
            model_instance1.save()
            self.assertTrue(os.path.exists(self.file_path))

            storage_instance.reload()
            key = model_instance1.__class__.__name__ + "." + model_instance1.id
            self.assertEqual(model_instance1.id,
                             storage_instance.all()[key].id)

            with self.assertRaises(TypeError):
                storage_instance.reload(1.5)

        # Additional test cases for 'save'
        model_instance3 = BaseModel()
        all_objects = storage_instance.all()
        self.assertTrue(len(all_objects) == 3 + initial_objects_count)
        storage_instance.save()
        storage_instance.reload()
        key = model_instance3.__class__.__name__ + "." + model_instance3.id
        self.assertEqual(model_instance3.id, storage_instance.all()[key].id)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
