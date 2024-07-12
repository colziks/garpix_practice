import unittest
from app import main

class TestMainFunction(unittest.TestCase):
    def test_unique_identifiers(self):
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        result = main(json_string)
        self.assertIn("id", result)
        self.assertIn("name", result)

if __name__ == "__main__":
    unittest.main()
