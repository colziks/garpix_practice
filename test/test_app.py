import unittest
import json
from app import main

class TestApp(unittest.TestCase):
    def setUp(self):
        # Чтение данных из файла 'распределение-педагогической-нагрузки.json'
        with open('распределение-педагогической-нагрузки.json', 'r', encoding='utf-8') as file:
            self.test_data = file.read()
        
    def test_main_function(self):
        # Проверяем, что функция main возвращает строку
        result = main(self.test_data)
        self.assertIsInstance(result, str, "The result should be a string")
        
        # Проверяем, что результат не пустой
        self.assertTrue(result, "The result should not be empty")
        
        # Проверяем, что результат можно прочитать как CSV
        try:
            df = pd.read_csv(pd.compat.StringIO(result))
            self.assertFalse(df.empty, "The DataFrame should not be empty")
        except Exception as e:
            self.fail(f"The result is not a valid CSV: {e}")

if __name__ == '__main__':
    unittest.main()
