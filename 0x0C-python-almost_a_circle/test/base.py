import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_automatic_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_automatic_id_plus_one(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(id=89)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 89)
        self.assertEqual(b5.id, 4)

    def test_base_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_base_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_base_to_json_string_with_id(self):
        json_str = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_base_from_json_string_none(self):
        json_str = Base.from_json_string(None)
        self.assertEqual(json_str, [])

    def test_base_from_json_string_empty_list(self):
        json_str = Base.from_json_string("[]")
        self.assertEqual(json_str, [])

    def test_base_from_json_string_with_id(self):
        json_str = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(json_str, [{'id': 89}])

if __name__ == '__main__':
    unittest.main()
