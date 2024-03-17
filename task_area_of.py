from math import pi, sqrt, isclose
import unittest


class calculate_area:
    @staticmethod
    def circle_area(rad):
        if rad <= 0:
            raise ValueError("radius should be >= 0")
        return pi * rad ** 2

    @staticmethod
    def triangle_area(s1, s2, s3):
        if s1 <= 0 and s2 <= 0 and s3 <= 0:
            raise ValueError("side lengths should be >= 0")
        p = (s1 + s2 + s3) / 2
        return sqrt(p * (p - s1) * (p - s2) * (p - s3))

    @staticmethod
    def is_right_triangle(s1, s2, s3):
        if s1 <= 0 and s2 <= 0 and s3 <= 0:
            raise ValueError("side lengths should be >= 0")
        sides = [s1, s2, s3]
        sides.sort()
        return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


class unit_tests(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(calculate_area.circle_area(1), pi)

    def test_triangle_area(self):
        self.assertAlmostEqual(calculate_area.triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(calculate_area.is_right_triangle(3, 4, 5))
        self.assertFalse(calculate_area.is_right_triangle(1, 1, 1))


if __name__ == "__main__":
    unittest.main()
