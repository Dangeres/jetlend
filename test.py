import unittest
from utils import delete_duplicates
    

class TestMain(unittest.TestCase):
    def test_duplicate(self):
        self.assertEqual(
            delete_duplicates(
                [
                    {"key1": "value1"},
                    {"k1": "v1", "k2": "v2", "k3": "v3"},
                    {},
                    {},
                    {"key1": "value1"},
                    {"key1": "value1"},
                    {"key2": "value2"}
                ]), 
                [
                    {"key1": "value1"}, 
                    {"k1": "v1", "k2": "v2", "k3": "v3"}, 
                    {}, 
                    {"key2": "value2"}
                ])

        # self.assertEqual()