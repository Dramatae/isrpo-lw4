import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_positive_integer_values(self):
        self.assertEqual(area(6, 4), 12)

    def test_area_zero_side(self):
        self.assertEqual(area(0, 4), 0)

    def test_area_float_values(self):
        self.assertEqual(area(2.5, 3.2), 4.0)

    def test_perimeter_positive_integer_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.0), 10.0)