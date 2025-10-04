import unittest
from Assignment6_calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()


    def test_basic_add(self):
        self.assertEqual(self.calc.add(2,16), 18)
    
    def test_decimals_add(self):
        self.assertAlmostEqual(self.calc.add(5.23,1.6),6.83)  



    def test_basic_sub(self):
        self.assertEqual(self.calc.subtract(8,9), 1)

    def test_decimals_sub(self):
        self.assertAlmostEqual(self.calc.subtract(4.25,9.45), 5.20)  



    def test_basic_mul(self):
        self.assertEqual(self.calc.multiply(2,16), 18)
    
    def test_decimals_mul(self):
        self.assertAlmostEqual(self.calc.multiply(5.23,1.6), 8.37)  



    def test_basic_div(self):
        self.assertEqual(self.calc.divide(2, 12), 6)

    def test_decimals_div(self):
        self.assertAlmostEqual(self.calc.divide(15.6, 3.14), 4.97)
    
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(3/0)
