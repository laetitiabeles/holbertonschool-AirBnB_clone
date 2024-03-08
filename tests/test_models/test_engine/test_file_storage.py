#!/usr/bin/python3

import unittest
from datetime import datetime
from time import sleep
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path


class TestStorage(unittest.TestCase):
    # def test_file_path(self):
    #     self.assertIsNone(FileStorage.__file_path)

    def test_file_path1(self):
        self.assertTrue(path.exists(FileStorage._FileStorage__file_path))

    def test_update_now(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        original_created_at = model.created_at
        sleep(1)
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)
        self.assertTrue(original_created_at, model.created_at)
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_save(self):
        model = BaseModel()
        self.assertIsNone(model.save())

    def test_update_type(self):
        model = BaseModel()
        self.assertTrue(type(model.updated_at) is datetime)

    def setUp(self):
        """instance for testing"""
        self.storage = FileStorage()

    def tearDown(self):
        """clean up after testing"""
        if os.path.exists(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)

    def test_pycode(self):
        style = pycodestyle.StyleGuide(quiet=True)
        files = [
            'models/engine/file_storage.py'
            'tests/test_models/test_engine/test_file_storage.py'
        ]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )

    def test_all(self):
        """test all method"""
        test_dict = self.storage.all()
        self.assertIsInstance(test_dict, dict)

    def test_new(self):
        """tests if new method adds object correctly"""
        user = User()
        self.storage.new(user)
        key = "User." + str(user.id)
        self.assertTrue(key in self.storage.all())

    def test_reload(self):
        """tests deserialization of objects"""
        user = User() in self.storage.all()

    if __name__ == '__main__':
        unittest.main()
