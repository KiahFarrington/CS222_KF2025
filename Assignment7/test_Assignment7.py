'''
TEST CASE GIVEN FROM PROFESSOR
'''

import unittest
from grade_calculator import calculate_grade

class TestGradeCalculator(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(calculate_grade(92), "A")
        
    def test_grade_b(self):
        self.assertEqual(calculate_grade(89), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(70), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(68), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(50), "F")
        
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_grade("ninety")

    def test_out_of_range_values(self):
        with self.assertRaises(ValueError):
            calculate_grade(-10)
        with self.assertRaises(ValueError):
            calculate_grade(110)

if __name__ == "__main__":
    unittest.main()
