import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 3)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, "4")

        r8 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r8.width, 1)
        self.assertEqual(r8.height, 2)
        self.assertEqual(r8.x, 3)
        self.assertEqual(r8.y, 4)
        self.assertEqual(r8.id, 5)

        with self.assertRaises(ValueError):
            r9 = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r10 = Rectangle(1, -2)

        r11 = Rectangle(0, 2)
        self.assertEqual(r11.width, 0)
        self.assertEqual(r11.height, 2)
        self.assertEqual(r11.x, 0)
        self.assertEqual(r11.y, 0)
        self.assertEqual(r11.id, 6)

        r12 = Rectangle(1, 0)
        self.assertEqual(r12.width, 1)
        self.assertEqual(r12.height, 0)
        self.assertEqual(r12.x, 0)
        self.assertEqual(r12.y, 0)
        self.assertEqual(r12.id, 7)

        with self.assertRaises(ValueError):
            r13 = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            r14 = Rectangle(1, 2, 3, -4)

    def test_area(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

        r3 = Rectangle(4, 5)
        self.assertEqual(r3.area(), 20)

    def test_str(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(str(r1), "[Rectangle] (8) 0/0 - 2/3")

        r2 = Rectangle(3, 4, 5)
        self.assertEqual(str(r2), "[Rectangle] (9) 5/0 - 3/4")

        r3 = Rectangle(4, 5, 6, 7)
        self.assertEqual(str(r3), "[Rectangle] (10) 6/7 - 4/

