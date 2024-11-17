import unittest
from src.app import farewell

class TestApp(unittest.TestCase):
    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")
        self.assertEqual(farewell("Bob"), "Goodbye, Bob!")

if __name__ == "__main__":
    unittest.main()
