import unittest
import os
from django.test import TestCase
import app
from core.utils import load_data_from_json, get_attribute_frequency

class ApplicationTestSuite(TestCase):
    
    def test_identify_minimal_identifiers(self):
        """Тестирование функции, находящей минимальный набор атрибутов."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(test_dir, 'sample_data.json')
        with open(file_path, 'r', encoding='utf-8'):
            test_data = load_data_from_json(file_path)

        expected_identifiers = ["name,color", "name,size"]
        self.assertIn(app.determine_minimal_identifiers(test_data), expected_identifiers)

    def test_execute_with_file_input(self):
        """Тестирование основной функции с указанным путем к файлу."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        test_file_path = os.path.join(test_dir, 'sample_data.json')

        expected_identifiers = ["name,color", "name,size"]
        self.assertIn(app.execute(file_path=test_file_path), expected_identifiers)

    def test_data_loading_from_json(self):
        """Тестирование функции загрузки данных из JSON."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(test_dir, 'sample_data.json')

        data = load_data_from_json(file_path)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)

        with self.assertRaises(ValueError):
            load_data_from_json("non_existent_file.json")

    def test_calculate_attribute_frequency(self):
        """Тестирование функции вычисления частоты атрибутов."""
        sample_data = [
            {"a": 1, "b": 2, "c": "hello"},
            {"a": 2, "b": 2, "c": "world"},
            {"a": 1, "b": 3, "c": "hello"}
        ]
        expected_frequency = [('a', {1, 2}), ('b', {2, 3}), ('c', {'hello', 'world'})]
        calculated_frequency = get_attribute_frequency(sample_data)
        self.assertEqual(calculated_frequency, expected_frequency)

if __name__ == '__main__':
    unittest.main()
