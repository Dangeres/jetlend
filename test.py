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
                ]
            ), 
            [
                {"key1": "value1"}, 
                {"k1": "v1", "k2": "v2", "k3": "v3"}, 
                {}, 
                {"key2": "value2"}
            ]
        )

        self.assertEqual(
            delete_duplicates(
                []
            ),
            []
        )

        self.assertEqual( # Важный тест, который ложит на лопатки хеширование через tuple
            delete_duplicates(
                [
                    {"1": "2"},
                    {"1": "2"},
                    {"1": "2"},
                    {"1": "3"},
                ]
            ),
            [
                {"1": "2"},
                {"1": "3"},
            ]
        )

        self.assertEqual(
            delete_duplicates(
                [
                    {"1": "2"},
                    {"1": "2"},
                    {"1": "2"},
                    {"1": "3"},
                    {},
                    {},
                    {"15": ["1", "2", "3"]},
                ]
            ),
            [
                {"1": "2"},
                {"1": "3"},
                {},
                {"15": ["1", "2", "3"]},
            ]
        )

        self.assertEqual(
            delete_duplicates(
                [
                    {"1": "2", "2": 3},
                    {"1": "2"},
                    {"1": "2"},
                    {"1": "3"},
                    {},
                    {},
                    {"15": ["1", "2", "3"]},
                ]
            ),
            [
                {"1": "2", "2": 3},
                {"1": "2"},
                {"1": "3"},
                {},
                {"15": ["1", "2", "3"]},
            ]
        )

        self.assertEqual(
            delete_duplicates(
                [
                    {},
                    {},
                    {},
                    {"key": {},},
                    {"key": {},},
                ]
            ),
            [
                {},
                {"key": {},},
            ]
        )